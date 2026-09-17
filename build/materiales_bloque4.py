# -*- coding: utf-8 -*-
"""Genera los anexos ficticios del bloque 4 de la sesión 1."""
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor


ROOT = Path(__file__).resolve().parents[1]
MATERIALS = ROOT / "materiales"
AUDIT = MATERIALS / "expediente-auditoria-sucursales"
BLUE = "005596"
LIGHT_BLUE = "DDEBF7"
GRAY = "D9E2F3"


def shade(cell, fill):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), fill)
    tc_pr.append(shd)


def set_cell_margins(cell, top=100, start=120, bottom=100, end=120):
    tc = cell._tc
    tc_pr = tc.get_or_add_tcPr()
    tc_mar = tc_pr.first_child_found_in("w:tcMar")
    if tc_mar is None:
        tc_mar = OxmlElement("w:tcMar")
        tc_pr.append(tc_mar)
    for tag, value in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = OxmlElement(f"w:{tag}")
        node.set(qn("w:w"), str(value))
        node.set(qn("w:type"), "dxa")
        tc_mar.append(node)


def remove_paragraph_borders(paragraph):
    p_pr = paragraph._p.get_or_add_pPr()
    old = p_pr.find(qn("w:pBdr"))
    if old is not None:
        p_pr.remove(old)
    p_bdr = OxmlElement("w:pBdr")
    for edge in ("top", "left", "bottom", "right", "between"):
        node = OxmlElement(f"w:{edge}")
        node.set(qn("w:val"), "nil")
        p_bdr.append(node)
    p_pr.append(p_bdr)


def base_document(title, subtitle):
    doc = Document()
    section = doc.sections[0]
    section.top_margin = Inches(0.7)
    section.bottom_margin = Inches(0.65)
    section.left_margin = Inches(0.8)
    section.right_margin = Inches(0.8)
    styles = doc.styles
    styles["Normal"].font.name = "Aptos"
    styles["Normal"].font.size = Pt(10.5)
    styles["Normal"].paragraph_format.space_after = Pt(6)
    for name, size in (("Title", 22), ("Heading 1", 15), ("Heading 2", 12)):
        style = styles[name]
        style.font.name = "Aptos Display"
        style.font.size = Pt(size)
        style.font.color.rgb = RGBColor(0, 0, 0)
        style.font.bold = True
    p = doc.add_paragraph(style="Title")
    p.add_run(title)
    remove_paragraph_borders(p)
    p.paragraph_format.space_after = Pt(4)
    p = doc.add_paragraph(subtitle)
    p.runs[0].font.color.rgb = RGBColor(70, 70, 70)
    p.paragraph_format.space_after = Pt(14)
    return doc


def add_table(doc, rows):
    table = doc.add_table(rows=1, cols=2)
    table.style = "Table Grid"
    table.autofit = False
    table.columns[0].width = Inches(2.0)
    table.columns[1].width = Inches(4.8)
    header = table.rows[0].cells
    header[0].text = "Campo"
    header[1].text = "Registro"
    for c in header:
        shade(c, BLUE)
        c.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        set_cell_margins(c)
        for r in c.paragraphs[0].runs:
            r.font.color.rgb = RGBColor(255, 255, 255)
            r.font.bold = True
    for i, (field, value) in enumerate(rows):
        cells = table.add_row().cells
        cells[0].text = field
        cells[1].text = value
        if i % 2:
            shade(cells[0], "F2F6FA")
            shade(cells[1], "F2F6FA")
        cells[0].paragraphs[0].runs[0].font.bold = True
        for c in cells:
            c.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            set_cell_margins(c)
    return table


def save(doc, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    core = doc.core_properties
    core.title = doc.paragraphs[0].text
    core.subject = "Material ficticio para capacitación en IA aplicada"
    core.author = "Rizo.ma"
    doc.save(path)


def build_notes():
    doc = base_document(
        "Notas de recorrido por sucursales",
        "Registro ficticio para convertir observaciones de campo en un informe de operaciones",
    )
    doc.add_paragraph(
        "Estas notas fueron tomadas durante una jornada de supervisión. Conservan abreviaturas, "
        "comentarios incompletos y datos que requieren verificación. El participante debe separar "
        "hechos, inferencias, compromisos y preguntas pendientes."
    )
    doc.add_heading("Notas sin depurar", level=1)
    notes = [
        "Vía España, 8:20. Dos instalaciones demoraron cerca de 35 minutos. El técnico dijo que el comprobador T-07 estaba lento. La etiqueta indica calibración hasta 31 de agosto. Quedaron en cambiarlo antes del jueves 18, pero no anoté quién lo asumió.",
        "Tocumen, 10:45. El checklist técnico parece actualizado y el comprobador T-12 tiene vigencia hasta diciembre. El material del mostrador todavía habla de una campaña 2025. Carla comentó que pediría reemplazo para el 20 de septiembre.",
        "La Chorrera, 13:10. El resumen del encargado dice que no hubo incidentes. En la hoja del técnico aparece una conexión con polaridad invertida, corregida antes de entregar el vehículo. Recomendaron repaso técnico, sin fecha.",
        "San Miguelito, 16:00. Tres clientes reclamaron por tiempos de espera. Había cuatro instalaciones acumuladas y solo una bahía operativa. El equipo propuso ajustar turnos, pero el reporte quedó sin firma y sin fecha de revisión.",
        "Gerencia quiere un informe de una página para mañana: qué pasó, impacto, prioridad, acción, dueño confirmado y dato que todavía falta. No presentar como confirmado lo que solo fue comentario verbal.",
    ]
    for item in notes:
        doc.add_paragraph(item, style="List Bullet")
    doc.add_heading("Criterios para el informe", level=1)
    add_table(doc, [
        ("Destinatario", "Gerencia de Operaciones y responsables de sucursal"),
        ("Horizonte", "Acciones de las próximas dos semanas"),
        ("Prioridad", "Alta, media o baja, acompañada por una evidencia de estas notas"),
        ("Control", "Marcar por confirmar cualquier dueño, fecha o causa que no esté expresamente registrada"),
        ("Salida", "Resumen ejecutivo, hallazgos por sucursal y plan de acción"),
    ])
    save(doc, MATERIALS / "13_notas_recorrido_sucursales.docx")


REPORTS = [
    (
        "AS-001_reporte_via_espana.docx",
        "Reporte de visita Vía España",
        [
            ("Código", "AS-001"), ("Fecha de visita", "12 de septiembre de 2026"),
            ("Responsable de sucursal", "María Gutiérrez"), ("Versión del checklist", "CT-03"),
            ("Equipo verificado", "Comprobador T-07"), ("Calibración", "Vencida el 31 de agosto de 2026"),
            ("Hallazgo", "Dos instalaciones tardaron 34 y 37 minutos. El comprobador respondió con demora."),
            ("Compromiso", "Sustituir el comprobador antes del 18 de septiembre de 2026."),
            ("Dueño del compromiso", "No registrado"), ("Evidencia citada", "EV-VE-019, no incluida en la carpeta"),
            ("Firma", "María Gutiérrez"),
        ],
    ),
    (
        "AS-002_reporte_tocumen.docx",
        "Reporte de visita Tocumen",
        [
            ("Código", "AS-002"), ("Fecha de visita", "13 de septiembre de 2026"),
            ("Responsable de sucursal", "Carlos Méndez"), ("Versión del checklist", "CT-04 vigente"),
            ("Equipo verificado", "Comprobador T-12"), ("Calibración", "Vigente hasta el 15 de diciembre de 2026"),
            ("Hallazgo", "El material de mostrador todavía corresponde a la campaña de 2025."),
            ("Compromiso", "Solicitar y colocar material actualizado antes del 20 de septiembre de 2026."),
            ("Dueño del compromiso", "Carla Rodríguez"), ("Evidencia citada", "Fotografía POP-TC-2025 incorporada en el reporte"),
            ("Firma", "Carlos Méndez"),
        ],
    ),
    (
        "AS-003_reporte_la_chorrera.docx",
        "Reporte de visita La Chorrera",
        [
            ("Código", "AS-003"), ("Fecha de visita", "14 de septiembre de 2026"),
            ("Responsable de sucursal", "Elena Castillo"), ("Versión del checklist", "CT-04 vigente"),
            ("Equipo verificado", "Comprobador T-15"), ("Calibración", "Vigente hasta el 10 de enero de 2027"),
            ("Resumen del encargado", "La jornada cerró sin incidentes técnicos."),
            ("Registro técnico", "Se detectó polaridad invertida durante una instalación. Se corrigió antes de entregar el vehículo."),
            ("Compromiso", "Realizar un repaso del procedimiento de conexión."),
            ("Dueño del compromiso", "Jefatura técnica regional"), ("Fecha compromiso", "No registrada"),
            ("Firma", "Elena Castillo"),
        ],
    ),
    (
        "AS-004_reporte_san_miguelito.docx",
        "Reporte de visita San Miguelito",
        [
            ("Código", "AS-004"), ("Fecha de visita", "15 de septiembre de 2026"),
            ("Responsable de sucursal", "Roberto Díaz"), ("Versión del checklist", "CT-03"),
            ("Equipo verificado", "Comprobador T-21"), ("Calibración", "Vigente hasta el 22 de noviembre de 2026"),
            ("Hallazgo", "Tres reclamos por espera. Cuatro instalaciones acumuladas y una sola bahía operativa."),
            ("Compromiso", "Probar un ajuste de turnos y revisar el tiempo promedio de instalación."),
            ("Dueño del compromiso", "Roberto Díaz"), ("Fecha compromiso", "No registrada"),
            ("Firma", "Pendiente"),
        ],
    ),
]


def build_reports():
    for filename, title, rows in REPORTS:
        doc = base_document(title, "Expediente ficticio de auditoría operativa de sucursales")
        doc.add_paragraph(
            "Este reporte registra observaciones de una visita operativa. Debe analizarse junto con "
            "los demás archivos de la carpeta; una afirmación aislada no resuelve contradicciones ni datos faltantes."
        )
        add_table(doc, rows)
        doc.add_heading("Reglas de revisión", level=1)
        for rule in [
            "El checklist vigente es CT-04.",
            "Todo equipo de diagnóstico debe tener calibración vigente.",
            "Cada compromiso requiere dueño y fecha.",
            "Cada reporte requiere firma y la evidencia citada debe estar disponible.",
            "Una contradicción debe escalarse; no se corrige por inferencia.",
        ]:
            doc.add_paragraph(rule, style="List Bullet")
        save(doc, AUDIT / filename)


if __name__ == "__main__":
    build_notes()
    build_reports()
    print("Generados 5 documentos del bloque 4")
