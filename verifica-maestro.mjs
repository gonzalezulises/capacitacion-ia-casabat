#!/usr/bin/env node
// Compuerta del maestro de procedimientos de la sesión 3.
//
// Por qué existe: los laboratorios 13 y 14 publican cuántos fallos tiene el
// archivo. Si alguien edita una fila del Excel y la cifra del deck se queda
// vieja, el ejercicio enseñaría una respuesta falsa que suena razonable. Esto
// vuelve a contar los fallos desde el archivo y compara con lo que dice el deck.
//
// La regla aplicada es la de materiales/09_reglas_de_nomenclatura.docx.
// Uso: node verifica-maestro.mjs   ·   Sale 1 si algo falla.

import { existsSync, readFileSync } from 'node:fs';
import { execFileSync } from 'node:child_process';

const MAESTRO = 'materiales/16_maestro_procedimientos.xlsx';
const DECK = 'sesion-3.html';

const fails = [];
const oks = [];
const ok = (m) => oks.push(m);
const fail = (m) => fails.push(m);

if (!existsSync(MAESTRO)) {
  console.log(`  FALLA ${MAESTRO}: no existe`);
  process.exit(1);
}

// El lector de Office del repo devuelve JSON estable y no necesita openpyxl.
const crudo = execFileSync('python3', ['build/office_reader.py', 'xlsx', MAESTRO],
  { encoding: 'utf8', maxBuffer: 8 * 1024 * 1024 });
const libro = JSON.parse(crudo);

// La cabecera real empieza en la fila 4: las dos primeras son título y nota.
const filas = libro.rows
  .map((fila) => Object.values(fila).map((v) => String(v).trim()))
  .filter((valores) => /^\d+$/.test(valores[0]));

const AREAS = new Set(['ADM', 'COM', 'OPE', 'FIN']);
const NOMBRE_OK = /^PR-([A-Z]+)-(\d+)_([^_]+(?:_[^_]+)*)_v(\d+)\.docx$/;
const SIN_TILDES = /^[A-Za-z0-9_]+$/;

const registros = filas.map(([n, archivo, codigo, titulo, area, estado, vigencia, dueno,
                              citados, revision, existentes]) => ({
  n: Number(n), archivo, codigo, titulo, area, estado, vigencia, dueno,
  citados: citados ? citados.split(';').map((s) => s.trim()).filter(Boolean) : [],
  revision,
  existentes: existentes ? existentes.split(';').map((s) => s.trim()).filter(Boolean) : [],
}));

registros.length >= 40
  ? ok(`${registros.length} procedimientos en el maestro`)
  : fail(`solo ${registros.length} filas; el laboratorio necesita al menos 40`);

// --- fallos de nombre, uno por archivo ---
function fallosDeNombre(r) {
  const malos = [];
  const m = r.archivo.match(NOMBRE_OK);
  if (!m) {
    if (!/\.docx$/.test(r.archivo)) malos.push('extensión');
    if (!/^PR-/.test(r.archivo)) malos.push('no empieza por PR-');
    if (/^PR_/.test(r.archivo)) malos.push('guion bajo en el código');
    if (!/_v\d+\./.test(r.archivo)) malos.push('versión');
    if (malos.length === 0) malos.push('estructura del nombre');
    return malos;
  }
  const [, area, correlativo, titulo] = m;
  if (!AREAS.has(area)) malos.push(`área «${area}»`);
  if (correlativo.length !== 3) malos.push(`correlativo «${correlativo}»`);
  if (!SIN_TILDES.test(titulo)) malos.push('título con espacios o tildes');
  return malos;
}

const conFalloDeNombre = registros.filter((r) => fallosDeNombre(r).length > 0);

// --- fallos que no se ven en el nombre ---
const codigoDelNombre = (archivo) => (archivo.match(/^PR[-_]([A-Z]+)[-_](\d+)/) || [])
  .slice(1).join('-').replace(/^/, 'PR-');

const codigoDistinto = registros.filter((r) => {
  const delNombre = codigoDelNombre(r.archivo);
  return delNombre && r.codigo && delNombre.replace(/-0*/g, '-') !== r.codigo.replace(/-0*/g, '-');
});

const porCodigo = {};
for (const r of registros.filter((x) => x.estado === 'Vigente')) {
  porCodigo[r.codigo] = (porCodigo[r.codigo] || 0) + 1;
}
const codigosDuplicados = Object.entries(porCodigo).filter(([, n]) => n > 1);

const citadosQueNoExisten = registros.filter((r) =>
  r.citados.some((a) => !r.existentes.includes(a)));
const existentesSinCitar = registros.filter((r) =>
  r.existentes.some((a) => !r.citados.includes(a)));

const letra = (a) => a.replace('ANEXO-', '');
const conSaltoDeLetra = registros.filter((r) => {
  const letras = r.citados.map(letra).filter((l) => /^[A-Z]$/.test(l)).sort();
  if (letras.length === 0) return false;
  const esperado = letras.map((_, i) => String.fromCharCode(65 + i));
  return letras.join('') !== esperado.join('');
});

const sinEstado = registros.filter((r) => r.estado === '');
const sinVigencia = registros.filter((r) => r.estado === 'Vigente' && r.vigencia === '');
const sinDueno = registros.filter((r) => r.dueno === '');
const borradorComoVigente = registros.filter((r) =>
  /BORRADOR/i.test(r.archivo) && r.estado === 'Vigente');
const revisionAnterior = registros.filter((r) =>
  r.vigencia && r.revision && r.revision < r.vigencia);

const CONTEOS = {
  'filas con el nombre mal puesto': conFalloDeNombre.length,
  'código de dentro distinto al del archivo': codigoDistinto.length,
  'códigos vigentes repetidos': codigosDuplicados.length,
  'anexos citados que no existen': citadosQueNoExisten.length,
  'anexos que existen y nadie cita': existentesSinCitar.length,
  'anexos con salto de letra': conSaltoDeLetra.length,
  'sin estado': sinEstado.length,
  'vigente sin fecha de vigencia': sinVigencia.length,
  'sin dueño': sinDueno.length,
  'borrador marcado vigente': borradorComoVigente.length,
  'revisado antes de entrar en vigencia': revisionAnterior.length,
};

console.log('  --- lo que el archivo contiene hoy ---');
for (const [etiqueta, n] of Object.entries(CONTEOS)) {
  console.log(`      ${String(n).padStart(3)}  ${etiqueta}`);
}
console.log(`      ${String(conFalloDeNombre.length).padStart(3)}  detalle de nombres:`);
for (const r of conFalloDeNombre) {
  console.log(`           ${r.archivo} → ${fallosDeNombre(r).join(', ')}`);
}

// Cada tipo de fallo tiene que estar presente: si una edición los borra, el
// laboratorio se queda sin nada que encontrar.
for (const [etiqueta, n] of Object.entries(CONTEOS)) {
  if (n === 0) fail(`el maestro ya no tiene ${etiqueta}: el laboratorio pierde ese caso`);
}
if (Object.values(CONTEOS).every((n) => n > 0)) {
  ok(`los ${Object.keys(CONTEOS).length} tipos de fallo siguen presentes en el archivo`);
}

// --- la cifra publicada en el deck coincide con el recuento real ---
if (!existsSync(DECK)) {
  fail(`${DECK}: no existe, no se puede contrastar la cifra publicada`);
} else {
  const html = readFileSync(DECK, 'utf8');
  const visible = html.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ');

  const esperadoNombres = conFalloDeNombre.length;
  const declarado = visible.match(/(\d+)\s+de\s+los\s+41\s+nombres/);
  if (!declarado) {
    fail(`${DECK}: no publica cuántos nombres están mal puestos (falta «N de los 41 nombres»)`);
  } else if (Number(declarado[1]) !== esperadoNombres) {
    fail(`${DECK} dice «${declarado[1]} de los 41 nombres», pero el archivo tiene ${esperadoNombres}`);
  } else {
    ok(`${DECK}: la cifra publicada (${esperadoNombres} nombres mal puestos) coincide con el archivo`);
  }

  const filasDeclaradas = visible.match(/(\d+)\s+procedimientos/);
  if (filasDeclaradas && Number(filasDeclaradas[1]) !== registros.length) {
    fail(`${DECK} dice «${filasDeclaradas[1]} procedimientos», pero el archivo tiene ${registros.length}`);
  } else if (filasDeclaradas) {
    ok(`${DECK}: el total de procedimientos coincide con el archivo (${registros.length})`);
  }
}

console.log('\n' + oks.map((o) => `  ok   ${o}`).join('\n'));
if (fails.length) {
  console.log('\n' + fails.map((f) => `  FALLA ${f}`).join('\n'));
  console.log(`\n${fails.length} problema(s). ${oks.length} comprobaciones correctas.`);
  process.exit(1);
}
console.log(`\nMaestro correcto: ${oks.length} comprobaciones.`);
