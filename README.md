# IA aplicada a Administración y Gerencia Comercial · Casa de las Baterías

Programa de **dos sesiones de 180 minutos** para las áreas de Administración y Gerencia Comercial
de Casa de las Baterías (Panamá, Costa Rica, El Salvador, Guatemala). 65 slides, 36 ejercicios con
prompts listos para copiar, **los archivos de trabajo incluidos** y dos anexos de consulta.

- **Cliente:** Casa de las Baterías
- **Formato:** presencial o remoto, con facilitador · 2 × 180 min
- **Patrón base:** [`capacitacion-gemini-payjoy`](../capacitacion-gemini-payjoy) — mismo `deck-stage.js`
  (idéntico byte a byte), identidad y contenidos propios
- **Identidad:** la del cliente, tomada de
  [`casabat-comparador-cliente`](../casabat-comparador-cliente)`/app/globals.css` y de su logotipo —
  azul `#1C5C92`, azul oscuro `#14456E`, rojo `#C0392B`, canvas `#F4F7FB`; Inter como sans (igual que
  el comparador), Antonio para titulares e IBM Plex Mono para los prompts. El logotipo está en
  `assets/`.

## Principio de diseño: ningún ejercicio depende de que el participante traiga algo

Los 36 ejercicios se resuelven con lo que está en el deck y en `materiales/`. Quien llega sin nada
trabaja igual. Quien trae su caso real lo usa en lugar del archivo — cada slide lo dice.

Los materiales son **casos de práctica**: contexto real de Casa de las Baterías, datos ficticios.
Ninguno contiene información real de clientes ni documentos vigentes de la empresa, y cada archivo
lo declara en su encabezado.

```
materiales/
  00_contexto_marca_casabat.md      quiénes somos, tono, qué no se promete   (de mercadeocasabat)
  01_plantilla_prompt_8_piezas.md   la plantilla del EJ 2, reencuadrada      (de mercadeocasabat)
  02_filtro_del_director.md         las 8 preguntas de autoevaluación
  03_politica_garantia.md           el caso del correo difícil               (de mercadeocasabat)
  04_ventas_sucursales_2026.csv     357 filas · 4 países · 6 meses
  05_bandeja_entrada.csv            20 asuntos con su primera línea
  06_correos_de_referencia.md       tres correos para extraer la voz
  07_notas_comite_operaciones.md    notas crudas de un comité
  08_reporte_mensual_mayo.md        el reporte del mes anterior
  09_reglas_de_nomenclatura.md      la regla contra la que se audita
  10_PR-ADM-014_v3_BORRADOR.md      la versión nueva del procedimiento
  11_tecnicas_de_prompting.md       catálogo de 12 técnicas (anexo A)
  12_gema_arquitecto_de_prompts.md  Gems y la gema constructora (anexo B)
  expediente-PR-ADM-014/            procedimiento vigente + 5 anexos
```

Cada nombre de archivo que aparece en un slide es un **enlace al archivo**: el participante no tiene
que buscarlo. Lo comprueba `verifica-materiales.mjs`.

**Los defectos son intencionales.** El archivo de ventas trae la misma categoría escrita de cinco
formas, fechas en dos formatos, duplicados, celdas vacías y una cantidad negativa; y también los
patrones que hay que encontrar: un Pareto donde 3 de 6 líneas concentran el 84 % del ingreso, una
caída sostenida de 107 a 29 unidades, un país que devuelve quince veces más que el resto y un
ingreso atípico de 34.500 contra una mediana de 950. El expediente trae tres desviaciones de
nomenclatura, un anexo referenciado que no existe, un anexo huérfano, un código interno que no
corresponde y una referencia a una versión equivocada. Si un ejercicio "no encuentra nada", el
problema está en el pedido, no en el archivo — y eso también se enseña.

`verifica-materiales.mjs` comprueba que esos defectos y patrones sigan ahí.

## De dónde sale el contenido

Cada bloque responde a una señal del diagnóstico pre-formación
(`Diagnostico_IA_AdministracionGerenciaComercial_2026-09-09`, n=3, encuesta abierta al corte):

| Señal en el diagnóstico | Dónde se resuelve |
| --- | --- |
| Los 3 respondientes usan IA de forma habitual o frecuente; ninguno es principiante | **No hay módulo de fundamentos** en ninguna de las dos sesiones |
| Las 3 dificultades convergen en prompting, por caminos distintos | S1 completa: mecánica (B1) y voz (B2) separadas, porque no son la misma habilidad |
| "Que no se note que es IA" / "que no salga genérica" | S1·B2 — ejemplos propios, ficha de voz, lista de tics, clon, prueba del compañero |
| "Cómo explicar con más detalle sin reescribir tanto" | S1·EJ 4 — la corrección quirúrgica |
| 2 de 3 piden análisis de datos; uno nombra la falta de licencia de Minitab | S2·B1 — con el límite explícito de qué no sustituye una herramienta validada |
| "Ejemplo de dashboard o gráficos" como entregable | S2·B2 — tablero de una página en HTML autocontenido |
| Actualización de procedimientos: nomenclatura, códigos, cruce de anexos, 20 días | S2·B3 — inventario, auditor, cruce bidireccional, captura ágil, control de cambios |
| Posible norma no escrita sobre el uso visible de IA | S1·EJ 17 — se nombra en sala en vez de asumir una lectura |
| Ventana de transferencia de 7 a 10 días (Baldwin y Ford) | S1·EJ 18 y S2·EJ 18 — compromisos con fecha; la S2 abre revisándolos |

Los ejercicios son **herramienta-agnósticos**: 2 de 3 respondientes usan ChatGPT y 1 usa Gemini, así
que lo que se enseña es la estructura del pedido, no los botones de una interfaz. Solo tres
ejercicios nombran herramienta concreta (Gems / Proyectos / GPT personalizados y NotebookLM), y en
esos se indica el equivalente.

## Estructura

```
index.html          hub del programa (una página, sin deck-stage)
sesion-1.html       El valor del prompt · 36 slides · 18 ejercicios + 6 de anexo · 180 min
sesion-2.html       Datos y documentos · 29 slides · 18 ejercicios · 180 min
assets/             el logotipo de la marca
materiales/         los archivos de trabajo
build/              generador de los decks (ver más abajo)
deck-stage.js       motor del deck (no modificar: el verificador comprueba su sha1)
verifica.mjs        compuerta de estructura
verifica-materiales.mjs  compuerta de los materiales
verifica-layout.js  compuerta de layout (se pega en la consola del navegador)
```

**Sesión 1 · El valor del prompt** — B1 El pedido bien hecho (50) · B2 Que no suene a IA (50) ·
B3 El trabajo de cada día (40) · B4 Confianza y control (40). Más dos anexos que no se recorren en
sesión: **A** el catálogo de 12 técnicas de prompting, **B** las Gems de Gemini y la gema
*Arquitecto de prompts*, con sus instrucciones completas.

La sesión 1 abre con la teoría mínima —qué hace un modelo cuando predice— y el
[Transformer Explainer](https://poloclub.github.io/transformer-explainer/) para verlo funcionar. La
sesión 2 abre separando **calcular** de **predecir**: el criterio técnico que sostiene todo lo demás.

**Sesión 2 · Datos y documentos** — B1 Conversa con tus datos (50) · B2 Tableros y reportes (40) ·
B3 Procedimientos y anexos (50) · B4 Lo que no se delega (40).

## Verificación

```bash
node verifica.mjs              # estructura del deck: 18 comprobaciones
node verifica-materiales.mjs   # materiales y trazabilidad: 26 comprobaciones
```

`verifica.mjs` comprueba que los footers numeren sin saltos, que los contadores del top-rail
apunten al total real y a su propia posición, que los minutos de la agenda sumen 180 y coincidan con
los dividers y con la suma de sus ejercicios, que cada ejercicio tenga concepto, pasos, prompt y
resultado, que ningún `var(--token)` apunte a un token inexistente, que no queden restos del deck
original, y que toda interrogación lleve su signo de apertura.

`verifica-materiales.mjs` comprueba que los defectos y patrones plantados sigan en los archivos, que
el expediente conserve sus desviaciones, que el borrador v3 mantenga sus cinco cambios frente al
vigente y —lo más importante— **que todo archivo citado en un deck exista de verdad**.

El layout **no se puede verificar fuera del navegador**: abre cada deck y pega `verifica-layout.js`
en la consola. Comprueba que ningún elemento **invada la banda del footer** ni se salga por la
derecha. Medir contra el borde del slide no basta: el footer es absoluto y el contenido lo tapa
antes de desbordar. Es lo que atrapa un prompt que creció dos líneas de más.

## Desarrollo

```bash
python3 -m http.server 8877     # y abrir http://localhost:8877
```

`materiales.zip` está versionado porque el hub lo ofrece como descarga. Al cambiar cualquier
material hay que regenerarlo:

```bash
rm -f materiales.zip && zip -qr materiales.zip materiales -x '*.DS_Store'
```

Los decks se generan desde `build/`: el contenido de cada sesión vive en `build/s1.py` y
`build/s2.py`, el estilo en `build/style.py` y los tipos de slide en `build/deck.py`.

```bash
cd build && python3 build.py    # reescribe sesion-1.html y sesion-2.html
```

La numeración de slides, los contadores del top-rail y los footers se derivan del orden de la lista:
al agregar o quitar un slide no hay que renumerar nada a mano. **Si editas el HTML directamente, el
siguiente `build.py` lo pisa** — o lo llevas también a `build/`, o dejas de usar el generador. Tras
cualquier cambio, correr las tres compuertas.

La densidad del bloque de prompt se elige sola según cuánto texto lleva (`dense` sobre ~470
caracteres, `denser` sobre ~620, contando el aviso de límite si lo hay). Los enlaces a los materiales
también se generan solos: `deck.py` indexa `materiales/` y convierte cada `<code>archivo</code>` en
un enlace, así que basta nombrar el archivo en el contenido.

## Navegación del deck

| Tecla | Acción |
| --- | --- |
| `←` `→` · `PgUp` `PgDn` · `Espacio` | Anterior / siguiente |
| `Home` `End` | Primer / último slide |
| `R` | Reset |

Imprimir → Guardar como PDF exporta un slide por página.

## Licencia

Privado. Material de capacitación para Casa de las Baterías vía Rizo.ma. No redistribuir sin autorización.
