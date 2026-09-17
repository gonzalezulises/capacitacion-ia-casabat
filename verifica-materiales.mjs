#!/usr/bin/env node
// Los materiales del taller tienen defectos y patrones PLANTADOS a propósito: si no están,
// los ejercicios se quedan sin respuesta. Esto comprueba que sigan ahí.
// Uso: node verifica-materiales.mjs   ·   Sale 1 si algo falla.

import { readFileSync, existsSync, readdirSync } from 'node:fs';
import { join } from 'node:path';
import { execFileSync } from 'node:child_process';

const M = 'materiales';
const EXP = join(M, 'expediente-PR-ADM-014');
const AUDIT = join(M, 'expediente-auditoria-sucursales');
const oks = [], fails = [];
const ok = (m) => oks.push(m);
const fail = (m) => fails.push(m);
const leer = (p) => readFileSync(p, 'utf8');
const leerOffice = (tipo, p) => JSON.parse(execFileSync('python3', ['build/office_reader.py', tipo, p], { encoding: 'utf8' }));
const DECKS = ['sesion-1.html', 'sesion-2.html'];
const sinTilde = (s) => s.normalize('NFKD').replace(/[̀-ͯ]/g, '');

// ---------- 0. Contrato Office ----------
const todos = [...readdirSync(M).filter(f => !f.startsWith('.')),
  ...readdirSync(EXP).filter(f => !f.startsWith('.')).map(f => `expediente-PR-ADM-014/${f}`),
  ...readdirSync(AUDIT).filter(f => !f.startsWith('.')).map(f => `expediente-auditoria-sucursales/${f}`)];
const docx = todos.filter(f => f.endsWith('.docx'));
const xlsx = todos.filter(f => f.endsWith('.xlsx'));
const retirados = todos.filter(f => /\.(?:md|csv)$/i.test(f));
docx.length === 22 ? ok('Office: 22 documentos Word') : fail(`Office: ${docx.length} DOCX; se esperaban 22`);
xlsx.length === 2 ? ok('Office: 2 libros Excel') : fail(`Office: ${xlsx.length} XLSX; se esperaban 2`);
retirados.length === 0 ? ok('Office: ningún MD o CSV para participantes')
  : fail(`Office: aún existen formatos retirados — ${retirados.join(' · ')}`);

if (existsSync('materiales.zip')) {
  const zip = execFileSync('unzip', ['-Z1', 'materiales.zip'], { encoding: 'utf8' }).trim().split('\n').filter(Boolean);
  const zipOffice = zip.filter(f => /\.(?:docx|xlsx)$/i.test(f));
  const zipRetirados = zip.filter(f => /\.(?:md|csv)$/i.test(f));
  zipOffice.length === 24 ? ok('ZIP: contiene los 24 archivos Office') : fail(`ZIP: contiene ${zipOffice.length} archivos Office; se esperaban 24`);
  zipRetirados.length === 0 ? ok('ZIP: no contiene MD o CSV') : fail(`ZIP: conserva formatos retirados — ${zipRetirados.join(' · ')}`);
}

// ---------- 1. El archivo de datos ----------
const ventasOffice = leerOffice('xlsx', join(M, '04_ventas_sucursales_2026.xlsx'));
const filas = ventasOffice.rows;
const tipos = ventasOffice.types;
filas.length === 357 ? ok('datos: 357 registros de ventas') : fail(`datos: ${filas.length} registros; se esperaban 357`);
const fechasTexto = tipos.filter(t => t.fecha === 'text').length;
const ingresosTexto = tipos.filter(t => t.ingreso_usd === 'text').length;
fechasTexto === 9 ? ok('datos: 9 fechas intencionalmente guardadas como texto') : fail(`datos: ${fechasTexto} fechas de texto; se esperaban 9`);
ingresosTexto === 2 ? ok('datos: 2 ingresos intencionalmente guardados como texto') : fail(`datos: ${ingresosTexto} ingresos de texto; se esperaban 2`);
const num = (s) => { const n = parseFloat(String(s).replace(/,/g, '').trim()); return isNaN(n) ? 0 : n; };
const norm = (s) => sinTilde(String(s)).trim().toLowerCase().replace(/\s+/g, ' ');
const mes = (f) => f.includes('/') ? `${f.slice(6, 10)}-${f.slice(3, 5)}` : f.slice(0, 7);

// defectos de calidad que el contrato de datos de la sesión 2 debe encontrar
const variantes = new Set(filas.map(f => f.linea_producto).filter(l => /ater/i.test(l) && /auto/i.test(l)));
variantes.size >= 4
  ? ok(`datos: la misma categoría escrita de ${variantes.size} formas distintas`)
  : fail(`datos: solo ${variantes.size} variantes de "Batería Auto" — el ejercicio de limpieza se queda sin caso`);

const paisVar = new Set(filas.map(f => f.pais).filter(p => /anam/i.test(p)));
paisVar.size >= 3 ? ok(`datos: país escrito de ${paisVar.size} formas`) : fail('datos: faltan variantes de país');

const chequeos = [
  ['fechas en otro formato', filas.filter(f => String(f.fecha).includes('/')).length, 5],
  ['celdas vacías en devoluciones', filas.filter(f => f.devoluciones === '').length, 5],
  ['números guardados como texto', filas.filter(f => String(f.ingreso_usd).includes(',')).length, 1],
  ['valores imposibles (negativos)', filas.filter(f => num(f.unidades) < 0).length, 1],
];
for (const [q, n, min] of chequeos) {
  n >= min ? ok(`datos: ${n} ${q}`) : fail(`datos: ${n} ${q} — se esperaban al menos ${min}`);
}
const claves = filas.map(f => Object.values(f).join('|'));
const dup = claves.length - new Set(claves).size;
dup >= 2 ? ok(`datos: ${dup} filas duplicadas exactas`) : fail(`datos: ${dup} duplicados — el ejercicio los pide`);

// patrones de negocio que el análisis reproducible debe encontrar
const ing = {};
for (const f of filas) ing[norm(f.linea_producto)] = (ing[norm(f.linea_producto)] || 0) + num(f.ingreso_usd);
const tot = Object.values(ing).reduce((a, b) => a + b, 0);
const orden = Object.entries(ing).sort((a, b) => b[1] - a[1]);
const top3 = orden.slice(0, 3).reduce((a, [, v]) => a + v, 0) / tot;
top3 > 0.7
  ? ok(`patrón Pareto: 3 de ${orden.length} líneas concentran el ${(top3 * 100).toFixed(0)} % del ingreso`)
  : fail(`patrón Pareto ausente: las 3 primeras líneas solo suman ${(top3 * 100).toFixed(0)} %`);

const dom = {};
for (const f of filas) if (norm(f.linea_producto) === 'servicio a domicilio') dom[mes(f.fecha)] = (dom[mes(f.fecha)] || 0) + num(f.unidades);
const serie = Object.keys(dom).sort().map(k => dom[k]);
const cae = serie.length >= 5 && serie[serie.length - 1] < serie[0] * 0.6;
cae ? ok(`patrón tendencia: servicio a domicilio cae de ${serie[0].toFixed(0)} a ${serie.at(-1).toFixed(0)} unidades`)
    : fail('patrón tendencia ausente: el servicio a domicilio no muestra caída sostenida');

const dev = {};
for (const f of filas) {
  const p = norm(f.pais).replace('panama', 'panama');
  dev[p] = dev[p] || [0, 0];
  dev[p][0] += num(f.devoluciones); dev[p][1] += num(f.unidades);
}
const tasas = Object.entries(dev).map(([p, [d, u]]) => [p, u ? d / u : 0]).sort((a, b) => b[1] - a[1]);
tasas[0][1] > tasas[1][1] * 2.5
  ? ok(`patrón grupo: ${tasas[0][0]} devuelve ${(tasas[0][1] * 100).toFixed(1)} % contra ${(tasas[1][1] * 100).toFixed(1)} % del siguiente`)
  : fail('patrón grupo ausente: ningún país destaca en devoluciones');

const ings = filas.map(f => num(f.ingreso_usd)).sort((a, b) => a - b);
const mediana = ings[Math.floor(ings.length / 2)];
ings.at(-1) > mediana * 8
  ? ok(`patrón outlier: máximo ${ings.at(-1).toLocaleString('es')} contra mediana ${mediana.toLocaleString('es')}`)
  : fail('patrón outlier ausente: no hay valor atípico detectable');

// ---------- 2. El expediente documental ----------
const archivos = readdirSync(EXP);
archivos.length === 6 ? ok(`expediente: ${archivos.length} documentos`) : fail(`expediente: ${archivos.length} documentos, se esperaban 6`);

const REGLA = /^PR-[A-Z]{3}-\d{3}(-ANEXO-[A-Z])?_[A-Za-z0-9_]+_v\d+\.docx$/;
const cumplen = archivos.filter(a => REGLA.test(a));
const incumplen = archivos.filter(a => !REGLA.test(a));
incumplen.length >= 3
  ? ok(`expediente: ${incumplen.length} nombres incumplen la regla — ${incumplen.join(' · ')}`)
  : fail(`expediente: solo ${incumplen.length} desviaciones de nomenclatura; el EJ 11 necesita varias`);
cumplen.length >= 3 ? ok(`expediente: ${cumplen.length} nombres correctos (hay con qué contrastar)`) : fail('expediente: faltan nombres correctos de referencia');

const proc = leerOffice('docx', join(EXP, 'PR-ADM-014_Gestion_de_Cotizaciones_v2.docx')).text;
// referencia rota: se menciona el Anexo E y no existe
const tieneE = archivos.some(a => /ANEXO-E/i.test(a));
/anexo e/i.test(proc) && !tieneE
  ? ok('expediente: el Anexo E se referencia y NO existe (referencia rota)')
  : fail('expediente: falta la referencia rota al Anexo E');
// anexo huerfano: existe y nadie lo referencia
const tieneF = archivos.some(a => /ANEXO-F/i.test(a));
tieneF && !/anexo f/i.test(proc)
  ? ok('expediente: el Anexo F existe y NADIE lo referencia (huérfano)')
  : fail('expediente: falta el anexo huérfano');
// mismo anexo con dos nombres distintos
/Tabla de descuentos \(Anexo B\)/i.test(proc) && /Anexo B/i.test(proc)
  ? ok('expediente: el Anexo B se menciona con dos nombres distintos')
  : oks.push('expediente: (aviso) revisar la doble denominación del Anexo B');
// referencia a una version que no es la del archivo
const anexoC = archivos.find(a => /ANEXO-C/i.test(a));
/ANEXO-C v2/i.test(proc) && /_V?v?1\.docx$/i.test(anexoC || '')
  ? ok('expediente: el procedimiento cita "ANEXO-C v2" pero el archivo es v1')
  : fail('expediente: falta la referencia a una versión distinta');
// codigo interno que no coincide con el nombre del archivo
const anexoB = leerOffice('docx', join(EXP, 'Anexo B - Tabla de descuentos.docx')).text;
/PR-ADM-011-ANEXO-B/.test(anexoB)
  ? ok('expediente: el Anexo B declara adentro un código que no es el suyo')
  : fail('expediente: falta el código interno inconsistente');

// ---------- 3. El borrador v3 contra el vigente ----------
const v3 = leerOffice('docx', join(M, '10_PR-ADM-014_v3_BORRADOR.docx')).text;
const cambios = [
  ['umbral de aprobación', /3\.000 dólares/.test(proc) && /5\.000 dólares/.test(v3)],
  ['control eliminado (doble verificación)', /doble verificación/i.test(proc) && !/doble verificación/i.test(v3.split('7 Control de cambios')[0])],
  ['cambio de responsable', /Jefatura de Administración/.test(proc) && /Coordinación Comercial/.test(v3)],
  ['sistema reemplazado', /sistema comercial/.test(proc) && /CRM/.test(v3)],
  ['plazo de vencimiento', /15 días calendario/.test(proc) && /20 días calendario/.test(v3)],
];
for (const [q, hay] of cambios) hay ? ok(`borrador v3: ${q}`) : fail(`borrador v3: falta el cambio de ${q}`);

// ---------- 4. Notas del comité ----------
const notas = leerOffice('docx', join(M, '07_notas_comite_operaciones.docx')).text;
/no quedó claro quién|no se dijo|no dijimos para cuándo|no se asignó/i.test(notas)
  ? ok('notas del comité: hay compromisos sin dueño o sin fecha (el hallazgo del EJ 13)')
  : fail('notas del comité: no hay compromisos huérfanos que encontrar');

// ---------- 5. Los correos citados por número corresponden ----------
// Los ejercicios dicen "el correo 4 de la pendientes": si alguien reordena el CSV, el
// taller se rompe en vivo y nadie lo nota hasta ese momento.
const pendientesOffice = leerOffice('xlsx', join(M, '05_correos_pendientes.xlsx'));
const pendientes = pendientesOffice.rows.map(f => `${f.n},${f.asunto},${f.primera_linea}`);
pendientes.length === 20 ? ok('pendientes: 20 correos') : fail(`pendientes: ${pendientes.length} correos, se esperaban 20`);
const esperados = [
  [1, /cotizaci[oó]n 8842/i, 'la cotización 8842 (S1 · EJ 2)'],
  [4, /garant[ií]a.*moto|moto.*8 meses/i, 'la garantía de moto de 8 meses (S1 · EJ 4)'],
  [11, /cr[eé]dito a 60 d[ií]as/i, 'el crédito a 60 días (S1 · EJ 3)'],
  [14, /instalaci[oó]n.*ventana|ventana/i, 'la instalación fuera de ventana (práctica)'],
];
for (const [n, re, que] of esperados) {
  const fila = pendientes[n - 1] || '';
  re.test(fila)
    ? ok(`correos pendientes: el ${n} sigue siendo ${que}`)
    : fail(`correos pendientes: el ${n} ya no es ${que} — dice "${fila.slice(0, 60)}…"`);
}

// ---------- 6. Todo archivo citado en los decks existe ----------
const citados = new Set();
for (const deck of ['sesion-1.html', 'sesion-2.html']) {
  const html = leer(deck);
  for (const m of html.matchAll(/<code>([^<]+\.(?:docx|xlsx))<\/code>/g)) citados.add(m[1]);
  for (const m of html.matchAll(/<code>(expediente-PR-ADM-014\/?)<\/code>/g)) citados.add(m[1]);
}
const disponibles = new Set([...readdirSync(M), ...readdirSync(EXP), ...readdirSync(AUDIT),
  'expediente-PR-ADM-014/', 'expediente-PR-ADM-014',
  'expediente-auditoria-sucursales/', 'expediente-auditoria-sucursales']);
const rotos = [...citados].filter(c => !disponibles.has(c) && !disponibles.has(c.split('/').pop()));
citados.size === 0
  ? fail('los decks no citan ningún material — los ejercicios siguen dependiendo de que el participante traiga archivos')
  : rotos.length
    ? fail(`los decks citan material que no existe: ${rotos.join(', ')}`)
    : ok(`decks: los ${citados.size} materiales citados existen en materiales/`);

// ---------- 7. Cada nombre de archivo del deck es un enlace que resuelve ----------
// Si el nombre queda como texto muerto, el participante tiene que adivinar la ruta.
let enlacesDeck = 0;
const enlacesRotos = [];
for (const deck of DECKS) {
  const html = leer(deck);
  const codigos = [...html.matchAll(/<code>([^<]+)<\/code>/g)].map(m => m[1]);
  const conEnlace = [...html.matchAll(/class="mat" href="([^"]+)"/g)].map(m => m[1]);
  enlacesDeck += conEnlace.length;
  for (const h of conEnlace) {
    const ruta = decodeURIComponent(h.split('#')[0]);
    if (!existsSync(ruta)) enlacesRotos.push(`${deck} → ${h}`);
  }
  // un <code> que nombra un archivo existente y NO quedó enlazado es un descuido
  const sueltos = codigos.filter(c => /\.(docx|xlsx)$/.test(c))
    .filter(c => !html.includes(`<code>${c}</code></a>`));
  if (sueltos.length) fail(`${deck}: nombres de archivo sin enlace — ${[...new Set(sueltos)].join(', ')}`);
}
enlacesRotos.length
  ? fail(`enlaces del deck que no resuelven: ${enlacesRotos.join(' · ')}`)
  : ok(`decks: ${enlacesDeck} nombres de archivo son enlaces y todos resuelven`);

// las anclas del hub existen
const hubHtml = leer('index.html');
for (const ancla of ['materiales', 'expediente']) {
  hubHtml.includes(`id="${ancla}"`)
    ? ok(`hub: ancla #${ancla} presente`)
    : fail(`hub: falta el ancla #${ancla}, a la que apuntan los decks`);
}

// ---------- 8. Todo material citado es alcanzable desde el hub ----------
// Servir el archivo no basta: si el hub no lo enlaza, el participante no llega.
const hub = leer('index.html');
const enlazados = new Set([...hub.matchAll(/href="materiales\/([^"]+)"/g)]
  .map(m => decodeURIComponent(m[1]).split('/').pop()));
const sinEnlace = [...citados]
  .map(c => c.replace(/\/$/, '').split('/').pop())
  .filter(c => c.includes('.') && !enlazados.has(c));
sinEnlace.length
  ? fail(`el hub no enlaza: ${[...new Set(sinEnlace)].join(', ')} — el participante no puede llegar a ellos`)
  : ok(`hub: los ${enlazados.size} materiales están enlazados y descargables`);
existsSync('materiales.zip')
  ? ok('hub: materiales.zip disponible para bajar todo de una vez')
  : fail('falta materiales.zip');

console.log(oks.map(o => `  ok   ${o}`).join('\n'));
if (fails.length) {
  console.log('\n' + fails.map(f => `  FALLA ${f}`).join('\n'));
  console.log(`\n${fails.length} problema(s). ${oks.length} comprobaciones correctas.`);
  process.exit(1);
}
console.log(`\nTodo correcto: ${oks.length} comprobaciones.`);
