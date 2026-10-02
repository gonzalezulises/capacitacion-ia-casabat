# -*- coding: utf-8 -*-
"""Genera 20_comparativa_herramientas.docx.

El detalle que no cabe en pantalla: ficha por herramienta, familia de modelos,
capacidades, fortalezas, límites y el enlace a la documentación de cada
fabricante. Consultado el 2 de octubre de 2026.

Lo que no se pudo verificar en fuente oficial está dicho como tal, en vez de
rellenarse con lo que publican los blogs de comparativas, que ese día daban
números que la propia documentación desmiente.
"""
from pathlib import Path

from docx.shared import Pt, RGBColor

from materiales_bloque4 import base_document, save

ROOT = Path(__file__).resolve().parents[1]
MATERIALS = ROOT / "materiales"

FUENTES = [
    ("Anthropic · Claude", "Models overview",
     "https://platform.claude.com/docs/en/about-claude/models/overview"),
    ("OpenAI", "Models",
     "https://developers.openai.com/api/docs/models"),
    ("Google · Gemini API", "Models",
     "https://ai.google.dev/gemini-api/docs/models"),
]

HERRAMIENTAS = [
    {
        "nombre": "Gemini · Google",
        "familia": [
            ("Gemini 3.1 Pro", "La línea de más capacidad: inteligencia avanzada, resolución "
                               "de problemas complejos y trabajo agéntico. Está en vista "
                               "previa, no en estable."),
            ("Gemini 3.8 Flash", "El estable de uso general, y el más capaz de la línea Flash. "
                                 "Admite texto, imágenes, vídeo y audio. Hace llamadas a "
                                 "funciones, devuelve salidas estructuradas y ejecuta código."),
            ("Gemini 2.5 Pro", "El Pro estable de la generación anterior, para tareas complejas "
                               "con razonamiento profundo."),
            ("Gemini 3.8 Live", "Conversación por voz con latencia baja, para hablar sin "
                                "esperas. Admite audio y vídeo en directo."),
            ("Gemini 3.8 Flash TTS", "Voz sintética de calidad de estudio en 130 idiomas."),
            ("Gemini 3.5 Transcribe", "Transcripción con separación de hablantes y marca de "
                                      "tiempo por palabra."),
            ("Nano Banana 2 y Pro", "Generación y edición de imágenes; la versión Pro llega a "
                                    "4K con texto bien representado."),
            ("Gemini Omni Flash y Lyria 3.5", "Vídeo con audio propio, y música."),
        ],
        "fuerte": [
            "Es la única de las tres que entiende audio y vídeo como entrada, no solo texto e "
            "imagen.",
            "Vive dentro de Workspace: la hoja de cálculo, el documento, el correo y Drive. Lo "
            "que produce se queda donde ya trabajas.",
            "Desde abril de 2026 el panel lateral de Hojas de cálculo construye y edita hojas "
            "enteras desde una instrucción en lenguaje natural.",
            "NotebookLM responde citando solo las fuentes que le cargaste, y genera resúmenes "
            "hablados en español, con variantes de México y Latinoamérica.",
            "Gemini Live comparte la cámara del teléfono en tiempo real, sin costo, en Android "
            "y iPhone.",
        ],
        "flojo": [
            "Las funciones que más valen dependen de la licencia: Sheets Canvas pide Workspace "
            "Business o Enterprise, Standard o Plus.",
            "La documentación pública no publica la ventana de contexto ni la fecha de corte "
            "por modelo, así que no se puede comparar ese dato de frente.",
            "En una cuenta sin los permisos adecuados, el botón sencillamente no aparece, y "
            "cuesta saber por qué.",
        ],
        "aqui": "El expediente de cotizaciones con citas, el resumen hablado para quien anda en "
                "ruta, y la cámara sobre una batería en sucursal.",
    },
    {
        "nombre": "ChatGPT · OpenAI",
        "familia": [
            ("GPT-6 Astra", "El más capaz para el trabajo exigente. Admite 1,05 millones de "
                            "unidades de texto de una vez y devuelve hasta 128.000. Conoce el "
                            "mundo hasta el 30 de abril de 2026."),
            ("GPT-6.1 Sol", "Tareas complejas a menor costo que Astra, con el mismo tamaño de "
                            "contexto."),
            ("GPT-6 Luna", "Para volumen alto, cuando importa la eficiencia. Corte de "
                           "conocimiento del 18 de mayo de 2026."),
            ("GPT-Live 1 y GPT-Realtime", "Voz a voz en tiempo real, incluida traducción."),
            ("GPT-Image 2.5", "Generación de imágenes."),
            ("GPT-Transcribe", "Transcripción de audio."),
        ],
        "fuerte": [
            "El más sólido cuando se le pone un archivo de datos encima: perfila las columnas, "
            "detecta lo que está roto y devuelve la hoja ya armada.",
            "El complemento para Excel y Google Sheets pasó a disponibilidad general el 5 de "
            "mayo de 2026: trabaja dentro de la hoja, escribe fórmulas y rastrea errores.",
            "El esfuerzo de razonamiento se ajusta en cinco niveles, de mínimo a máximo, según "
            "si urge la respuesta o la precisión.",
            "Las tareas programadas corren una vez, en horario, por un evento o en vigilancia "
            "continua, y avisan del resultado.",
            "Tiene modelos especializados por sector, como ciberseguridad y ciencias de la "
            "vida.",
        ],
        "flojo": [
            "Lo que produce nace fuera de tus herramientas: hay que descargarlo y guardarlo "
            "donde corresponda.",
            "Si devuelve el tablero como imagen, no se puede filtrar ni explorar; hay que "
            "pedirlo explícitamente como archivo.",
            "No admite audio ni vídeo como entrada en los modelos de texto: para eso usa la "
            "familia de voz, que es otra cosa.",
        ],
        "aqui": "Limpiar las ventas del semestre, unificar las categorías y devolver el Excel "
                "con el filtro por país ya puesto.",
    },
    {
        "nombre": "Claude · Anthropic",
        "familia": [
            ("Claude Opus 5.5", "El recomendado para la mayoría del trabajo. Un millón de "
                                "unidades de contexto, unas 555.000 palabras, y hasta 128.000 "
                                "de salida. Conoce el mundo hasta junio de 2026."),
            ("Claude Fable 5.1", "Para razonamiento exigente y trabajos largos encadenados."),
            ("Claude Sonnet 5.5", "La mejor combinación de velocidad e inteligencia."),
            ("Claude Haiku 4.5", "El más rápido, con 200.000 de contexto."),
        ],
        "fuerte": [
            "Un millón de unidades de contexto con razonamiento adaptativo siempre activo: "
            "decide solo cuánto pensar según lo difícil que sea lo que le pides.",
            "Fuerte en documentos largos y en trabajo encadenado, que es el caso de un "
            "expediente con anexos o una política con excepciones.",
            "Devuelve páginas que se usan con el ratón, no capturas de pantalla: se filtra, se "
            "pasa el cursor y se comparte por enlace.",
            "Desde abril de 2026, esos tableros pueden quedar guardados y recargar los datos "
            "cada vez que se abren.",
            "Su documentación de buenas prácticas es la más explícita sobre cuántos ejemplos "
            "poner y dónde colocar los documentos largos.",
        ],
        "flojo": [
            "No vive dentro de la hoja de cálculo ni del correo como las otras dos: se trabaja "
            "en su propia ventana.",
            "El tablero se calcula con los datos que subiste; si el archivo cambia, hay que "
            "volver a subirlo.",
            "No admite audio ni vídeo como entrada: solo texto e imagen.",
        ],
        "aqui": "Cruzar la política de garantía con el reclamo de un cliente, auditar los 41 "
                "procedimientos y dejar un tablero que se comparte con un enlace.",
    },
]

NO_VERIFICADO = [
    "La ventana de contexto y la fecha de corte de los modelos Gemini no aparecen por modelo en "
    "la documentación pública consultada.",
    "Google reparte la familia en muchas líneas —Pro, Flash, Flash-Lite— y la de más capacidad "
    "estaba en vista previa el día de la consulta. Comparar «el modelo principal» de las tres "
    "casas no es una comparación entre iguales.",
    "Los precios de las aplicaciones de chat para empresa cambian por región y por plan: "
    "confírmalos en la página oficial de cada proveedor antes de contratar.",
    "Varios artículos de comparativa publicados en 2026 dan números que la documentación de los "
    "propios fabricantes desmiente. Cuando algo no cuadre, manda la fuente oficial.",
]


def build():
    doc = base_document(
        "Las tres herramientas, comparadas",
        "Material de consulta de la sesión 1. Ficha por herramienta con su familia de modelos, "
        "fortalezas, límites y el uso que tendría en Casa de las Baterías. Consultado en la "
        "documentación oficial de cada fabricante el 2 de octubre de 2026.")

    doc.add_heading("Cómo leer esto", level=1)
    doc.add_paragraph(
        "Las tres resuelven con solvencia el trabajo de oficina. La diferencia ya no está en "
        "cuál escribe mejor, sino en qué puede leer cada una, dónde vive el resultado y qué te "
        "deja en la mano al terminar. Las cifras de modelos son del interfaz de programación; "
        "en la aplicación de chat los límites los pone el plan contratado.")

    for h in HERRAMIENTAS:
        doc.add_heading(h["nombre"], level=1)

        doc.add_heading("Familia de modelos", level=2)
        for nombre, descripcion in h["familia"]:
            p = doc.add_paragraph(style="List Bullet")
            p.add_run(f"{nombre}. ").bold = True
            p.add_run(descripcion)

        doc.add_heading("Dónde es más fuerte", level=2)
        for punto in h["fuerte"]:
            doc.add_paragraph(punto, style="List Bullet")

        doc.add_heading("Dónde se queda corta", level=2)
        for punto in h["flojo"]:
            doc.add_paragraph(punto, style="List Bullet")

        p = doc.add_paragraph()
        p.add_run("Para qué la usaría en CasaBat: ").bold = True
        p.add_run(h["aqui"])

    doc.add_heading("Lo que no se pudo verificar", level=1)
    doc.add_paragraph(
        "Un comparativo honesto dice también lo que no sabe. Estos puntos quedaron sin "
        "confirmar en fuente oficial:")
    for punto in NO_VERIFICADO:
        doc.add_paragraph(punto, style="List Bullet")

    doc.add_heading("Fuentes", level=1)
    for casa, titulo, url in FUENTES:
        p = doc.add_paragraph(style="List Bullet")
        p.add_run(f"{casa} · ").bold = True
        p.add_run(f"{titulo}. ")
        enlace = p.add_run(url)
        enlace.font.size = Pt(9)
        enlace.font.color.rgb = RGBColor(0x1C, 0x5C, 0x92)

    save(doc, MATERIALS / "20_comparativa_herramientas.docx")


if __name__ == "__main__":
    build()
    print(f"20_comparativa_herramientas.docx: {len(HERRAMIENTAS)} herramientas, "
          f"{sum(len(h['familia']) for h in HERRAMIENTAS)} modelos fichados")
