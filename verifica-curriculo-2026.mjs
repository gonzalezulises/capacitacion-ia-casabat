#!/usr/bin/env node
// Compuerta curricular: evita que una regeneración reintroduzca conceptos,
// productos o una carga de trabajo que ya no corresponden al programa 2026.

import { readFileSync, existsSync } from 'node:fs';

const fails = [];
const oks = [];
const ok = (m) => oks.push(m);
const fail = (m) => fails.push(m);
const read = (p) => readFileSync(p, 'utf8');

const decks = ['sesion-1.html', 'sesion-2.html'];
for (const file of decks) {
  if (!existsSync(file)) {
    fail(`${file}: no existe`);
    continue;
  }
  const html = read(file);
  const ejercicios = (html.match(/<div class="ex-num">/g) || []).length;
  ejercicios === 12
    ? ok(`${file}: 12 laboratorios principales`)
    : fail(`${file}: tiene ${ejercicios} ejercicios; se esperaban 12 laboratorios principales`);
  html.includes('PAUSA · 15 MIN')
    ? ok(`${file}: declara la pausa de 15 minutos`)
    : fail(`${file}: no declara PAUSA · 15 MIN en la agenda`);
}

const s1 = read('sesion-1.html');
for (const concepto of ['GENERAR', 'RECUPERAR', 'CALCULAR', 'ACTUAR']) {
  s1.includes(concepto)
    ? ok(`sesión 1: incluye el modo ${concepto.toLowerCase()}`)
    : fail(`sesión 1: falta el modo ${concepto.toLowerCase()}`);
}
for (const concepto of ['PROYECTO', 'GEM', 'PLUGIN']) {
  s1.includes(concepto)
    ? ok(`sesión 1: diferencia ${concepto.toLowerCase()}`)
    : fail(`sesión 1: no diferencia ${concepto.toLowerCase()}`);
}

const s2 = read('sesion-2.html');
for (const concepto of ['REPRODUCIBLE', 'OCR', 'INYECCIÓN DE PROMPTS', 'APROBACIÓN HUMANA', 'DETERMINISTA']) {
  s2.includes(concepto)
    ? ok(`sesión 2: incluye ${concepto.toLowerCase()}`)
    : fail(`sesión 2: falta ${concepto.toLowerCase()}`);
}

const publicables = [
  ...decks.map(read),
  read('practica.html'),
  read('index.html'),
].join('\n');

for (const [patron, etiqueta] of [
  [/NotebookLM/gi, 'nombre retirado NotebookLM'],
  [/GPT personalizado/gi, 'GPT personalizado como opción vigente'],
  [/razonamiento paso a paso/gi, 'petición de razonamiento interno paso a paso'],
  [/Lo que hacías en Minitab/gi, 'promesa de reemplazo de Minitab'],
]) {
  const n = (publicables.match(patron) || []).length;
  n === 0 ? ok(`no aparece ${etiqueta}`) : fail(`aparece ${etiqueta} ${n} vez/veces`);
}

const hub = read('index.html');
hub.includes('<b>24</b><span>laboratorios principales')
  ? ok('hub: comunica 24 laboratorios principales')
  : fail('hub: no comunica los 24 laboratorios principales');

for (const material of [
  'materiales/01_especificacion_de_tarea.docx',
  'materiales/02_pruebas_de_aceptacion.docx',
  'materiales/12_contexto_persistente_y_flujos.docx',
]) {
  existsSync(material) ? ok(`${material}: presente`) : fail(`${material}: falta`);
}

console.log(oks.map(o => `  ok   ${o}`).join('\n'));
if (fails.length) {
  console.log('\n' + fails.map(f => `  FALLA ${f}`).join('\n'));
  console.log(`\n${fails.length} problema(s). ${oks.length} comprobaciones correctas.`);
  process.exit(1);
}
console.log(`\nTodo correcto: ${oks.length} comprobaciones.`);
