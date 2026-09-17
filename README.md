# IA aplicada a Administración y Gerencia Comercial · Casa de las Baterías

Programa 2026 de dos sesiones de 180 minutos para Administración y Gerencia Comercial. Conserva los casos CasaBat y la práctica guiada, pero pasa del prompt aislado a sistemas de trabajo con fuentes, pruebas, versiones, seguridad y aprobación humana.

- **Cliente:** Casa de las Baterías
- **Formato:** presencial o remoto, con facilitador · 2 × 180 min
- **Carga en vivo:** 6 laboratorios por sesión · 15 minutos de pausa incluidos
- **Práctica:** 16 ejercicios en 4 niveles
- **Datos:** todos los materiales incluidos son ficticios
- **Identidad:** azul `#1C5C92`, azul oscuro `#14456E`, rojo `#C0392B`; Inter, Antonio e IBM Plex Mono

## Diseño curricular

### Sesión 1 · Del pedido al sistema de trabajo

| Bloque | Min | Resultado |
| --- | ---: | --- |
| Elegir antes de pedir | 40 | Mapa generar/recuperar/calcular/actuar y línea base |
| Especificar y dar voz | 40 | Especificación en cinco partes y criterios de aceptación |
| Pausa | 15 | — |
| Contexto persistente | 45 | Decisión entre Proyecto, Gem o Plugin; versión y dueño |
| Probar antes de confiar | 40 | Suite de cinco casos, métrica y revisión |

### Sesión 2 · Datos, documentos y control

| Bloque | Min | Resultado |
| --- | ---: | --- |
| Datos reproducibles | 65 | Contrato, limpieza, método y reconciliación |
| Pausa | 15 | — |
| Documentos que resisten | 35 | OCR, citas, vigencia y contradicciones |
| Controles deterministas | 30 | Validador de nomenclatura y prueba de inyección |
| Flujo con aprobación | 35 | Entrada, borrador, aprobación, salida y traspaso |

## Materiales

Los casos usan contexto de CasaBat sin información real de clientes ni documentos vigentes. Los defectos son intencionales: el CSV trae variantes, vacíos, duplicados, fechas heterogéneas y un valor imposible; el expediente trae desviaciones de nomenclatura, referencias rotas, anexos huérfanos y versiones contradictorias.

```text
materiales/
  00_contexto_marca_casabat.md
  01_especificacion_de_tarea.md
  02_pruebas_de_aceptacion.md
  03_politica_garantia.md
  04_ventas_sucursales_2026.csv
  05_correos_pendientes.csv
  06_correos_de_referencia.md
  07_notas_comite_operaciones.md
  08_reporte_mensual_mayo.md
  09_reglas_de_nomenclatura.md
  10_PR-ADM-014_v3_BORRADOR.md
  11_tecnicas_de_prompting.md
  12_contexto_persistente_y_flujos.md
  expediente-PR-ADM-014/
```

Un archivo real solo debe usarse anonimizado y dentro del entorno, plan, configuración, retención y política aprobados por la empresa.

## Estructura

```text
index.html                    hub del programa
sesion-1.html                 deck generado de la sesión 1
sesion-2.html                 deck generado de la sesión 2
practica.html                 guía de 16 ejercicios
build/s1.py                   fuente de la sesión 1
build/s2.py                   fuente de la sesión 2
build/practica.py             fuente de la práctica
build/deck.py                 render compartido
materiales/                   archivos de trabajo
materiales.zip                descarga conjunta
deck-stage.js                 motor del deck; no modificar
verifica.mjs                  estructura, tiempos y enlaces
verifica-curriculo-2026.mjs   conceptos y términos vigentes
verifica-materiales.mjs       casos, patrones y trazabilidad
verifica-practica.mjs         respuestas objetivas de la guía
verifica-layout.js            comprobación visual en navegador
```

## Desarrollo

Los HTML de sesión y práctica son generados. Edita las fuentes en `build/`, no los archivos generados.

```bash
cd build && python3 build.py
cd build && python3 practica.py
```

Si cambia cualquier material, regenera `materiales.zip`.

```bash
rm -f materiales.zip
zip -qr materiales.zip materiales -x '*.DS_Store'
```

## Verificación

```bash
node verifica.mjs
node verifica-curriculo-2026.mjs
node verifica-materiales.mjs
node verifica-practica.mjs
```

`verifica.mjs` comprueba numeración, integridad de ejercicios, agenda de 180 minutos —incluida la pausa—, enlaces, puntuación y tokens visuales. La compuerta curricular evita reintroducir carga o términos retirados. Las otras dos recalculan patrones desde los archivos y verifican que toda respuesta y enlace siga siendo correcto.

Para la comprobación visual, sirve el sitio localmente y ejecuta `verifica-layout.js` en cada deck:

```bash
python3 -m http.server 8877
```

## Navegación del deck

| Tecla | Acción |
| --- | --- |
| `←` `→` · `PgUp` `PgDn` · `Espacio` | Anterior / siguiente |
| `Home` `End` | Primer / último slide |
| `R` | Reset |

Imprimir → Guardar como PDF exporta un slide por página.

## Licencia

Privado. Material de capacitación para Casa de las Baterías vía Rizo.ma. No redistribuir sin autorización.
