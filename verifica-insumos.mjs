#!/usr/bin/env node
// Auditoría de insumos: ningún laboratorio puede pedir algo que no existe.
//
// Por qué existe: un laboratorio pedía «el reclamo del cliente» y ese texto no
// estaba en ninguna parte; otro mandaba usar «las cifras del laboratorio 10»,
// que nadie veía. Cada hallazgo se arregló a mano, uno por uno. Esto los busca
// todos de una vez, en las tres sesiones.
//
// Lo que comprueba, laboratorio por laboratorio:
//   1. Todo archivo nombrado en cualquier parte del slide existe en materiales/.
//   2. Lo que el laboratorio declara como entrada también se nombra donde se usa.
//   3. Una referencia a «el laboratorio N» apunta a uno anterior de esa sesión.
//   4. Lo que el prompt dice adjuntar o pegar está declarado como entrada.
//   5. El prompt no deja huecos sin explicar.
//
// Uso: node verifica-insumos.mjs   ·   Sale 1 si algo falla.

import { readFileSync, existsSync, readdirSync } from 'node:fs';
import { join } from 'node:path';

const DECKS = ['sesion-1.html', 'sesion-2.html', 'sesion-3.html'];
const fails = [];
const oks = [];
const ok = (m) => oks.push(m);
const fail = (m) => fails.push(m);

// --- inventario real de materiales ---
const materiales = new Set();
const recorrer = (dir) => {
  for (const entrada of readdirSync(dir, { withFileTypes: true })) {
    if (entrada.name.startsWith('.')) continue;
    const ruta = join(dir, entrada.name);
    if (entrada.isDirectory()) { materiales.add(entrada.name + '/'); recorrer(ruta); }
    else materiales.add(entrada.name);
  }
};
recorrer('materiales');
ok(`materiales/: ${materiales.size} archivos y carpetas disponibles`);

const texto = (html) => html.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
const trozo = (sec, re) => { const m = sec.match(re); return m ? texto(m[1]) : ''; };

let laboratorios = 0;

for (const deck of DECKS) {
  if (!existsSync(deck)) { fail(`${deck}: no existe`); continue; }
  const html = readFileSync(deck, 'utf8');
  const sesion = Number(deck.match(/\d/)[0]);
  const todas = html.split(/(?=<section\b)/).slice(1);
  const secciones = todas.filter((s) => s.includes('class="ex-num"'));
  const problemas = [];

  // Un archivo nombrado en cualquier slide —laboratorio, receta o lista de
  // materiales— tiene que existir. El defecto se cuela igual en una receta.
  for (const sec of todas) {
    const donde = (sec.match(/data-label="([^"]+)"/) || [, '?'])[1];
    for (const nombre of new Set([...sec.matchAll(/<code>([^<]+)<\/code>/g)].map((m) => m[1].trim()))) {
      if (!/\.(docx|xlsx|png|jpg|csv|pdf)$|\/$/.test(nombre)) continue;
      if (!materiales.has(nombre)) problemas.push(`el slide «${donde}» nombra «${nombre}», que no está en materiales/`);
    }
  }

  secciones.forEach((sec, indice) => {
    laboratorios += 1;
    const numero = Number((sec.match(/<div class="ex-num">(\d+)<\/div>/) || [, 0])[1]);
    const titulo = (sec.match(/<h2 class="ex-title">([^<]+)</) || [, '?'])[1];
    const señala = (m) => problemas.push(`«${titulo}» (lab ${numero}): ${m}`);

    // ---- 1. todo archivo nombrado existe ----
    const nombrados = [...sec.matchAll(/<code>([^<]+)<\/code>/g)].map((m) => m[1].trim());
    for (const nombre of new Set(nombrados)) {
      // un <code> puede ser un nombre de columna o un valor de dato, no un archivo
      if (!/\.(docx|xlsx|png|jpg|csv|pdf)$|\/$/.test(nombre)) continue;
      if (!materiales.has(nombre)) señala(`nombra «${nombre}», que no está en materiales/`);
    }

    // ---- 2. la entrada del laboratorio declara algo ----
    const entrada = (sec.match(/<span class="input"><b>[^<]*<\/b>([\s\S]*?)<\/span>/) || [, ''])[1];
    const archivosEntrada = [...entrada.matchAll(/<code>([^<]+)<\/code>/g)].map((m) => m[1].trim());
    if (!texto(entrada)) señala('no declara ninguna entrada');

    // ---- 3. las referencias a otro laboratorio apuntan hacia atrás ----
    // Se mira todo el slide menos el rótulo que lleva su propio número.
    const sinSuPropioNumero = texto(sec).replace(/LABORATORIO\s+\d+/i, ' ');
    for (const m of sinSuPropioNumero.matchAll(/laboratorios? (\d+)(?:\s*y\s*(\d+))?/gi)) {
      for (const ref of [m[1], m[2]].filter(Boolean).map(Number)) {
        if (ref >= numero) señala(`se apoya en el laboratorio ${ref}, que no es anterior`);
        if (ref > secciones.length) señala(`cita un laboratorio ${ref} que no existe`);
      }
    }

    // ---- 4. lo que el prompt manda adjuntar está declarado como entrada ----
    const promptTxt = texto((sec.match(/<div class="prompt-card[\s\S]*?(?=<div class="result")/) || [''])[0]);
    if (/te (adjunto|paso|subo|mando|envío)|adjunta|sube el archivo/i.test(promptTxt)) {
      const declaraAlgo = archivosEntrada.length > 0 ||
        /tu |tus |propio|real|anonimizad|compañer/i.test(texto(entrada));
      if (!declaraAlgo) señala('el prompt manda adjuntar algo y la entrada no declara ningún archivo');
    }

    // ---- 5. el prompt no deja huecos crípticos ----
    for (const [patron, queja] of [
      [/pega (aquí|aca|acá)/i, 'dice «pega aquí» sin decir de dónde sale'],
      [/…/, 'tiene puntos suspensivos en lugar de texto'],
      [/&lt;\/?[a-z_]+&gt;/, 'usa etiquetas tipo XML'],
      [/(?<!\b(?:cifras|borrador|respuestas|guion|lista|texto|notas|tabla)\b[^[]{0,24})\[(pégalo|pégalas|pégala)\]/i,
       'dice «[pégalo]» sin nombrar antes qué se pega'],
    ]) {
      if (patron.test(queja.includes('XML') ? sec : promptTxt)) señala(`el prompt ${queja}`);
    }
  });

  problemas.length === 0
    ? ok(`${deck}: los ${secciones.length} laboratorios piden solo lo que existe`)
    : problemas.forEach((p) => fail(`${deck}: ${p}`));
}

ok(`${laboratorios} laboratorios auditados en ${DECKS.length} sesiones`);

console.log(oks.map((o) => `  ok   ${o}`).join('\n'));
if (fails.length) {
  console.log('\n' + fails.map((f) => `  FALLA ${f}`).join('\n'));
  console.log(`\n${fails.length} problema(s). ${oks.length} comprobaciones correctas.`);
  process.exit(1);
}
console.log(`\nInsumos correctos: ${oks.length} comprobaciones.`);
