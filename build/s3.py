# -*- coding: utf-8 -*-
"""Sesión 3 — Lo que pidieron Administración y Gerencia Comercial.

Cada bloque responde a una necesidad escrita en el formulario previo, con sus
palabras. El lenguaje de esta sesión lo vigila verifica-lenguaje.mjs: frases
cortas, sin jerga y sin conceptos gritados en mayúsculas.
"""
from deck import (Deck, cover, statement, agenda, howto, divider,
                  exercise_case, closing, filelist, cards, recipe)


def prompt(*paragraphs):
    return '\n'.join(f'          <p>{paragraph}</p>' for paragraph in paragraphs)


RAIL1 = 'BLOQUE 01 <span class="sep"></span> PEDIR BIEN LA PRIMERA VEZ'
RAIL2 = 'BLOQUE 02 <span class="sep"></span> QUE SUENE A TI'
RAIL3 = 'BLOQUE 03 <span class="sep"></span> TUS CIFRAS EN UNA PANTALLA'
RAIL4 = 'BLOQUE 04 <span class="sep"></span> PROCEDIMIENTOS SIN DOLOR'

TODAS = 'Gemini, ChatGPT o Claude'

d = Deck('Sesión 3 · IA para Administración y Gerencia Comercial · Casa de las Baterías', {'sesion': 3})

# ---------------------------------------------------------------- apertura

d.add('Portada', 'cover', cover(
    'CASA DE LAS BATERÍAS · ADMINISTRACIÓN Y GERENCIA COMERCIAL',
    'IA PARA ADMINISTRACIÓN<br/>Y <span class="acc">GERENCIA COMERCIAL</span>.',
    'Sesión 3 de 3 · 16 laboratorios sobre las cuatro cosas que pidieron en el formulario previo.',
    'Sesión 3 · Edición 2026', 180))

d.add('De dónde sale', None, statement(
    'PUNTO DE PARTIDA',
    'Esta sesión no la armamos nosotros.<br/>La armaron <span style="color:var(--brand-br);">tus respuestas</span>.',
    '<p style="font-size:28px;line-height:1.48;color:var(--bone-2);max-width:1480px;margin-top:34px;">'
    'Cinco personas contestaron el formulario. Nadie empieza de cero: todos usan IA ya. '
    'Pero las cuatro cosas que pidieron siguen pendientes. '
    '<b style="color:var(--bone);">Hoy las resolvemos, en ese orden.</b></p>', 80))

d.add('Lo que pidieron', 'paper', cards(
    'LAS CUATRO COSAS QUE PIDIERON',
    'Cuatro pedidos.<br/>Cuatro bloques.',
    'Entre comillas, lo que escribieron en el formulario. Debajo, dónde se resuelve hoy.',
    [('«Qué prompts usar»',
      'Tres de cinco lo pidieron. Uno dijo: «tengo que corregir demasiado lo que genera».',
      'Bloque 1. Sales con seis pedidos tuyos, guardados y probados.'),
     ('«Que no se vea que es IA»',
      'La misma persona lo dijo dos veces. También: «que no salga genérica».',
      'Bloque 2. Sacamos tu forma de escribir de tus propios correos.'),
     ('«Ejemplo de dashboard o gráficos»',
      'Tres de cinco. Otro pidió «mejorar la presentación de indicadores en menos tiempo».',
      'Bloque 3. Un tablero de verdad, en la herramienta que tengas.'),
     ('«Nomenclatura y códigos»',
      'El pedido más concreto: revisar nombres, códigos y anexos de procedimientos.',
      'Bloque 4. Cuarenta y un procedimientos auditados en una pasada.')], cols=4))

d.add('Agenda', 'paper', agenda(
    '4 BLOQUES <span class="sep"></span> 16 LABORATORIOS <span class="sep"></span> RITMO DEL FACILITADOR',
    'De «no sé qué pedirle»<br/>a «esto ya lo tengo listo».',
    [('01 · BLOQUE 1', 'Pedir bien la primera vez',
      [('El mismo pedido, dos resultados', ''), ('Las seis partes', ''),
       ('Tu biblioteca de pedidos', ''), ('Tu caso', '')]),
     ('02 · BLOQUE 2', 'Que suene a ti',
      [('Tu forma de escribir', ''), ('Las frases que delatan', ''),
       ('Cambiar una cosa sin tocar el resto', ''), ('Tu caso', '')]),
     ('03 · BLOQUE 3', 'Tus cifras en una pantalla',
      [('Las cinco cifras que miras', ''), ('Tu tablero del lunes', ''),
       ('El gráfico que se entiende solo', ''), ('Tu caso', '')]),
     ('04 · BLOQUE 4', 'Procedimientos sin dolor',
      [('Cuarenta y un nombres', ''), ('El anexo fantasma', ''),
       ('Veinte días', ''), ('Tu caso', '')])]))

d.add('Cómo se trabaja', 'paper', howto(
    'REGLAS DE LA SESIÓN',
    'Usa la herramienta que ya tienes.<br/>Sal con algo hecho.',
    # Tres tarjetas, no cuatro: el grid del molde es de tres columnas y la cuarta
    # cae a una segunda fila que invade el pie. Lo detectó verifica-layout.js.
    [('Da igual cuál uses',
      'Gemini, ChatGPT o Claude. Los tableros y los gráficos traen receta para cada una. '
      'Sin acceso, trabaja en pareja.'),
     ('Trae tu caso, aunque sea a medias',
      'Cada bloque cierra con tu trabajo. Si no traes nada, usa el archivo del curso. '
      'Quítale nombres y teléfonos de clientes antes de subirlo.'),
     ('Lo que salga lo revisas tú',
      'La IA no aprueba una cotización ni publica un procedimiento. Eso lleva tu firma.')]))

d.add('Los materiales', 'paper', filelist(
    'ARCHIVOS DE LA SESIÓN',
    'Dos archivos nuevos.<br/><span style="color:var(--brand);">Casos inventados de CasaBat</span>.',
    'Están todos en la página del taller. No hay que preparar nada antes de empezar.',
    [('NUEVOS EN ESTA SESIÓN', [
        ('15_prompts_que_fallaron.docx', 'Ocho pedidos flojos y su versión arreglada'),
        ('16_maestro_procedimientos.xlsx', 'Cuarenta y un procedimientos con nombres y anexos mal'),
        ('09_reglas_de_nomenclatura.docx', 'La regla contra la que se revisan los nombres'),
        ('04_ventas_sucursales_2026.xlsx', 'Ventas del semestre en cuatro países'),
     ]),
     ('YA LOS CONOCES', [
        ('06_correos_de_referencia.docx', 'Tres correos para sacar tu forma de escribir'),
        ('00_contexto_marca_casabat.docx', 'Tono de CasaBat y lo que no se promete'),
        ('05_correos_pendientes.xlsx', 'Veinte correos, uno de garantía difícil'),
        ('03_politica_garantia.docx', 'Qué cubre la garantía y qué no'),
     ])]))

# ---------------------------------------------------------------- bloque 1

d.add('Bloque 1', 'section-div', divider(
    1, 4, 45, '4 LABORATORIOS', 'Pedir bien<br/>la primera vez.',
    TODAS + ' · tu tarea más repetida.',
    'Dejar de corregir tres veces lo que podía salir bien de una.',
    'Seis pedidos tuyos, escritos, probados y guardados donde los encuentres.'))

d.add('Laboratorio 1', 'paper', exercise_case(
    1, RAIL1, 12, 'El mismo pedido, dos resultados muy distintos.',
    'Jefatura de Gerencia Comercial', '<code>15_prompts_que_fallaron.docx</code>', TODAS,
    'Alguien pidió «hazme un correo para el cliente sobre la cotización». Volvió un correo '
    'de seis párrafos, sin número de cotización y sin monto.',
    'Qué le faltaba al pedido. No era cortesía: eran datos.',
    ['Abre el caso 1 del archivo y lee el pedido flojo.',
     'Pídeselo tal cual a tu herramienta y mira lo que vuelve.',
     'Ahora pega el pedido arreglado y compara los dos resultados.'],
    prompt('Escribe un correo de la jefatura comercial al contacto de una flota.',
           'La cotización 9011 por 4.320 dólares venció el viernes. Necesito que confirme si '
           'todavía la quiere con el precio nuevo.',
           'Tres párrafos cortos, cercano y directo. Cierra pidiendo respuesta esta semana. '
           'No prometas descuentos ni plazos de garantía.'),
    'Los dos correos, uno al lado del otro, y la lista de lo que cambió.',
    'Puedes señalar las cuatro cosas que el segundo pedido dice y el primero no.'))

d.add('Laboratorio 2', 'paper', exercise_case(
    2, RAIL1, 12, 'Las seis partes que le faltan a casi todo pedido.',
    'Analista de Administración', 'tu tarea más repetida de la semana', TODAS,
    'Cuando el resultado sale flojo, casi siempre falta una de seis cosas. La más olvidada '
    'es la última: qué hacer cuando un dato no está.',
    'Cuál de las seis le falta a tu pedido de siempre.',
    ['Escribe tu pedido habitual tal como lo escribes hoy.',
     'Marca cuáles de las seis partes le faltan.',
     'Reescríbelo con las que falten y pruébalo.'],
    prompt('Quién habla y a quién · el dato concreto · qué tiene que pasar · la forma · '
           'lo que no se toca · qué hacer si falta un dato.',
           'Revisa mi pedido con esa lista de seis. Dime cuáles le faltan y escríbelo otra vez '
           'con todas. No cambies lo que ya estaba bien.'),
    'Tu pedido de siempre, reescrito, con las seis partes visibles.',
    'El resultado sale usable en el primer intento, sin tener que corregirlo.'))

d.add('Laboratorio 3', 'paper', exercise_case(
    3, RAIL1, 12, 'Guarda el pedido que funcionó, dale un nombre.',
    'Coordinador de Administración', 'los pedidos de los laboratorios 1 y 2', TODAS,
    'El pedido bueno se pierde en el chat de ayer. La semana siguiente se vuelve a escribir '
    'desde cero, peor que la primera vez.',
    'Qué seis pedidos tuyos vale la pena guardar para siempre.',
    ['Elige seis tareas que repites cada semana.',
     'Guarda cada pedido en tu herramienta y ponle un nombre que entiendas.',
     'Pásale uno a un compañero y que lo use sin preguntarte nada.'],
    prompt('Ayúdame a ordenar mis pedidos guardados.',
           'Para cada uno: un nombre corto, para qué sirve, qué le tengo que cambiar cada vez '
           'y qué archivo necesita.',
           'Avísame si dos de mis seis piden lo mismo con otras palabras.'),
    'Seis pedidos guardados con nombre, y uno de ellos probado por otra persona.',
    'Tu compañero lo usa y obtiene lo mismo que tú, sin que le expliques.'))

d.add('Laboratorio 4', 'paper', exercise_case(
    4, RAIL1, 9, 'Tu caso: el pedido del lunes por la mañana.',
    'Cada participante, con su propio trabajo', 'la primera tarea de tu lunes', TODAS,
    'El lunes tienes una tarea que vas a hacer igual que siempre. Hoy la dejas resuelta '
    'antes de que llegue.',
    'Si el pedido sale bien sin que tengas que arreglarlo.',
    ['Escribe la tarea concreta del lunes, con su archivo si lo tiene.',
     'Armá el pedido con las seis partes y pruébalo aquí.',
     'Guárdalo con nombre y anota qué le cambiarás cada semana.'],
    prompt('<span class="kw">APLICACIÓN INDIVIDUAL</span> · Mi tarea del lunes es [descríbela]. '
           'El archivo que uso es [cuál].',
           'Ayúdame a escribir el pedido con las seis partes. Después dime qué parte queda '
           'débil y por qué.'),
    'Un pedido guardado, probado y listo para el lunes.',
    'Lo usas el lunes sin volver a escribirlo y sin corregir el resultado.'))

# ---------------------------------------------------------------- bloque 2

d.add('Bloque 2', 'section-div', divider(
    2, 4, 45, '4 LABORATORIOS', 'Que suene a ti,<br/>no a robot.',
    TODAS + ' · tres correos tuyos · el tono de CasaBat.',
    'Que lo que escribas con IA se parezca a lo que escribes tú.',
    'Tu ficha de voz, la lista de frases prohibidas y un correo difícil resuelto.'))

d.add('Laboratorio 5', 'paper', exercise_case(
    5, RAIL2, 12, 'Tu forma de escribir ya existe. Hay que sacarla.',
    'Jefatura de Administración', '<code>06_correos_de_referencia.docx</code> o tres correos tuyos', TODAS,
    'Pedirle «que no suene a IA» no sirve: es una queja, no una instrucción. Lo que funciona '
    'es darle tres correos tuyos y pedirle el patrón.',
    'Cómo escribes tú: cómo arrancas, qué largo tienen tus frases, cómo cierras.',
    ['Pega tres correos tuyos, o los tres del archivo.',
     'Pide una ficha con tu forma de arrancar, de explicar y de cerrar.',
     'Corrige la ficha donde no te reconozcas.'],
    prompt('Te pego tres correos míos. No los califiques.',
           'Dime cómo arranco, qué largo tienen mis frases, si trato de tú o de usted, cómo '
           'doy una mala noticia y cómo cierro.',
           'Hazme una ficha de media página que pueda pegarte la próxima vez.'),
    'Una ficha de media página con tu forma de escribir.',
    'Le pegas la ficha a un correo nuevo y te reconoces en el resultado.'))

d.add('Laboratorio 6', 'paper', exercise_case(
    6, RAIL2, 12, 'Las frases que delatan a la IA en tres segundos.',
    'Analista de Administración', '<code>00_contexto_marca_casabat.docx</code>', TODAS,
    'Hay frases que nadie de CasaBat usa al hablar. «Esperamos que se encuentre muy bien». '
    '«No dude en contactarnos». «La mejor calidad del mercado».',
    'Qué frases salen de tu lista negra y cuáles son promesas que no puedes hacer.',
    ['Junta diez frases de relleno que veas en los resultados.',
     'Busca en el archivo de marca qué promesas están prohibidas.',
     'Arma una lista y pégasela a la herramienta como regla fija.'],
    prompt('Esta es mi lista de frases que no quiero ver nunca: [pégala].',
           'Revisa este correo y quítalas todas sin cambiar lo que dice. Marca en negrita lo '
           'que tocaste.',
           'Si encuentras una promesa de precio, de plazo o de garantía que el texto no puede '
           'sostener, señálala.'),
    'Tu lista negra y el correo limpio, con los cambios marcados.',
    'El correo ya no tiene relleno y no promete nada que CasaBat no pueda cumplir.'))

d.add('Laboratorio 7', 'paper', exercise_case(
    7, RAIL2, 12, 'Cambiar una cosa sin que te reescriba todo.',
    'Jefatura de Gerencia Comercial', 'el correo del laboratorio 6', TODAS,
    'Pides un ajuste pequeño y vuelve el texto entero distinto. Se pierden datos que estaban '
    'bien y toca comparar línea por línea.',
    'Cómo pedir un cambio chico y que el resto quede intacto.',
    ['Toma un texto que ya casi te sirve.',
     'Pide solo dos cambios y di qué no se toca.',
     'Compara con el anterior y comprueba que nada más se movió.'],
    prompt('Este correo ya dice lo que quiero. Cámbiame solo dos cosas.',
           'El primer párrafo es muy largo: pártelo en dos. El cierre suena duro: suavízalo.',
           'No toques el resto, ni el orden, ni los montos. Devuélvemelo completo y marca en '
           'negrita lo que cambiaste.'),
    'El texto con dos cambios y todo lo demás igual.',
    'Comparas las dos versiones y solo cambió lo que pediste.'))

d.add('Laboratorio 8', 'paper', exercise_case(
    8, RAIL2, 9, 'Tu caso: el correo que llevas días sin escribir.',
    'Cada participante, con su propio trabajo',
    'un correo difícil real, o el de garantía de <code>05_correos_pendientes.xlsx</code>', TODAS,
    'Hay un correo pendiente porque cuesta escribirlo. Un cliente que insiste con una batería '
    'de moto de ocho meses. Un proveedor que no entregó.',
    'Qué le dices, qué no le prometes y con qué tono.',
    ['Elige el correo difícil y escribe en una línea qué quieres lograr.',
     'Pega tu ficha de voz y tu lista negra del bloque.',
     'Pide el correo y revísalo contra la política de garantía.'],
    prompt('<span class="kw">APLICACIÓN INDIVIDUAL</span> · Tengo que escribir a [quién] sobre '
           '[qué]. Quiero lograr [qué].',
           'Usa mi ficha de voz y mi lista negra, que te pego abajo. Tres párrafos.',
           'Si la respuesta depende de algo que no te di, pregúntame antes de escribir.'),
    'El correo difícil, listo para enviar, con tu voz.',
    'Lo lees en voz alta y suena a ti; no promete nada que la política no cubra.'))

# ---------------------------------------------------------------- bloque 3

d.add('Bloque 3', 'section-div', divider(
    3, 4, 50, '4 LABORATORIOS', 'Tus cifras en<br/>una pantalla.',
    'Una receta para Gemini, una para ChatGPT y una para Claude.',
    'Un tablero que sirva para la reunión del lunes, no una galería de gráficos.',
    'Tu tablero, un gráfico que se explica solo y la receta de tu herramienta.'))

d.add('Laboratorio 9', 'paper', exercise_case(
    9, RAIL3, 12, 'Antes de dibujar nada: ¿qué cinco cifras miras?',
    'Gerencia Comercial', '<code>04_ventas_sucursales_2026.xlsx</code>', TODAS,
    'Pedir «hazme un dashboard» devuelve catorce gráficos, dos tortas de nueve pedazos y '
    'ningún total. Bonito en la pantalla, inservible en la reunión.',
    'Qué cinco cifras abres primero el lunes. Esas son el tablero; el resto estorba.',
    ['Escribe las cinco cifras que de verdad miras.',
     'Para cada una, di de qué columna del archivo sale.',
     'Pide la lista de los problemas del archivo antes de calcular.'],
    prompt('Estas son las cinco cifras que necesito: [escríbelas].',
           'Antes de calcular, dime qué problemas tiene el archivo: categorías escritas de '
           'varias formas, fechas en dos formatos, celdas vacías, números raros.',
           'Después dame cada cifra con la columna de donde sale. No agregues cifras que no '
           'te pedí.'),
    'Las cinco cifras, de dónde sale cada una y la lista de problemas del archivo.',
    'Las cinco caben en una pantalla y cada una se puede rastrear a una columna.'))

d.add('Laboratorio 10', 'paper', exercise_case(
    10, RAIL3, 15, 'Tu tablero para la reunión del lunes.',
    'Gerencia Comercial', '<code>04_ventas_sucursales_2026.xlsx</code>',
    'elige tu receta: Gemini, ChatGPT o Claude',
    'Hay que llevar a la reunión el semestre de cuatro países. Cuatro cifras arriba, un '
    'gráfico debajo y un filtro por país. Nada más.',
    'Qué va arriba, qué va abajo y qué se queda fuera.',
    ['Decide las cuatro cifras de arriba y el gráfico de abajo.',
     'Abre la receta de tu herramienta en los tres slides que siguen.',
     'Haz el tablero y filtra por Panamá para comprobarlo.'],
    prompt('Hazme un tablero de una pantalla con este archivo de ventas.',
           'Arriba cuatro cifras: ingreso del semestre, unidades, devoluciones y la sucursal '
           'que más cayó. Debajo, barras de ingreso por línea de producto, de mayor a menor.',
           'Que se pueda filtrar por país. Nada más: ni tortas, ni cifras que no te pedí.'),
    'Un tablero de una pantalla que se filtra por país.',
    'Cambias el filtro a Guatemala y las cuatro cifras de arriba se mueven.',
    'Las devoluciones vienen vacías en ocho filas. Decide si eso es cero o si es un dato '
    'que falta, y déjalo escrito en el tablero.'))

d.add('Receta tablero · Gemini', 'paper', recipe(
    'RECETA A <span class="sep"></span> GEMINI',
    'Tu tablero en Gemini.',
    'Gemini trabaja dentro de la hoja de cálculo. El tablero queda en Sheets y se comparte como '
    'cualquier hoja.',
    ['Sube el archivo a Drive y ábrelo con Hojas de cálculo.',
     'Haz una copia de la hoja. Trabaja en la copia.',
     'Abre Gemini con el botón de la esquina y pégale el pedido.',
     'Pide una tabla dinámica, cuatro tarjetas de cifra y un gráfico de barras.',
     'Añade un segmentador por país: es el filtro de Sheets.',
     'Revisa que las cifras cuadren con la hoja original antes de compartir.'],
    'PEGA ESTO EN GEMINI',
    '          <p>Trabaja sobre la copia de esta hoja, no sobre la original.</p>\n'
    '          <p>Hazme una tabla dinámica con ingreso, unidades y devoluciones por país y por '
    'línea de producto. Arriba, cuatro tarjetas con los totales del semestre.</p>\n'
    '          <p>Un gráfico de barras de ingreso por línea, de mayor a menor. Y un segmentador '
    'por país.</p>\n'
    '          <p>Las categorías vienen escritas de varias formas. Antes de sumar, dime cuáles '
    'crees que son la misma y espera mi visto bueno.</p>',
    'Si Gemini no aparece en tu hoja, puede ser la licencia de la cuenta. Hazlo en pareja y '
    'sigue con la receta de ChatGPT.'))

d.add('Receta tablero · ChatGPT', 'paper', recipe(
    'RECETA B <span class="sep"></span> CHATGPT',
    'Tu tablero en ChatGPT.',
    'ChatGPT analiza el archivo y devuelve el tablero como imagen, como hoja descargable o como '
    'página web. Pide el formato que vas a usar.',
    ['Arrastra el archivo al chat.',
     'Pide primero el perfil de columnas y los problemas del archivo.',
     'Después pide el tablero y di en qué formato lo quieres.',
     'Para la reunión, pide una hoja de Excel con el tablero ya armado.',
     'Si quieres filtrar en vivo, pide una página web de una sola pantalla.',
     'Comprueba dos cifras a mano antes de llevarlo.'],
    'PEGA ESTO EN CHATGPT',
    '          <p>Te subo las ventas del semestre de Casa de las Baterías.</p>\n'
    '          <p>Primero dime qué problemas tiene el archivo: categorías repetidas con otra '
    'escritura, fechas en dos formatos, celdas vacías, números imposibles. No corrijas nada '
    'todavía.</p>\n'
    '          <p>Cuando te dé el visto bueno, hazme un tablero de una pantalla: cuatro cifras '
    'arriba y barras de ingreso por línea debajo, de mayor a menor.</p>\n'
    '          <p>Dámelo como archivo de Excel con el filtro por país ya puesto.</p>',
    'Si te devuelve una imagen, no sirve para la reunión: no se puede filtrar. Pide el Excel '
    'o la página web.'))

d.add('Receta tablero · Claude', 'paper', recipe(
    'RECETA C <span class="sep"></span> CLAUDE',
    'Tu tablero en Claude.',
    'Claude devuelve el tablero como una página que se abre al lado del chat y se usa con el '
    'ratón. Es la vía más rápida para un tablero que se filtra en vivo.',
    ['Sube el archivo al chat.',
     'Pide el perfil de columnas y los problemas antes de nada.',
     'Pide el tablero como una página de una sola pantalla.',
     'Pruébalo ahí mismo: cambia el filtro de país y mira si se mueve.',
     'Pide los cambios hablando; la página se actualiza sola.',
     'Para compartirlo, publícalo y manda el enlace.'],
    'PEGA ESTO EN CLAUDE',
    '          <p>Te subo las ventas del semestre de Casa de las Baterías.</p>\n'
    '          <p>Antes de calcular, dime qué problemas tiene el archivo y espera mi '
    'respuesta.</p>\n'
    '          <p>Después hazme un tablero de una sola pantalla: cuatro cifras arriba, barras '
    'de ingreso por línea debajo y un filtro por país que funcione con el ratón.</p>\n'
    '          <p>Sin tortas. Sin cifras que no te pedí. Si una cifra sale de una columna con '
    'celdas vacías, dilo en el propio tablero.</p>',
    'El tablero sale de los datos que subiste. Si cambias el archivo, hay que volver a '
    'pedirlo: no se actualiza solo.'))

d.add('Laboratorio 11', 'paper', exercise_case(
    11, RAIL3, 12, 'El gráfico que se entiende sin que lo expliques.',
    'Gerencia Comercial', 'las cifras del laboratorio 10',
    'elige tu receta: Gemini, ChatGPT o Claude',
    'En el archivo, tres de seis líneas de producto hacen el 84 por ciento del ingreso. Eso '
    'se ve en un gráfico y se pierde en una tabla.',
    'Qué gráfico cuenta esa historia y qué gráfico la esconde.',
    ['Escribe en una frase qué quieres que entienda quien lo vea.',
     'Pide el gráfico más simple que diga eso.',
     'Quita todo lo que no ayude: colores de más, leyendas repetidas, decimales.'],
    prompt('Quiero que quien vea esto entienda una sola cosa: [escríbela].',
           'Dame el gráfico más simple que lo muestre. Ordena de mayor a menor y pon el valor '
           'sobre cada barra.',
           'Sin tortas, sin tres dimensiones, sin colores que no signifiquen nada. Si crees que '
           'otro tipo de gráfico lo dice mejor, propónmelo y explica por qué.'),
    'Un gráfico que se explica solo, con su título escrito por ti.',
    'Alguien que no estuvo en la reunión lo mira y dice lo que querías que entendiera.'))

d.add('Receta gráfico · Gemini', 'paper', recipe(
    'RECETA A <span class="sep"></span> GEMINI',
    'Tu gráfico en Gemini.',
    'El gráfico nace dentro de la hoja. Se edita con los menús de Sheets cuando la IA no acierta '
    'con el detalle.',
    ['Selecciona la columna de líneas y la de ingreso.',
     'Pide el gráfico a Gemini desde la hoja.',
     'Ordena de mayor a menor en la tabla, no en el gráfico.',
     'Añade el valor sobre cada barra desde el menú del gráfico.',
     'Escribe tú el título: la IA pone títulos genéricos.'],
    'PEGA ESTO EN GEMINI',
    '          <p>Con la tabla de ingreso por línea de producto, hazme un gráfico de barras '
    'horizontales.</p>\n'
    '          <p>De mayor a menor, con el valor en dólares sobre cada barra, sin decimales.</p>\n'
    '          <p>Un solo color, salvo las tres líneas que más venden: esas en el azul de la '
    'marca. Deja el título vacío, lo escribo yo.</p>',
    'Si ordena mal, revisa la tabla de origen: el gráfico copia el orden de las filas.'))

d.add('Receta gráfico · ChatGPT', 'paper', recipe(
    'RECETA B <span class="sep"></span> CHATGPT',
    'Tu gráfico en ChatGPT.',
    'ChatGPT dibuja el gráfico al analizar el archivo. Pídelo como imagen para pegar, o dentro '
    'de la hoja si lo vas a seguir editando.',
    ['Pide el gráfico después de haber limpiado las categorías.',
     'Di el tipo exacto: barras horizontales, ordenadas, con el valor encima.',
     'Pide la imagen en buena resolución para la presentación.',
     'Si lo vas a editar, pídelo dentro de un archivo de Excel.',
     'Revisa que los nombres de las líneas no salgan cortados.'],
    'PEGA ESTO EN CHATGPT',
    '          <p>Con las categorías ya unificadas, hazme un gráfico de barras horizontales de '
    'ingreso por línea de producto.</p>\n'
    '          <p>De mayor a menor, el valor en dólares sobre cada barra y sin decimales. Un '
    'solo color, y las tres líneas que más venden en azul oscuro.</p>\n'
    '          <p>Dámelo como imagen grande y también dentro de un Excel, por si necesito '
    'moverle algo.</p>',
    'Si los nombres salen cortados, pide más margen a la izquierda o barras horizontales en '
    'vez de verticales.'))

d.add('Receta gráfico · Claude', 'paper', recipe(
    'RECETA C <span class="sep"></span> CLAUDE',
    'Tu gráfico en Claude.',
    'Claude devuelve el gráfico dentro de una página que se abre al lado. Se puede pasar el '
    'ratón por encima y ver el dato de cada barra.',
    ['Pide el gráfico dentro de una página, no como imagen.',
     'Di el tipo, el orden y qué se destaca.',
     'Pásale el ratón por encima para comprobar los valores.',
     'Pide los ajustes hablando: «sube el contraste», «quita los decimales».',
     'Descarga la imagen desde la página cuando te sirva.'],
    'PEGA ESTO EN CLAUDE',
    '          <p>Hazme una página con un gráfico de barras horizontales de ingreso por línea '
    'de producto.</p>\n'
    '          <p>De mayor a menor, valor en dólares sobre cada barra, sin decimales. Las tres '
    'líneas que más venden en azul oscuro, el resto en gris.</p>\n'
    '          <p>Que al pasar el ratón por una barra se vea el ingreso y las unidades. El '
    'título lo escribo yo: déjalo vacío.</p>',
    'Para la presentación necesitas la imagen: descárgala de la página. La página sola no entra '
    'en un archivo de diapositivas.'))

d.add('Laboratorio 12', 'paper', exercise_case(
    12, RAIL3, 11, 'Tu caso: el tablero de tu área.',
    'Cada participante, con su propio trabajo',
    'un archivo tuyo sin datos de clientes, o el de ventas del curso', TODAS,
    'Cada área mira sus cifras: cobros, cierre de caja, inventario, cotizaciones del mes. Hoy '
    'sale el tablero de las tuyas.',
    'Qué cinco cifras son las tuyas y quién más las va a mirar.',
    ['Escribe tus cinco cifras y de dónde sale cada una.',
     'Usa la receta de tu herramienta para armarlo.',
     'Muéstraselo a un compañero y que te diga qué no entiende.'],
    prompt('<span class="kw">APLICACIÓN INDIVIDUAL</span> · Mis cinco cifras son [escríbelas] '
           'y salen de [qué archivo].',
           'Hazme un tablero de una pantalla con esas cinco y un gráfico que las explique.',
           'Dime también qué cifra no se puede calcular bien con lo que te di, y qué columna '
           'me falta.'),
    'Tu tablero, con tus cifras, probado por otra persona.',
    'Tu compañero lo mira y entiende las cinco cifras sin que se las expliques.'))

# ---------------------------------------------------------------- bloque 4

d.add('Bloque 4', 'section-div', divider(
    4, 4, 50, '4 LABORATORIOS', 'Procedimientos<br/>sin dolor.',
    TODAS + ' · 41 procedimientos · la regla de nombres.',
    'Hacer en una pasada el cruce de nombres, códigos y anexos que hoy se hace a mano.',
    'Los 41 procedimientos revisados, los anexos cruzados y un plan de veinte días.'))

d.add('Laboratorio 13', 'paper', exercise_case(
    13, RAIL4, 14, 'Cuarenta y un nombres. Doce están mal puestos.',
    'Analista de Administración',
    '<code>16_maestro_procedimientos.xlsx</code> · <code>09_reglas_de_nomenclatura.docx</code>',
    TODAS,
    'Hoy esto se revisa archivo por archivo. Son 41 procedimientos y la regla tiene siete '
    'puntos. A ojo se escapan los repetidos.',
    'Cuáles rompen la regla y qué parte del nombre falla en cada uno.',
    ['Pega la regla primero. Sin la regla, la IA inventa su criterio.',
     'Pide una fila por archivo, los 41, sin agrupar ni resumir.',
     'Comprueba a mano tres de los que marcó y tres de los que dejó pasar.'],
    prompt('Te pego la regla de nombres y la lista de los 41 procedimientos.',
           'Revísalos uno por uno. Dame una tabla con archivo, qué regla rompe, qué parte del '
           'nombre está mal y cómo debería llamarse.',
           'Si cumple, ponlo como correcto. No te saltes ninguno y no agrupes. Al final dime '
           'cuántos están mal.'),
    'La tabla de los 41, con el nombre corregido propuesto para cada uno.',
    'Encuentra los 12 de los 41 nombres mal puestos, y los tres que revisas a mano coinciden.',
    'Dos archivos rompen la regla y además tienen el código repetido. Revisar el nombre no es '
    'revisar el contenido: son dos pasadas distintas.'))

d.add('Laboratorio 14', 'paper', exercise_case(
    14, RAIL4, 13, 'El anexo que se cita y no existe.',
    'Analista de Administración', '<code>16_maestro_procedimientos.xlsx</code>', TODAS,
    'Un procedimiento cita el anexo D. El anexo D no está. Y hay un anexo C guardado que nadie '
    'cita desde ninguna parte.',
    'Qué anexos faltan, cuáles sobran y qué códigos aparecen dos veces como vigentes.',
    ['Pide el cruce en las dos direcciones: citados contra existentes.',
     'Pide aparte los códigos que aparecen más de una vez como vigentes.',
     'Ordena los hallazgos por lo que más riesgo tiene.'],
    prompt('Con la columna de anexos citados y la de anexos que existen, hazme tres listas.',
           'Primera: anexos citados que no existen. Segunda: anexos que existen y nadie cita. '
           'Tercera: letras de anexo con un salto, como citar A, B y D sin la C.',
           'Aparte, dime qué códigos están dos veces como vigentes. Pon cada hallazgo con su '
           'número de fila.'),
    'Las tres listas de anexos y la lista de códigos repetidos, con su fila.',
    'Cada hallazgo apunta a una fila del archivo y puedes abrirla y comprobarlo.'))

d.add('Laboratorio 15', 'paper', exercise_case(
    15, RAIL4, 14, 'Veinte días para actualizar un procedimiento.',
    'Jefatura de Administración',
    'los hallazgos de los laboratorios 13 y 14 · <code>10_PR-ADM-014_v3_BORRADOR.docx</code>', TODAS,
    'El plazo es de veinte días y el dueño del proceso tiene media hora. Lo que se hace con '
    'esa media hora decide si el borrador sale o no.',
    'Qué le preguntas al dueño y qué puedes redactar sin molestarlo.',
    ['Pide las diez preguntas que hay que hacerle al dueño.',
     'Con sus respuestas, pide el borrador y la lista de cambios.',
     'Marca qué cambió respecto a la versión vigente y por qué.'],
    prompt('Tengo veinte días para actualizar este procedimiento y media hora con su dueño.',
           'Dame diez preguntas concretas, ordenadas por lo que más decide. Nada de preguntas '
           'de relleno.',
           'Después, con mis respuestas, redacta el borrador y una tabla de cambios: qué '
           'cambió, por qué y quién lo pidió. Lo que no me hayas preguntado, déjalo igual.'),
    'Las diez preguntas, el borrador y la tabla de cambios.',
    'La tabla deja ver qué cambió y por qué; el borrador no toca nada que no se haya decidido.',
    'El borrador sigue siendo borrador hasta que alguien lo firme. No le pongas fecha de '
    'vigencia tú.'))

d.add('Laboratorio 16', 'paper', exercise_case(
    16, RAIL4, 9, 'Tu caso: el procedimiento que tienes pendiente.',
    'Cada participante, con su propio trabajo', 'un procedimiento de tu área, sin datos de clientes', TODAS,
    'Todos tienen uno pendiente: el que nadie ha actualizado, el que tiene anexos sueltos, el '
    'que dos áreas usan distinto.',
    'Qué parte puedes dejar resuelta hoy y qué necesitas pedirle a alguien.',
    ['Escribe cuál es y qué le falta.',
     'Aplícale la revisión de nombre y el cruce de anexos.',
     'Saca las preguntas para su dueño y ponles fecha.'],
    prompt('<span class="kw">APLICACIÓN INDIVIDUAL</span> · Mi procedimiento pendiente es '
           '[cuál] y le falta [qué].',
           'Revísale el nombre y el código con la regla que te pego. Cruza sus anexos.',
           'Después dame las preguntas para su dueño y qué puedo redactar yo sin esperarlo.'),
    'Tu procedimiento revisado y las preguntas listas con fecha.',
    'Sales con una tarea concreta y con nombre de la persona a la que se la vas a pedir.'))

d.add('Cierre', None, closing(
    'CIERRE DEL PROGRAMA',
    'Pediste cuatro cosas.<br/>Te vas con <span style="color:var(--brand-br);">cuatro cosas hechas</span>.',
    [('SEIS PEDIDOS', 'Guardados con nombre, probados por otra persona, listos para el lunes.'),
     ('TU VOZ', 'Una ficha de media página y la lista de frases que no vuelven a aparecer.'),
     ('UN TABLERO', 'Cinco cifras en una pantalla, con la receta de la herramienta que usas.'),
     ('CUARENTA Y UN NOMBRES', 'Revisados en una pasada, con los anexos cruzados en las dos direcciones.')]))

HTML = d.render()
