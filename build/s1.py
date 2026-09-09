# -*- coding: utf-8 -*-
"""Sesion 1 — "Que no se note". Prompting aplicado y voz propia.
Cada bloque responde a una senal del diagnostico pre-formacion (n=3, 2026-09-09)."""
from deck import (Deck, cover, statement, stats, agenda, howto, divider,
                  exercise, governance, closing, filelist)

RAIL1 = 'BLOQUE 01 <span class="sep"></span> EL PEDIDO BIEN HECHO'
RAIL2 = 'BLOQUE 02 <span class="sep"></span> QUE NO SUENE A IA'
RAIL3 = 'BLOQUE 03 <span class="sep"></span> EL TRABAJO DE CADA DÍA'
RAIL4 = 'BLOQUE 04 <span class="sep"></span> CONFIANZA Y CONTROL'

d = Deck('Sesión 1 · Que no se note · IA aplicada a Administración y Gerencia Comercial',
         {'sesion': 1})

# ---------------- apertura ----------------
d.add('Portada', 'cover', cover(
    'CASA DE LAS BATERÍAS · ADMINISTRACIÓN Y GERENCIA COMERCIAL',
    'QUE NO<br/><span class="acc">SE NOTE</span>.',
    'Sesión 1 de 2 · Prompting aplicado y voz propia · 180 minutos · 18 ejercicios sobre tus casos reales.',
    'Sesión 1 · 2026'))

d.add('El punto de partida', None, statement(
    'POR QUÉ ARRANCAMOS AQUÍ',
    'Ya usas IA todos los días.<br/>Hoy no venimos a<br/><span style="color:var(--green-br);">explicarte qué es</span>.',
    '<p style="font-size:30px;line-height:1.45;color:var(--bone-2);max-width:1400px;margin-top:36px;">'
    'La encuesta previa lo dejó claro: nadie en este grupo está empezando. Todos usan ChatGPT o Gemini '
    'de forma habitual o frecuente. Por eso esta sesión no tiene módulo de fundamentos: empieza donde '
    'de verdad se traba el trabajo — en <b style="color:var(--bone);">cómo le pides las cosas</b> y en '
    '<b style="color:var(--bone);">cómo logras que el resultado sea tuyo y no de la máquina</b>.</p>', 84))

d.add('El diagnóstico', 'paper', stats(
    'LO QUE DIJO LA ENCUESTA PREVIA',
    'Tres respuestas, un solo tema debajo.',
    [('RESPONDIENTES', '3', 'Panamá y Guatemala. La encuesta sigue abierta en Costa Rica y El Salvador.'),
     ('NIVEL DE USO', '0', 'Personas en nivel principiante. Todos usan IA de forma habitual o frecuente.'),
     ('CONVERGENCIA', '3/3', 'Las tres dificultades apuntan al prompting, por caminos distintos: mecánica, estructura y voz.'),
     ('PIDEN LLEVARSE', '2/3', 'Algo tangible y reutilizable: prompts, palabras clave, ejemplos — no conceptos.')]))

d.add('Agenda', 'paper', agenda(
    '4 BLOQUES <span class="sep"></span> 18 EJERCICIOS <span class="sep"></span> 180 MIN',
    'Lo que vamos a recorrer.',
    [('01 · BLOQUE 1 · 50 MIN', 'El pedido bien hecho',
      [('El mismo pedido, dos veces', '10 MIN'), ('Las 8 piezas sobre tu caso', '10 MIN'),
       ('El filtro del director', '10 MIN'), ('Corregir sin reescribir', '10 MIN'),
       ('Tu biblioteca de pedidos', '10 MIN')]),
     ('02 · BLOQUE 2 · 50 MIN', 'Que no suene a IA',
      [('Dale tus propios ejemplos', '10 MIN'), ('Tu ficha de voz en 8 reglas', '10 MIN'),
       ('Los tics que te delatan', '10 MIN'), ('Tu clon: Gem, Proyecto o GPT', '10 MIN'),
       ('La prueba del compañero', '10 MIN')]),
     ('03 · BLOQUE 3 · 40 MIN', 'El trabajo de cada día',
      [('El correo difícil', '10 MIN'), ('Triage de la bandeja', '10 MIN'),
       ('De notas a acuerdos', '10 MIN'), ('Capacitación exprés', '10 MIN')]),
     ('04 · BLOQUE 4 · 40 MIN', 'Confianza y control',
      [('El semáforo de lo que subes', '10 MIN'), ('La marca [VERIFICAR]', '10 MIN'),
       ('¿Se dice que lo hiciste con IA?', '10 MIN'), ('Tu plan de 10 días', '10 MIN')])]))

d.add('Cómo se ejecuta cada ejercicio', 'paper', howto(
    'ANTES DE EMPEZAR',
    'Cada ejercicio se ejecuta<br/>en <span style="color:var(--green);">tres pasos</span>.',
    [('Abre el material que indica el slide',
      'Ningún ejercicio depende de que hayas traído algo: los archivos están en la carpeta '
      '<code>materiales/</code> y cada slide dice cuál usar. Si trajiste tu caso real, mejor — '
      'úsalo en lugar del archivo.'),
     ('Copia el prompt y ejecútalo',
      'Cada ejercicio trae el pedido completo en el bloque verde. Funciona igual en ChatGPT y en '
      'Gemini: lo que se enseña es la estructura del pedido, no los botones de una herramienta.'),
     ('Compara con el resultado esperado',
      'Abajo a la derecha dice qué deberías obtener. Si lo tuyo está lejos, no empieces de cero: '
      'corrige una sola parte del pedido y vuelve a lanzarlo.')]))

d.add('Los materiales', 'paper', filelist(
    'LA CARPETA DEL TALLER',
    'Todo lo que necesitas<br/><span style="color:var(--green);">ya está aquí</span>.',
    'Los archivos son material de práctica: casos ficticios con el contexto real de Casa de las '
    'Baterías. Ninguno contiene datos reales de clientes ni documentos vigentes de la empresa.',
    [('DE REFERENCIA · SE USAN VARIAS VECES', [
        ('00_contexto_marca_casabat.md', 'Quiénes somos, tono, qué no se promete'),
        ('01_plantilla_prompt_8_piezas.md', 'La plantilla del EJ 2, reutilizable'),
        ('02_filtro_del_director.md', 'Las 8 preguntas del EJ 3'),
        ('06_correos_de_referencia.md', 'Tres correos para el EJ 6'),
     ]),
     ('CASOS DE LA SESIÓN', [
        ('03_politica_garantia.md', 'El correo difícil · EJ 11'),
        ('05_bandeja_entrada.csv', 'Veinte correos para el EJ 12'),
        ('07_notas_comite_operaciones.md', 'Notas crudas para el EJ 13'),
        ('expediente-PR-ADM-014/', 'El procedimiento del EJ 14'),
     ])]))

# ---------------- bloque 1 ----------------
d.add('Bloque 1', 'section-div', divider(
    1, 4, 50, '5 EJERCICIOS', 'El pedido<br/>bien hecho.',
    'ChatGPT o Gemini, indistinto.',
    'Pasar del pedido suelto a la instrucción completa, y aprender a corregirla.',
    'Tu plantilla de 8 piezas rellenada y 3 pedidos guardados.'))

d.add('Ejercicio 1 · Dos veces el mismo pedido', 'paper', exercise(
    1, RAIL1, 10, 'El mismo pedido, dos veces.',
    'ChatGPT o Gemini · el que ya usas',
    'La IA no responde genérico por ser mala: responde genérico porque <b>le diste un pedido genérico</b>. '
    'La diferencia se ve en 4 minutos.',
    ['Lanza el <b>pedido A</b> tal como lo escribirías hoy, de corrido.',
     'Sin borrar nada, lanza el <b>pedido B</b> en un chat nuevo.',
     'Pon las dos respuestas lado a lado y marca <b>qué tuviste que corregir</b> en cada una.'],
    '          <p><span class="kw">EL CASO (real del archivo):</span> el correo 1 de '
    '<code>05_bandeja_entrada.csv</code> — un cliente pregunta si la cotización 8842, de hace una '
    'semana, sigue vigente. Según el procedimiento, vence a los 15 días.</p>\n'
    '          <p><span class="kw">A ·</span> Escríbeme un correo al cliente sobre la cotización 8842.</p>\n'
    '          <p><span class="kw">B ·</span> Actúa como asistente de Administración de Casa de las '
    'Baterías en Panamá. Escribe un correo al contacto de un cliente de flota que pregunta si su '
    'cotización 8842, emitida hace 7 días, sigue vigente.</p>\n'
    '          <p>Contexto: sí sigue vigente, vence a los 15 días de emitida. Quiero que responda '
    'antes de que venza y que sepa que puede cerrarla por WhatsApp.</p>\n'
    '          <p>Tono cercano y directo, español centroamericano neutro, de tú. Máximo 8 líneas. '
    'No inventes montos, fechas exactas ni condiciones: si te faltan, pídemelos.</p>',
    'Dos correos claramente distintos. El A hay que reescribirlo casi entero; el B se manda con uno o dos ajustes. '
    'Esa distancia es todo lo que enseña esta sesión.'))

d.add('Ejercicio 2 · Las 8 piezas', 'paper', exercise(
    2, RAIL1, 10, 'Las 8 piezas, sobre tu caso.',
    'ChatGPT o Gemini · plantilla reutilizable',
    'El activo no es un prompt mágico: es <b>tu contexto escrito una vez</b>. Las partes 1, 2, 5 y 6 casi '
    'no cambian — por eso después van dentro de tu clon.',
    ['Abre <b><code>01_plantilla_prompt_8_piezas.md</code></b>: es la misma que ya usa Mercadeo.',
     'Aplícala al caso 11 de la bandeja — un cliente de flota pide pasar de 30 a 60 días de crédito.',
     'Rellena solo <b>[3] objetivo</b>, <b>[4] insumos</b> y <b>[7] formato</b>; el resto queda fijo. '
     'Guárdala: la reusas el resto del día.'],
    '          <p><span class="kw">[1] CONTEXTO ·</span> Casa de las Baterías, Administración, Panamá. '
    'Un cliente de flota con contrato pide ampliar su crédito de 30 a 60 días.</p>\n'
    '          <p><span class="kw">[2] ROL ·</span> Asistente de Administración con experiencia en cartera. '
    'Español centroamericano neutro, de tú.</p>\n'
    '          <p><span class="kw">[3] OBJETIVO ·</span> Un correo de respuesta. Sale bien si el cliente '
    'entiende qué necesitamos de él para evaluarlo, sin que suene a negativa.</p>\n'
    '          <p><span class="kw">[4] INSUMOS ·</span> Te pego el Anexo D de condiciones de crédito '
    '(<code>expediente-PR-ADM-014/</code>). Es tu única fuente. No inventes cifras.</p>\n'
    '          <p><span class="kw">[5] RESTRICCIONES ·</span> No prometas la ampliación: la aprueba Finanzas. '
    'No cites plazos que no estén en el anexo.</p>\n'
    '          <p><span class="kw">[6] CRITERIOS ·</span> Cumple el objetivo, no inventa datos, separa lo que '
    'está aprobado de lo que hay que gestionar.</p>\n'
    '          <p><span class="kw">[7] FORMATO ·</span> Correo de máximo 8 líneas, con asunto.</p>\n'
    '          <p><span class="kw">[8] VERIFICACIÓN ·</span> Antes de responder, di qué supuestos hiciste y '
    'qué te falta. Marca [VERIFICAR] todo dato que hayas asumido.</p>',
    'Un resultado que ya no necesita cinco idas y vueltas. Y, sobre todo, una plantilla que sirve para la próxima '
    'vez — que es lo que pediste llevarte.'))

d.add('Ejercicio 3 · El filtro del director', 'paper', exercise(
    3, RAIL1, 10, 'Que se corrija antes de dártelo.',
    'ChatGPT o Gemini · sobre la salida del ejercicio 2',
    'Revisar tú cada salida es el cuello de botella. <b>El modelo puede aplicarse tu propio criterio</b> '
    'si se lo escribes como lista de verificación.',
    ['Toma la respuesta del ejercicio anterior, la que casi te sirve.',
     'Abre <b><code>02_filtro_del_director.md</code></b> y copia su versión corta.',
     'Pídele que <b>se autoevalúe y entregue la versión corregida</b>. Cuenta cuántas de esas '
     'correcciones ibas a hacer tú a mano.'],
    '          <p>Antes de darme la versión final, evalúa tu propia respuesta con estas preguntas y '
    'responde cada una con sí o no y una línea de justificación:</p>\n'
    '          <p><span class="kw">1.</span> ¿Cumple el objetivo que pedí?<br/>'
    '<span class="kw">2.</span> ¿Suena a una persona de Casa de las Baterías o suena a IA?<br/>'
    '<span class="kw">3.</span> ¿Promete algo que no puedo sostener?<br/>'
    '<span class="kw">4.</span> ¿Usa precios, plazos o coberturas que yo no te di?<br/>'
    '<span class="kw">5.</span> ¿Propone una acción concreta?<br/>'
    '<span class="kw">6.</span> ¿Inventaste algún dato?<br/>'
    '<span class="kw">7.</span> ¿Algo de esto necesita revisión de otra área?<br/>'
    '<span class="kw">8.</span> ¿Se usa tal cual o hay que rehacerlo?</p>\n'
    '          <p>Después entrégame <span class="kw">solo la versión corregida</span>.</p>',
    'La segunda versión suele ser la que ibas a producir tú después de dos rondas de edición. El filtro se '
    'guarda una vez y se reusa siempre.'))

d.add('Ejercicio 4 · Corregir sin reescribir', 'paper', exercise(
    4, RAIL1, 10, 'Corregir sin volver a explicar todo.',
    'ChatGPT o Gemini · sobre cualquier salida anterior',
    'El desgaste no está en pedir: está en <b>volver a explicarlo entero</b> cada vez que algo sale mal. '
    'La corrección quirúrgica nombra qué cambia y blinda el resto.',
    ['Identifica <b>una sola cosa</b> que está mal: el tono, la extensión, un párrafo.',
     'Pide el cambio nombrando explícitamente <b>qué se queda intacto</b>.',
     'Repite hasta tres veces. Si a la tercera no llega, el problema está en el pedido original, no en la corrección.'],
    '          <p>Mantén el texto anterior exactamente igual, <span class="kw">salvo</span> [lo que cambia: '
    'el segundo párrafo / el saludo / la despedida].</p>\n'
    '          <p>Cámbialo así: [instrucción concreta].</p>\n'
    '          <p>No toques el resto: ni el orden, ni la extensión, ni las palabras que ya funcionan. '
    'Devuélveme el texto completo con ese único cambio aplicado y, debajo, <span class="kw">una línea</span> '
    'diciendo qué modificaste.</p>',
    'El texto vuelve con el cambio pedido y nada más movido. Se acaba el "me arregló una cosa y me dañó otras dos".'))

d.add('Ejercicio 5 · Tu biblioteca', 'paper', exercise(
    5, RAIL1, 10, 'Los tres pedidos que repites cada semana.',
    'Tu bloc de notas, Docs o Keep · lo que ya usas',
    'Un pedido que vive en tu historial <b>se pierde el lunes</b>. Lo que se guarda con nombre y se vuelve '
    'a abrir es lo único que cambia tu semana.',
    ['Escribe las <b>tres tareas</b> que hiciste con IA más de una vez este mes. Si no te viene ninguna, '
     'usa tres de la bandeja: responder una consulta de garantía, redactar un recordatorio de pago, '
     'contestar una solicitud de crédito.',
     'Para cada una, guarda el pedido que mejor funcionó, con las 8 piezas ya rellenadas.',
     'Ponles nombre en imperativo y déjalas donde las encuentres en 10 segundos.'],
    '          <p><span class="kw">Formato de cada ficha:</span></p>\n'
    '          <p>NOMBRE · [Redactar recordatorio de pago] — cuándo se usa: [cada lunes, cartera vencida]</p>\n'
    '          <p>PEDIDO · [las 8 piezas, ya rellenadas]</p>\n'
    '          <p>QUÉ CAMBIO CADA VEZ · [cliente, monto, fecha]</p>\n'
    '          <p>ÚLTIMA REVISIÓN · [fecha]</p>',
    'Tres fichas guardadas. Es el entregable mínimo de esta sesión: si mañana te quedas solo con esto, '
    'ya recuperaste el tiempo del taller.'))

# ---------------- bloque 2 ----------------
d.add('Bloque 2', 'section-div', divider(
    2, 4, 50, '5 EJERCICIOS', 'Que no<br/>suene a IA.',
    'ChatGPT o Gemini · más tu propio archivo de textos.',
    'Que el resultado pase como tuyo, sin que tengas que reescribirlo.',
    'Tu ficha de voz y un clon que la aplica solo.'))

d.add('Ejercicio 6 · Dale tus ejemplos', 'paper', exercise(
    6, RAIL2, 10, 'Enséñale a escribir como tú.',
    'ChatGPT o Gemini · con tres textos tuyos reales',
    'Describir tu estilo con adjetivos no funciona. <b>Mostrarle tres textos tuyos, sí.</b> El modelo copia '
    'patrones mucho mejor de lo que sigue descripciones.',
    ['Abre <b><code>06_correos_de_referencia.md</code></b>: tres correos de una jefatura administrativa. '
     'Si trajiste tres correos tuyos, usa los tuyos — funcionan mejor.',
     'Pégalos completos y pídele que extraiga el patrón <b>antes</b> de escribir nada.',
     'Recién entonces pídele el texto nuevo: la respuesta al caso 14 de la bandeja, el reclamo por '
     'la instalación fuera de la ventana acordada.'],
    '          <p>Te voy a pegar tres correos escritos por la misma persona. '
    '<span class="kw">No los edites ni los comentes.</span></p>\n'
    '          <p>[TEXTO 1] · [TEXTO 2] · [TEXTO 3]</p>\n'
    '          <p>Primero dime, en una lista corta, <span class="kw">qué patrón</span> ves en cómo escribo: '
    'largo de frase, cómo abro, cómo cierro, qué palabras repito, qué nunca uso, cuánto rodeo doy antes de ir al punto.</p>\n'
    '          <p>Después, y solo después, escribe la respuesta al cliente que reclama que la '
    'instalación a domicilio llegó tres horas tarde, siguiendo ese mismo patrón. '
    'Si tienes que elegir entre sonar correcto y sonar como yo, <span class="kw">suena como yo</span>.</p>',
    'Un texto que reconoces como propio. Es la respuesta directa a "quiero que no se note que es IA": '
    'no se nota cuando el patrón es el tuyo.'))

d.add('Ejercicio 7 · Tu ficha de voz', 'paper', exercise(
    7, RAIL2, 10, 'Tu voz, en ocho reglas.',
    'ChatGPT o Gemini · a partir del ejercicio 6',
    'El patrón que acaba de extraer es un activo. <b>Escrito como ocho reglas</b>, lo pegas en cualquier '
    'herramienta y funciona igual en las dos.',
    ['Pídele que convierta el patrón en <b>ocho reglas en imperativo</b>, verificables.',
     'Borra las que no te representen y agrega las tuyas a mano — esto no se delega entero.',
     'Guárdala. En el ejercicio 9 la metes dentro de tu clon.'],
    '          <p>Convierte el patrón que identificaste en <span class="kw">ocho reglas de escritura</span>, '
    'en imperativo y comprobables. Nada de "sé claro" ni "usa un tono cercano": tienen que ser reglas que '
    'alguien pueda auditar.</p>\n'
    '          <p>Ejemplo del nivel que busco: "Abre con el hecho, nunca con un saludo de dos líneas". '
    '"Ninguna frase pasa de 25 palabras". "Cierra con una pregunta concreta o con la acción que espero".</p>\n'
    '          <p>Agrega una novena regla que diga <span class="kw">qué nunca hago</span>.</p>',
    'Una ficha de nueve líneas que puedes pegar en cualquier chat. Es transferible: sirve igual en ChatGPT '
    'que en Gemini, porque no depende de la herramienta.'))

d.add('Ejercicio 8 · Los tics', 'paper', exercise(
    8, RAIL2, 10, 'Los tics que la delatan.',
    'ChatGPT o Gemini · sobre un texto ya generado',
    'Lo que hace que un texto "se note" no es el contenido: es un <b>puñado de muletillas</b> que casi ningún '
    'humano usa y casi todo modelo repite.',
    ['Toma un texto que hayas generado hoy y pídele la <b>lista de sus propios tics</b>.',
     'Añade los que tú detectas y arma tu lista negra.',
     'Vuelve a pedir el texto <b>prohibiendo esa lista explícitamente</b>.'],
    '          <p>Lee este texto que generaste y dime qué partes <span class="kw">delatan que lo escribió una IA</span>: '
    'muletillas, frases de relleno, estructuras demasiado simétricas, entusiasmo de más.</p>\n'
    '          <p>Después reescríbelo con estas prohibiciones: nada de "en el mundo actual", "es importante '
    'destacar", "no dudes en", "en resumen", "sin duda"; ninguna lista de tres elementos que suene armada '
    'para rellenar; ningún cierre motivacional.</p>\n'
    '          <p>Si una frase no aporta información, <span class="kw">bórrala</span> en vez de suavizarla.</p>',
    'El mismo contenido, entre un 20 y un 30 % más corto, sin las costuras. Guarda la lista negra: se pega '
    'una vez al clon y deja de aparecer.'))

d.add('Ejercicio 9 · Tu clon', 'paper', exercise(
    9, RAIL2, 10, 'El clon que ya sabe quién eres.',
    'Gem (Gemini) · Proyecto o GPT personalizado (ChatGPT)',
    'Repetir tu contexto en cada chat es el impuesto invisible. <b>Un clon guarda las partes fijas</b> '
    'y tú solo escribes lo que cambia.',
    ['Crea un <b>Gem</b> en Gemini o un <b>Proyecto / GPT personalizado</b> en ChatGPT. Es equivalente.',
     'Pega dentro: <b><code>00_contexto_marca_casabat.md</code></b>, tu ficha de voz del EJ 7, tu lista '
     'negra del EJ 8 y la versión corta de <b><code>02_filtro_del_director.md</code></b>.',
     'Pruébalo con un pedido de una línea. Si aún tienes que explicarle quién eres, algo faltó adentro.'],
    '          <p><span class="kw">INSTRUCCIONES DEL CLON (pegar en la configuración):</span></p>\n'
    '          <p>Eres mi asistente de escritura en Casa de las Baterías. Yo soy [cargo] de [área] en [país].</p>\n'
    '          <p>Este es el contexto de la empresa: [pega <code>00_contexto_marca_casabat.md</code>].</p>\n'
    '          <p>Escribes siempre siguiendo estas reglas de voz: [pega tu ficha del EJ 7].</p>\n'
    '          <p>Nunca uses: [pega tu lista negra del EJ 8].</p>\n'
    '          <p>Nunca inventes precios, plazos ni cobertura: márcalos [VERIFICAR].</p>\n'
    '          <p>Antes de entregar, revísate con el filtro de 8 preguntas y corrígete.</p>',
    'Un asistente al que le escribes "recordatorio de pago para [cliente]" y devuelve algo casi listo. '
    'A partir de aquí, el resto de la sesión se hace dentro de él.',
    caveat='El clon hereda lo que le metes. Si pegas dentro un texto terminado como ejemplo, tenderá a '
           'repetirlo casi igual: pega <b>reglas</b>, no salidas.'))

d.add('Ejercicio 10 · La prueba del compañero', 'paper', exercise(
    10, RAIL2, 10, 'La prueba del compañero.',
    'Tu clon + la persona sentada al lado',
    '"Que no se note" no es una sensación: es un criterio que <b>otra persona</b> puede aplicar. Si no lo '
    'defines, no sabes cuándo parar de corregir.',
    ['Produce con tu clon un texto real que vayas a mandar esta semana.',
     'Dáselo a la persona de al lado <b>sin decirle cómo lo hiciste</b>.',
     'Pregúntale dos cosas: ¿lo firmarías tú? y ¿qué parte te suena rara? Anota la respuesta.'],
    '          <p><span class="kw">Criterio de aceptación (anótalo tú, no lo pidas a la IA):</span></p>\n'
    '          <p>1. ¿Un compañero lo mandaría tal cual con su nombre?</p>\n'
    '          <p>2. ¿Hay alguna frase que tú nunca dirías?</p>\n'
    '          <p>3. ¿Cuánto tuviste que editar? Si pasa del 20 %, el problema está en el clon: vuelve al EJ 7.</p>\n'
    '          <p>4. ¿Se sostiene sin ningún dato inventado?</p>',
    'Un umbral propio en vez de una sensación. Y una respuesta honesta a la pregunta de fondo: si el texto '
    'pasa la prueba del compañero, ya no importa cómo se produjo.'))

# ---------------- bloque 3 ----------------
d.add('Bloque 3', 'section-div', divider(
    3, 4, 40, '4 EJERCICIOS', 'El trabajo<br/>de cada día.',
    'Tu clon del bloque 2 · correo, notas y documentos reales.',
    'Aplicar lo anterior a las cuatro tareas que más tiempo consumen.',
    'Cuatro pedidos guardados sobre tus tareas reales.'))

d.add('Ejercicio 11 · El correo difícil', 'paper', exercise(
    11, RAIL3, 10, 'El correo que te da pereza escribir.',
    'Tu clon · caso real de esta semana',
    'Redactar y mejorar correos es hoy el uso número uno del grupo. El salto no está en escribirlo más rápido: '
    'está en <b>no perder el cliente ni prometer lo que no puedes</b>.',
    ['El caso es el correo 4 de <b><code>05_bandeja_entrada.csv</code></b>: una batería de moto de 8 meses.',
     'Pega <b><code>03_politica_garantia.md</code></b> completo. Sin la política, la IA inventa una '
     'respuesta amable que no puedes sostener — compruébalo pidiéndoselo primero sin ella.',
     'Pide tres versiones con distinto grado de firmeza y elige tú.'],
    '          <p>Caso: un cliente reclama la garantía de una batería de moto comprada hace 8 meses '
    'que ya no arranca. Insiste en que le corresponde reemplazo completo.</p>\n'
    '          <p>Esta es la política que aplica: [pega <code>03_politica_garantia.md</code>]. '
    'Es tu única fuente sobre plazos y condiciones.</p>\n'
    '          <p>No puedo ofrecer nada que no esté ahí, ni insinuar excepciones.</p>\n'
    '          <p>Escribe <span class="kw">tres versiones</span> de la respuesta: una conciliadora, una neutra '
    'y una firme. Todas dicen lo mismo de fondo y ninguna promete nada fuera de lo anterior.</p>\n'
    '          <p>Ninguna versión inventa plazos ni montos. Lo que no te di, lo marcas con [VERIFICAR].</p>',
    'Tres borradores con el mismo fondo y distinta temperatura. La política dice 6 meses sin prorrateo '
    'para moto: la respuesta correcta explica la causa y ofrece una alternativa, nunca cierra con un '
    '"no aplica". Eliges por criterio comercial, no por cansancio de redactar.'))

d.add('Ejercicio 12 · Triage de bandeja', 'paper', exercise(
    12, RAIL3, 10, 'Veinte correos, cuatro decisiones.',
    'Tu clon · con el texto de tu bandeja, sin datos sensibles',
    'La bandeja no se resuelve leyendo más rápido: se resuelve <b>clasificando antes de responder</b>. '
    'La IA es buena clasificando; tú eres bueno decidiendo.',
    ['Abre <b><code>05_bandeja_entrada.csv</code></b>: 20 asuntos con su primera línea, ya sin datos '
     'de personas. Así se prepara tu bandeja real antes de subirla.',
     'Pide la clasificación en cuatro cubos y el borrador solo del cubo A.',
     'Responde tú los del cubo C. Ese no se delega.'],
    '          <p>Te paso 20 asuntos con su primera línea. Clasifícalos en cuatro grupos:</p>\n'
    '          <p><span class="kw">A ·</span> Responde en una línea (confirmar, agradecer, acusar recibo).<br/>'
    '<span class="kw">B ·</span> Necesita un dato que hay que buscar.<br/>'
    '<span class="kw">C ·</span> Decide una persona, no un correo.<br/>'
    '<span class="kw">D ·</span> No requiere respuesta.</p>\n'
    '          <p>Devuélvelo como tabla: asunto, grupo, y por qué. Después redacta <span class="kw">solo</span> '
    'los borradores del grupo A, en mi voz.</p>',
    'Una tabla que convierte una bandeja en cuatro decisiones, y los borradores de la mitad trivial listos. '
    'El grupo C queda visible: es el que de verdad te estaba costando la mañana.',
    caveat='No pegues datos de clientes identificables, montos de contratos ni cédulas. Para clasificar, '
           'el asunto y una línea bastan — el resto es riesgo sin beneficio.'))

d.add('Ejercicio 13 · De notas a acuerdos', 'paper', exercise(
    13, RAIL3, 10, 'De notas sueltas a acuerdos con dueño.',
    'Tu clon · tus notas de la última reunión',
    'Una minuta que solo narra lo que se dijo no sirve. La que sirve <b>tiene dueño, fecha y una decisión</b> '
    'por línea — y eso se le puede exigir al formato.',
    ['Abre <b><code>07_notas_comite_operaciones.md</code></b>: notas crudas de un comité, desordenadas.',
     'Exige el formato de salida por adelantado; sin eso devuelve un resumen narrativo.',
     'Cuenta los compromisos que quedaron sin dueño o sin fecha: hay varios, y ese es el hallazgo real.'],
    '          <p>Estas son las notas crudas de un comité de operaciones: '
    '[pega <code>07_notas_comite_operaciones.md</code>].</p>\n'
    '          <p>Devuélveme <span class="kw">dos bloques y nada más</span>.</p>\n'
    '          <p><span class="kw">1. DECISIONES ·</span> tabla con: qué se decidió, quién lo dijo, qué queda '
    'bloqueado si no se cumple.</p>\n'
    '          <p><span class="kw">2. COMPROMISOS ·</span> tabla con: acción, dueño, fecha límite, '
    'cómo sabremos que se cumplió.</p>\n'
    '          <p>Si un compromiso no tiene dueño o no tiene fecha en mis notas, <span class="kw">no lo inventes</span>: '
    'ponlo igual y marca la casilla como [FALTA].</p>',
    'Dos tablas que se pegan en el correo de seguimiento. En estas notas hay al menos tres compromisos '
    'sin dueño o sin fecha: la homologación del criterio de devoluciones, la actualización del '
    'procedimiento y el análisis del servicio a domicilio.'))

d.add('Ejercicio 14 · Capacitación exprés', 'paper', exercise(
    14, RAIL3, 10, 'El material de capacitación, en una tarde.',
    'Tu clon · sobre un procedimiento o producto real',
    'Producir material formativo desde cero es de lo más lento del área. Con la fuente correcta, la IA arma '
    '<b>el guion y la evaluación</b>; tú aportas el criterio de qué es importante.',
    ['La fuente es <b><code>expediente-PR-ADM-014/</code></b>, el procedimiento de cotizaciones.',
     'Dásela completa. Sin fuente produce contenido plausible y equivocado — vale la pena verlo una vez.',
     'Revisa tú las preguntas de evaluación: ahí se cuela el error que nadie detecta.'],
    '          <p>Fuente única: [pega <code>PR-ADM-014_Gestion_de_Cotizaciones_v2.md</code>]. '
    'No uses conocimiento externo; si algo no está en la fuente, dilo.</p>\n'
    '          <p>Arma un módulo de capacitación de 20 minutos para asistentes comerciales nuevos con:</p>\n'
    '          <p><span class="kw">1.</span> Objetivo en una frase: qué sabrá hacer al terminar.<br/>'
    '<span class="kw">2.</span> Guion de [5] puntos, cada uno con un ejemplo del día a día.<br/>'
    '<span class="kw">3.</span> Los [3] errores más comunes y cómo se ven.<br/>'
    '<span class="kw">4.</span> [5] preguntas de evaluación con su respuesta y la línea de la fuente que la sustenta.</p>',
    'Un módulo listo para revisar, no para publicar. La cuarta parte es la clave: cada respuesta apunta a la '
    'fuente, así que verificarlo te toma minutos en vez de una tarde.',
    caveat='Todo material que se publique al equipo pasa por quien es dueño del procedimiento. La IA acelera '
           'la redacción; no valida el contenido técnico ni sustituye la aprobación del área.'))

# ---------------- bloque 4 ----------------
d.add('Bloque 4', 'section-div', divider(
    4, 4, 40, '4 EJERCICIOS', 'Confianza<br/>y control.',
    'Tu clon · tu criterio · una conversación de sala.',
    'Saber qué se sube, qué se verifica y qué se dice — antes de que sea un problema.',
    'Tu semáforo de datos y un compromiso a 10 días.'))

d.add('Ejercicio 15 · El semáforo', 'paper', exercise(
    15, RAIL4, 10, 'Qué sí y qué nunca le pegas.',
    'Ejercicio en papel · después se pega al clon',
    'La regla no puede ser "usa el sentido común": cuando hay prisa, el sentido común pierde. '
    '<b>Una lista de tres colores</b>, escrita antes, sí aguanta.',
    ['Escribe tu propia lista en tres columnas, con ejemplos de tu semana, no genéricos.',
     'Contrasta las dudas con la sala: lo que a ti te parece verde a otro le parece rojo.',
     'Pega la columna roja dentro de tu clon como prohibición explícita.'],
    '          <p><span class="kw">VERDE ·</span> Va sin pensarlo: texto que tú escribiste, documentos públicos '
    'de la empresa, datos que ya son de dominio público, ejemplos con nombres cambiados.</p>\n'
    '          <p><span class="kw">ÁMBAR ·</span> Solo con datos anonimizados o con visto bueno: cuadros internos '
    'sin identificar personas, procedimientos no publicados, información de proveedores.</p>\n'
    '          <p><span class="kw">ROJO ·</span> No entra nunca: datos personales de clientes o del equipo, '
    'contratos vigentes, credenciales, información financiera no publicada, cualquier cosa bajo acuerdo '
    'de confidencialidad.</p>\n'
    '          <p>Ante la duda, un caso ámbar se trata como rojo hasta que alguien lo autorice.</p>',
    'Tu lista, con ejemplos reales de tu área. Es lo que hace que la regla funcione un martes a las 5 de la tarde.',
    caveat='Esta lista es un punto de partida operativo, no la política oficial de la empresa. '
           'Lo que aplica en materia de protección de datos y confidencialidad lo definen Legal y TI, '
           'y varía entre Panamá, Costa Rica, El Salvador y Guatemala.'))

d.add('Ejercicio 16 · La marca VERIFICAR', 'paper', exercise(
    16, RAIL4, 10, 'Obligarla a mostrar las costuras.',
    'Tu clon · sobre cualquier salida con cifras',
    'El error caro no es el que se ve: es el dato inventado que <b>suena perfectamente razonable</b>. '
    'La defensa es exigir que marque lo que asumió.',
    ['Toma cualquier salida tuya que contenga cifras, fechas o condiciones.',
     'Pide la auditoría del propio texto, separando lo que le diste de lo que rellenó.',
     'Verifica tú, en la fuente, solo lo marcado. Ese es todo el trabajo que queda.'],
    '          <p>Revisa el texto que acabas de darme y sepáralo en tres listas:</p>\n'
    '          <p><span class="kw">DATO DADO ·</span> lo que salió de lo que yo te pegué. Cita la línea.<br/>'
    '<span class="kw">DATO ASUMIDO ·</span> lo que completaste tú porque parecía razonable. Márcalo [VERIFICAR].<br/>'
    '<span class="kw">DATO FALTANTE ·</span> lo que necesitarías para que esto quede completo.</p>\n'
    '          <p>No corrijas nada todavía. Solo muéstrame las tres listas.</p>\n'
    '          <p>Si algo de la primera lista no lo puedes citar textualmente, muévelo a la segunda.</p>',
    'La lista corta de lo que hay que comprobar. Casi siempre es mucho más corta de lo que temías — y casi '
    'nunca vacía, que es exactamente el punto.'))

d.add('Ejercicio 17 · Decirlo o no decirlo', 'paper', exercise(
    17, RAIL4, 10, '¿Se dice que lo hiciste con IA?',
    'Conversación de sala · sin herramienta',
    'En la encuesta apareció una vez: <b>"que no se note que es IA"</b>. Eso puede ser un estándar de calidad '
    'o puede ser una norma no escrita. No es lo mismo, y conviene saber cuál es.',
    ['Cada quien responde para sí: ¿te incomodaría que un colega supiera que ese correo lo redactaste con IA?',
     'Compartan las respuestas en la sala. Busquen si hay un patrón o son posiciones individuales.',
     'Cierren con <b>una sola línea</b> de acuerdo práctico para el área.'],
    '          <p><span class="kw">Las tres preguntas de la sala:</span></p>\n'
    '          <p>1. ¿Hay alguna situación en la que <span class="kw">sí</span> conviene decir que se usó IA? '
    '(por ejemplo, un informe que otra persona va a auditar)</p>\n'
    '          <p>2. ¿Hay alguna en la que declarar el uso <span class="kw">reste</span> valor al trabajo?</p>\n'
    '          <p>3. ¿La incomodidad viene de la herramienta, o de no poder responder por el contenido '
    'si alguien lo cuestiona?</p>\n'
    '          <p>Acuerdo del área, en una línea: [escríbanlo].</p>',
    'Una línea de acuerdo que evita la ambigüedad. La respuesta más frecuente en estos talleres es la tercera: '
    'lo que incomoda no es la herramienta, es firmar algo que no podrías defender.'))

d.add('Ejercicio 18 · Plan de 10 días', 'paper', exercise(
    18, RAIL4, 10, 'Qué haces distinto el lunes.',
    'Tu ficha, escrita a mano · foto al terminar',
    'Lo que no se aplica en los primeros días después de una formación, <b>no se aplica nunca</b>. '
    'Por eso esto no es un cierre simbólico: es el ejercicio con más efecto de la sesión.',
    ['Elige <b>dos</b> de los pedidos que guardaste hoy. Solo dos.',
     'Escribe cuándo los vas a usar, sobre qué tarea concreta, y qué señal te dirá que funcionó.',
     'Tómale foto y ponla donde la veas. Lo revisamos al abrir la sesión 2.'],
    '          <p><span class="kw">PEDIDO 1 ·</span> [nombre] — lo uso el [día] para [tarea real]. '
    'Sabré que sirvió si [señal concreta: me tomó la mitad del tiempo / no tuve que reescribirlo].</p>\n'
    '          <p><span class="kw">PEDIDO 2 ·</span> [nombre] — lo uso el [día] para [tarea real]. '
    'Sabré que sirvió si [señal].</p>\n'
    '          <p><span class="kw">OPCIONAL PARA LA SESIÓN 2 ·</span> si puedes, trae un cuadro o un '
    'export tuyo. No es requisito: la sesión 2 trae sus propios archivos.</p>',
    'Dos compromisos con fecha y una señal de éxito. Lo único que se revisa al abrir la sesión 2 es esto: '
    'cuál usaste y cuál no.'))

# ---------------- cierre ----------------
d.add('Gobernanza', None, governance(
    'ANTES DE CERRAR',
    'Lo que aplica<br/><span style="color:var(--green-br);">en los cuatro países</span>.',
    'Casa de las Baterías opera en Panamá, El Salvador, Costa Rica y Guatemala, y lo que se puede hacer con '
    'información de clientes no es idéntico en los cuatro. Estas son prácticas de trabajo, no asesoría legal: '
    'la política que manda la definen Legal y TI.',
    [('Cuenta de trabajo,<br/>no personal',
      'Todo lo laboral se hace desde la cuenta corporativa. Un chat en una cuenta personal queda fuera del '
      'alcance de la empresa y no se puede auditar ni recuperar.'),
     ('El semáforo,<br/>antes de pegar',
      'La lista roja del ejercicio 15 no es una recomendación: datos personales, contratos y credenciales '
      'no entran en ninguna herramienta de IA sin autorización expresa.'),
     ('Quien firma,<br/>responde',
      'La IA no responde por el contenido. Si un dato marcado [VERIFICAR] llegó al cliente sin comprobar, '
      'la responsabilidad es de quien lo mandó. Ese es el único límite que no se negocia.')]))

d.add('Cierre', 'closing', closing(
    'CIERRE DE LA SESIÓN 1',
    'LA IA NO<br/>FIRMA.<br/><span class="acc">TÚ SÍ.</span>',
    [('HOY MISMO', 'Guarda tus tres pedidos y tu ficha de voz donde los encuentres. Si cierras el navegador '
      'sin guardarlos, mañana empiezas de cero.'),
     ('ESTOS 10 DÍAS', 'Los dos compromisos del ejercicio 18. Se revisan al abrir la sesión 2 — no para '
      'evaluarte, para ajustar el contenido a lo que de verdad se atascó.'),
     ('PARA LA SESIÓN 2', 'No hace falta preparar nada: los archivos están en la misma carpeta. '
      'Si tienes un cuadro propio y quieres trabajarlo, tráelo — el ejercicio funciona igual.')]))

HTML = d.render()
