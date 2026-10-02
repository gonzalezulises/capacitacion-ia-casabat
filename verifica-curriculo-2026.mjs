#!/usr/bin/env node
// Compuerta curricular: evita que una regeneración reintroduzca conceptos,
// productos o una carga de trabajo que ya no corresponden al programa 2026.

import { readFileSync, existsSync, readdirSync } from 'node:fs';
import { execFileSync } from 'node:child_process';

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

// --- sesión 1, bloque 1: de dónde sale la respuesta ---
// El bloque enseñaba a encadenar Slide Deck, infografía y Canvas en un solo
// laboratorio: una demo de botones que además no cabía en su tiempo. Ahora
// enseña a distinguir de dónde viene una respuesta, y estas comprobaciones
// cuidan que los tres sitios sigan contrastándose.
const bloque1S1 = laboratoriosS1.slice(0, 4).join('\n');
for (const [patron, que] of [
  [/chat/i, 'el chat a secas'],
  [/cuaderno|NotebookLM/i, 'el cuaderno con documentos'],
  [/busque en internet|búsqueda/i, 'la búsqueda en internet'],
]) {
  patron.test(bloque1S1)
    ? ok(`sesión 1: el bloque 1 contrasta ${que}`)
    : fail(`sesión 1: el bloque 1 ya no contrasta ${que}`);
}
/cita|citas|frase exacta/i.test(bloque1S1)
  ? ok('sesión 1: el bloque 1 exige citar la fuente')
  : fail('sesión 1: el bloque 1 ya no exige citar la fuente');

// Los hechos del bloque salen de los materiales. Si alguien edita la política o
// el procedimiento, el laboratorio enseñaría un dato falso y nadie lo notaría.
const leerDocx = (ruta) => JSON.parse(
  execFileSync('python3', ['build/office_reader.py', 'docx', ruta],
    { encoding: 'utf8', maxBuffer: 8 * 1024 * 1024 })).text;

const politica = leerDocx('materiales/03_politica_garantia.docx');
const plazoMoto = (politica.match(/Batería de moto:\s*(\d+)\s*meses/i) || [])[1];
plazoMoto === '6'
  ? ok(`sesión 1: la política sigue dando ${plazoMoto} meses a la batería de moto`)
  : fail(`sesión 1: la política da ${plazoMoto} meses a la moto; el laboratorio 1 dice seis`);
/ocho meses/i.test(bloque1S1) && plazoMoto === '6'
  ? ok('sesión 1: el caso de ocho meses sigue quedando fuera de plazo')
  : fail('sesión 1: el caso de garantía ya no queda fuera de plazo');

const vigente = leerDocx('materiales/expediente-PR-ADM-014/PR-ADM-014_Gestion_de_Cotizaciones_v2.docx');
const borrador = leerDocx('materiales/10_PR-ADM-014_v3_BORRADOR.docx');
const umbral = (texto) => {
  const m = texto.match(/supera los\s*([\d.,]+)\s*dólares/i);
  return m ? Number(m[1].replace(/[.,]/g, '')) : null;
};
const umbralVigente = umbral(vigente);
const umbralBorrador = umbral(borrador);
const montoCaso = 4200;
(umbralVigente && umbralBorrador && umbralVigente < montoCaso && montoCaso < umbralBorrador)
  ? ok(`sesión 1: 4.200 sigue cayendo entre el umbral vigente (${umbralVigente}) y el del borrador (${umbralBorrador})`)
  : fail(`sesión 1: con umbrales ${umbralVigente} y ${umbralBorrador}, una cotización de 4.200 ya no distingue las dos versiones`);

/4\.200/.test(bloque1S1)
  ? ok('sesión 1: el laboratorio 2 usa el monto que separa las dos versiones')
  : fail('sesión 1: el laboratorio 2 ya no usa el monto de 4.200');

// El anexo que se cita y no existe es lo que el laboratorio 3 hace descubrir.
const anexosQueExisten = readdirSync('materiales/expediente-PR-ADM-014')
  .map(n => (n.match(/ANEXO-([A-Z])/i) || n.match(/Anexo ([A-Z])/) || [])[1])
  .filter(Boolean).map(l => l.toUpperCase());
const citaAnexoE = /Anexo E/i.test(vigente);
(citaAnexoE && !anexosQueExisten.includes('E'))
  ? ok('sesión 1: el procedimiento sigue citando el Anexo E, que no está en el expediente')
  : fail('sesión 1: el Anexo E ya no es una referencia rota; el laboratorio 3 pierde su hallazgo');

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

// Las cuatro necesidades siguen cubiertas, sin atarlas a un bloque fijo: el
// reparto puede cambiar, lo que no puede es que una necesidad se caiga.
for (const [patron, pedido] of [
  [/instrucción explícita|ejemplos|elegir, no acumular/i, '«qué prompts usar» · 3 de 5 respondientes'],
  [/tu estilo|suene a ti/i, '«que no se vea que es IA»'],
  [/tablero|gráfico que se entiende|cinco cifras/i, '«ejemplo de dashboard o gráficos» · 3 de 5'],
  [/nombres|anexo|procedimiento/i, '«nomenclatura y códigos de procedimientos»'],
]) {
  patron.test(laboratoriosS3.join('\n'))
    ? ok(`sesión 3: sigue respondiendo ${pedido}`)
    : fail(`sesión 3: ya no responde ${pedido}`);
}

// Lo que separa un laboratorio profesional de un ejercicio suelto: cada uno
// declara qué técnica practica, y la técnica está fichada en el material de
// consulta con su fuente.
const sinTecnica = laboratoriosS3.filter(section => !/TÉCNICAS?\s+[\d\s,Y]+·/.test(section));
sinTecnica.length === 0
  ? ok('sesión 3: los 16 laboratorios declaran qué técnica practican')
  : fail(`sesión 3: ${sinTecnica.length} laboratorio(s) no declaran técnica`);

const TECNICAS = ['INSTRUCCIÓN EXPLÍCITA', 'EJEMPLOS', 'TU ESTILO', 'DELIMITADORES',
                  'ORDEN', 'QUE CITE ANTES', 'COLUMNAS', 'PARTIR Y ENCADENAR'];
const practicadas = TECNICAS.filter(t => new RegExp(t, 'i').test(s3));
practicadas.length >= 7
  ? ok(`sesión 3: practica ${practicadas.length} de las ${TECNICAS.length} técnicas del material`)
  : fail(`sesión 3: solo practica ${practicadas.length} técnicas; se esperaban al menos 7`);

// Las tres casas tienen que seguir citadas: es lo que separa esto de una opinión.
for (const casa of ['GOOGLE', 'OPENAI', 'ANTHROPIC']) {
  new RegExp(casa, 'i').test(s3)
    ? ok(`sesión 3: cita a ${casa.toLowerCase()}`)
    : fail(`sesión 3: ya no cita a ${casa.toLowerCase()}`);
}

existsSync('materiales/17_tecnicas_y_cuando_usarlas.docx')
  ? ok('materiales/17_tecnicas_y_cuando_usarlas.docx: presente')
  : fail('materiales/17_tecnicas_y_cuando_usarlas.docx: falta');

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
