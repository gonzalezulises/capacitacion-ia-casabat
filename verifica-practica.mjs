#!/usr/bin/env node
// La guía de práctica publica respuestas exactas. Si un material cambia y la respuesta no,
// la guía enseña algo falso — y nadie lo nota, porque suena razonable.
// Esto recalcula cada cifra desde los archivos y la compara con lo que dice practica.html.

import { readFileSync, existsSync } from 'node:fs';
import { join } from 'node:path';
import { execFileSync } from 'node:child_process';

const M = 'materiales';
const EXP = join(M, 'expediente-PR-ADM-014');
const oks = [], fails = [];
const ok = (m) => oks.push(m);
const fail = (m) => fails.push(m);
const leer = (p) => readFileSync(p, 'utf8');
const leerOffice = (tipo, p) => JSON.parse(execFileSync('python3', ['build/office_reader.py', tipo, p], { encoding: 'utf8' }));
const sinTilde = (s) => s.normalize('NFKD').replace(/[̀-ͯ]/g, '');
const norm = (s) => sinTilde(String(s)).trim().toLowerCase().replace(/\s+/g, ' ');
const num = (s) => { const n = parseFloat(String(s).replace(/,/g, '').trim()); return isNaN(n) ? 0 : n; };

if (!existsSync('practica.html')) { console.log('  FALLA practica.html no existe'); process.exit(1); }
const G = leer('practica.html');
const dice = (txt, que) => G.includes(txt)
  ? ok(`la guía dice ${que}: «${txt}»`)
  : fail(`la guía NO dice ${que} — se esperaba «${txt}» y el archivo dice otra cosa`);

const retirados = [...G.matchAll(/href="([^"]+\.(?:md|csv))"/gi)].map(m => m[1]);
retirados.length === 0
  ? ok('la guía solo enlaza formatos Office')
  : fail(`la guía aún enlaza formatos retirados: ${[...new Set(retirados)].join(' · ')}`);

// --- filas del Excel de ventas
const filas = leerOffice('xlsx', join(M, '04_ventas_sucursales_2026.xlsx')).rows;
const mes = (f) => f.includes('/') ? `${f.slice(6, 10)}-${f.slice(3, 5)}` : f.slice(0, 7);

// EJ 11 · serie del servicio a domicilio
const dom = {};
for (const f of filas) if (norm(f.linea_producto) === 'servicio a domicilio') dom[mes(f.fecha)] = (dom[mes(f.fecha)] || 0) + num(f.unidades);
const serie = Object.keys(dom).sort().map(k => Math.round(dom[k]));
// en español la última va con «y»: se compara con el mismo formato que se publica
const enEs = (xs) => xs.join(', ').replace(/, (\S+)$/, ' y $1');
dice(`<b>${enEs(serie)}</b>`, 'la serie mensual del servicio a domicilio');
const caida = Math.round((1 - serie.at(-1) / serie[0]) * 100);
dice(`<b>${caida} %</b>`, 'la caída del servicio a domicilio');

// EJ 9 · devoluciones por país
const dv = {};
for (const f of filas) { const p = norm(f.pais); dv[p] = dv[p] || [0, 0]; dv[p][0] += num(f.devoluciones); dv[p][1] += num(f.unidades); }
const tasas = Object.entries(dv).filter(([, [, u]]) => u).map(([p, [d, u]]) => [p, d / u * 100]);
const gt = tasas.find(([p]) => p.includes('guatemala'))[1];
const resto = tasas.filter(([p]) => !p.includes('guatemala')).map(([, t]) => t);
dice(`<b>${gt.toFixed(2).replace('.', ',')} %</b>`, 'la tasa de devoluciones de Guatemala');
const rango = `${Math.min(...resto).toFixed(2).replace('.', ',')}–${Math.max(...resto).toFixed(2).replace('.', ',')} %`;
dice(rango, 'el rango del resto de países');

// EJ 14 · composición de junio
const jun = {};
for (const f of filas) if (mes(f.fecha) === '2026-06') jun[norm(f.linea_producto)] = (jun[norm(f.linea_producto)] || 0) + num(f.ingreso_usd);
const totJun = Object.values(jun).reduce((a, b) => a + b, 0);
const top = Object.entries(jun).sort((a, b) => b[1] - a[1]).slice(0, 3);
for (const [linea, v] of top) {
  const pct = (v / totJun * 100).toFixed(1).replace('.', ',');
  dice(`<b>${pct} %</b>`, `el peso de ${linea} en junio`);
}
const miles = Math.round(totJun / 100) / 10;                      // 103.4 -> "103.400"
const totTxt = `${String(Math.round(miles * 1000)).replace(/\B(?=(\d{3})+(?!\d))/g, '.')}`;
dice(totTxt, 'el ingreso total de junio (aprox.)');

// EJ 4 · correos con plazo
const pend = leerOffice('xlsx', join(M, '05_correos_pendientes.xlsx')).rows
  .map(f => `${f.n},${f.asunto},${f.primera_linea}`);
const pat = /\b(\d+\s*(d[ií]as?|meses?|horas?)|del \d+ al \d+|el \d+|jueves|lunes|semana|septiembre|agosto|mora)\b/i;
const conPlazo = pend.map((l, i) => [i + 1, l]).filter(([, l]) => pat.test(l)).map(([n]) => n);
dice(`<b>${conPlazo.length}</b> de los 20`, 'cuántos correos traen plazo');
dice(`<b>${enEs(conPlazo)}</b>`, 'qué correos traen plazo');

// EJ 10 · umbrales en los tres documentos
const v2 = leerOffice('docx', join(EXP, 'PR-ADM-014_Gestion_de_Cotizaciones_v2.docx')).text;
const v3 = leerOffice('docx', join(M, '10_PR-ADM-014_v3_BORRADOR.docx')).text;
const ac = leerOffice('docx', join(EXP, 'PR-ADM-014-ANEXO-C_matriz_de_aprobacion_V1.docx')).text;
const u2 = v2.match(/supera los ([\d.]+) dólares/)[1];
const u3 = v3.match(/supera los ([\d.]+) dólares/)[1];
dice(`umbral ${u2}`, 'el umbral del procedimiento vigente');
dice(`umbral ${u3}`, 'el umbral del borrador');
/Jefatura de Administración/.test(v2) ? ok('el v2 sigue asignando la aprobación a Jefatura de Administración')
  : fail('el v2 ya no dice Jefatura de Administración: la respuesta del EJ 10 quedó falsa');
/3\.001 a 10\.000/.test(ac) ? ok('el Anexo C sigue aprobando de 3.001 a 10.000')
  : fail('el Anexo C cambió su rango: revisar la respuesta del EJ 10');
/Fecha de vigencia \| Pendiente/.test(v3) ? ok('el v3 sigue sin fecha de vigencia (es lo que lo hace borrador)')
  : fail('el v3 ya tiene fecha de vigencia: la respuesta del EJ 10 deja de ser correcta');

// EJ 5 y 6 · política de garantía
const pol = leerOffice('docx', join(M, '03_politica_garantia.docx')).text;
/Batería de moto: 6 meses/.test(pol) ? ok('la política sigue diciendo 6 meses para moto (EJ 6)')
  : fail('el plazo de garantía de moto cambió: la respuesta del EJ 6 quedó falsa');
/no requiere volver a la sucursal de compra original/.test(pol) ? ok('la política sigue permitiendo cualquier sucursal (EJ 6)')
  : fail('cambió la regla de sucursal: revisar el EJ 6');
/El chequeo de batería es gratuito siempre/.test(pol) ? ok('el chequeo sigue siendo gratuito siempre (EJ 5 y 6)')
  : fail('cambió la gratuidad del chequeo: revisar los EJ 5 y 6');
/Presentar el comprobante de compra original/.test(pol) ? ok('el comprobante sigue siendo un requisito (EJ 5)')
  : fail('el comprobante ya no es el requisito 1: revisar el EJ 5');

// --- integridad de la guía
const enlaces = [...new Set([...G.matchAll(/href="(materiales\/[^"]+)"/g)].map(m => decodeURIComponent(m[1])))];
const rotos = enlaces.filter(h => !existsSync(h));
rotos.length ? fail(`la guía enlaza material inexistente: ${rotos.join(', ')}`)
  : ok(`la guía enlaza ${enlaces.length} materiales y todos existen`);
const nEj = (G.match(/class="ej" id="ej\d+"/g) || []).length;
nEj === 16 ? ok('16 ejercicios publicados') : fail(`${nEj} ejercicios, se esperaban 16`);
const nResp = (G.match(/<summary>Ver la respuesta<\/summary>/g) || []).length;
nResp === nEj ? ok(`los ${nEj} ejercicios traen respuesta`) : fail(`${nResp} respuestas para ${nEj} ejercicios`);
const nCrit = (G.match(/Cómo sabes que está bien/g) || []).length;
nCrit === nEj ? ok(`los ${nEj} ejercicios traen criterio de aceptación`) : fail(`${nCrit} criterios para ${nEj} ejercicios`);

// puntuación española
const visible = G.replace(/<style[\s\S]*?<\/style>/g, ' ').replace(/<[^>]+>/g, ' ');
const ci = (visible.match(/\?/g) || []).length, ai = (visible.match(/¿/g) || []).length;
ci === ai ? ok(`${ai} interrogaciones, todas con signo de apertura`) : fail(`${ai} "¿" para ${ci} "?"`);

console.log(oks.map(o => `  ok   ${o}`).join('\n'));
if (fails.length) {
  console.log('\n' + fails.map(f => `  FALLA ${f}`).join('\n'));
  console.log(`\n${fails.length} problema(s). ${oks.length} comprobaciones correctas.`);
  process.exit(1);
}
console.log(`\nTodo correcto: ${oks.length} comprobaciones.`);
