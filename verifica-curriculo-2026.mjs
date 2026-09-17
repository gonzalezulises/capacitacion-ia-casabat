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
  ejercicios === 16
    ? ok(`${file}: 16 laboratorios principales`)
    : fail(`${file}: tiene ${ejercicios} ejercicios; se esperaban 16 laboratorios principales`);
  !/\b\d+\s+MIN(?:UTOS)?\b/.test(html.replace(/<style[\s\S]*?<\/style>/gi, ''))
    ? ok(`${file}: no impone tiempos fijos`)
    : fail(`${file}: aún impone tiempos fijos`);
}

const s1 = read('sesion-1.html');
const laboratoriosS1 = s1
  .split(/(?=<section\b)/)
  .filter(section => section.includes('<div class="ex-num">'));

const laboratoriosDeCorreo = laboratoriosS1.filter(section => /correo/i.test(section)).length;
laboratoriosDeCorreo <= 3
  ? ok(`sesión 1: limita a ${laboratoriosDeCorreo} los laboratorios centrados en correo`)
  : fail(`sesión 1: ${laboratoriosDeCorreo} de 12 laboratorios siguen centrados en correo; máximo 3`);

for (const [sesion, html] of [[1, s1], [2, read('sesion-2.html')]]) {
  const laboratorios = html.split(/(?=<section\b)/).filter(section => section.includes('<div class="ex-num">'));
  for (let bloque = 0; bloque < 4; bloque++) {
    const cierre = laboratorios[bloque * 4 + 3] || '';
    /APLICACIÓN INDIVIDUAL/i.test(cierre)
      ? ok(`sesión ${sesion}: bloque ${bloque + 1} cierra con aplicación individual`)
      : fail(`sesión ${sesion}: bloque ${bloque + 1} no cierra con aplicación individual`);
  }
}

for (const [patron, capacidad] of [
  [/NotebookLM|Gemini Notebook/i, 'NotebookLM o Gemini Notebook'],
  [/Deep Research/i, 'Deep Research'],
  [/Canvas/i, 'Canvas'],
  [/Gem Manager|crea(?:r)? (?:una|la) Gem/i, 'creación real de una Gem'],
]) {
  laboratoriosS1.some(section => patron.test(section))
    ? ok(`sesión 1: practica ${capacidad}`)
    : fail(`sesión 1: no incluye un laboratorio de ${capacidad}`);
}

const laboratorio3 = laboratoriosS1[2] || '';
const cadena03 = ['SLIDE DECK', 'INFOGRAFÍA', 'CANVAS'];
let cursor03 = 0;
const cadena03Completa = cadena03.every(paso => {
  const posicion = laboratorio3.toUpperCase().indexOf(paso, cursor03);
  if (posicion < 0) return false;
  cursor03 = posicion + paso.length;
  return true;
});
cadena03Completa
  ? ok('sesión 1: laboratorio 3 encadena Slide Deck → infografía → Canvas')
  : fail('sesión 1: laboratorio 3 no encadena Slide Deck → infografía → Canvas en ese orden');

const bloque4 = laboratoriosS1.slice(12, 16).join('\n');
const cadenaBloque4 = ['PTCF', 'GOOGLE DOCS', 'GOOGLE VIDS', 'ASK GEMINI'];
let cursorBloque4 = 0;
const cadenaBloque4Completa = cadenaBloque4.every(paso => {
  const posicion = bloque4.toUpperCase().indexOf(paso, cursorBloque4);
  if (posicion < 0) return false;
  cursorBloque4 = posicion + paso.length;
  return true;
});
cadenaBloque4Completa
  ? ok('sesión 1: bloque 4 encadena PTCF/Docs → Vids → auditoría en Drive')
  : fail('sesión 1: bloque 4 no encadena PTCF/Docs → Vids → auditoría en Drive en ese orden');

for (const material of [
  'materiales/13_notas_recorrido_sucursales.docx',
  'materiales/expediente-auditoria-sucursales/AS-001_reporte_via_espana.docx',
  'materiales/expediente-auditoria-sucursales/AS-002_reporte_tocumen.docx',
  'materiales/expediente-auditoria-sucursales/AS-003_reporte_la_chorrera.docx',
  'materiales/expediente-auditoria-sucursales/AS-004_reporte_san_miguelito.docx',
]) {
  existsSync(material) ? ok(`${material}: presente`) : fail(`${material}: falta`);
}

for (const concepto of ['GENERAR', 'RECUPERAR', 'CALCULAR', 'ACTUAR']) {
  s1.includes(concepto)
    ? ok(`sesión 1: incluye el modo ${concepto.toLowerCase()}`)
    : fail(`sesión 1: falta el modo ${concepto.toLowerCase()}`);
}
const s2 = read('sesion-2.html');
for (const concepto of ['REPRODUCIBLE', 'OCR', 'INYECCIÓN DE PROMPTS', 'APROBACIÓN HUMANA', 'DETERMINISTA']) {
  s2.includes(concepto)
    ? ok(`sesión 2: incluye ${concepto.toLowerCase()}`)
    : fail(`sesión 2: falta ${concepto.toLowerCase()}`);
}

const laboratoriosS2 = s2
  .split(/(?=<section\b)/)
  .filter(section => section.includes('<div class="ex-num">'));

for (const [patron, capacidad] of [
  [/Fill with Gemini|Rellenar con Gemini/i, 'limpieza semántica con Fill with Gemini'],
  [/tabla dinámica/i, 'tablas dinámicas'],
  [/segmentador|slicer/i, 'segmentadores'],
  [/sensibilidad|escenario/i, 'escenarios y sensibilidad'],
  [/optimiza|optimización/i, 'optimización con restricciones'],
  [/Sheets Canvas|Canvas de Sheets/i, 'Sheets Canvas'],
]) {
  laboratoriosS2.some(section => patron.test(section))
    ? ok(`sesión 2: practica ${capacidad}`)
    : fail(`sesión 2: no incluye un laboratorio de ${capacidad}`);
}

const artefactosS2 = ['bitácora', 'tabla dinámica', 'árbol de hipótesis', 'sensibilidad',
  'matriz de decisión', 'tabla estructurada', 'plan de asignación', 'dashboard', 'brief'];
for (const artefacto of artefactosS2) {
  new RegExp(artefacto, 'i').test(s2)
    ? ok(`sesión 2: produce ${artefacto}`)
    : fail(`sesión 2: no produce ${artefacto}`);
}

const cadenaFinalS2 = laboratoriosS2.slice(12, 16).join('\n');
const cadenaS2 = ['SHEETS', 'DASHBOARD', 'SLIDES', 'DECISIÓN'];
let cursorS2 = 0;
const cadenaS2Completa = cadenaS2.every(paso => {
  const posicion = cadenaFinalS2.toUpperCase().indexOf(paso, cursorS2);
  if (posicion < 0) return false;
  cursorS2 = posicion + paso.length;
  return true;
});
cadenaS2Completa
  ? ok('sesión 2: bloque 4 encadena Sheets → dashboard → Slides → decisión')
  : fail('sesión 2: bloque 4 no encadena Sheets → dashboard → Slides → decisión en ese orden');

existsSync('materiales/14_inventario_demanda_sucursales.xlsx')
  ? ok('sesión 2: anexo de inventario y demanda presente')
  : fail('sesión 2: falta materiales/14_inventario_demanda_sucursales.xlsx');

const publicables = [
  ...decks.map(read),
  read('practica.html'),
  read('index.html'),
].join('\n');

for (const [patron, etiqueta] of [
  [/GPT personalizado/gi, 'GPT personalizado como opción vigente'],
  [/razonamiento paso a paso/gi, 'petición de razonamiento interno paso a paso'],
  [/Lo que hacías en Minitab/gi, 'promesa de reemplazo de Minitab'],
]) {
  const n = (publicables.match(patron) || []).length;
  n === 0 ? ok(`no aparece ${etiqueta}`) : fail(`aparece ${etiqueta} ${n} vez/veces`);
}

const hub = read('index.html');
hub.includes('<b>32</b><span>laboratorios principales')
  ? ok('hub: comunica 32 laboratorios principales')
  : fail('hub: no comunica los 32 laboratorios principales');

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
