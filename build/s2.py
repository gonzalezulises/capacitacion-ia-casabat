# -*- coding: utf-8 -*-
"""Sesion 2 — "Datos y documentos". Los dos frentes especificos del diagnostico:
analisis de datos sin licencia (R1, R2) y automatizacion documental (R2)."""
from deck import (Deck, cover, statement, stats, agenda, howto, divider,
                  exercise, governance, closing, filelist)

RAIL1 = 'BLOQUE 01 <span class="sep"></span> CONVERSA CON TUS DATOS'
RAIL2 = 'BLOQUE 02 <span class="sep"></span> TABLEROS Y REPORTES'
RAIL3 = 'BLOQUE 03 <span class="sep"></span> PROCEDIMIENTOS Y ANEXOS'
RAIL4 = 'BLOQUE 04 <span class="sep"></span> LO QUE NO SE DELEGA'

d = Deck('Sesión 2 · Datos y documentos · IA aplicada a Administración y Gerencia Comercial',
         {'sesion': 2})

# ---------------- apertura ----------------
d.add('Portada', 'cover', cover(
    'CASA DE LAS BATERÍAS · ADMINISTRACIÓN Y GERENCIA COMERCIAL',
    'DATOS Y<br/><span class="acc">DOCUMENTOS</span>.',
    'Sesión 2 de 2 · Análisis sin licencia y control documental · 180 minutos · 18 ejercicios sobre tus archivos.',
    'Sesión 2 · 2026'))

d.add('Dónde quedamos', None, statement(
    'ANTES DE ARRANCAR',
    'Diez días después.<br/><span style="color:var(--green-br);">¿Qué se atascó?</span>',
    '<p style="font-size:30px;line-height:1.45;color:var(--bone-2);max-width:1400px;margin-top:36px;">'
    'Quince minutos de apertura, no de cortesía: cada quien dice cuál de sus dos compromisos usó y cuál no. '
    'Lo que <b style="color:var(--bone);">no</b> se usó importa más que lo que sí — ahí está el obstáculo real, '
    'y esta sesión se ajusta a eso. Después entramos a los dos frentes que la encuesta marcó con nombre propio: '
    '<b style="color:var(--bone);">los datos que hoy no puedes analizar</b> y '
    '<b style="color:var(--bone);">los procedimientos que revisas a mano</b>.</p>', 84))

d.add('Los dos frentes', 'paper', stats(
    'LO QUE PIDIÓ LA ENCUESTA, TEXTUALMENTE',
    'Dos necesidades con nombre propio.',
    [('ANÁLISIS', '2/3', 'Piden resolver más rápido el análisis de datos: "organización de cuadros, analíticas".'),
     ('LA BARRERA', 'MINITAB', 'Una de las respuestas nombra la falta de licencia como el obstáculo — no la falta de habilidad.'),
     ('SE QUIEREN LLEVAR', 'UN TABLERO', '"Ejemplo de dashboard o gráficos" fue una de las tres respuestas a qué llevarse.'),
     ('EL CASO MÁS CONCRETO', '20 DÍAS', 'Actualizar procedimientos con control de nomenclatura y cruce de anexos, contra reloj.')]))

d.add('Agenda', 'paper', agenda(
    '4 BLOQUES <span class="sep"></span> 18 EJERCICIOS <span class="sep"></span> 180 MIN',
    'Lo que vamos a recorrer.',
    [('01 · BLOQUE 1 · 50 MIN', 'Conversa con tus datos',
      [('De la hoja sucia a la hoja lista', '10 MIN'), ('Que te explique tu propio archivo', '10 MIN'),
       ('Lo que hacías en Minitab', '10 MIN'), ('De hallazgo a causa y acción', '10 MIN'),
       ('Lo que estos datos no dicen', '10 MIN')]),
     ('02 · BLOQUE 2 · 40 MIN', 'Tableros y reportes',
      [('El gráfico correcto', '10 MIN'), ('Tu tablero en una página', '10 MIN'),
       ('El reporte que se arma solo', '10 MIN'), ('El deck que pide una decisión', '10 MIN')]),
     ('03 · BLOQUE 3 · 50 MIN', 'Procedimientos y anexos',
      [('El inventario del expediente', '10 MIN'), ('El auditor de nomenclatura', '10 MIN'),
       ('El cruce de referencias', '10 MIN'), ('Captura ágil con el dueño', '10 MIN'),
       ('Control de cambios', '10 MIN')]),
     ('04 · BLOQUE 4 · 40 MIN', 'Lo que no se delega',
      [('Responder solo con la fuente', '10 MIN'), ('Tu protocolo de aceptación', '10 MIN'),
       ('Cuándo esto no aplica', '10 MIN'), ('El siguiente lunes', '10 MIN')])]))

d.add('Cómo se ejecuta cada ejercicio', 'paper', howto(
    'ANTES DE EMPEZAR',
    'Hoy se trabaja<br/>con <span style="color:var(--green);">archivos de verdad</span>.',
    [('Los archivos están en la carpeta',
      'Cada ejercicio dice cuál abrir. Son casos de práctica con el contexto de Casa de las Baterías, '
      'y traen los mismos defectos que traen los archivos reales. Si trajiste el tuyo, mejor: úsalo.'),
     ('Aplica el semáforo antes de subir',
      'La lista roja de la sesión 1 sigue vigente: nada de datos personales, contratos ni credenciales. '
      'Si trabajas con un archivo tuyo, borra esas columnas antes de subirlo. Toma treinta segundos.'),
     ('Verifica una fila a mano',
      'Cuando el resultado sea un número, comprueba uno tú mismo contra el archivo. Una sola fila. '
      'Es la diferencia entre usar el resultado y confiar en él.')]))

d.add('Los materiales', 'paper', filelist(
    'LA CARPETA DEL TALLER',
    'Los archivos de hoy<br/><span style="color:var(--green);">ya tienen los defectos</span>.',
    'Material de práctica con el contexto real de Casa de las Baterías y datos ficticios. El archivo de '
    'ventas trae suciedad y patrones puestos a propósito; el expediente trae desviaciones de nomenclatura '
    'y referencias rotas. Si no encuentras nada, no es que el archivo esté limpio: revisa el pedido.',
    [('BLOQUES 1 Y 2 · DATOS', [
        ('04_ventas_sucursales_2026.csv', '357 filas, 4 países, 6 meses · EJ 1 a 7'),
        ('08_reporte_mensual_mayo.md', 'El reporte del mes anterior · EJ 8'),
     ]),
     ('BLOQUE 3 · DOCUMENTOS', [
        ('expediente-PR-ADM-014/', 'Procedimiento y 5 anexos · EJ 10 a 12'),
        ('09_reglas_de_nomenclatura.md', 'La regla contra la que se audita · EJ 11'),
        ('07_notas_comite_operaciones.md', 'Lo que pidió el dueño del proceso · EJ 13'),
        ('10_PR-ADM-014_v3_BORRADOR.md', 'La versión nueva · EJ 14'),
     ])]))

# ---------------- bloque 1 ----------------
d.add('Bloque 1', 'section-div', divider(
    1, 4, 50, '5 EJERCICIOS', 'Conversa<br/>con tus datos.',
    'ChatGPT o Gemini, subiendo el archivo · Google Sheets.',
    'Analizar sin licencia de software estadístico y sin depender de otra área.',
    'Tu archivo perfilado y cinco hallazgos con causa y acción.'))

d.add('Ejercicio 1 · La hoja lista', 'paper', exercise(
    1, RAIL1, 10, 'De la hoja sucia a la hoja lista.',
    'ChatGPT o Gemini · sube tu archivo .csv o .xlsx',
    'El 80 % de los análisis fallidos no falla por el análisis: falla porque <b>la hoja estaba sucia</b> y '
    'nadie lo notó. Esto se hace primero, siempre.',
    ['Sube <b><code>04_ventas_sucursales_2026.csv</code></b> tal como está. No lo limpies antes.',
     'Pide el diagnóstico de calidad <b>antes</b> de pedir cualquier análisis.',
     'Corrige tú lo que decida corregirse. La limpieza automática silenciosa es el peor hábito posible.'],
    '          <p>Te subo <code>04_ventas_sucursales_2026.csv</code>. '
    '<span class="kw">No lo analices todavía.</span> '
    'Primero dame un diagnóstico de calidad del archivo:</p>\n'
    '          <p>1. Cuántas filas y columnas, y qué representa cada columna según lo que ves.<br/>'
    '2. Celdas vacías por columna, en número y porcentaje.<br/>'
    '3. Duplicados: qué filas se repiten y por qué criterio.<br/>'
    '4. Formatos inconsistentes: fechas en dos formatos, números como texto, espacios sobrantes, '
    'la misma categoría escrita de varias maneras.<br/>'
    '5. Valores imposibles o sospechosos, con la fila donde están.</p>\n'
    '          <p>Devuélvelo como tabla y termina con: <span class="kw">qué habría que arreglar antes de '
    'confiar en cualquier análisis de este archivo</span>.</p>',
    'En este archivo hay, como mínimo: la misma categoría escrita de cinco formas, el país en cuatro, '
    'fechas en dos formatos, ocho celdas vacías, tres filas duplicadas y una cantidad negativa. '
    'Si tu diagnóstico no los encuentra todos, el pedido fue demasiado vago.'))

d.add('Ejercicio 2 · Que te lo explique', 'paper', exercise(
    2, RAIL1, 10, 'Que te explique tu propio archivo.',
    'ChatGPT o Gemini · mismo archivo, ya revisado',
    'Preguntar antes de entender lleva a respuestas que confirman lo que ya creías. '
    '<b>Primero que describa; después preguntas tú.</b>',
    ['Con el mismo archivo, pide el perfilado sin insinuar lo que esperas encontrar.',
     'Lee las preguntas que propone: suelen incluir una que no se te había ocurrido.',
     'Elige las tres que de verdad afectarían una decisión y descarta el resto.'],
    '          <p>Con el archivo ya revisado, descríbeme qué contiene sin sacar conclusiones todavía:</p>\n'
    '          <p>1. Qué mide cada columna y en qué unidad.<br/>'
    '2. El período que cubre y si hay huecos en el tiempo.<br/>'
    '3. Para las columnas numéricas: mínimo, máximo, promedio, mediana y qué tan dispersos están.<br/>'
    '4. Para las de categoría: cuántos valores distintos y cuáles concentran la mayoría.</p>\n'
    '          <p>Después propón <span class="kw">las cinco preguntas de negocio</span> que este archivo '
    'sí puede responder — y dos que la gente suele hacerle a un archivo así y que <span class="kw">este '
    'no puede responder</span>, explicando por qué.</p>',
    'Un retrato del archivo y una lista de preguntas legítimas. Las dos preguntas que no se pueden responder '
    'te ahorran el análisis que ibas a hacer mal.'))

d.add('Ejercicio 3 · Lo de Minitab', 'paper', exercise(
    3, RAIL1, 10, 'Lo que hacías con software estadístico.',
    'ChatGPT o Gemini · con el archivo cargado',
    'Pareto, tendencia, dispersión y detección de atípicos <b>no necesitan una licencia</b>: necesitan que '
    'pidas el análisis correcto y que puedas reproducirlo.',
    ['Sobre el mismo archivo: nombra el análisis que necesitas, no la herramienta que usabas.',
     'Exige que muestre el procedimiento, no solo el gráfico: sin eso no es auditable.',
     'Comprueba un número a mano contra el archivo antes de usarlo en cualquier lado.'],
    '          <p>Con este archivo, hazme el siguiente análisis y muéstrame <span class="kw">cómo lo calculaste</span>, '
    'paso a paso, con la fórmula o el código que usaste:</p>\n'
    '          <p><span class="kw">a)</span> Pareto de <code>ingreso_usd</code> por '
    '<code>linea_producto</code>: qué pocas líneas concentran el grueso.<br/>'
    '<span class="kw">b)</span> Tendencia de <code>unidades</code> por mes para Servicio a Domicilio: '
    '¿el cambio es sostenido o es ruido?<br/>'
    '<span class="kw">c)</span> Valores atípicos de <code>ingreso_usd</code>: qué filas se salen del '
    'comportamiento normal y cuánto.<br/>'
    '<span class="kw">d)</span> Devoluciones sobre unidades por <code>pais</code>: ¿hay alguno que se '
    'separe del resto más allá de la variación normal?</p>\n'
    '          <p>Entrega cada uno con: el número, el gráfico y <span class="kw">una frase</span> de qué significa.</p>',
    'Los cuatro análisis con su gráfico y su procedimiento a la vista. En este archivo: tres líneas '
    'concentran el 84 % del ingreso, el servicio a domicilio cae de 107 a 29 unidades en seis meses, '
    'hay un ingreso de 34.500 contra una mediana de 950, y un país devuelve quince veces más que el resto.',
    caveat='Sirve para explorar y decidir, no para certificar. Si el análisis alimenta una decisión '
           'auditable de calidad, hace falta una herramienta validada y reproducible: eso es una decisión '
           'de licenciamiento que el taller no resuelve. Comprueba siempre un número a mano.'))

d.add('Ejercicio 4 · Causa y acción', 'paper', exercise(
    4, RAIL1, 10, 'De cinco hallazgos a cinco decisiones.',
    'ChatGPT o Gemini · sobre los resultados del EJ 3',
    'Un hallazgo sin causa probable y sin acción es <b>una observación bonita</b>. Lo que se lleva a una '
    'reunión es la tercera columna.',
    ['Pide los hallazgos en formato de cuatro columnas obligatorias.',
     'Exige que distinga lo que el dato demuestra de lo que solo sugiere. Esa línea es tuya, no suya.',
     'Contrasta la causa que propone para las devoluciones con lo que dice el comité en '
     '<b><code>07_notas_comite_operaciones.md</code></b>: ahí hay una explicación que el dato no contiene.'],
    '          <p>Con base en el análisis anterior, dame <span class="kw">cinco hallazgos</span> en tabla '
    'de cuatro columnas:</p>\n'
    '          <p><span class="kw">1. HALLAZGO ·</span> qué muestra el dato, con la cifra.<br/>'
    '<span class="kw">2. EVIDENCIA ·</span> de qué filas o columnas sale.<br/>'
    '<span class="kw">3. CAUSA PROBABLE ·</span> tu hipótesis, marcada claramente como hipótesis.<br/>'
    '<span class="kw">4. ACCIÓN ·</span> qué haría alguien de [tu área] esta semana con esto.</p>\n'
    '          <p>Separa explícitamente lo que <span class="kw">el dato demuestra</span> de lo que '
    '<span class="kw">el dato sugiere</span>. Si un hallazgo no tiene acción posible, no lo incluyas.</p>',
    'Cinco filas que se pegan tal cual en un correo o en un comité. La causa que proponga para Guatemala '
    'será una hipótesis razonable y probablemente equivocada: el comité ya dijo que allá registran los '
    'cambios por garantía como devolución. El dato solo no podía saberlo, y ese es el punto.'))

d.add('Ejercicio 5 · El límite', 'paper', exercise(
    5, RAIL1, 10, 'Lo que estos datos no dicen.',
    'ChatGPT o Gemini · cierre del análisis',
    'La afirmación que te mete en problemas <b>no es la que está mal</b>: es la que el archivo nunca pudo '
    'sostener y nadie cuestionó.',
    ['Antes de presentar el análisis del archivo, pide la lista de límites.',
     'Ponla en el reporte, al final, en tres líneas.',
     'Si alguien pregunta por un límite que ya estaba escrito, la conversación cambia por completo.'],
    '          <p>Antes de que yo use esto, dime <span class="kw">qué no se puede concluir</span> con este archivo:</p>\n'
    '          <p>1. Qué preguntas parecen respondidas pero no lo están, y qué dato faltaría.<br/>'
    '2. Dónde el tamaño de la muestra o el período es demasiado corto para afirmar algo.<br/>'
    '3. Qué diferencias podrían ser variación normal y no un cambio real.<br/>'
    '4. Qué sesgo tiene la forma en que se recogieron estos datos.</p>\n'
    '          <p>Escríbelo en <span class="kw">tres líneas</span> que yo pueda pegar al final del reporte, '
    'en lenguaje de negocio y sin tecnicismos.</p>',
    'Tres líneas de límites al pie del reporte. Es lo que separa un análisis defendible de uno que se cae '
    'en la primera pregunta incómoda.'))

# ---------------- bloque 2 ----------------
d.add('Bloque 2', 'section-div', divider(
    2, 4, 40, '4 EJERCICIOS', 'Tableros<br/>y reportes.',
    'ChatGPT o Gemini · Google Sheets · Looker Studio.',
    'Convertir el análisis en algo que otro entienda sin que tú lo expliques.',
    'Un tablero de una página y la plantilla de tu reporte mensual.'))

d.add('Ejercicio 6 · El gráfico correcto', 'paper', exercise(
    6, RAIL2, 10, 'El gráfico correcto para la pregunta.',
    'ChatGPT o Gemini · sobre tus hallazgos del EJ 4',
    'La mayoría de los gráficos de trabajo son de torta cuando deberían ser de barras. '
    '<b>La forma la manda la pregunta</b>, no la costumbre.',
    ['Escribe la pregunta que el gráfico debe contestar, en una frase.',
     'Pide la forma antes que el gráfico, y que justifique la elección.',
     'Rechaza el gráfico que necesite que tú lo expliques para entenderse.'],
    '          <p>Para cada uno de mis hallazgos, dime <span class="kw">qué tipo de gráfico</span> lo comunica '
    'mejor y por qué, considerando: comparar categorías, ver evolución en el tiempo, mostrar composición, '
    'ver relación entre dos variables o ver distribución.</p>\n'
    '          <p>Descarta explícitamente los que no sirven para cada caso y di por qué.</p>\n'
    '          <p>Después genera cada gráfico con estas reglas: <span class="kw">un solo mensaje por gráfico</span>, '
    'el título dice la conclusión y no el tema, ejes con su unidad, sin efectos 3D, sin más de [6] colores, '
    'y ordenado de mayor a menor cuando sean categorías.</p>',
    'Gráficos cuyo título ya dice la conclusión. Si alguien entiende el hallazgo sin que tú hables, '
    'está bien hecho.'))

d.add('Ejercicio 7 · Tu tablero', 'paper', exercise(
    7, RAIL2, 10, 'Tu tablero en una página.',
    'ChatGPT o Gemini · resultado en HTML o en Looker Studio',
    'Un tablero no es muchos gráficos juntos: es <b>la respuesta a cinco preguntas fijas</b> que alguien '
    'se hace cada mes, siempre las mismas.',
    ['Las cinco preguntas salen de <b><code>08_reporte_mensual_mayo.md</code></b>: son las que ese '
     'reporte contesta todos los meses. Si tu jefatura pregunta otras cosas, cámbialas.',
     'Pide el tablero como página de un solo archivo, que abra en el navegador sin instalar nada.',
     'Ábrelo y verifica un número contra el CSV antes de compartirlo con nadie.'],
    '          <p>Con los datos de <code>04_ventas_sucursales_2026.csv</code>, arma un '
    '<span class="kw">tablero de una sola página</span> que responda: 1) ingreso por línea de producto, '
    '2) comportamiento por país, 3) evolución mensual del servicio a domicilio, 4) devoluciones sobre '
    'unidades por país, 5) las cinco sucursales de mayor ingreso.</p>\n'
    '          <p>Estructura: arriba las [4] cifras que resumen el período, con su variación contra el período '
    'anterior; en el medio los gráficos que responden las preguntas; abajo la tabla de detalle.</p>\n'
    '          <p>Entrégamelo como <span class="kw">un archivo HTML autocontenido</span> que se abra en '
    'cualquier navegador sin conexión ni instalación. Que cada cifra indique de qué columna del archivo sale.</p>',
    'Un archivo que abres con doble clic y se ve como un tablero. Esto responde literalmente a lo que se '
    'pidió llevarse de la formación.',
    caveat='Un tablero generado así es una foto de ese archivo: no se actualiza solo. Si necesitas que se '
           'refresque con datos nuevos cada mes, el camino es Looker Studio o Sheets conectado a la fuente — '
           'y eso requiere que alguien sea dueño de mantenerlo.'))

d.add('Ejercicio 8 · El reporte mensual', 'paper', exercise(
    8, RAIL2, 10, 'El reporte que se arma solo.',
    'ChatGPT o Gemini · con tu reporte del mes pasado',
    'Si el reporte tiene la misma estructura todos los meses, <b>la estructura es la plantilla</b> y lo único '
    'que cambia son los datos y la lectura.',
    ['Abre <b><code>08_reporte_mensual_mayo.md</code></b> y pide que extraiga la plantilla, no que lo resuma.',
     'Guarda la plantilla con marcas claras de qué se rellena cada mes.',
     'Rellénala con los datos del CSV y compárala con el reporte de mayo: fíjate en qué se repite.'],
    '          <p>Te pego el reporte del mes anterior. '
    '<span class="kw">No lo resumas ni lo mejores.</span></p>\n'
    '          <p>Extrae su estructura como plantilla reutilizable: qué secciones tiene, en qué orden, '
    'qué tipo de contenido va en cada una, qué extensión, y <span class="kw">qué partes cambian cada mes</span> '
    'frente a cuáles se mantienen.</p>\n'
    '          <p>Después rellénala con los datos de <code>04_ventas_sucursales_2026.csv</code> para junio, '
    'respetando la forma de escribir del original. Donde falte un dato, deja [FALTA] visible — '
    'no lo completes con lo del mes pasado.</p>',
    'La plantilla del reporte y la primera versión del mes ya redactada. El [FALTA] es intencional: '
    'el hueco visible es mejor que un dato heredado del mes anterior.'))

d.add('Ejercicio 9 · El deck de decisión', 'paper', exercise(
    9, RAIL2, 10, 'Cinco slides que piden una decisión.',
    'ChatGPT o Gemini · Google Slides o Canva para el armado',
    'Una presentación que solo informa consume tiempo de todos. La que sirve <b>termina en una pregunta</b> '
    'que alguien tiene que responder ese día.',
    ['Escribe primero la decisión que buscas. Si no hay decisión, manda un correo, no una presentación.',
     'Exige cinco slides. La restricción de cantidad es lo que obliga a priorizar.',
     'El último slide es la pregunta, con opciones y una recomendación tuya.'],
    '          <p>Con los hallazgos del bloque anterior, arma una presentación de '
    '<span class="kw">exactamente cinco slides</span> para [audiencia] cuyo objetivo es que decidan [decisión concreta]:</p>\n'
    '          <p><span class="kw">1.</span> La situación en una frase y una cifra.<br/>'
    '<span class="kw">2.</span> Qué está pasando, con el gráfico que lo demuestra.<br/>'
    '<span class="kw">3.</span> Por qué pasa: hipótesis, marcada como hipótesis.<br/>'
    '<span class="kw">4.</span> Las opciones sobre la mesa, con lo que cuesta cada una.<br/>'
    '<span class="kw">5.</span> Lo que recomiendo y qué necesito que se decida hoy.</p>\n'
    '          <p>Cada título es una afirmación, no un tema. Nada de "Análisis de ventas": '
    '"Las ventas de [X] caen por tercer mes".</p>',
    'Cinco slides con títulos que ya cuentan la historia. Alguien que solo lea los títulos entiende el caso '
    'completo — y esa es la prueba.'))

# ---------------- bloque 3 ----------------
d.add('Bloque 3', 'section-div', divider(
    3, 4, 50, '5 EJERCICIOS', 'Procedimientos,<br/>códigos y anexos.',
    'ChatGPT o Gemini con archivos · NotebookLM para el grounding.',
    'Convertir la revisión manual de documentos en una revisión asistida y trazable.',
    'El auditor de nomenclatura y la tabla de control de cambios.'))

d.add('Ejercicio 10 · El inventario', 'paper', exercise(
    10, RAIL3, 10, 'Primero el inventario, después la revisión.',
    'ChatGPT o Gemini · sube el expediente de procedimientos',
    'Nadie puede auditar lo que no ha listado. El <b>inventario es el paso que casi siempre se salta</b>, '
    'y es el que descubre que faltaban dos anexos.',
    ['Sube los <b>seis archivos</b> de <b><code>expediente-PR-ADM-014/</code></b>, con todo y sus nombres.',
     'Pide el inventario como tabla, sin ninguna corrección todavía.',
     'Compara el inventario con la lista de documentos relacionados del procedimiento. La diferencia '
     'es el primer hallazgo, y aparece antes de auditar nada.'],
    '          <p>Te subo los documentos del procedimiento PR-ADM-014. '
    '<span class="kw">No corrijas nada.</span> '
    'Hazme el inventario en una tabla con una fila por documento:</p>\n'
    '          <p>Nombre del archivo · código que declara adentro · título · versión · fecha · '
    'dueño del proceso si aparece · tipo (procedimiento, instructivo, formato, anexo) · '
    'a qué documento pertenece si es anexo.</p>\n'
    '          <p>Al final, tres listas: documentos <span class="kw">sin código</span>, '
    'documentos <span class="kw">sin versión o sin fecha</span>, y archivos cuyo '
    '<span class="kw">nombre no coincide</span> con el título o el código que declaran adentro.</p>\n'
    '          <p>Si un dato no está en el documento, escribe [NO DECLARA]. No lo deduzcas.</p>',
    'La foto real del expediente: seis archivos, uno sin fecha de vigencia, uno cuyo código interno no '
    'es el suyo, y una lista de documentos relacionados que menciona cinco anexos cuando solo hay cuatro. '
    'Eso hoy se descubre cuando lo pregunta un auditor.'))

d.add('Ejercicio 11 · El auditor', 'paper', exercise(
    11, RAIL3, 10, 'El auditor de nomenclatura.',
    'ChatGPT o Gemini · mejor dentro de un clon dedicado',
    'La regla de nomenclatura existe y está escrita. Lo que consume el tiempo es <b>compararla contra cien '
    'archivos a mano</b> — y eso es exactamente lo que no hay que hacer a mano.',
    ['Abre <b><code>09_reglas_de_nomenclatura.md</code></b> y pégala textual. Nunca de memoria.',
     'Pide la comparación archivo por archivo, con el nombre corregido propuesto.',
     'Revisa tú las excepciones legítimas antes de renombrar nada.'],
    '          <p>Esta es la regla de nomenclatura que aplica: '
    '[pega <code>09_reglas_de_nomenclatura.md</code>, secciones de estructura y reglas 1 a 7].</p>\n'
    '          <p>Ejemplos válidos: los que trae la propia regla.</p>\n'
    '          <p>Compara <span class="kw">cada archivo del inventario</span> contra esa regla y devuélveme '
    'una tabla: nombre actual · ¿cumple? · qué parte falla exactamente · nombre corregido propuesto.</p>\n'
    '          <p>Ordena por gravedad: primero los que rompen el código, después los de formato, '
    'al final los cosméticos. <span class="kw">No renombres nada</span>, solo propón.</p>',
    'En este expediente hay <span style="color:var(--green);">tres</span> nombres que incumplen: uno sin '
    'ninguna estructura, uno con la V de versión en mayúscula y uno con el correlativo en dos dígitos '
    'en vez de tres. Si tu tabla trae menos de tres, el pedido se quedó corto.',
    caveat='La propuesta es un borrador, no una autorización. Renombrar documentos controlados rompe enlaces '
           'y referencias cruzadas: el cambio se aplica por el procedimiento de control documental que ya '
           'existe, con su aprobación, nunca directamente sobre el repositorio.'))

d.add('Ejercicio 12 · El cruce', 'paper', exercise(
    12, RAIL3, 10, 'El cruce de referencias y anexos.',
    'ChatGPT o Gemini · con el expediente completo cargado',
    'El error clásico no es el anexo que falta: es <b>el anexo que existe y nadie referencia</b>, o la '
    'referencia a un anexo que se eliminó hace dos versiones.',
    ['Carga el procedimiento y sus cinco anexos en la misma conversación.',
     'Pide el cruce en las <b>dos direcciones</b>. Una sola dirección deja la mitad de los errores.',
     'Verifica a mano los dos casos que encuentre antes de reportarle el resultado a nadie.'],
    '          <p>Con el procedimiento y sus anexos cargados, hazme el cruce en las dos direcciones:</p>\n'
    '          <p><span class="kw">A · De la referencia al documento:</span> lista cada mención a un anexo, '
    'formato o documento externo dentro del texto, con la sección donde aparece, e indica si ese documento '
    'está entre los que te di. Si no está: [NO ENCONTRADO].</p>\n'
    '          <p><span class="kw">B · Del documento a la referencia:</span> lista cada anexo que te di e '
    'indica desde qué parte del procedimiento se le menciona. Si nadie lo menciona: [HUÉRFANO].</p>\n'
    '          <p>Marca también las referencias a <span class="kw">versiones distintas</span> del mismo '
    'documento y las menciones al mismo anexo con nombres diferentes.</p>',
    'Dos listas. En este expediente: el <b>Anexo E</b> se referencia dos veces y no existe; el '
    '<b>Anexo F</b> existe y nadie lo menciona; el Anexo B aparece con dos nombres distintos; y el '
    'procedimiento cita el ANEXO-C v2 cuando el archivo es v1. Cuatro hallazgos, ninguno visible a ojo.'))

d.add('Ejercicio 13 · Captura ágil', 'paper', exercise(
    13, RAIL3, 10, 'Capturar el requerimiento sin tres reuniones.',
    'Tu clon · en la reunión con el dueño del proceso',
    'Cuando hay veinte días para actualizar, el cuello de botella no es redactar: es <b>sacarle al dueño del '
    'proceso lo que tiene en la cabeza</b> sin cuatro rondas de correos.',
    ['<b>Antes:</b> pide el cuestionario a partir de <code>PR-ADM-014_Gestion_de_Cotizaciones_v2.md</code>.',
     '<b>Después:</b> usa <b><code>07_notas_comite_operaciones.md</code></b> como si fueran las notas de '
     'esa reunión — el comité ya decidió subir el umbral de aprobación a 5.000.',
     'Devuelve el borrador el mismo día, con las dudas marcadas en vez de resueltas por tu cuenta.'],
    '          <p><span class="kw">ANTES ·</span> Este es el procedimiento vigente: '
    '[pega <code>PR-ADM-014_Gestion_de_Cotizaciones_v2.md</code>]. Genera '
    '[12] preguntas para el dueño del proceso que sirvan para detectar qué cambió en la práctica: '
    'pasos que ya no se hacen, pasos nuevos no documentados, responsables que cambiaron, sistemas que '
    'se reemplazaron, controles que se dejaron de aplicar. Ordénalas de mayor a menor impacto.</p>\n'
    '          <p><span class="kw">DESPUÉS ·</span> Estas son las notas de la reunión: '
    '[pega <code>07_notas_comite_operaciones.md</code>]. Redacta el '
    'borrador de la versión nueva respetando la estructura y la redacción formal del documento vigente. '
    'Cambia <span class="kw">solo</span> lo que las notas indican. Todo lo que las notas no cubren, '
    'déjalo idéntico. Lo que quedó ambiguo, márcalo [CONFIRMAR CON DUEÑO] en vez de resolverlo tú.</p>',
    'Un cuestionario que hace productiva la reunión y un borrador el mismo día. Las notas dicen "subir el '
    'umbral a 5 mil, arranca el lunes 8" pero no dicen quién actualiza el documento ni para cuándo: eso '
    'debe salir marcado como [CONFIRMAR CON DUEÑO], no resuelto por la IA.'))

d.add('Ejercicio 14 · Control de cambios', 'paper', exercise(
    14, RAIL3, 10, 'La tabla de control de cambios.',
    'ChatGPT o Gemini · versión vigente y borrador nuevo',
    'La tabla de cambios se escribe al final, de memoria y a las apuradas. Por eso <b>casi nunca refleja '
    'lo que de verdad cambió</b> — y es lo primero que revisa una auditoría.',
    ['Carga las dos versiones: <code>PR-ADM-014_Gestion_de_Cotizaciones_v2.md</code> del expediente y '
     '<b><code>10_PR-ADM-014_v3_BORRADOR.md</code></b>.',
     'Pide la comparación exhaustiva antes de la tabla; la tabla sale de la comparación, no al revés.',
     'Verifica que ningún cambio quede sin justificación: el que no la tiene, o se revierte o se explica.'],
    '          <p>Te doy dos versiones del mismo procedimiento: la vigente (v2) y el borrador (v3).</p>\n'
    '          <p>Compáralas y dame una tabla con una fila por cambio: sección · qué decía antes · qué dice '
    'ahora · tipo de cambio (redacción, alcance, responsable, control, sistema) · '
    '<span class="kw">impacto</span> (¿afecta a quién ejecuta el proceso, a un control o solo a la forma?).</p>\n'
    '          <p>Señala aparte: cambios que <span class="kw">eliminan un control</span>, cambios que '
    '<span class="kw">cambian un responsable</span> y cambios que afectan a otros documentos que referencian '
    'a este.</p>\n'
    '          <p>Al final, redacta el resumen de cambios en el formato de la tabla de control del documento.</p>',
    'Entre v2 y v3 hay cinco cambios: el umbral sube de 3.000 a 5.000, la aprobación pasa de Jefatura de '
    'Administración a Coordinación Comercial, el vencimiento pasa de 15 a 20 días, el sistema comercial '
    'se reemplaza por el CRM y — el importante — <b>desaparece la doble verificación del punto 4.4</b>. '
    'Ese último elimina un control y no puede pasar sin aprobación explícita.'))

# ---------------- bloque 4 ----------------
d.add('Bloque 4', 'section-div', divider(
    4, 4, 40, '4 EJERCICIOS', 'Lo que no<br/>se delega.',
    'NotebookLM · tu criterio · tu firma.',
    'Cerrar con el protocolo que hace verificable todo lo anterior.',
    'Tu protocolo de aceptación y el plan del siguiente lunes.'))

d.add('Ejercicio 15 · Solo con la fuente', 'paper', exercise(
    15, RAIL4, 10, 'Que responda solo con lo que dice el documento.',
    'NotebookLM · o tu clon con la restricción escrita',
    'Cuando la respuesta tiene que salir <b>únicamente del documento</b>, el modelo debe poder citar de dónde. '
    'Sin cita, no hay forma de distinguir lo que leyó de lo que recordó.',
    ['Sube <b><code>expediente-PR-ADM-014/</code></b> y <b><code>03_politica_garantia.md</code></b> a un '
     'cuaderno de NotebookLM, o cárgalos en tu clon con la restricción explícita.',
     'Pregunta cosas que hoy te obligarían a abrir tres archivos: qué descuento máximo puede dar un '
     'asistente, qué plazo de crédito aplica a un cliente nuevo, qué pasa si quien aprueba no está.',
     'Verifica dos citas abriendo el documento. Si una no está donde dice, el resto también se revisa.'],
    '          <p>Responde <span class="kw">únicamente</span> con lo que está escrito en los documentos '
    'que te di. Tienes prohibido usar conocimiento general.</p>\n'
    '          <p>Cada afirmación va acompañada del <span class="kw">documento y la sección</span> de donde sale.</p>\n'
    '          <p>Si la respuesta no está en los documentos, responde exactamente: '
    '"No está en los documentos proporcionados" — y no completes con lo que suene razonable.</p>\n'
    '          <p>Si dos documentos se contradicen, muéstrame <span class="kw">ambos</span> con su cita '
    'y dime cuál es más reciente.</p>\n'
    '          <p>Preguntas: ¿qué descuento máximo autoriza un asistente comercial sin subir a jefatura? '
    '¿Qué plazo de crédito aplica a un cliente nuevo? ¿Qué se hace si quien debe aprobar no responde '
    'en el plazo? ¿Cubre la garantía una batería de moto de ocho meses?</p>',
    'Respuestas con la fuente al lado. Y una contradicción que aparece sola: el Anexo C dice que la '
    'aprobación arranca sobre 3.000, mientras el borrador v3 la sube a 5.000. Cuál manda depende de cuál '
    'esté vigente, y esa pregunta es exactamente la que hay que hacerle a un humano.'))

d.add('Ejercicio 16 · Tu protocolo', 'paper', exercise(
    16, RAIL4, 10, 'Tu protocolo de aceptación.',
    'Ejercicio en papel · se pega al clon al terminar',
    'Sin un criterio escrito, la decisión de dar algo por bueno la toma <b>el cansancio</b>. '
    'Cinco preguntas fijas, siempre las mismas, resuelven eso.',
    ['Escribe tus cinco preguntas de aceptación para el tipo de entregable que más produces.',
     'Que sean verificables: cada una se responde con sí o no, no con "más o menos".',
     'Pégalas al final de tu clon como último paso obligatorio antes de entregar.'],
    '          <p><span class="kw">Punto de partida — adáptalo a tu área:</span></p>\n'
    '          <p>1. ¿Puedo señalar la fuente de cada cifra y cada afirmación?<br/>'
    '2. ¿Verifiqué a mano al menos un dato contra el original?<br/>'
    '3. ¿Está marcado con [VERIFICAR] todo lo que fue asumido?<br/>'
    '4. ¿Lo firmaría con mi nombre si alguien lo cuestiona en una reunión?<br/>'
    '5. ¿Hay algo aquí que deba aprobar otra persona antes de que salga?</p>\n'
    '          <p>Si alguna respuesta es no, <span class="kw">no sale</span>. No es una guía: es una compuerta.</p>',
    'Cinco preguntas escritas y pegadas donde trabajas. Es lo que convierte todo lo anterior en algo que '
    'puedes usar sin supervisión.'))

d.add('Ejercicio 17 · Cuándo no aplica', 'paper', exercise(
    17, RAIL4, 10, 'Dónde esto deja de servir.',
    'Conversación de sala · lista propia',
    'Saber dónde <b>no</b> usar la herramienta es parte de saber usarla. Y suele ser la parte que nadie '
    'enseña en una capacitación.',
    ['Cada quien escribe dos tareas de su semana donde esto no debería usarse, y por qué.',
     'Compartan en la sala y busquen los casos donde no hay acuerdo — ahí está lo interesante.',
     'Escriban la lista del área. Una lista corta, de cinco líneas, que todos puedan recordar.'],
    '          <p><span class="kw">Casos donde el equipo suele coincidir en que no aplica:</span></p>\n'
    '          <p>· Decisiones sobre personas: desempeño, contratación, disciplina.<br/>'
    '· Documentos que se firman ante terceros sin revisión de quien firma.<br/>'
    '· Cifras que van a un estado financiero, a un ente regulador o a un cliente, sin verificación en la fuente.<br/>'
    '· Cualquier cosa que requiera confidencialidad contractual con un proveedor o cliente.<br/>'
    '· Análisis que sustente una decisión auditable, sin un método reproducible detrás.</p>\n'
    '          <p>Agreguen los dos casos propios de [su área] y quiten los que aquí no apliquen.</p>',
    'La lista del área, escrita por el área. Vale más que cualquier política importada, porque está en '
    'el lenguaje de las tareas que ustedes hacen.'))

d.add('Ejercicio 18 · El siguiente lunes', 'paper', exercise(
    18, RAIL4, 10, 'Qué queda funcionando el lunes.',
    'Tu ficha, escrita a mano · foto al terminar',
    'De todo lo de hoy, <b>solo sobrevive lo que tenga dueño y fecha</b>. Lo demás se recuerda con cariño '
    'y no se vuelve a abrir.',
    ['Elige un flujo completo, no un prompt suelto: el que más tiempo te devuelve.',
     'Define quién lo mantiene cuando tú no estés. Sin dueño, muere en tres semanas.',
     'Fija la fecha en que lo revisas y qué señal te dirá que sirvió.'],
    '          <p><span class="kw">EL FLUJO ·</span> [cuál: el auditor de nomenclatura, el tablero mensual, '
    'el reporte, el cruce de anexos].</p>\n'
    '          <p><span class="kw">SOBRE QUÉ CORRE ·</span> [qué archivo o expediente real, cada cuánto].</p>\n'
    '          <p><span class="kw">DUEÑO ·</span> [quién lo mantiene y quién lo usa si esa persona no está].</p>\n'
    '          <p><span class="kw">SEÑAL DE QUE SIRVIÓ ·</span> [qué medirás: horas de revisión, hallazgos '
    'detectados antes de la auditoría, días del ciclo de actualización].</p>\n'
    '          <p><span class="kw">FECHA DE REVISIÓN ·</span> [cuándo lo miras de nuevo].</p>',
    'Un flujo con dueño, señal y fecha. Es el único entregable de las dos sesiones que se puede verificar '
    'dentro de un mes.'))

# ---------------- cierre ----------------
d.add('Gobernanza', None, governance(
    'ANTES DE CERRAR',
    'Tres reglas que<br/><span style="color:var(--green-br);">no dependen de la herramienta</span>.',
    'Todo lo que se hizo hoy toca documentos y datos de la empresa. Estas son prácticas de trabajo, no '
    'asesoría legal: la política aplicable en cada país la definen Legal y TI, y conviene consultarla antes '
    'de institucionalizar cualquiera de estos flujos.',
    [('El documento controlado<br/>se cambia por su vía',
      'Renombrar, versionar o publicar un procedimiento sigue el control documental que ya existe. '
      'La IA propone; la aprobación y el registro no cambian de dueño.'),
     ('Ningún número sale<br/>sin verificar uno',
      'Antes de que una cifra llegue a un comité, a un cliente o a un reporte, se comprueba al menos un '
      'valor contra la fuente. Una fila. Siempre.'),
     ('La licencia es<br/>una decisión aparte',
      'Que la IA cubra hoy el análisis exploratorio no resuelve si hace falta una herramienta validada '
      'para lo auditable. Eso se plantea a quien decide licencias, con el caso de uso en la mano.')]))

d.add('Cierre', 'closing', closing(
    'CIERRE DEL PROGRAMA',
    'SIN FUENTE,<br/><span class="acc">NO HAY DATO</span>.',
    [('ESTA SEMANA', 'El flujo del ejercicio 18, corriendo sobre un caso real. Uno solo, bien hecho, '
      'vale más que cinco a medias.'),
     ('EN 30 DÍAS', 'Revisa tu señal: ¿bajaron las horas de revisión, aparecieron hallazgos antes? '
      'Si no se movió nada, el flujo estaba mal elegido — no tú.'),
     ('LO QUE QUEDA ABIERTO', 'La licencia de software estadístico y la política de uso de IA por país '
      'son decisiones que exceden esta formación. Quedan planteadas, con el caso de uso documentado.')]))

HTML = d.render()
