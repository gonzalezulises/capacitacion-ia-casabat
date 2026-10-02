#!/usr/bin/env node
// Compuerta curricular: evita que una regeneración reintroduzca conceptos,
// productos o una carga de trabajo que ya no corresponden al programa 2026.

import { readFileSync, existsSync } from 'node:fs';

const fails = [];
const oks = [];
const ok = (m) => oks.push(m);
const fail = (m) => fails.push(m);
const read = (p) => readFileSync(p, 'utf8');

const decks = ['sesion-1.html', 'sesion-2.html', 'sesion-3.html'];
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

for (const [sesion, html] of [[1, s1], [2, read('sesion-2.html')], [3, read('sesion-3.html')]]) {
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

// --- sesión 3: cada pedido del formulario previo tiene su bloque ---
// El instrumento (5 respuestas, cohorte Administración y Gerencia Comercial)
// pidió cuatro cosas. Si una regeneración borra el bloque que la resuelve, la
// sesión deja de responder lo que se preguntó.
const s3 = read('sesion-3.html');
const laboratoriosS3 = s3
  .split(/(?=<section\b)/)
  .filter(section => section.includes('<div class="ex-num">'));

for (const [bloque, patron, pedido] of [
  [1, /seis partes|pedido que funcionó|dos resultados/i, '«qué prompts usar» · 3 de 5 respondientes'],
  [2, /forma de escribir|frases que delatan|sin que te reescriba/i, '«que no se vea que es IA»'],
  [3, /tablero|gráfico que se entiende|cinco cifras/i, '«ejemplo de dashboard o gráficos» · 3 de 5'],
  [4, /nombres|anexo|procedimiento/i, '«nomenclatura y códigos de procedimientos»'],
]) {
  const laboratorios = laboratoriosS3.slice((bloque - 1) * 4, bloque * 4).join('\n');
  patron.test(laboratorios)
    ? ok(`sesión 3: el bloque ${bloque} responde ${pedido}`)
    : fail(`sesión 3: el bloque ${bloque} ya no responde ${pedido}`);
}

// Los tableros y los gráficos se piden en tres herramientas distintas, porque el
// instrumento reportó ChatGPT en 3 respuestas y Gemini en 2.
const recetasS3 = s3.split(/(?=<section\b)/).filter(section => /RECETA [ABC]/.test(section));
recetasS3.length === 6
  ? ok('sesión 3: seis recetas por herramienta (tablero y gráfico × Gemini, ChatGPT y Claude)')
  : fail(`sesión 3: hay ${recetasS3.length} recetas; se esperaban 6`);

for (const herramienta of ['GEMINI', 'CHATGPT', 'CLAUDE']) {
  const propias = recetasS3.filter(section => section.includes(`<span>RECETA`) &&
    new RegExp(`RECETA [ABC] <span class="sep"></span> ${herramienta}`).test(section));
  propias.length === 2
    ? ok(`sesión 3: ${herramienta.toLowerCase()} tiene su receta de tablero y de gráfico`)
    : fail(`sesión 3: ${herramienta.toLowerCase()} tiene ${propias.length} recetas; se esperaban 2`);
}

// Cada receta entrega un bloque para copiar y pegar: sin eso es una explicación,
// no una receta.
const sinBloque = recetasS3.filter(section => !/PEGA ESTO EN/.test(section));
sinBloque.length === 0
  ? ok('sesión 3: las seis recetas traen su bloque para copiar y pegar')
  : fail(`sesión 3: ${sinBloque.length} receta(s) sin bloque para copiar`);

for (const material of [
  'materiales/15_prompts_que_fallaron.docx',
  'materiales/16_maestro_procedimientos.xlsx',
]) {
  existsSync(material) ? ok(`${material}: presente`) : fail(`${material}: falta`);
}

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
hub.includes('<b>48</b><span>laboratorios principales')
  ? ok('hub: comunica 48 laboratorios principales')
  : fail('hub: no comunica los 48 laboratorios principales');

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
