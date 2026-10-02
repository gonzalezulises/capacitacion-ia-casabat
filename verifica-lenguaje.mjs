#!/usr/bin/env node
// Compuerta de lenguaje de la sesión 3.
//
// Por qué existe: en las sesiones anteriores los laboratorios quedaron escritos
// en un registro que el participante no usa — «la operación cognitiva y el
// artefacto que produce», «contrato de datos y bitácora localizable», palabras
// sueltas en mayúsculas como DETERMINISTA. Nadie lo notó al generar el deck
// porque ningún verificador miraba el lenguaje. Este sí.
//
// Lo que comprueba, en el texto que el participante lee:
//   1. Ninguna frase pasa de 25 palabras.
//   2. No aparece jerga de la lista negra, que tiene alternativa en español llano.
//   3. El cuerpo de un laboratorio no grita conceptos en mayúsculas.
//   4. Cada laboratorio nombra algo real de Casa de las Baterías.
//   5. La situación de cada laboratorio se lee de un tirón.
//
// Uso: node verifica-lenguaje.mjs   ·   Sale 1 si algo falla.

import { readFileSync, existsSync } from 'node:fs';

const DECK = 'sesion-3.html';
const MAX_PALABRAS_FRASE = 25;
const MAX_PALABRAS_SITUACION = 45;
const MAX_PALABRAS_PASO = 22;

const fails = [];
const oks = [];
const ok = (m) => oks.push(m);
const fail = (m) => fails.push(m);

// Jerga que no entra. Cada entrada va con la alternativa que sí se usa, porque
// una lista negra sin alternativa se vuelve un acertijo para quien la encuentra.
const JERGA = [
  ['artefacto', 'di qué cosa es: el correo, la tabla, el tablero'],
  ['operación cognitiva', 'di qué hace la persona: comparar, decidir, revisar'],
  ['reproducible', '«que otra persona pueda repetirlo»'],
  ['determinista', '«la regla es fija: se cumple o no se cumple»'],
  ['inyección de prompts', '«el archivo trae instrucciones escondidas»'],
  ['taxonomía', '«lista de nombres buenos»'],
  ['canónic', '«el nombre que vale»'],
  ['bitácora', '«registro» o «lista de lo que encontraste»'],
  ['trazabilidad', '«se puede llegar al dato que lo sostiene»'],
  ['granular', '«con más detalle»'],
  ['accionable', '«que se puede usar tal cual»'],
  ['holístic', '«completo»'],
  ['sinergia', 'di qué gana cada parte'],
  ['paradigma', '«forma de trabajar»'],
  ['framework', '«plantilla» o «guía»'],
  ['workflow', '«flujo de trabajo»'],
  ['pipeline', '«cadena de pasos»'],
  ['insight', '«hallazgo» o «lo que descubriste»'],
  ['deliverable', '«lo que entregas»'],
  ['stakeholder', 'di quién: tu jefatura, el cliente, Mercadeo'],
  ['quick win', '«algo que se resuelve rápido»'],
  ['deep dive', '«revisar a fondo»'],
  ['empoderar', 'di qué puede hacer ahora'],
  ['socializar', '«contarlo» o «compartirlo»'],
  ['operacionaliz', '«ponerlo a funcionar»'],
  ['instanciar', '«crear uno»'],
  ['parametriz', '«dejar el dato editable»'],
  ['orquestar', '«encadenar»'],
  ['idempotente', '«se puede repetir sin romper nada»'],
  ['capacidad instalada', 'di qué queda funcionando y quién lo usa'],
  ['valor agregado', 'di qué gana la persona'],
  ['a nivel de', '«en» o «para»'],
  ['en términos de', '«en» o «sobre»'],
  ['de cara a', '«para»'],
  ['poner en valor', '«mostrar lo que vale»'],
  ['dicha ', '«esa» / «ese»'],
  ['el mismo mencionado', '«ese»'],
  ['cabe destacar', 'dilo directo'],
  ['es importante mencionar', 'dilo directo'],
  ['en el dinámico mundo', 'empieza por el hecho'],
  ['en la era digital', 'empieza por el hecho'],
];

// Palabras del negocio. Un laboratorio que no nombra ninguna está contextualizado
// en el aire, y eso fue lo que se pidió no repetir.
const CASABAT = [
  'vía españa', 'tocumen', 'david', 'soyapango', 'santa ana', 'alajuela', 'heredia',
  'mixco', 'quetzaltenango', 'san josé', 'san salvador', 'zona 4', 'sucursal',
  'batería', 'baterías', 'cotización', 'cotizaciones', 'garantía', 'flota', 'flotas',
  'domicilio', 'energía solar', 'respaldo de energía', 'montacarga', 'moto',
  'panamá', 'guatemala', 'costa rica', 'el salvador', 'casabat', 'casa de las baterías',
  'cierre de caja', 'proveedor', 'inventario', 'procedimiento', 'anexo', 'reclamo',
];

// Rótulos del molde del deck: van en mayúsculas por diseño, no son jerga gritada.
const ROTULOS = new Set([
  'CONCEPTO', 'CLAVE', 'PASO', 'RESULTADO', 'ESPERADO', 'SITUACIÓN', 'CASABAT',
  'DECISIÓN', 'CRITERIO', 'ENTREGABLE', 'LABORATORIO', 'EJERCICIO', 'HERRAMIENTA',
  'ROL', 'ENTRADA', 'IA', 'AGENDA', 'SESIÓN', 'BLOQUE', 'APLICACIÓN', 'PRÁCTICA',
  'INDIVIDUAL', 'MATERIAL', 'CONSULTA', 'PROMPT', 'DEL', 'PARTICIPANTE', 'LA', 'DE',
  'MIN', 'MINUTOS', 'ARCHIVOS', 'DATOS', 'DOCUMENTOS', 'REGLAS', 'TALLER', 'CIERRE',
  'PROGRAMA', 'PUNTO', 'PARTIDA', 'Y', 'EN', 'CON', 'SIN', 'LOS', 'LAS', 'UN', 'UNA',
  'QUÉ', 'CÓMO', 'ANTES', 'RECETA', 'OPCIÓN', 'GEMINI', 'CHATGPT', 'CLAUDE', 'EXCEL',
  'SHEETS', 'DRIVE', 'CANVAS', 'COPIA', 'PEGA', 'TU', 'SE', 'A', 'O', 'NO', 'ES',
]);

if (!existsSync(DECK)) {
  console.log(`  FALLA ${DECK}: no existe`);
  process.exit(1);
}
const html = readFileSync(DECK, 'utf8');

const sinEtiquetas = (s) => s
  .replace(/<br\s*\/?>/gi, ' ')
  .replace(/<[^>]+>/g, ' ')
  .replace(/&nbsp;/g, ' ')
  .replace(/&amp;/g, '&')
  .replace(/&hellip;/g, '…')
  .replace(/\s+/g, ' ')
  .trim();

const visible = (s) => sinEtiquetas(
  s.replace(/<style[\s\S]*?<\/style>/gi, ' ')
   .replace(/<script[\s\S]*?<\/script>/gi, ' ')
   .replace(/<!--[\s\S]*?-->/g, ' ')
);

const palabras = (s) => s.split(/\s+/).filter(Boolean).length;

// La longitud se mide por párrafo escrito, no sobre el slide entero: un rótulo
// («SITUACIÓN CASABAT»), el pie de página y el riel no son prosa, y pegados unos
// a otros fingen frases larguísimas que nadie escribió.
function parrafos(fuente) {
  const limpio = fuente
    .replace(/<style[\s\S]*?<\/style>/gi, ' ')
    .replace(/<script[\s\S]*?<\/script>/gi, ' ')
    .replace(/<!--[\s\S]*?-->/g, ' ')
    .replace(/<div class="footer">[\s\S]*?<\/div>\s*<\/div>/g, ' ')
    .replace(/<div class="top-rail">[\s\S]*?<\/div>/g, ' ')
    .replace(/<span class="label[^"]*">[^<]*<\/span>/g, ' ')
    .replace(/<b>[A-ZÁÉÍÓÚÑ\s]{3,}<\/b>/g, ' ')      // rótulos en versalita
    .replace(/<span>[A-ZÁÉÍÓÚÑ\s·\/\d]+<\/span>/g, ' ');

  const trozos = [];
  const empujar = (texto) => {
    const t = sinEtiquetas(texto);
    if (palabras(t) > 2) trozos.push(t);
  };

  // Contenedores que de verdad llevan texto escrito por una persona.
  for (const clase of ['situation', 'decision', 'concept', 'criterion', 'caveat', 'observa']) {
    for (const m of limpio.matchAll(new RegExp(`class="${clase}"[^>]*>([\\s\\S]*?)</(?:div|p)>`, 'g'))) {
      empujar(m[1]);
    }
  }
  // «Entregable» lleva el criterio anidado: se corta antes para no contarlo dos veces.
  for (const m of limpio.matchAll(/<div class="result">([\s\S]*?)<\/div>/g)) {
    empujar(m[1].split('<div class="criterion"')[0]);
  }
  for (const etiqueta of ['p', 'li', 'h1', 'h2', 'h3']) {
    for (const m of limpio.matchAll(new RegExp(`<${etiqueta}\\b[^>]*>([\\s\\S]*?)</${etiqueta}>`, 'g'))) {
      empujar(m[1]);
    }
  }
  return trozos;
}

// Las frases se cortan en punto, pero no en los puntos de una cifra (3.000) ni
// de una abreviatura de archivo (.docx), que no terminan una oración.
function frases(texto) {
  return texto
    .replace(/(\d)\.(\d)/g, '$1·$2')
    .replace(/\.(docx|xlsx|html|csv|pdf|js|mjs)/gi, '·$1')
    .split(/(?<=[.:;?!])\s+|\s+·\s+|\s+—\s+/)
    .map((f) => f.trim())
    .filter((f) => palabras(f) > 2);
}

const texto = visible(html);

// --- 1. frases largas ---
const prosa = parrafos(html);
const largas = prosa.flatMap(frases).filter((f) => palabras(f) > MAX_PALABRAS_FRASE);
largas.length === 0
  ? ok(`ninguna de las ${prosa.length} piezas de texto tiene una frase de más de ${MAX_PALABRAS_FRASE} palabras`)
  : largas.slice(0, 6).forEach((f) =>
      fail(`frase de ${palabras(f)} palabras: «${f.slice(0, 130)}…»`));
if (largas.length > 6) fail(`…y ${largas.length - 6} frase(s) larga(s) más`);

// --- 2. jerga ---
const enBajo = texto.toLowerCase();
const encontrada = JERGA.filter(([termino]) => enBajo.includes(termino));
encontrada.length === 0
  ? ok(`sin jerga: ${JERGA.length} términos de la lista negra ausentes`)
  : encontrada.forEach(([termino, alternativa]) =>
      fail(`dice «${termino}» — usa ${alternativa}`));

// --- laboratorios ---
const secciones = html.split(/(?=<section\b)/).slice(1);
const labs = secciones.filter((s) => s.includes('class="ex-num"'));
labs.length === 16
  ? ok('16 laboratorios para revisar')
  : fail(`hay ${labs.length} laboratorios; se esperaban 16`);

const tituloDe = (s) => (s.match(/<h2 class="ex-title">([^<]+)</) || [, '?'])[1];
const bloqueDe = (s, clase) => {
  const m = s.match(new RegExp(`<div class="${clase}">([\\s\\S]*?)</div>`));
  return m ? sinEtiquetas(m[1]) : '';
};

// --- 3. mayúsculas-concepto en el cuerpo del laboratorio ---
// Un nombre de archivo o de código va en <code> y puede llevar mayúsculas con
// todo derecho (PR-OPE-190_..._BORRADOR.docx). Eso no es gritar: se excluye.
// Fuera del análisis: los nombres de archivo y los rótulos que pone el molde
// («QUÉ TIENES QUE DECIDIR», «CON QUÉ SALES»). Ninguno lo escribe el redactor
// del laboratorio, así que no son suyos ni puede arreglarlos desde el texto.
const sinCodigo = (s) => s
  .replace(/<code>[\s\S]*?<\/code>/g, ' ')
  .replace(/<span class="label[^"]*">[^<]*<\/span>/g, ' ')
  .replace(/<b>[A-ZÁÉÍÓÚÑ\s]{3,}<\/b>/g, ' ')
  .replace(/<span>[A-ZÁÉÍÓÚÑ\s·\/\d]+<\/span>/g, ' ');
let gritos = 0;
for (const bruto of labs) {
  const s = sinCodigo(bruto);
  const cuerpo = [bloqueDe(s, 'situation'), bloqueDe(s, 'decision'),
                  ...[...s.matchAll(/<li>([\s\S]*?)<\/li>/g)].map((m) => sinEtiquetas(m[1])),
                  ...[...s.matchAll(/<p>([\s\S]*?)<\/p>/g)].map((m) => sinEtiquetas(m[1]))].join(' ');
  const mayus = [...new Set(cuerpo.match(/\b[A-ZÁÉÍÓÚÑ]{4,}\b/g) || [])]
    .filter((w) => !ROTULOS.has(w));
  if (mayus.length) {
    gritos += mayus.length;
    fail(`«${tituloDe(bruto)}» grita en mayúsculas: ${mayus.join(', ')} — escríbelo normal`);
  }
}
if (gritos === 0) ok('ningún laboratorio grita conceptos en mayúsculas');

// --- 3b. nada de dar por visto lo que no vieron ---
// El grupo llega nuevo: no ha hecho las otras sesiones ni conoce los archivos.
// Un slide que diga «ya los conoces» deja fuera a toda la sala.
const SUPUESTOS = [
  ['ya los conoces', 'agrupa los archivos por para qué sirven, no por si son nuevos'],
  ['ya conoces', 'no des por visto nada: el grupo llega nuevo'],
  ['nuevos en esta sesión', '«nuevo» solo tiene sentido si vieron los anteriores'],
  ['archivos nuevos', 'para ellos todos son nuevos'],
  ['como vimos', 'no hubo un antes'],
  ['como ya sabes', 'no lo des por sabido'],
  ['ya saben', 'no lo des por sabido'],
  ['recordarás', 'no hay nada que recordar'],
  ['la sesión anterior', 'esta sesión se da suelta'],
  ['sesión pasada', 'esta sesión se da suelta'],
  ['en la sesión 1', 'puede que no la hayan hecho'],
  ['en la sesión 2', 'puede que no la hayan hecho'],
];
const supuestos = SUPUESTOS.filter(([frase]) => enBajo.includes(frase));
supuestos.length === 0
  ? ok(`no da por visto nada: ${SUPUESTOS.length} fórmulas de conocimiento previo ausentes`)
  : supuestos.forEach(([frase, por_que]) =>
      fail(`dice «${frase}» — ${por_que}`));

// --- 3c. el deck no juzga a quien lo lee ---
// La segunda lámina llegó a decir «lo que falta es el criterio» y «corregir tres
// veces lo que podía salir bien a la primera». Eso es un diagnóstico sobre los
// participantes, hecho antes de que abran la boca. El material enseña una
// técnica; no califica a la sala.
const JUICIOS = [
  ['lo que falta es el criterio', 'di qué suma la técnica, no qué le falta a la persona'],
  ['nadie es principiante', 'suena a que se les mide; di que el grupo arranca con ventaja'],
  ['no tienen criterio', 'nunca'],
  ['no saben', 'habla de lo que la herramienta no sabe, no la persona'],
  ['corregir tres veces', 'no retrates su trabajo como ineficiente'],
  ['el problema de ustedes', 'nunca'],
  ['lo hacen mal', 'nunca'],
  ['se equivocan al', 'habla del pedido, no de quien lo escribe'],
  ['deberían saber', 'nunca'],
  ['es una queja', 'califica el pedido sin descalificar a quien pregunta'],
];
const juicios = JUICIOS.filter(([frase]) => enBajo.includes(frase));
juicios.length === 0
  ? ok(`sin juicios sobre la sala: ${JUICIOS.length} fórmulas ausentes`)
  : juicios.forEach(([frase, por_que]) => fail(`juzga a los participantes: «${frase}» — ${por_que}`));

// --- 3d. la apertura habla de la herramienta, no de la audiencia ---
// Tres versiones seguidas de este slide describían a la sala: lo que ya usan,
// lo que les falta, el oficio que tienen. Nadie pidió ese diagnóstico. La
// apertura explica cómo funciona la herramienta y qué capacidades se
// desarrollan; de los asistentes no dice nada.
const apertura = html.split(/(?=<section\b)/)
  .filter((x) => /data-label="0[12]/.test(x)).join(' ');   // portada y punto de partida
const SOBRE_LA_SALA = ['ustedes', 'el grupo', 'los participantes', 'las cinco personas',
  'nadie es', 'ya usan', 'el oficio', 'arranca con ventaja', 'lo tienen', 'ya saben',
  'principiante', 'cada quien', 'la sala'];
const sobran = SOBRE_LA_SALA.filter((f) => visible(apertura).toLowerCase().includes(f));
sobran.length === 0
  ? ok('portada y apertura hablan de la herramienta, no de quien asiste')
  : sobran.forEach((f) => fail(`la apertura habla de la audiencia: «${f}» — descríbela técnicamente`));

// Y sí dice qué capacidades se desarrollan: es una apertura de curso.
/capacidades/i.test(visible(apertura))
  ? ok('la apertura enuncia las capacidades de la sesión')
  : fail('la apertura no dice qué capacidades se desarrollan');

// --- 3e. el criterio describe el resultado, no predice al modelo ---
// «La primera, ninguna» daba por hecho que el pedido vago fallaría. Si el
// modelo acierta, el ejercicio se cae. Un criterio dice qué tiene que tener el
// resultado para darlo por bueno; conseguirlo es trabajo del participante.
const PREDICE = [
  [/\bdetecta\b/i, 'describe lo que el resultado contiene, no lo que la IA hará'],
  [/\bencuentra\b/i, 'describe lo que el resultado contiene, no lo que la IA hará'],
  [/\bresponde que\b/i, 'di qué debe sostener la respuesta, no cuál será'],
  [/\breconoce\b/i, 'di qué distingue el resultado, no que el modelo lo reconozca'],
  [/\bdescubres\b/i, 'di con qué sale el participante, no qué le pasará'],
  [/\bno (trae|devuelve|dice)\b/i, 'no apuestes a que el modelo falle'],
];
let predicciones = 0;
for (const bruto of labs) {
  const criterio = bloqueDe(bruto, 'criterion');
  if (!criterio) continue;
  const titulo = (bruto.match(/<h2 class="ex-title">([^<]+)</) || [, '?'])[1];
  for (const [patron, consejo] of PREDICE) {
    if (patron.test(criterio)) {
      predicciones += 1;
      fail(`«${titulo}»: el criterio predice al modelo — ${consejo}`);
    }
  }
}
if (predicciones === 0) ok('los criterios describen el resultado, no predicen al modelo');

// --- 3f. sin superlativos que no se han medido ---
const SUPERLATIVOS = ['lo mejor del mercado', 'el mejor del mercado', 'la mejor del mercado',
  'el más potente', 'la más potente', 'sin rival', 'imbatible', 'el líder del mercado',
  'la mejor herramienta', 'insuperable'];
const presumidos = SUPERLATIVOS.filter((f) => enBajo.includes(f));
presumidos.length === 0
  ? ok(`sin superlativos sin prueba: ${SUPERLATIVOS.length} fórmulas ausentes`)
  : presumidos.forEach((f) => fail(`dice «${f}» sin una prueba comparativa que lo sostenga`));

// --- 4. cada laboratorio aterriza en CasaBat ---
const sinContexto = labs.filter((s) => {
  const t = visible(s).toLowerCase();
  return !CASABAT.some((p) => t.includes(p));
});
sinContexto.length === 0
  ? ok('los 16 laboratorios nombran algo real de Casa de las Baterías')
  : sinContexto.forEach((s) =>
      fail(`«${tituloDe(s)}» no nombra nada de CasaBat: ponle sucursal, producto o documento`));

// --- 5. la situación se lee de un tirón, y los pasos son órdenes cortas ---
let densos = 0;
for (const s of labs) {
  const situacion = bloqueDe(s, 'situation');
  if (palabras(situacion) > MAX_PALABRAS_SITUACION) {
    densos += 1;
    fail(`«${tituloDe(s)}»: la situación tiene ${palabras(situacion)} palabras (máximo ${MAX_PALABRAS_SITUACION})`);
  }
  const pasos = [...s.matchAll(/<ol class="steps">([\s\S]*?)<\/ol>/g)]
    .flatMap((m) => [...m[1].matchAll(/<li>([\s\S]*?)<\/li>/g)].map((x) => sinEtiquetas(x[1])));
  for (const paso of pasos) {
    if (palabras(paso) > MAX_PALABRAS_PASO) {
      densos += 1;
      fail(`«${tituloDe(s)}»: un paso tiene ${palabras(paso)} palabras (máximo ${MAX_PALABRAS_PASO}): «${paso.slice(0, 90)}…»`);
    }
  }
}
if (densos === 0) ok(`situaciones de ${MAX_PALABRAS_SITUACION} palabras o menos y pasos de ${MAX_PALABRAS_PASO} o menos`);

// --- 6. las tres herramientas tienen su propia receta de tablero y de gráfico ---
const recetas = secciones.filter((s) => /RECETA/.test(s));
for (const herramienta of ['Gemini', 'ChatGPT', 'Claude']) {
  const n = recetas.filter((s) => new RegExp(herramienta, 'i').test(s)).length;
  n >= 1
    ? ok(`${herramienta}: ${n} receta(s) propia(s)`)
    : fail(`${herramienta}: sin receta propia`);
}

// --- el bloque 1 de la sesión 1, reescrito con el mismo listón ---
// Solo esos cuatro laboratorios: el resto de esa sesión es anterior a esta
// compuerta y no se ha reescrito.
if (existsSync('sesion-1.html')) {
  const s1 = readFileSync('sesion-1.html', 'utf8');
  const labs1 = s1.split(/(?=<section\b)/).slice(1)
    .filter((x) => x.includes('class="ex-num"')).slice(0, 4);
  labs1.length === 4
    ? ok('sesión 1: cuatro laboratorios en el bloque 1 para revisar')
    : fail(`sesión 1: ${labs1.length} laboratorios en el bloque 1`);

  const texto1 = labs1.map((x) => visible(x)).join(' ').toLowerCase();
  const jerga1 = JERGA.filter(([t]) => texto1.includes(t));
  jerga1.length === 0
    ? ok('sesión 1 · bloque 1: sin jerga de la lista negra')
    : jerga1.forEach(([t, alt]) => fail(`sesión 1 · bloque 1: dice «${t}» — usa ${alt}`));

  let problemas1 = 0;
  for (const bruto of labs1) {
    const x = sinCodigo(bruto);
    const titulo = (bruto.match(/<h2 class="ex-title">([^<]+)</) || [, '?'])[1];
    for (const f of parrafos(x).flatMap(frases)) {
      if (palabras(f) > MAX_PALABRAS_FRASE) {
        problemas1 += 1;
        fail(`sesión 1 · «${titulo}»: frase de ${palabras(f)} palabras`);
      }
    }
    const cuerpo = [bloqueDe(x, 'situation'), bloqueDe(x, 'decision'),
                    ...[...x.matchAll(/<li>([\s\S]*?)<\/li>/g)].map((m) => sinEtiquetas(m[1]))].join(' ');
    const gritos1 = [...new Set(cuerpo.match(/\b[A-ZÁÉÍÓÚÑ]{4,}\b/g) || [])].filter((w) => !ROTULOS.has(w));
    if (gritos1.length) {
      problemas1 += 1;
      fail(`sesión 1 · «${titulo}» grita: ${gritos1.join(', ')}`);
    }
    if (!CASABAT.some((c) => visible(bruto).toLowerCase().includes(c))) {
      problemas1 += 1;
      fail(`sesión 1 · «${titulo}» no nombra nada de CasaBat`);
    }
  }
  if (problemas1 === 0) ok('sesión 1 · bloque 1: frases cortas, sin gritos y anclado en CasaBat');
}

console.log(oks.map((o) => `  ok   ${o}`).join('\n'));
if (fails.length) {
  console.log('\n' + fails.map((f) => `  FALLA ${f}`).join('\n'));
  console.log(`\n${fails.length} problema(s) de lenguaje. ${oks.length} comprobaciones correctas.`);
  process.exit(1);
}
console.log(`\nLenguaje correcto: ${oks.length} comprobaciones.`);
