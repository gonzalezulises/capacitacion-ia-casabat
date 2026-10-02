# -*- coding: utf-8 -*-
"""Genera los dos materiales ficticios de la sesión 3.

  15_prompts_que_fallaron.docx    ocho pedidos flojos, qué devolvieron y cómo se arreglan
  16_maestro_procedimientos.xlsx  cuarenta procedimientos con fallos de nombre y de anexos

Los fallos del Excel están puestos a propósito y responden a la regla de
09_reglas_de_nomenclatura.docx. verifica-maestro.mjs los vuelve a contar desde el
archivo, así que si una fila cambia, la cifra del deck deja de cuadrar y avisa.
"""
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

from materiales_bloque4 import base_document, save

ROOT = Path(__file__).resolve().parents[1]
MATERIALS = ROOT / "materiales"

BLUE = "1C5C92"
LIGHT = "E8F1F9"


# --------------------------------------------------------------------------
# 15_prompts_que_fallaron.docx
# --------------------------------------------------------------------------

PROMPTS = [
    {
        "titulo": "«Hazme un correo para el cliente»",
        "area": "Gerencia Comercial",
        "flojo": "Hazme un correo para el cliente sobre la cotización.",
        "salio": "Un correo de seis párrafos que abre con «Esperamos que se encuentre muy "
                 "bien» y promete «la mejor calidad del mercado». No dice número de "
                 "cotización, ni monto, ni qué se le pide al cliente.",
        "falta": "Quién escribe, a quién, qué pasó, qué necesitas que haga el cliente y "
                 "para cuándo. Sin eso la IA rellena con frases de catálogo.",
        "reparado": "Escribe un correo de la jefatura comercial al contacto de una flota. "
                    "La cotización 9011 por 4.320 dólares venció el viernes. Necesito que "
                    "confirme si todavía la quiere con el precio nuevo. Tres párrafos "
                    "cortos, tono cercano y directo, cierra pidiendo respuesta esta semana. "
                    "No prometas descuentos ni plazos de garantía.",
    },
    {
        "titulo": "«Analiza este Excel»",
        "area": "Administración",
        "flojo": "Analiza este Excel y dime qué ves.",
        "salio": "Una lista de diez observaciones sueltas, varias obvias («hay cuatro "
                 "países»), sin una sola cifra y sin decir qué hacer con nada de eso.",
        "falta": "La pregunta. «Analiza» no es una pregunta: no dice qué decisión está "
                 "esperando esa respuesta.",
        "reparado": "En este archivo de ventas del semestre, dime qué tres líneas de "
                    "producto concentran más ingreso y qué porcentaje del total suman. "
                    "Dame la cifra, el porcentaje y las filas de donde sale. Antes de "
                    "calcular, avísame si hay categorías escritas de varias formas.",
    },
    {
        "titulo": "«Mejora este texto»",
        "area": "Administración",
        "flojo": "Mejora este texto.",
        "salio": "El texto completo reescrito de arriba abajo, con otro orden y otro tono. "
                 "Se perdieron dos datos que sí estaban bien y hubo que comparar línea "
                 "por línea para recuperarlos.",
        "falta": "Decir qué está mal y qué no se toca. «Mejora» le da permiso para "
                 "cambiarlo todo.",
        "reparado": "Este correo ya dice lo que quiero. Cámbiame solo dos cosas: el primer "
                    "párrafo es muy largo, pártelo en dos; y la frase del cierre suena "
                    "dura, suavízala. No toques el resto, ni el orden, ni los montos. "
                    "Devuélveme el correo completo y márcame en negrita lo que cambiaste.",
    },
    {
        "titulo": "«Hazme un dashboard»",
        "area": "Gerencia Comercial",
        "flojo": "Hazme un dashboard con estos datos.",
        "salio": "Catorce gráficos, cuatro de ellos del mismo dato, dos tortas con nueve "
                 "pedazos y ningún total. Bonito en la pantalla, inservible en la reunión.",
        "falta": "Las cifras que de verdad miras y la pregunta que el tablero contesta. "
                 "Sin eso, la IA dibuja todo lo que puede dibujar.",
        "reparado": "Hazme un tablero de una pantalla para la reunión de ventas del lunes. "
                    "Arriba cuatro cifras: ingreso del semestre, unidades, devoluciones y "
                    "la sucursal que más cayó. Debajo un gráfico de barras de ingreso por "
                    "línea de producto, ordenado de mayor a menor. Nada más. Que se pueda "
                    "filtrar por país.",
    },
    {
        "titulo": "«Revisa si los nombres están bien»",
        "area": "Administración",
        "flojo": "Revisa si los nombres de estos procedimientos están bien.",
        "salio": "«La mayoría parece correcta.» Marcó tres archivos al azar y se le pasaron "
                 "los códigos repetidos, que eran justo el problema.",
        "falta": "La regla. Sin pegarle la norma, la IA inventa su propio criterio de qué "
                 "es un nombre bien puesto.",
        "reparado": "Te pego la regla de nombres y la lista de cuarenta procedimientos. "
                    "Revisa uno por uno y dame una tabla: archivo, qué regla rompe, qué "
                    "parte del nombre está mal y cómo debería llamarse. Si un archivo "
                    "cumple, ponlo como correcto. No te saltes ninguno y no agrupes.",
    },
    {
        "titulo": "«Resume la reunión»",
        "area": "Administración",
        "flojo": "Resume la reunión.",
        "salio": "Un párrafo que cuenta de qué se habló. No quedó claro qué se decidió, "
                 "quién quedó encargado de qué, ni para cuándo.",
        "falta": "Qué quieres sacar del resumen. Un resumen de lo hablado y una lista de "
                 "compromisos no son el mismo documento.",
        "reparado": "De estas notas del comité, sácame dos listas. Primera: lo que se "
                    "decidió, una línea por decisión. Segunda: los compromisos, con "
                    "responsable y fecha. Si una fecha o un responsable no aparece en las "
                    "notas, escribe «falta» en vez de suponerlo.",
    },
    {
        "titulo": "«Explícame esto para la gerencia»",
        "area": "Gerencia Comercial",
        "flypaso": "",
        "flojo": "Explícame esto para presentarlo a la gerencia.",
        "salio": "Once diapositivas con mucho texto y tres recomendaciones que el archivo "
                 "no sostenía. Hubo que quitar dos por no tener de dónde salían.",
        "falta": "Cuánto espacio tienes, qué sabe ya quien escucha y qué le vas a pedir al "
                 "final.",
        "reparado": "Prepárame tres diapositivas para la gerencia comercial. Saben del "
                    "tema, no necesitan introducción. Diapositiva uno: qué encontré, con "
                    "la cifra. Dos: por qué pasa, separando lo que sé de lo que supongo. "
                    "Tres: qué pido. Si una afirmación no sale del archivo, no la pongas.",
    },
    {
        "titulo": "«Que no suene a inteligencia artificial»",
        "area": "Administración",
        "flojo": "Escríbelo pero que no suene a IA.",
        "salio": "El mismo texto con dos emojis y un «¡Hola!» al inicio. Seguía sonando "
                 "igual: las mismas frases de relleno y el mismo ritmo parejo.",
        "falta": "Un ejemplo de cómo escribes tú. «Que no suene a IA» no es una "
                 "instrucción: es una queja.",
        "reparado": "Te pego tres correos míos. Fíjate en cómo arranco, qué largo tienen "
                    "mis frases y cómo cierro. Ahora escribe este aviso con ese mismo "
                    "estilo. Nada de «esperamos que se encuentre bien» ni «no dude en "
                    "contactarnos». Frases cortas. Si no sabes un dato, déjalo en blanco.",
    },
]


def build_prompts():
    doc = base_document(
        "Ocho pedidos que salieron mal y cómo se arreglan",
        "Material de práctica del taller. Los ocho casos son ficticios, armados con los "
        "pedidos que más se repiten en Administración y Gerencia Comercial. Se usan en la "
        "sesión 3, laboratorio 1. Si trajiste un pedido tuyo que salió mal, usa el tuyo: "
        "funciona mejor.")

    doc.add_paragraph(
        "Cómo leer cada caso: primero el pedido tal como se escribió, luego lo que "
        "devolvió la IA, después lo que le faltaba y al final el mismo pedido arreglado. "
        "La diferencia entre el flojo y el arreglado casi nunca es la cortesía ni la "
        "longitud: es decir quién, qué, con qué datos y qué no se toca.")

    for i, caso in enumerate(PROMPTS, start=1):
        doc.add_heading(f"{i}. {caso['titulo']}", level=1)
        p = doc.add_paragraph()
        p.add_run(f"Área: {caso['area']}").italic = True

        for rotulo, cuerpo in (("Lo que se pidió", caso["flojo"]),
                               ("Lo que devolvió", caso["salio"]),
                               ("Qué le faltaba", caso["falta"]),
                               ("El mismo pedido, arreglado", caso["reparado"])):
            p = doc.add_paragraph()
            p.add_run(f"{rotulo}: ").bold = True
            p.add_run(cuerpo)

    doc.add_heading("Las seis partes que hacen la diferencia", level=1)
    doc.add_paragraph(
        "Ninguno de los ocho pedidos arreglados tiene las seis, y no hace falta. Pero "
        "cuando un resultado sale flojo, casi siempre falta una de estas:")
    for parte, explicacion in (
        ("Quién habla y a quién", "«la jefatura comercial al contacto de una flota»"),
        ("El dato concreto", "«la cotización 9011 por 4.320 dólares»"),
        ("Qué tiene que pasar", "«que confirme si la quiere al precio nuevo»"),
        ("La forma", "«tres párrafos cortos», «una tabla», «tres diapositivas»"),
        ("Lo que no se toca", "«no cambies los montos ni el orden»"),
        ("Qué hacer si falta un dato", "«escribe falta en vez de suponerlo»"),
    ):
        p = doc.add_paragraph(style="List Bullet")
        p.add_run(f"{parte}. ").bold = True
        p.add_run(explicacion)

    save(doc, MATERIALS / "15_prompts_que_fallaron.docx")


# --------------------------------------------------------------------------
# 16_maestro_procedimientos.xlsx
# --------------------------------------------------------------------------
# Cada fila es (archivo, codigo_interno, titulo, area, estado, vigencia, dueno,
#               anexos_citados, ultima_revision)
# Los fallos están puestos a propósito. La columna de comentario no existe: el
# participante tiene que encontrarlos con la regla en la mano.

PROCEDIMIENTOS = [
    # --- correctos ---
    ("PR-ADM-014_Gestion_de_Cotizaciones_v2.docx", "PR-ADM-014", "Gestión de Cotizaciones",
     "Administración", "Vigente", "2026-03-02", "Jefatura de Administración",
     "ANEXO-A; ANEXO-B; ANEXO-C; ANEXO-D; ANEXO-F", "2026-03-02"),
    ("PR-COM-007_Atencion_de_Reclamos_v4.docx", "PR-COM-007", "Atención de Reclamos",
     "Comercial", "Vigente", "2026-01-20", "Gerencia Comercial", "ANEXO-A; ANEXO-B", "2026-01-20"),
    ("PR-OPE-102_Despacho_a_Domicilio_v3.docx", "PR-OPE-102", "Despacho a Domicilio",
     "Operaciones", "Vigente", "2025-11-11", "Jefatura de Operaciones", "ANEXO-A", "2025-11-11"),
    ("PR-FIN-045_Cierre_de_Caja_Diario_v5.docx", "PR-FIN-045", "Cierre de Caja Diario",
     "Finanzas", "Vigente", "2026-02-14", "Contraloría", "ANEXO-A; ANEXO-B", "2026-02-14"),
    ("PR-ADM-009_Compra_de_Insumos_v1.docx", "PR-ADM-009", "Compra de Insumos",
     "Administración", "Vigente", "2025-09-30", "Jefatura de Administración", "", "2025-09-30"),
    ("PR-COM-012_Visita_a_Flotas_v2.docx", "PR-COM-012", "Visita a Flotas",
     "Comercial", "Vigente", "2026-04-08", "Gerencia Comercial", "ANEXO-A", "2026-04-08"),
    ("PR-OPE-118_Instalacion_en_Sucursal_v2.docx", "PR-OPE-118", "Instalación en Sucursal",
     "Operaciones", "Vigente", "2026-01-15", "Jefatura de Operaciones", "ANEXO-A; ANEXO-B", "2026-01-15"),
    ("PR-FIN-051_Pago_a_Proveedores_v3.docx", "PR-FIN-051", "Pago a Proveedores",
     "Finanzas", "Vigente", "2025-12-05", "Contraloría", "ANEXO-A", "2025-12-05"),
    ("PR-ADM-021_Control_de_Activos_v1.docx", "PR-ADM-021", "Control de Activos",
     "Administración", "Vigente", "2026-05-19", "Jefatura de Administración", "ANEXO-A", "2026-05-19"),
    ("PR-OPE-130_Reciclaje_de_Baterias_v4.docx", "PR-OPE-130", "Reciclaje de Baterías",
     "Operaciones", "Vigente", "2026-02-27", "Jefatura de Operaciones", "ANEXO-A; ANEXO-B", "2026-02-27"),
    ("PR-COM-019_Cotizacion_de_Energia_Solar_v2.docx", "PR-COM-019", "Cotización de Energía Solar",
     "Comercial", "Vigente", "2026-06-03", "Gerencia Comercial", "ANEXO-A", "2026-06-03"),
    ("PR-FIN-033_Conciliacion_Bancaria_v6.docx", "PR-FIN-033", "Conciliación Bancaria",
     "Finanzas", "Vigente", "2026-03-18", "Contraloría", "ANEXO-A; ANEXO-B", "2026-03-18"),
    ("PR-ADM-027_Archivo_de_Documentos_v1.docx", "PR-ADM-027", "Archivo de Documentos",
     "Administración", "Vigente", "2025-10-22", "Jefatura de Administración", "", "2025-10-22"),
    ("PR-OPE-141_Mantenimiento_de_Montacargas_v2.docx", "PR-OPE-141", "Mantenimiento de Montacargas",
     "Operaciones", "Vigente", "2026-04-29", "Jefatura de Operaciones", "ANEXO-A", "2026-04-29"),
    ("PR-COM-024_Seguimiento_de_Garantias_v3.docx", "PR-COM-024", "Seguimiento de Garantías",
     "Comercial", "Vigente", "2026-05-06", "Gerencia Comercial", "ANEXO-A; ANEXO-B", "2026-05-06"),
    ("PR-FIN-060_Viaticos_y_Gastos_v2.docx", "PR-FIN-060", "Viáticos y Gastos",
     "Finanzas", "Vigente", "2026-01-09", "Contraloría", "ANEXO-A", "2026-01-09"),
    ("PR-ADM-035_Induccion_de_Personal_Nuevo_v2.docx", "PR-ADM-035", "Inducción de Personal Nuevo",
     "Administración", "Vigente", "2026-02-02", "Jefatura de Administración", "ANEXO-A", "2026-02-02"),
    ("PR-OPE-155_Ruta_de_Asistencia_v1.docx", "PR-OPE-155", "Ruta de Asistencia",
     "Operaciones", "Vigente", "2026-06-11", "Jefatura de Operaciones", "ANEXO-A", "2026-06-11"),
    ("PR-COM-031_Precios_por_Pais_v2.docx", "PR-COM-031", "Precios por País",
     "Comercial", "Vigente", "2026-04-15", "Gerencia Comercial", "ANEXO-A; ANEXO-B", "2026-04-15"),
    ("PR-FIN-072_Facturacion_Electronica_v3.docx", "PR-FIN-072", "Facturación Electrónica",
     "Finanzas", "Vigente", "2026-05-27", "Contraloría", "ANEXO-A", "2026-05-27"),
    ("PR-ADM-041_Control_de_Llaves_v1.docx", "PR-ADM-041", "Control de Llaves",
     "Administración", "Vigente", "2025-08-14", "Jefatura de Administración", "", "2025-08-14"),
    ("PR-OPE-167_Prueba_de_Carga_v2.docx", "PR-OPE-167", "Prueba de Carga",
     "Operaciones", "Vigente", "2026-03-25", "Jefatura de Operaciones", "ANEXO-A", "2026-03-25"),

    # --- con fallos de nombre ---
    # área de cuatro letras
    ("PR-ADMI-048_Entrega_de_Uniformes_v1.docx", "PR-ADMI-048", "Entrega de Uniformes",
     "Administración", "Vigente", "2026-02-19", "Jefatura de Administración", "ANEXO-A", "2026-02-19"),
    # área de dos letras
    ("PR-CO-005_Registro_de_Visitas_v2.docx", "PR-CO-005", "Registro de Visitas",
     "Comercial", "Vigente", "2026-01-28", "Gerencia Comercial", "", "2026-01-28"),
    # correlativo sin ceros a la izquierda
    ("PR-COM-7_Atencion_Telefonica_v1.docx", "PR-COM-7", "Atención Telefónica",
     "Comercial", "Vigente", "2025-12-18", "Gerencia Comercial", "ANEXO-A", "2025-12-18"),
    # correlativo de dos dígitos
    ("PR-ADM-14_Gestion_de_Cotizaciones_Mayoreo_v1.docx", "PR-ADM-014", "Gestión de Cotizaciones Mayoreo",
     "Administración", "Vigente", "2026-03-02", "Jefatura de Administración", "ANEXO-A", "2026-03-02"),
    # título con espacios y tildes
    ("PR-OPE-031_Gestión de Rutas_v2.docx", "PR-OPE-031", "Gestión de Rutas",
     "Operaciones", "Vigente", "2026-04-02", "Jefatura de Operaciones", "ANEXO-A", "2026-04-02"),
    # versión en mayúscula
    ("PR-FIN-084_Arqueo_de_Caja_V1.docx", "PR-FIN-084", "Arqueo de Caja",
     "Finanzas", "Vigente", "2026-05-13", "Contraloría", "ANEXO-A", "2026-05-13"),
    # versión con decimal
    ("PR-COM-038_Descuentos_Autorizados_v1.2.docx", "PR-COM-038", "Descuentos Autorizados",
     "Comercial", "Vigente", "2026-06-17", "Gerencia Comercial", "ANEXO-A; ANEXO-B", "2026-06-17"),
    # guion bajo en el código
    ("PR_ADM_018_Solicitud_de_Vacaciones_v2.docx", "PR-ADM-018", "Solicitud de Vacaciones",
     "Administración", "Vigente", "2026-02-11", "Jefatura de Administración", "", "2026-02-11"),
    # extensión en mayúscula
    ("PR-OPE-173_Carga_de_Inventario_v1.DOCX", "PR-OPE-173", "Carga de Inventario",
     "Operaciones", "Vigente", "2026-01-07", "Jefatura de Operaciones", "ANEXO-A", "2026-01-07"),
    # sin versión
    ("PR-FIN-091_Presupuesto_Anual.docx", "PR-FIN-091", "Presupuesto Anual",
     "Finanzas", "Vigente", "2026-03-11", "Contraloría", "ANEXO-A", "2026-03-11"),
    # área que no existe en la regla
    ("PR-RRH-012_Evaluacion_de_Desempeno_v2.docx", "PR-RRH-012", "Evaluación de Desempeño",
     "Gente", "Vigente", "2026-04-22", "Jefatura de Gente", "ANEXO-A", "2026-04-22"),

    # --- con fallos de contenido, no de nombre ---
    # el código de dentro no coincide con el del archivo
    ("PR-ADM-052_Entrega_de_Caja_Chica_v1.docx", "PR-ADM-050", "Entrega de Caja Chica",
     "Administración", "Vigente", "2026-05-20", "Jefatura de Administración", "ANEXO-A", "2026-05-20"),
    # dos vigentes con el mismo código
    ("PR-COM-007_Atencion_de_Reclamos_v5.docx", "PR-COM-007", "Atención de Reclamos",
     "Comercial", "Vigente", "2026-06-24", "Gerencia Comercial", "ANEXO-A; ANEXO-B", "2026-06-24"),
    # cita un anexo con salto de letra: A, B, D sin C
    ("PR-OPE-184_Traslado_entre_Sucursales_v2.docx", "PR-OPE-184", "Traslado entre Sucursales",
     "Operaciones", "Vigente", "2026-02-25", "Jefatura de Operaciones",
     "ANEXO-A; ANEXO-B; ANEXO-D", "2026-02-25"),
    # estado vacío
    ("PR-FIN-099_Prestamos_a_Colaboradores_v1.docx", "PR-FIN-099", "Préstamos a Colaboradores",
     "Finanzas", "", "2026-01-30", "Contraloría", "ANEXO-A", "2026-01-30"),
    # sin fecha de vigencia pero marcado vigente
    ("PR-ADM-058_Uso_de_Vehiculos_v2.docx", "PR-ADM-058", "Uso de Vehículos",
     "Administración", "Vigente", "", "Jefatura de Administración", "ANEXO-A", "2026-03-04"),
    # sin dueño
    ("PR-COM-044_Campanas_de_Temporada_v1.docx", "PR-COM-044", "Campañas de Temporada",
     "Comercial", "Vigente", "2026-05-02", "", "ANEXO-A", "2026-05-02"),
    # borrador tratado como vigente en la columna de estado
    ("PR-OPE-190_Atencion_de_Emergencias_v1_BORRADOR.docx", "PR-OPE-190", "Atención de Emergencias",
     "Operaciones", "Vigente", "2026-06-30", "Jefatura de Operaciones", "ANEXO-A", "2026-06-30"),
    # revisión anterior a la vigencia
    ("PR-FIN-105_Reembolso_de_Gastos_v2.docx", "PR-FIN-105", "Reembolso de Gastos",
     "Finanzas", "Vigente", "2026-04-18", "Contraloría", "ANEXO-A", "2025-11-18"),
]

ANEXOS_EXISTENTES = {
    # código de procedimiento -> letras de anexo que existen de verdad en el archivo
    "PR-ADM-014": ["A", "B", "C", "D", "F"],
    "PR-COM-007": ["A", "B"],
    "PR-OPE-102": ["A"],
    "PR-FIN-045": ["A", "B"],
    "PR-COM-012": ["A"],
    "PR-OPE-118": ["A", "B", "C"],   # el C existe y nadie lo cita: huérfano
    "PR-FIN-051": ["A"],
    "PR-ADM-021": ["A"],
    "PR-OPE-130": ["A", "B"],
    "PR-COM-019": ["A"],
    "PR-FIN-033": ["A", "B"],
    "PR-OPE-141": ["A"],
    "PR-COM-024": ["A", "B"],
    "PR-FIN-060": ["A"],
    "PR-ADM-035": ["A"],
    "PR-OPE-155": ["A"],
    "PR-COM-031": ["A", "B"],
    "PR-FIN-072": ["A"],
    "PR-OPE-167": ["A"],
    "PR-ADMI-048": ["A"],
    "PR-COM-7": ["A"],
    "PR-ADM-014-MAYOREO": ["A"],
    "PR-OPE-031": ["A"],
    "PR-FIN-084": ["A"],
    "PR-COM-038": ["A"],          # cita A y B, pero solo existe A: referencia rota
    "PR-OPE-173": ["A"],
    "PR-FIN-091": ["A"],
    "PR-RRH-012": ["A"],
    "PR-ADM-052": ["A"],
    "PR-OPE-184": ["A", "B"],     # cita D, que no existe
    "PR-FIN-099": ["A"],
    "PR-ADM-058": ["A"],
    "PR-COM-044": ["A"],
    "PR-OPE-190": ["A"],
    "PR-FIN-105": ["A"],
}

CABECERAS = ["n", "archivo", "codigo_en_el_documento", "titulo", "area", "estado",
             "fecha_vigencia", "dueno", "anexos_citados", "ultima_revision",
             "anexos_que_existen"]


def build_maestro():
    wb = Workbook()
    ws = wb.active
    ws.title = "Procedimientos"

    # La tabla arranca en la fila 1, sin título decorativo encima: así el archivo
    # se puede subir a Gemini, ChatGPT o Claude y la primera fila ya es la cabecera.
    # El aviso de datos ficticios vive en la hoja «Léeme».
    fila_cabecera = 1
    for col, nombre in enumerate(CABECERAS, start=1):
        celda = ws.cell(row=fila_cabecera, column=col, value=nombre)
        celda.font = Font(bold=True, color="FFFFFF", size=10)
        celda.fill = PatternFill("solid", fgColor=BLUE)
        celda.alignment = Alignment(vertical="center", wrap_text=True)

    borde = Side(style="thin", color="D3DEEA")
    for i, fila in enumerate(PROCEDIMIENTOS, start=1):
        archivo, codigo, titulo, area, estado, vigencia, dueno, anexos, revision = fila
        clave = codigo
        if archivo.startswith("PR-ADM-14_"):
            clave = "PR-ADM-014-MAYOREO"
        existentes = "; ".join(f"ANEXO-{letra}" for letra in ANEXOS_EXISTENTES.get(clave, []))
        valores = [i, archivo, codigo, titulo, area, estado, vigencia, dueno, anexos,
                   revision, existentes]
        for col, valor in enumerate(valores, start=1):
            celda = ws.cell(row=fila_cabecera + i, column=col, value=valor)
            celda.font = Font(size=9.5)
            celda.alignment = Alignment(vertical="top", wrap_text=(col in (2, 9, 11)))
            celda.border = Border(bottom=borde)
            if i % 2 == 0:
                celda.fill = PatternFill("solid", fgColor="F7FAFD")

    anchos = [4, 46, 20, 32, 16, 12, 14, 26, 30, 14, 26]
    for col, ancho in enumerate(anchos, start=1):
        ws.column_dimensions[get_column_letter(col)].width = ancho
    ws.freeze_panes = ws.cell(row=fila_cabecera + 1, column=1)

    leeme = wb.create_sheet("Léeme")
    leeme["A1"] = "Casa de las Baterías · Maestro de procedimientos"
    leeme["A1"].font = Font(bold=True, size=14, color=BLUE)
    avisos = [
        "Datos ficticios. Corte del 30 de junio de 2026.",
        "Ningún procedimiento, código, dueño ni fecha de este archivo es real.",
        "Los fallos de nombre y de anexos están puestos a propósito: son lo que el "
        "ejercicio busca.",
        "La regla contra la que se revisa está en 09_reglas_de_nomenclatura.docx.",
        "Si tu área tiene su propio maestro, usa el tuyo: el ejercicio funciona igual.",
        "Se usa en la sesión 3, laboratorios 13, 14 y 15.",
    ]
    for i, aviso in enumerate(avisos, start=3):
        leeme.cell(row=i, column=1, value=aviso).alignment = Alignment(wrap_text=True)
    leeme.column_dimensions["A"].width = 96

    MATERIALS.mkdir(parents=True, exist_ok=True)
    wb.save(MATERIALS / "16_maestro_procedimientos.xlsx")


if __name__ == "__main__":
    build_prompts()
    build_maestro()
    print(f"15_prompts_que_fallaron.docx: {len(PROMPTS)} casos")
    print(f"16_maestro_procedimientos.xlsx: {len(PROCEDIMIENTOS)} filas")
