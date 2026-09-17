# Curso CasaBat con Office y casos de trabajo Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publicar un curso CasaBat de dos sesiones de 180 minutos con 24 laboratorios contextualizados, 16 prácticas y 19 materiales canónicos en Word y Excel.

**Architecture:** Los binarios Office serán las únicas fuentes para participantes. Un lector estándar de OOXML permitirá que los verificadores recalculen los hallazgos sin depender de copias Markdown o CSV. Los generadores Python seguirán siendo la fuente de los HTML y usarán una plantilla de ejercicio centrada en situación, rol, entrada, decisión, entregable y criterio.

**Tech Stack:** Python 3, Node.js ESM, OOXML, python-docx del runtime de Codex, artifact_tool, HTML/CSS estático, GitHub y Vercel.

**Spec:** `docs/superpowers/specs/2026-09-17-materiales-office-y-ejercicios-casabat-design.md`

## Global Constraints

- Dos sesiones de 180 minutos, cuatro bloques y una pausa de 15 minutos por sesión.
- Exactamente tres laboratorios por bloque, doce por sesión y 24 en total.
- Mantener 16 ejercicios de práctica distribuidos en cuatro niveles.
- `materiales/` y `materiales.zip` contienen exactamente 17 `.docx` y 2 `.xlsx`, sin `.md` ni `.csv`.
- Los defectos didácticos y las respuestas objetivas actuales se conservan.
- Los documentos Office son canónicos; no se mantiene una fuente paralela con el contenido.
- Los casos son ficticios y compartidos por Administración y Gerencia Comercial.
- `deck-stage.js` y la identidad visual general no se modifican.

---

### Task 1: Convertir los criterios aprobados en pruebas rojas

**Files:**
- Modify: `verifica.mjs`
- Modify: `verifica-curriculo-2026.mjs`
- Modify: `verifica-materiales.mjs`
- Modify: `verifica-practica.mjs`

**Interfaces:**
- Consumes: HTML actuales y árbol `materiales/` previo a la migración.
- Produces: compuertas que exigen 24 laboratorios, metadatos de negocio y formatos Office.

- [ ] **Step 1: Cambiar las expectativas de estructura**

En `verifica.mjs`, establecer `EJ_POR_SESION = 12`, exigir tres ejercicios por cada uno de los cuatro rieles y comprobar en cada ejercicio las clases `situation`, `role`, `input`, `decision`, `result` y `criterion`.

- [ ] **Step 2: Cambiar la compuerta curricular**

En `verifica-curriculo-2026.mjs`, exigir doce laboratorios por sesión, 24 en el hub y los tres casos por bloque definidos en la especificación.

- [ ] **Step 3: Cambiar las expectativas de materiales**

En `verifica-materiales.mjs`, exigir exactamente 17 `.docx` y 2 `.xlsx`, cero `.md` o `.csv`, enlaces Office y un ZIP con los mismos 19 archivos.

- [ ] **Step 4: Ejecutar las cuatro compuertas y observar el fallo esperado**

Run: `node verifica.mjs; node verifica-curriculo-2026.mjs; node verifica-materiales.mjs; node verifica-practica.mjs`

Expected: FAIL porque el sitio todavía publica 6 laboratorios por sesión y materiales Markdown/CSV.

- [ ] **Step 5: Commit**

```bash
git add verifica.mjs verifica-curriculo-2026.mjs verifica-materiales.mjs verifica-practica.mjs
git commit -m "test: exigir laboratorios CasaBat y materiales Office"
```

### Task 2: Crear y validar los dos libros Excel canónicos

**Files:**
- Create temporarily then remove: `build/migrate_xlsx.mjs`
- Create: `materiales/04_ventas_sucursales_2026.xlsx`
- Create: `materiales/05_correos_pendientes.xlsx`
- Delete: `materiales/04_ventas_sucursales_2026.csv`
- Delete: `materiales/05_correos_pendientes.csv`
- Create: `build/office_reader.py`

**Interfaces:**
- Consumes: las 357 filas de ventas y los 20 correos actuales.
- Produces: `office_reader.py xlsx <ruta>` con JSON de encabezados, filas y tipos de celda para los verificadores.

- [ ] **Step 1: Marcar la operación de artefacto y crear el migrador temporal**

Usar el runtime y `artifact_tool`. Los datos válidos se escribirán como fechas y números reales. Las nueve fechas heterogéneas y los dos números intencionalmente textuales permanecerán como texto.

- [ ] **Step 2: Exportar los libros con estructura utilitaria**

Crear una hoja por libro, encabezado azul CasaBat, filtros, panel congelado, anchos por contenido, formatos de fecha y moneda, y sin hojas vacías.

- [ ] **Step 3: Crear el lector OOXML sin dependencias externas**

Implementar con `zipfile` y `xml.etree.ElementTree` lectura de shared strings, inline strings, números, fechas, booleanos, celdas vacías y texto DOCX en orden documental.

- [ ] **Step 4: Sustituir los CSV y ejecutar la compuerta de materiales**

Run: `node verifica-materiales.mjs`

Expected: seguirá FAIL por los documentos Markdown, pero deberá reconocer 357 ventas, 20 correos y sus defectos desde Excel.

- [ ] **Step 5: Renderizar e inspeccionar ambos libros**

Recalcular, inspeccionar rangos clave y renderizar cada hoja. Confirmar que no haya `####`, texto truncado, tipos incorrectos ni fórmulas con error.

- [ ] **Step 6: Eliminar el migrador y commit**

```bash
git add build/office_reader.py materiales
git commit -m "feat: migrar datos del curso a Excel"
```

### Task 3: Crear y validar los 17 documentos Word canónicos

**Files:**
- Create temporarily then remove: `build/migrate_docx.py`
- Create: `materiales/*.docx`
- Create: `materiales/expediente-PR-ADM-014/*.docx`
- Delete: `materiales/*.md`
- Delete: `materiales/expediente-PR-ADM-014/*.md`

**Interfaces:**
- Consumes: el contenido de los 17 Markdown actuales.
- Produces: documentos Carta editables cuyo texto es legible mediante `office_reader.py docx <ruta>`.

- [ ] **Step 1: Marcar la creación de 17 DOCX**

Usar el runtime de documentos una sola vez con `--expected-output-count 17`.

- [ ] **Step 2: Generar documentos utilitarios y editables**

Aplicar Arial, títulos negros, jerarquía Word nativa, página Carta, tablas con encabezado azul CasaBat, bordes gris claro, filas alternas y sin portada decorativa.

- [ ] **Step 3: Preservar las anomalías del expediente**

Mantener exactamente tres nombres conformes y tres no conformes, código interno erróneo del Anexo B, Anexo E ausente, Anexo F huérfano, referencia a Anexo C v2 con archivo v1 y contradicciones del borrador v3.

- [ ] **Step 4: Sustituir los Markdown y actualizar referencias internas a Office**

Todos los ejemplos de extensiones, archivos y reglas deben referirse a `.docx` y `.xlsx` cuando corresponda.

- [ ] **Step 5: Renderizar e inspeccionar las páginas**

Run: `render_docx.py` para los 17 archivos. Inspeccionar todas las páginas y corregir solapamientos, tablas partidas de forma ilegible, encabezados huérfanos y espacios excesivos.

- [ ] **Step 6: Ejecutar la compuerta de materiales y commit**

Run: `node verifica-materiales.mjs`

Expected: los archivos y defectos Office pasan; los enlaces del sitio pueden seguir fallando hasta Task 5.

```bash
git add materiales build/office_reader.py verifica-materiales.mjs
git commit -m "feat: migrar documentos del curso a Word"
```

### Task 4: Incorporar la plantilla de laboratorio contextualizado

**Files:**
- Modify: `build/deck.py`
- Modify: `build/style.py`

**Interfaces:**
- Produces: `exercise_case(num, rail_l, minutos, titulo, rol, entrada, herramienta, situacion, decision, pasos, prompt_html, entregable, criterio, caveat=None)`.

- [ ] **Step 1: Confirmar que la prueba estructural falla sin los seis elementos**

Run: `node verifica.mjs`

Expected: FAIL por ausencia de `situation`, `role`, `input`, `decision` y `criterion`.

- [ ] **Step 2: Añadir el constructor `exercise_case`**

Renderizar situación, rol, entrada, decisión, entregable y criterio con clases verificables. La herramienta queda en segundo plano y el prompt conserva su área copiable.

- [ ] **Step 3: Ajustar CSS sin modificar el motor**

Dar prioridad visual al título y a la situación. Usar una fila compacta para rol, entrada y herramienta, y un cierre separado para entregable y criterio sin reducir el texto por debajo de un tamaño legible.

- [ ] **Step 4: Regenerar una sesión de prueba y comprobar estructura**

Run: `cd build && python3 build.py`

Expected: la generación termina sin error; la compuerta seguirá roja por el contenido no migrado a 12 laboratorios.

- [ ] **Step 5: Commit**

```bash
git add build/deck.py build/style.py
git commit -m "feat: añadir plantilla de laboratorio contextualizado"
```

### Task 5: Reescribir las dos sesiones con 24 laboratorios CasaBat

**Files:**
- Modify: `build/s1.py`
- Modify: `build/s2.py`
- Regenerate: `sesion-1.html`
- Regenerate: `sesion-2.html`

**Interfaces:**
- Consumes: `exercise_case` y los 19 archivos Office.
- Produces: 12 laboratorios por sesión, tres en cada bloque, con minutos 40, 40, 45, 40 y pausa de 15.

- [ ] **Step 1: Reescribir sesión 1**

Implementar los doce casos aprobados: bandeja del lunes, cotización 8842, seguimiento, crédito, garantía, voz CasaBat, selección del flujo, configuración persistente, prueba cruzada, suite de cinco casos, archivo hostil y versión 0.2.

- [ ] **Step 2: Reescribir sesión 2**

Implementar los doce casos aprobados: calidad del Excel, devoluciones Guatemala, Servicio a Domicilio, cotización de 4.200 dólares, anexos roto y huérfano, borrador v3, paquete publicable, código interior, documento hostil, sección de junio, paquete gerencial y traspaso.

- [ ] **Step 3: Regenerar y ejecutar las compuertas de estructura y currículo**

Run: `cd build && python3 build.py && cd .. && node verifica.mjs && node verifica-curriculo-2026.mjs`

Expected: PASS con doce ejercicios, tres por bloque y 180 minutos en ambas sesiones.

- [ ] **Step 4: Commit**

```bash
git add build/s1.py build/s2.py sesion-1.html sesion-2.html
git commit -m "feat: contextualizar 24 laboratorios CasaBat"
```

### Task 6: Contextualizar las 16 prácticas y actualizar el hub

**Files:**
- Modify: `build/practica.py`
- Regenerate: `practica.html`
- Modify: `index.html`
- Modify: `README.md`
- Regenerate: `materiales.zip`

**Interfaces:**
- Consumes: materiales Office y respuestas recalculadas por `office_reader.py`.
- Produces: 16 prácticas con caso, archivo, encargo, criterio y respuesta; hub con 24 laboratorios y 19 descargas Office.

- [ ] **Step 1: Sustituir extensiones y títulos abstractos**

Reescribir los títulos y encargos para que cada práctica nombre una tarea CasaBat concreta. Mantener cuatro niveles y 16 respuestas.

- [ ] **Step 2: Recalcular respuestas objetivas desde Excel y Word**

Adaptar `verifica-practica.mjs` para leer JSON del lector OOXML y validar serie, tasas, composición, umbrales y política.

- [ ] **Step 3: Actualizar hub y README**

Publicar 24 laboratorios, doce por sesión, 16 prácticas y los 19 archivos Office. Aclarar que README sigue en Markdown por ser documentación técnica.

- [ ] **Step 4: Regenerar el ZIP sin formatos retirados**

Crear `materiales.zip` con ruta de carpeta estable, exactamente 19 archivos Office y sin metadatos del sistema.

- [ ] **Step 5: Ejecutar las cuatro compuertas**

Run: `node verifica.mjs && node verifica-curriculo-2026.mjs && node verifica-materiales.mjs && node verifica-practica.mjs`

Expected: PASS en las cuatro.

- [ ] **Step 6: Commit**

```bash
git add build/practica.py practica.html index.html README.md materiales.zip verifica-practica.mjs
git commit -m "feat: publicar práctica y hub con materiales Office"
```

### Task 7: Verificar visualmente, publicar y comprobar producción

**Files:**
- Verify: `sesion-1.html`
- Verify: `sesion-2.html`
- Verify: `practica.html`
- Verify: `index.html`

**Interfaces:**
- Consumes: árbol completo probado.
- Produces: commit de producción y dominio `https://ia-casabat.rizo.ma/` verificado.

- [ ] **Step 1: Ejecutar toda la verificación local desde un árbol limpio**

Run: `node verifica.mjs && node verifica-curriculo-2026.mjs && node verifica-materiales.mjs && node verifica-practica.mjs`

- [ ] **Step 2: Servir el sitio y verificar visualmente**

Run: `python3 -m http.server 8877`

Ejecutar `verifica-layout.js` y recorrer hub, ambas sesiones y práctica en navegador. Confirmar cero desbordes, enlaces rotos y errores de consola.

- [ ] **Step 3: Revisar cambios y commit final si hace falta**

Run: `git diff --check && git status --short`

- [ ] **Step 4: Integrar y publicar**

Actualizar la rama de producción en GitHub. Dejar que la integración GitHub–Vercel despliegue el commit probado o desplegar el mismo artefacto con Vercel si la integración no lo inicia.

- [ ] **Step 5: Verificar el despliegue exacto**

Comprobar que el dominio público sirve el nuevo commit, comunica 24 laboratorios, descarga `.docx` y `.xlsx`, abre el ZIP correcto y no registra errores de consola.

