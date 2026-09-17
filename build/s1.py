# -*- coding: utf-8 -*-
"""Sesión 1 — Elegir la herramienta, investigar, crear y dejar capacidad instalada."""
from deck import (Deck, cover, statement, agenda, howto, divider,
                  exercise_case, closing, filelist, cards)


def prompt(*paragraphs):
    return '\n'.join(f'          <p>{paragraph}</p>' for paragraph in paragraphs)


RAIL1 = 'BLOQUE 01 <span class="sep"></span> ELEGIR EL ENTORNO'
RAIL2 = 'BLOQUE 02 <span class="sep"></span> INVESTIGAR Y CONVERTIR'
RAIL3 = 'BLOQUE 03 <span class="sep"></span> CREAR UNA GEM ÚTIL'
RAIL4 = 'BLOQUE 04 <span class="sep"></span> LLEVARLA A OPERACIÓN'

d = Deck('Sesión 1 · De una necesidad a capacidad instalada · Casa de las Baterías', {'sesion': 1})

d.add('Portada', 'cover', cover(
    'CASA DE LAS BATERÍAS · ADMINISTRACIÓN Y GERENCIA COMERCIAL',
    'DE LA NECESIDAD<br/>A LA <span class="acc">CAPACIDAD</span>.',
    'Sesión 1 de 2 · 16 laboratorios con NotebookLM, Deep Research, Canvas, Gems, Docs, Vids y Drive.',
    'Sesión 1 · Edición 2026'))

d.add('El trabajo primero', None, statement(
    'PUNTO DE PARTIDA',
    'La herramienta cambia cuando<br/>cambia el <span style="color:var(--brand-br);">trabajo que necesitas resolver</span>.',
    '<p style="font-size:28px;line-height:1.48;color:var(--bone-2);max-width:1480px;margin-top:34px;">'
    'Hoy CasaBat debe ordenar una bandeja, comprender un expediente, investigar una oportunidad, convertirla en un prototipo y dejar una capacidad reutilizable. '
    'No son cinco prompts parecidos: son <b style="color:var(--bone);">cinco formas distintas de trabajar con IA</b>.</p>', 82))

d.add('Cuatro modos', 'paper', cards(
    'ANTES DE ELEGIR PRODUCTO',
    'Cuatro trabajos distintos pueden verse como el mismo chat.',
    'Identificar el modo evita pedir una redacción cuando en realidad necesitas fuentes, investigación, cálculo o una aprobación.',
    [('GENERAR', 'Crear o transformar un artefacto.', 'Ejemplo: prototipo en Canvas. Riesgo: forma sin evidencia.'),
     ('RECUPERAR', 'Responder desde fuentes seleccionadas.', 'Ejemplo: expediente en NotebookLM. Riesgo: fuente incompleta.'),
     ('CALCULAR', 'Obtener una cifra reproducible.', 'Ejemplo: prueba de una regla. Riesgo: datos defectuosos.'),
     ('ACTUAR', 'Cambiar algo fuera de la IA.', 'Ejemplo: compartir o habilitar. Requiere aprobación.')], cols=4))

d.add('Agenda', 'paper', agenda(
    '4 BLOQUES <span class="sep"></span> 16 LABORATORIOS <span class="sep"></span> RITMO DEL FACILITADOR',
    'Una necesidad CasaBat.<br/>Cinco experiencias de IA.',
    [('01 · BLOQUE 1', 'Elegir el entorno',
      [('Priorizar', ''), ('NotebookLM', ''), ('Cadena visual', ''), ('Aplicación individual', '')]),
     ('02 · BLOQUE 2', 'Investigar y convertir',
      [('Deep Research', ''), ('Auditar fuentes', ''), ('Canvas', ''), ('Aplicación individual', '')]),
     ('03 · BLOQUE 3', 'Crear una Gem útil',
      [('Elegir caso', ''), ('Crear la Gem', ''), ('Prueba cruzada', ''), ('Aplicación individual', '')]),
     ('04 · BLOQUE 4', 'Llevarla a operación',
      [('Informe en Docs', ''), ('Microvideo en Vids', ''), ('Auditoría en Drive', ''), ('Aplicación individual', '')])]))

d.add('Cómo se trabaja', 'paper', howto(
    'REGLAS DEL TALLER',
    'No simules la función.<br/>Úsala y deja evidencia.',
    [('Confirma acceso antes de empezar',
      'Gemini, NotebookLM, Deep Research, Canvas y Gems pueden depender de licencia, región o habilitación del administrador. Trabaja en parejas si una cuenta no tiene acceso.'),
     ('Usa solo contexto aprobado',
      'Los archivos del curso son ficticios. En investigación abierta no cargues nombres, ventas ni información real de clientes.'),
     ('Distingue salida de decisión',
      'La IA puede investigar, sintetizar y prototipar. El dueño humano valida fuentes, aprueba el artefacto y decide su uso.')]))

d.add('Los materiales', 'paper', filelist(
    'ARCHIVOS DE LA SESIÓN',
    'Una base Office.<br/><span style="color:var(--brand);">Cuatro usos diferentes</span>.',
    'Cada equipo reutiliza los mismos materiales ficticios, pero cambia de entorno, dinámica y entregable.',
    [('COMPRENDER E INVESTIGAR', [
        ('05_correos_pendientes.xlsx', 'Una única dinámica de bandeja · laboratorio 1'),
        ('expediente-PR-ADM-014/', 'Seis fuentes para NotebookLM · laboratorio 2'),
        ('00_contexto_marca_casabat.docx', 'Contexto para investigación y Canvas'),
        ('07_notas_comite_operaciones.docx', 'Preguntas internas para contrastar con fuentes públicas'),
     ]),
     ('CREAR Y PROBAR', [
        ('03_politica_garantia.docx', 'Fuente de la Gem de orientación'),
        ('06_correos_de_referencia.docx', 'Patrones observables de voz CasaBat'),
        ('01_especificacion_de_tarea.docx', 'Estructura de instrucciones para la Gem'),
        ('02_pruebas_de_aceptacion.docx', 'Casos normales, límite y adversariales'),
     ])]))

d.add('Mapa de herramientas', 'paper', cards(
    'UNA NECESIDAD, CUATRO ENTORNOS',
    'La variedad útil no es cambiar de marca.<br/>Es cambiar de capacidad.',
    'En la interfaz los nombres pueden variar por cuenta. La decisión estable es fuente cerrada, web abierta, artefacto editable o comportamiento reusable.',
    [('NOTEBOOKLM', 'Conversa con un conjunto controlado de fuentes y devuelve citas.', 'Úsalo para expedientes, políticas y síntesis verificable.'),
     ('DEEP RESEARCH', 'Propone un plan y recorre múltiples fuentes públicas.', 'Úsalo cuando la respuesta debe buscarse fuera de CasaBat.'),
     ('CANVAS', 'Crea y edita documentos, presentaciones o prototipos.', 'Úsalo cuando el entregable necesita iteración visual.'),
     ('GEM', 'Conserva instrucciones y archivos para una tarea repetitiva.', 'Úsala cuando otra persona debe repetir el trabajo.')], cols=4))

d.add('Bloque 1', 'section-div', divider(
    1, 4, 40, '4 LABORATORIOS', 'Elegir el<br/>entorno.',
    'Gemini · NotebookLM · matriz de decisión.',
    'Distinguir una respuesta rápida de un trabajo basado en fuentes o de una capacidad reusable.',
    'Una prioridad, un cuaderno citado y una decisión de herramienta.'))

d.add('Laboratorio 1', 'paper', exercise_case(
    1, RAIL1, 10, 'Lunes a las ocho: decide qué merece atención.',
    'Coordinador de Administración', '<code>05_correos_pendientes.xlsx</code>', 'Gemini',
    'Llegas con <b>20 correos pendientes</b>. Antes de producir respuestas necesitas distinguir bloqueo, dinero, plazo, aprobación y simple ruido.',
    'Qué ocho casos se atienden primero y qué tipo de trabajo requiere cada uno.',
    ['Revisa asunto y primera línea de los 20 registros.',
     'Clasifica cada caso como generar, recuperar, calcular, actuar o archivar.',
     'Selecciona ocho y defiende el orden con evidencia visible.'],
    prompt('Revisa los 20 registros del Excel y prioriza solo ocho.',
           'Devuelve ID, señal de prioridad, modo de trabajo, fuente necesaria, dueño propuesto y riesgo de esperar. No redactes respuestas.',
           'No conviertas tono urgente en prioridad: exige plazo, dinero, cliente, bloqueo o aprobación.'),
    'Una tabla de triaje que pueda usarse en la reunión de las 8:30.',
    'Cada posición cita una señal del registro y separa dueño propuesto de dueño confirmado.'))

d.add('Laboratorio 2', 'paper', exercise_case(
    2, RAIL1, 10, 'Convierte seis documentos en una sala de evidencia.',
    'Analista de Procesos', '<code>expediente-PR-ADM-014/</code>', 'NotebookLM / Gemini Notebook',
    'Gerencia necesita entender el procedimiento de cotizaciones sin leer seis archivos durante la reunión. El expediente contiene referencias rotas, versiones contradictorias y un anexo huérfano.',
    'Qué puede afirmarse desde las fuentes, qué se contradice y qué debe escalarse.',
    ['Crea un cuaderno y carga los seis Word del expediente.',
     'Pregunta por vigencia, aprobadores, anexos citados y contradicciones; abre las citas.',
     'Genera un mapa mental o informe breve y marca los vacíos sin resolver.'],
    prompt('Usa únicamente las fuentes seleccionadas del expediente PR-ADM-014.',
           'Devuelve: regla vigente, documento que la sostiene, contradicción, impacto y pregunta para el dueño. Incluye una cita verificable por hallazgo.',
           'No resuelvas contradicciones por mayoría de documentos ni uses conocimiento externo.'),
    'Un cuaderno CasaBat con mapa de fuentes y briefing de cinco hallazgos citados.',
    'Cada hallazgo abre la ubicación correcta de la fuente; las contradicciones siguen visibles.'))

d.add('Laboratorio 3', 'paper', exercise_case(
    3, RAIL1, 20, 'Del expediente a una presentación defendible.',
    'Secretaría del Comité de Cotizaciones', 'NotebookLM del laboratorio 2 · expediente PR-ADM-014', 'NotebookLM Studio + Gemini Canvas',
    'El comité está por comenzar. Necesita una historia visual breve, pero cada regla y contradicción debe seguir conectada con el expediente.',
    'Qué necesita decidir el comité, qué evidencia lo sostiene y qué conflicto no puede resolverse todavía.',
    ['Genera en NotebookLM un Slide Deck ejecutivo de cinco láminas.',
     'Genera después una infografía del mismo expediente y úsala para detectar omisiones.',
     'Lleva ambos artefactos a Canvas, corrige la narrativa y ensaya un pitch de 90 segundos.'],
    prompt('<span class="kw">1 · SLIDE DECK</span> · Decisión requerida, regla vigente, contradicciones, impacto y preguntas al dueño.',
           '<span class="kw">2 · INFOGRAFÍA</span> · Resume documentos, relaciones y alertas; compara contra el deck y señala una omisión.',
           '<span class="kw">3 · CANVAS</span> · Crea una presentación editable de cinco slides, incorpora la corrección y cierra con la decisión solicitada.'),
    'Slide Deck, infografía, presentación Canvas y pitch de 90 segundos.',
    'Las cinco slides preservan citas, muestran conflictos y no inventan una versión oficial.'))

d.add('Laboratorio 4', 'paper', exercise_case(
    4, RAIL1, 10, 'Aplicación individual: elige la arquitectura de tu propio reto.',
    'Participante en su función', 'una tarea real anonimizada de su trabajo', 'Gemini + matriz de herramientas',
    'Cada área de CasaBat tiene tareas distintas. El reto es identificar si tu caso necesita generar, recuperar, calcular o actuar antes de escoger una herramienta.',
    'Qué entorno usarías, qué entrada mínima necesita y qué decisión seguirá siendo humana.',
    ['Describe una tarea real sin incluir datos sensibles.',
     'Clasifícala por modo de trabajo y selecciona una herramienta.',
     'Diseña una primera prueba pequeña y compárala con otra alternativa.'],
    prompt('<span class="kw">APLICACIÓN INDIVIDUAL</span> · Analiza esta tarea de mi puesto: [descríbela sin datos sensibles].',
           'Devuelve modo, herramienta, entrada, entregable, riesgo, aprobación humana y una prueba que pueda ejecutar hoy.',
           'Cuestiona mi elección si una herramienta más simple resuelve mejor el trabajo.'),
    'Una ficha de arquitectura aplicada a una tarea propia.',
    'La elección se justifica por el tipo de trabajo y termina en una prueba ejecutable.'))

d.add('Bloque 2', 'section-div', divider(
    2, 4, 40, '4 LABORATORIOS', 'Investigar y<br/>convertir.',
    'Deep Research · navegador · Canvas.',
    'Investigar una oportunidad pública, comprobar afirmaciones y convertir evidencia en un prototipo discutible.',
    'Un informe auditado y un artefacto Canvas listo para recibir feedback.'))

d.add('Laboratorio 5', 'paper', exercise_case(
    5, RAIL2, 15, '¿Existe una oportunidad en las flotas comerciales?',
    'Gerente Comercial', '<code>00_contexto_marca_casabat.docx</code> · web pública', 'Gemini Deep Research',
    'CasaBat evalúa un piloto de <b>salud preventiva de baterías para flotas en Panamá</b>. Antes de diseñarlo necesita señales de demanda, comprador, alternativas y barreras.',
    'Si la evidencia justifica entrevistar clientes y qué hipótesis sigue abierta.',
    ['Activa Deep Research y revisa el plan antes de iniciarlo.',
     'Exige señales recientes, fuentes primarias y separación entre Panamá y otros mercados.',
     'Define tres criterios para aceptar o rechazar la recomendación.'],
    prompt('Investiga la viabilidad de un piloto CasaBat de diagnóstico preventivo de baterías para flotas comerciales en Panamá.',
           'Cubre comprador, problema, alternativas, señales locales, barreras y fuentes primarias. Separa evidencia, inferencia y vacíos.',
           'Recomienda realizar o no diez entrevistas; no estimes mercado sin base verificable.'),
    'Plan editado, informe con fuentes y recomendación GO / NO GO para entrevistas.',
    'La conclusión está vinculada a evidencia fechada y declara al menos dos incertidumbres críticas.'))

d.add('Laboratorio 6', 'paper', exercise_case(
    6, RAIL2, 10, 'Tres afirmaciones del informe van a juicio.',
    'Revisor de Evidencia', 'informe de Deep Research del laboratorio 4', 'Navegador + Gemini',
    'El informe es convincente, pero una decisión comercial no puede descansar en citas que solo parecen relevantes. El equipo contrario intentará invalidar tres afirmaciones clave.',
    'Qué afirmaciones están confirmadas, parcialmente respaldadas o no respaldadas.',
    ['Elige una cifra, una afirmación causal y una señal de mercado.',
     'Abre cada fuente y comprueba fecha, autoridad, alcance y relación con Panamá.',
     'Clasifica y reescribe cualquier afirmación más fuerte que su evidencia.'],
    prompt('Audita tres afirmaciones del informe. Para cada una devuelve texto exacto, fuente, evidencia localizada, fecha, alcance y veredicto: CONFIRMADA, PARCIAL o NO RESPALDADA.',
           'Si la fuente no prueba la afirmación, reduce el lenguaje o elimina la conclusión. No uses el propio resumen como evidencia.'),
    'Una tarjeta de auditoría por afirmación y una recomendación corregida.',
    'Otra persona puede abrir la fuente y reproducir el veredicto sin confiar en la IA.'))

d.add('Laboratorio 7', 'paper', exercise_case(
    7, RAIL2, 15, 'De informe a prototipo que Gerencia puede discutir.',
    'Diseñador de la Propuesta', 'hallazgos validados · <code>00_contexto_marca_casabat.docx</code>', 'Gemini Canvas',
    'Gerencia necesita ver el piloto, cuestionar sus supuestos y cambiar una sección sin reconstruir el documento.',
    'Qué propuesta mínima permite autorizar o rechazar diez entrevistas.',
    ['Abre Canvas y pide un prototipo de una página, no una presentación extensa.',
     'Incluye problema, cliente, hipótesis, evidencia, exclusiones y próximo experimento.',
     'Un compañero marca una sección; edítala en Canvas y conserva la versión anterior.'],
    prompt('En Canvas crea un prototipo ejecutivo de una página para el piloto de salud preventiva de baterías de flota.',
           'Incluye usuario, situación, promesa, evidencia, incertidumbres, entrevistas, métrica y decisión. No inventes precios.',
           'Tras el feedback, modifica solo la sección seleccionada y exporta a Docs o comparte el Canvas.'),
    'Canvas editable con versión inicial, cambio localizado y decisión solicitada.',
    'El artefacto distingue hechos de hipótesis y puede revisarse sin leer el informe completo.'))

d.add('Laboratorio 8', 'paper', exercise_case(
    8, RAIL2, 10, 'Aplicación individual: investiga una decisión que hoy está abierta.',
    'Participante como dueño de la decisión', 'una pregunta real de su área · fuentes públicas', 'Deep Research + Canvas',
    'El participante elige una decisión de compras, ventas, operaciones, talento o administración que todavía carece de evidencia suficiente.',
    'Qué debe investigarse, qué fuentes aceptar y qué artefacto ayudaría a decidir.',
    ['Formula la decisión y tres preguntas que podrían cambiarla.',
     'Diseña el plan de investigación y excluye datos internos sensibles.',
     'Prototipa en Canvas el formato en que presentarías la recomendación.'],
    prompt('<span class="kw">APLICACIÓN INDIVIDUAL</span> · Diseña una investigación para esta decisión de mi área: [decisión].',
           'Propón preguntas, fuentes primarias, criterios de descarte, incertidumbres y estructura del artefacto final en Canvas.',
           'No ejecutes aún recomendaciones irreversibles ni completes vacíos con estimaciones sin fuente.'),
    'Plan de investigación y prototipo de una página para una decisión propia.',
    'La decisión, la evidencia aceptable y los vacíos están separados de la recomendación.'))

d.add('Bloque 3', 'section-div', divider(
    3, 4, 45, '4 LABORATORIOS', 'Crear una<br/>Gem útil.',
    'Gem Manager · archivos Word · prueba por pares.',
    'Seleccionar una tarea repetitiva, crear una Gem real y comprobar que otra persona puede usarla.',
    'Una Gem v0.1 con fuentes, límites y evidencia de transferencia.'))

d.add('Laboratorio 9', 'paper', exercise_case(
    9, RAIL3, 10, 'No todo lo repetitivo merece una Gem.',
    'Dueño de Proceso', '<code>01_especificacion_de_tarea.docx</code>', 'Gemini',
    'CasaBat podría reutilizar orientación de garantías, revisión de expedientes o briefs de apertura de sucursal. Solo una tarea cabe en el piloto de esta semana.',
    'Qué caso tiene frecuencia, fuente estable, resultado verificable y un error reversible.',
    ['Puntúa los tres casos por frecuencia, estabilidad, variación, riesgo y aceptación.',
     'Descarta cualquier caso que implique aprobar, enviar o modificar sistemas.',
     'Elige uno y define alcance, fuera de alcance, dueño y métrica base.'],
    prompt('Compara tres candidatas a Gem: orientar garantías, revisar integridad de expediente y preparar brief de apertura.',
           'Usa una matriz 1–5 para frecuencia, fuente estable, variación, riesgo, prueba objetiva y reversibilidad. Recomienda una sola para siete días.',
           'La Gem solo prepara orientación o borradores; no decide cobertura, aprueba expedientes ni publica.'),
    'Ficha de selección con caso elegido, límites, dueño y métrica de partida.',
    'La recomendación excluye decisiones irreversibles y tiene una prueba objetiva.'))

d.add('Laboratorio 10', 'paper', exercise_case(
    10, RAIL3, 20, 'Crea la Gem Orientador de Garantías CasaBat.',
    'Constructor de la Gem', '<code>03_politica_garantia.docx</code> · <code>06_correos_de_referencia.docx</code>', 'Gemini · Gem Manager',
    'Las sucursales necesitan orientación consistente sin memorizar política, tono y condiciones de detención.',
    'Qué instrucciones y archivos necesita la Gem para ayudar sin conceder una garantía.',
    ['Abre Gem Manager y crea una Gem personalizada con nombre y descripción.',
     'Carga la política y referencias ficticias; redacta objetivo, flujo, salida y límites.',
     'Guarda como v0.1 y ejecuta un caso normal antes de compartirla.'],
    prompt('Configura <span class="kw">Orientador de Garantías CasaBat v0.1</span>.',
           'Debe pedir producto, compra, comprobante, síntoma y país; citar política; separar orientación de decisión; marcar [VERIFICAR] y detenerse si falta un dato crítico.',
           'Nunca concede cobertura, inventa excepciones, promete reemplazo ni solicita datos personales innecesarios.'),
    'Una Gem creada en la interfaz, con dos fuentes, instrucciones versionadas y primera ejecución.',
    'Otra persona identifica propósito, entradas, salida, detención, fuente, dueño y versión sin explicación oral.'))

d.add('Laboratorio 11', 'paper', exercise_case(
    11, RAIL3, 15, 'Tu compañero intenta romper la Gem.',
    'Revisor de otra Sucursal', '<code>02_pruebas_de_aceptacion.docx</code> · Gem v0.1', 'Gemini Gems',
    'La Gem funciona para quien la creó. Ahora otra persona prueba una batería de moto con cuatro meses, otra con ocho meses y un caso sin producto, fecha ni comprobante.',
    'Si la Gem orienta, rechaza o se detiene de forma consistente sin depender del autor.',
    ['Comparte la Gem o intercambia pantalla sin explicar sus instrucciones.',
     'Ejecuta los tres casos y guarda salida, fuente, dato faltante y decisión bloqueada.',
     'Marca PASS o FAIL y entrega el hallazgo al constructor.'],
    prompt('Prueba la Gem con tres casos: dentro de plazo, fuera de plazo e incompleto.',
           'Para cada uno registra pregunta inicial, fuente citada, orientación, dato faltante, detención y PASS o FAIL.',
           'No corrijas la respuesta manualmente: el objetivo es evaluar la configuración v0.1.'),
    'Registro de tres pruebas y un fallo reproducible para la siguiente versión.',
    'El caso incompleto se detiene; el caso de ocho meses no recibe cobertura inventada.'))

d.add('Laboratorio 12', 'paper', exercise_case(
    12, RAIL3, 10, 'Aplicación individual: diseña una Gem para tu trabajo.',
    'Participante como dueño del proceso', 'una tarea repetitiva y reversible de su puesto', 'Gem Manager',
    'Cada participante identifica una tarea que repite y que otra persona debería poder ejecutar con el mismo estándar, sin delegar aprobaciones ni acciones irreversibles.',
    'Si el caso merece una Gem y cómo comprobar que funciona fuera de la memoria del autor.',
    ['Define usuario, disparador, entrada, fuente y salida esperada.',
     'Redacta instrucciones, límites y condición de detención.',
     'Crea tres pruebas: normal, incompleta y límite.'],
    prompt('<span class="kw">APLICACIÓN INDIVIDUAL</span> · Diseña una Gem para esta tarea repetitiva: [tarea].',
           'Incluye usuario, objetivo, flujo, fuentes permitidas, salida, fuera de alcance, detención y tres pruebas de aceptación.',
           'La Gem prepara trabajo para revisión; no aprueba, envía ni modifica sistemas.'),
    'Especificación o Gem inicial aplicada al puesto del participante.',
    'Otra persona puede probarla con criterios observables y sin explicación oral.'))

d.add('Bloque 4', 'section-div', divider(
    4, 4, 40, '4 LABORATORIOS', 'Convertir y<br/>comprobar.',
    'Gemini PTCF · Google Docs · Google Vids · Drive Ask Gemini.',
    'Convertir observaciones en comunicación operativa y auditar si sus afirmaciones tienen evidencia.',
    'Un informe, un microvideo y una auditoría cruzada, aplicados después a un reto propio.'))

d.add('Laboratorio 13', 'paper', exercise_case(
    13, RAIL4, 10, 'De notas de campo a un informe que se pueda ejecutar.',
    'Coordinador de Operaciones', '<code>13_notas_recorrido_sucursales.docx</code>', 'Gemini PTCF + Google Docs',
    'Un recorrido por cuatro sucursales dejó observaciones mezcladas, compromisos incompletos y comentarios verbales. Gerencia necesita una página que permita actuar sin convertir supuestos en hechos.',
    'Qué ocurrió, qué importa primero y qué dueño o fecha todavía debe confirmarse.',
    ['Estructura en Gemini el encargo con Persona, Tarea, Contexto y Formato.',
     'Lleva la salida a Google Docs y usa Ayúdame a escribir para ordenar el informe.',
     'Revisa cada acción y marca como por confirmar los datos ausentes.'],
    prompt('<span class="kw">PTCF</span> · Actúa como Coordinador de Operaciones. Convierte las notas en un informe para Gerencia.',
           'En Google Docs organiza: resumen, hallazgos por sucursal y plan con prioridad, evidencia, acción, dueño, fecha y dato faltante.',
           'No presentes comentarios verbales, causas ni responsables propuestos como hechos confirmados.'),
    'Informe de una página en Google Docs con acciones trazables.',
    'Cada prioridad cita una nota y los dueños o fechas ausentes permanecen visibles.'))

d.add('Laboratorio 14', 'paper', exercise_case(
    14, RAIL4, 15, 'El informe se convierte en una instrucción que el equipo sí verá.',
    'Responsable de Comunicación Operativa', 'Google Doc del laboratorio 13', 'Google Vids',
    'El equipo de sucursales no leerá el informe completo durante la jornada. Necesita una cápsula breve que explique una desviación concreta, la conducta esperada y cómo comprobarla.',
    'Qué mensaje merece convertirse en video y qué detalle debe permanecer en el informe.',
    ['Abre Google Vids y referencia el documento del laboratorio anterior.',
     'Genera un storyboard corto con situación, conducta y comprobación.',
     'Revisa voz, imágenes y afirmaciones contra el documento antes de compartir.'],
    prompt('Crea en Google Vids un microvideo para el equipo de sucursales basado en @[informe del laboratorio 13].',
           'Explica una desviación prioritaria, la conducta esperada, el responsable de verificar y la evidencia de cumplimiento.',
           'Duración objetivo: una cápsula breve. No agregues políticas, cifras ni responsables ausentes del informe.'),
    'Storyboard y microvideo operativo listo para revisión.',
    'El video conserva el sentido del informe, tiene una acción observable y no inventa información.'))

d.add('Laboratorio 15', 'paper', exercise_case(
    15, RAIL4, 15, 'Audita en Drive si la historia está respaldada.',
    'Auditor de Operaciones', '<code>AS-001_reporte_via_espana.docx</code> · <code>AS-002_reporte_tocumen.docx</code> · <code>AS-003_reporte_la_chorrera.docx</code> · <code>AS-004_reporte_san_miguelito.docx</code>', 'Google Drive · Ask Gemini',
    'Antes de circular el informe y el video, el equipo debe revisar la carpeta completa. Hay checklist desactualizado, calibración vencida, evidencia ausente, una contradicción y compromisos incompletos.',
    'Qué afirmaciones están respaldadas, cuáles deben corregirse y qué sucursal requiere seguimiento.',
    ['Sube los cuatro reportes a una carpeta y ábrela en Drive.',
     'Usa Ask Gemini para comparar checklist, calibración, compromiso, evidencia y firma.',
     'Contrasta el resultado con el informe y el video; corrige cualquier afirmación más fuerte que la evidencia.'],
    prompt('Con Ask Gemini audita los cuatro reportes de la carpeta.',
           'Devuelve por sucursal: checklist, calibración, contradicción, evidencia faltante, compromiso, dueño, fecha, firma y estado.',
           'Cita el archivo. No resuelvas contradicciones por inferencia ni marques cerrado un compromiso incompleto.'),
    'Matriz de auditoría y lista de correcciones al informe o al video.',
    'Detecta todas las anomalías plantadas y cada conclusión puede abrirse en su documento fuente.'))

d.add('Laboratorio 16', 'paper', exercise_case(
    16, RAIL4, 10, 'Aplicación individual: diseña tu propia cadena de comunicación y control.',
    'Participante en su función', 'un caso real anonimizado de su área', 'Gemini + Docs o Slides + Vids + Drive',
    'El participante toma una situación reconocible de su puesto y diseña cómo convertir evidencia dispersa en un mensaje útil sin perder trazabilidad.',
    'Qué herramientas necesita la cadena, qué produce cada paso y dónde debe revisar una persona.',
    ['Define una situación y el destinatario del resultado.',
     'Diseña al menos tres pasos: organizar, comunicar y comprobar.',
     'Ejecuta un primer artefacto o deja un prototipo listo para completar.'],
    prompt('<span class="kw">APLICACIÓN INDIVIDUAL</span> · Diseña una cadena para este reto de mi trabajo: [reto anonimizado].',
           'Para cada paso indica herramienta, entrada, transformación, salida, control humano y evidencia que debe conservarse.',
           'Reduce la cadena si un paso no agrega una capacidad distinta.'),
    'Mapa de cadena y primer artefacto aplicado al trabajo del participante.',
    'Cada herramienta agrega una función distinta y la salida final conserva una ruta hacia la evidencia.'))

d.add('Cierre', None, closing(
    'CIERRE DE SESIÓN 1',
    'No aprendiste cuatro botones.<br/>Aprendiste a <span style="color:var(--brand-br);">elegir y gobernar</span>.',
    [('EVIDENCIA INTERNA', 'NotebookLM convierte un expediente en hallazgos citados, sin ocultar contradicciones.'),
     ('EVIDENCIA EXTERNA', 'Deep Research investiga; Canvas convierte; la revisión humana decide.'),
     ('CAPACIDAD REUSABLE', 'Una Gem solo entra en piloto con fuentes, límites, pruebas, dueño y versión.')]))

HTML = d.render()
