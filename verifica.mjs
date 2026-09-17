#!/usr/bin/env node
// Verificador del deck. Comprueba invariantes que a mano se rompen sin que se note:
// numeración de slides, contadores del top-rail, minutos por bloque, integridad de
// cada ejercicio, enlaces del hub y puntuación española.
// Uso: node verifica.mjs   ·   Sale 1 si algo falla.

import { readFileSync, existsSync } from 'node:fs';
import { createHash } from 'node:crypto';

const fails = [];
const oks = [];
const ok = (m) => oks.push(m);
const fail = (m) => fails.push(m);

const DECKS = ['sesion-1.html', 'sesion-2.html'];
const EJ_POR_SESION = 16;

// texto visible: sin <style>, <script> ni etiquetas
function visible(html) {
  return html
    .replace(/<style[\s\S]*?<\/style>/gi, ' ')
    .replace(/<script[\s\S]*?<\/script>/gi, ' ')
    .replace(/<!--[\s\S]*?-->/g, ' ')
    .replace(/<[^>]+>/g, ' ')
    .replace(/&nbsp;/g, ' ')
    .replace(/&amp;/g, '&')
    .replace(/\s+/g, ' ');
}

for (const file of DECKS) {
  if (!existsSync(file)) { fail(`${file}: no existe`); continue; }
  const html = readFileSync(file, 'utf8');

  // --- secciones ---
  const secciones = [...html.matchAll(/<section\b[^>]*data-label="([^"]+)"[^>]*>/g)].map(m => m[1]);
  const cierres = (html.match(/<\/section>/g) || []).length;
  if (secciones.length !== cierres) fail(`${file}: ${secciones.length} <section> vs ${cierres} </section>`);
  else ok(`${file}: ${secciones.length} slides, etiquetas balanceadas`);

  // --- numeración del footer: 01..N consecutiva ---
  const nums = [...html.matchAll(/<div class="rhs">(\d{2})<\/div>/g)].map(m => Number(m[1]));
  const esperado = Array.from({ length: secciones.length }, (_, i) => i + 1);
  if (JSON.stringify(nums) !== JSON.stringify(esperado)) {
    fail(`${file}: footers numerados ${nums.join(',')} — se esperaba 1..${secciones.length}`);
  } else ok(`${file}: footers 01..${String(secciones.length).padStart(2, '0')} consecutivos`);

  // --- contador del top-rail "NN / TT" apunta al total real ---
  const contadores = [...html.matchAll(/<span>(\d{2}) \/ (\d{2})<\/span>/g)];
  const malTotal = contadores.filter(m => Number(m[2]) !== secciones.length);
  if (malTotal.length) fail(`${file}: ${malTotal.length} contadores con total ≠ ${secciones.length} (ej: ${malTotal[0][0]})`);
  else ok(`${file}: ${contadores.length} contadores de top-rail con total correcto`);

  // el contador debe coincidir con la posición real del slide
  const bloquesSeccion = html.split(/<section\b/).slice(1);
  bloquesSeccion.forEach((s, i) => {
    const m = s.match(/<span>(\d{2}) \/ \d{2}<\/span>/);
    if (m && Number(m[1]) !== i + 1) fail(`${file}: slide ${i + 1} dice "${m[0]}" en el top-rail`);
  });

  // --- ejercicios: numeración y partes obligatorias ---
  const exNums = [...html.matchAll(/<div class="ex-num">(\d{2})<\/div>/g)].map(m => Number(m[1]));
  const exEsperado = Array.from({ length: EJ_POR_SESION }, (_, i) => i + 1);
  if (JSON.stringify(exNums) !== JSON.stringify(exEsperado)) {
    fail(`${file}: ejercicios ${exNums.join(',')} — se esperaba 1..${EJ_POR_SESION}`);
  } else ok(`${file}: ${EJ_POR_SESION} ejercicios numerados sin saltos`);

  for (const s of bloquesSeccion) {
    if (!s.includes('class="ex-num"')) continue;
    const t = (s.match(/<h2 class="ex-title">([^<]+)</) || [, '?'])[1];
    for (const parte of ['prompt-card', 'class="result"', 'class="situation"', 'class="role"',
                         'class="input"', 'class="decision"', 'class="criterion"', 'ol class="steps"']) {
      if (!s.includes(parte)) fail(`${file}: el ejercicio "${t}" no tiene ${parte}`);
    }
  }

  const labsPorBloque = {};
  for (const s of bloquesSeccion) {
    if (!s.includes('class="ex-num"')) continue;
    const b = s.match(/BLOQUE (\d{2}) <span class="sep">/);
    if (b) labsPorBloque[Number(b[1])] = (labsPorBloque[Number(b[1])] || 0) + 1;
  }
  for (let b = 1; b <= 4; b++) {
    if ((labsPorBloque[b] || 0) !== 4) fail(`${file}: bloque ${b} tiene ${labsPorBloque[b] || 0} laboratorios; se esperaban 4`);
  }
  if ([1, 2, 3, 4].every(b => labsPorBloque[b] === 4)) ok(`${file}: cuatro laboratorios en cada bloque`);

  // --- ritmo presencial: el deck no impone minutos por bloque ni ejercicio ---
  const tiemposFijos = visible(html).match(/\b\d+\s+MIN(?:UTOS)?\b/g) || [];
  tiemposFijos.length === 0
    ? ok(`${file}: sin tiempos fijos; el facilitador controla el ritmo`)
    : fail(`${file}: conserva tiempos fijos — ${[...new Set(tiemposFijos)].join(', ')}`);

  // --- puntuación española: todo ? y ! con su signo de apertura ---
  const txt = visible(html);
  const cierraInt = (txt.match(/\?/g) || []).length;
  const abreInt = (txt.match(/¿/g) || []).length;
  const cierraExc = (txt.match(/!/g) || []).length;
  const abreExc = (txt.match(/¡/g) || []).length;
  if (cierraInt !== abreInt) {
    const sospechosas = (txt.match(/[^¿?]{0,70}\?/g) || []).filter(f => !f.includes('¿')).slice(0, 3);
    fail(`${file}: ${abreInt} "¿" para ${cierraInt} "?" — revisar: ${JSON.stringify(sospechosas)}`);
  } else ok(`${file}: ${abreInt} interrogaciones, todas con signo de apertura`);
  if (cierraExc !== abreExc) fail(`${file}: ${abreExc} "¡" para ${cierraExc} "!"`);

  // --- restos de plantilla ---
  for (const resto of ['[CLIENTE', 'PAYJOY', 'PayJoy', 'REMOTE  LAB', 'Lorem', 'TODO:']) {
    if (html.includes(resto)) fail(`${file}: quedó "${resto}" del deck original`);
  }

  // --- ningún color apunta a un token que no existe ---
  // Al cambiar la paleta quedaron 9 var(--green) sin definir: el texto salía sin acento
  // y nada avisaba. Esto lo detecta.
  const definidos = new Set([...html.matchAll(/(--[a-z0-9-]+)\s*:/g)].map(m => m[1]));
  const usados = [...new Set([...html.matchAll(/var\((--[a-z0-9-]+)\)/g)].map(m => m[1]))];
  const huerfanos = usados.filter(t => !definidos.has(t));
  huerfanos.length
    ? fail(`${file}: usa tokens que no existen — ${huerfanos.join(', ')}`)
    : ok(`${file}: los ${usados.length} tokens de color usados están definidos`);

  // --- el motor y las fuentes están declarados ---
  if (!html.includes('<script src="deck-stage.js">')) fail(`${file}: no carga deck-stage.js`);
  if (!/family=Antonio/.test(html)) fail(`${file}: no carga la tipografía Antonio de la marca`);
  if (!/<title>[^<]{10,}<\/title>/.test(html)) fail(`${file}: sin <title> descriptivo`);
}

// --- hub ---
if (!existsSync('index.html')) fail('index.html: no existe');
else {
  const hub = readFileSync('index.html', 'utf8');
  for (const href of [...hub.matchAll(/href="([^"]+\.html)"/g)].map(m => m[1])) {
    if (!existsSync(href)) fail(`index.html enlaza a ${href}, que no existe`);
  }
  ok('index.html: todos los enlaces internos resuelven a un archivo real');
  const t = visible(hub);
  if ((t.match(/\?/g) || []).length !== (t.match(/¿/g) || []).length) fail('index.html: interrogación sin signo de apertura');
}

// --- el motor no fue modificado respecto al deck de origen ---
const ORIGEN = '/Users/ulisesgonzalez/GitHub/capacitacion-gemini-payjoy/deck-stage.js';
if (!existsSync('deck-stage.js')) fail('deck-stage.js: no existe');
else if (existsSync(ORIGEN)) {
  const h = (p) => createHash('sha1').update(readFileSync(p)).digest('hex');
  if (h('deck-stage.js') !== h(ORIGEN)) fail('deck-stage.js difiere del motor original de capacitacion-gemini-payjoy');
  else ok('deck-stage.js: idéntico al motor original (sha1 coincide)');
}

console.log(oks.map(o => `  ok   ${o}`).join('\n'));
if (fails.length) {
  console.log('\n' + fails.map(f => `  FALLA ${f}`).join('\n'));
  console.log(`\n${fails.length} problema(s). ${oks.length} comprobaciones correctas.`);
  process.exit(1);
}
console.log(`\nTodo correcto: ${oks.length} comprobaciones.`);
