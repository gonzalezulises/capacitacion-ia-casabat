#!/usr/bin/env node
// Compuerta del archivo de cotizaciones de la sesión 1, laboratorio 7.
//
// Por qué existe: el laboratorio publica cuántas cotizaciones llevan más de dos
// semanas sin respuesta y cuánto dinero hay en juego. Si alguien regenera el
// archivo o edita una fila y esas cifras se quedan viejas, el ejercicio enseña
// un dato falso que suena razonable. Aquí se recalculan desde el archivo.
//
// Comprueba además que el patrón del ejercicio siga en pie: el descuento alto
// no mejora la conversión. Sin eso, el laboratorio no tiene nada que descubrir.
//
// Uso: node verifica-cotizaciones.mjs   ·   Sale 1 si algo falla.

import { existsSync, readFileSync } from 'node:fs';
import { execFileSync } from 'node:child_process';

const ARCHIVO = 'materiales/21_cotizaciones_semestre.xlsx';
const DECK = 'sesion-3.html';
const DIAS_SIN_RESPUESTA = 14;

const fails = [];
const oks = [];
const ok = (m) => oks.push(m);
const fail = (m) => fails.push(m);

if (!existsSync(ARCHIVO)) {
  console.log(`  FALLA ${ARCHIVO}: no existe`);
  process.exit(1);
}

const libro = JSON.parse(execFileSync('python3', ['build/office_reader.py', 'xlsx', ARCHIVO],
  { encoding: 'utf8', maxBuffer: 16 * 1024 * 1024 }));
const filas = libro.rows.filter((r) => String(r.n).trim() !== '');

const numero = (v) => {
  const s = String(v).replace(/,/g, '').trim();
  if (s === '') return null;
  const n = Number(s);
  return Number.isNaN(n) ? null : n;
};

filas.length >= 60
  ? ok(`${filas.length} cotizaciones en el archivo`)
  : fail(`solo ${filas.length} cotizaciones; el laboratorio necesita al menos 60`);

// --- el patrón que el laboratorio hace descubrir ---
const tramo = (lo, hi) => filas.filter((r) => {
  const d = numero(r.descuento_pct);
  return d !== null && d >= lo && d <= hi;
});
const conversion = (grupo) =>
  grupo.length ? grupo.filter((r) => r.estado === 'Ganada').length / grupo.length : 0;

const moderado = tramo(10, 12);
const alto = tramo(13, 100);
const porcentaje = (x) => (x * 100).toFixed(1);

conversion(alto) < conversion(moderado)
  ? ok(`el descuento alto sigue convirtiendo peor: ${porcentaje(conversion(alto))} % contra ` +
       `${porcentaje(conversion(moderado))} % del tramo moderado`)
  : fail(`el descuento alto ya no convierte peor (${porcentaje(conversion(alto))} % contra ` +
         `${porcentaje(conversion(moderado))} %): el laboratorio se queda sin hallazgo`);

// --- las cifras que el deck publica ---
const vencidas = filas.filter((r) => {
  const d = numero(r.dias_sin_respuesta);
  return d !== null && d > DIAS_SIN_RESPUESTA && r.estado !== 'Ganada';
});
const importeVencido = vencidas.reduce((a, r) => a + (numero(r.importe_usd) || 0), 0);

if (!existsSync(DECK)) {
  fail(`${DECK}: no existe, no se puede contrastar lo publicado`);
} else {
  const visible = readFileSync(DECK, 'utf8').replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ');

  const totalPublicado = visible.match(/Sesenta y dos|(\d+)\s+cotizaciones del semestre/i);
  totalPublicado
    ? ok(`${DECK}: declara el total de cotizaciones`)
    : fail(`${DECK}: el laboratorio no dice cuántas cotizaciones trae el archivo`);

  const sinRespuesta = visible.match(/([A-Za-zÁÉÍÓÚáéíóúÑñ]+|\d+)\s+llevan más de dos semanas sin\s+respuesta/i);
  if (!sinRespuesta) {
    fail(`${DECK}: el laboratorio no publica cuántas llevan más de dos semanas sin respuesta`);
  } else {
    const PALABRAS = { doce: 12, trece: 13, catorce: 14, quince: 15, dieciséis: 16,
                       diecisiete: 17, dieciocho: 18, diecinueve: 19, veinte: 20 };
    const declarado = PALABRAS[sinRespuesta[1].toLowerCase()] ?? Number(sinRespuesta[1]);
    declarado === vencidas.length
      ? ok(`${DECK}: las ${vencidas.length} sin respuesta coinciden con el archivo`)
      : fail(`${DECK} dice ${declarado} sin respuesta; el archivo tiene ${vencidas.length}`);
  }

  const miles = Math.round(importeVencido / 1000);
  new RegExp(`${miles}\\.000|${miles - 1}\\.000|${miles + 1}\\.000`).test(visible)
    ? ok(`${DECK}: el importe en juego coincide con el archivo (${importeVencido.toFixed(0)} USD)`)
    : fail(`${DECK}: el importe de las vencidas es ${importeVencido.toFixed(0)} USD y no coincide con lo publicado`);
}

// --- los defectos puestos a propósito siguen ahí ---
const DEFECTOS = {
  'importe guardado como texto': filas.filter((r) => typeof r.importe_usd === 'string' &&
    /,/.test(r.importe_usd)).length,
  'margen imposible': filas.filter((r) => (numero(r.margen_pct) || 0) > 100).length,
  'días sin respuesta en blanco': filas.filter((r) => String(r.dias_sin_respuesta).trim() === '').length,
  'fechas en dos formatos': new Set(filas.map((r) => /^\d{4}-/.test(String(r.fecha_envio)) ? 'iso' : 'otro')).size,
  'cotizaciones duplicadas': filas.length - new Set(filas.map((r) => r.cotizacion)).size,
};
for (const [etiqueta, n] of Object.entries(DEFECTOS)) {
  n > (etiqueta === 'fechas en dos formatos' ? 1 : 0)
    ? ok(`defecto presente: ${etiqueta} (${n})`)
    : fail(`el archivo ya no tiene ${etiqueta}: el laboratorio pierde ese caso`);
}

console.log(oks.map((o) => `  ok   ${o}`).join('\n'));
if (fails.length) {
  console.log('\n' + fails.map((f) => `  FALLA ${f}`).join('\n'));
  console.log(`\n${fails.length} problema(s). ${oks.length} comprobaciones correctas.`);
  process.exit(1);
}
console.log(`\nCotizaciones correctas: ${oks.length} comprobaciones.`);
