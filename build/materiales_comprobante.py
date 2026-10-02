# -*- coding: utf-8 -*-
"""Genera 19_comprobante_foto.png: la foto de un recibo, como la manda un cliente.

El laboratorio de visión no se resuelve leyendo bien: el recibo trae la fecha sin
año y un código de producto que no dice si la batería es de moto o de auto. Con
la política en la mano, el plazo depende de las dos cosas. La respuesta correcta
no es un veredicto, es pedir los dos datos que faltan.

La imagen se genera aquí para que el defecto esté puesto a propósito y no
dependa de encontrar una foto. verifica-materiales.mjs comprueba que exista.
"""
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
MATERIALS = ROOT / "materiales"

ANCHO, ALTO = 760, 1180
PAPEL = (250, 249, 245)
TINTA = (38, 38, 40)


def _fuente(tam, negrita=False):
    candidatas = [
        "/System/Library/Fonts/Supplemental/Courier New Bold.ttf" if negrita
        else "/System/Library/Fonts/Supplemental/Courier New.ttf",
        "/System/Library/Fonts/Menlo.ttc",
    ]
    for ruta in candidatas:
        if Path(ruta).exists():
            try:
                return ImageFont.truetype(ruta, tam)
            except OSError:
                continue
    return ImageFont.load_default()


LINEAS = [
    ("CASA DE LAS BATERIAS", 34, True, "centro"),
    ("Sucursal Via Espana", 24, False, "centro"),
    ("RUC 155-xxxx-xxxxx DV 00", 18, False, "centro"),
    ("", 10, False, "centro"),
    ("-" * 42, 20, False, "izq"),
    ("RECIBO DE VENTA    No. 0 0 4 7 2 1", 22, True, "izq"),
    ("-" * 42, 20, False, "izq"),
    ("", 8, False, "izq"),
    ("FECHA:  14/07        HORA: 11:42", 24, True, "izq"),
    ("CAJA:   03           VEND: 118", 22, False, "izq"),
    ("", 10, False, "izq"),
    ("CANT  DESCRIPCION           IMPORTE", 20, True, "izq"),
    ("-" * 42, 20, False, "izq"),
    ("  1   BAT-7421 12V 7AH        68.50", 22, False, "izq"),
    ("      SERIE 4471-A", 20, False, "izq"),
    ("  1   INSTALACION             12.00", 22, False, "izq"),
    ("", 10, False, "izq"),
    ("-" * 42, 20, False, "izq"),
    ("SUBTOTAL                      80.50", 22, False, "izq"),
    ("ITBMS 7%                       5.64", 22, False, "izq"),
    ("TOTAL                         86.14", 26, True, "izq"),
    ("-" * 42, 20, False, "izq"),
    ("", 10, False, "izq"),
    ("EFECTIVO                      90.00", 20, False, "izq"),
    ("CAMBIO                         3.86", 20, False, "izq"),
    ("", 14, False, "izq"),
    ("Conserve este comprobante", 20, False, "centro"),
    ("para cualquier reclamo de", 20, False, "centro"),
    ("garantia.", 20, False, "centro"),
    ("", 12, False, "centro"),
    ("GRACIAS POR SU COMPRA", 22, True, "centro"),
]


def build():
    recibo = Image.new("RGB", (ANCHO, ALTO), PAPEL)
    lienzo = ImageDraw.Draw(recibo)

    y = 60
    for texto, tam, negrita, alineado in LINEAS:
        if not texto:
            y += tam
            continue
        fuente = _fuente(tam, negrita)
        ancho_texto = lienzo.textlength(texto, font=fuente)
        x = (ANCHO - ancho_texto) / 2 if alineado == "centro" else 70
        # la impresora de tickets marca desigual: cada línea con su propio gris
        gris = tuple(min(255, c + random.randint(0, 28)) for c in TINTA)
        lienzo.text((x, y), texto, font=fuente, fill=gris)
        y += tam + 12

    # El sello de la fecha salió flojo: es parte del ejercicio que no se lea el año.
    lienzo.rectangle([(66, 352), (430, 392)], fill=None)

    # Fotografiado con el móvil: ligera rotación, sombra lateral y algo de grano.
    recibo = recibo.rotate(-1.6, expand=True, fillcolor=(226, 226, 224), resample=Image.BICUBIC)
    sombra = Image.new("L", recibo.size, 0)
    ImageDraw.Draw(sombra).rectangle([(0, 0), (90, recibo.size[1])], fill=70)
    recibo.paste(Image.new("RGB", recibo.size, (205, 204, 201)), (0, 0), sombra.filter(ImageFilter.GaussianBlur(40)))

    pixeles = recibo.load()
    for _ in range(int(recibo.size[0] * recibo.size[1] * 0.02)):
        x = random.randint(0, recibo.size[0] - 1)
        y = random.randint(0, recibo.size[1] - 1)
        r, g, b = pixeles[x, y]
        ruido = random.randint(-14, 14)
        pixeles[x, y] = (max(0, min(255, r + ruido)),
                         max(0, min(255, g + ruido)),
                         max(0, min(255, b + ruido)))

    recibo = recibo.filter(ImageFilter.GaussianBlur(0.6))
    MATERIALS.mkdir(parents=True, exist_ok=True)
    destino = MATERIALS / "19_comprobante_foto.png"
    recibo.save(destino, "PNG", optimize=True)
    return destino


if __name__ == "__main__":
    random.seed(14)          # la misma foto en cada generación
    destino = build()
    print(f"{destino.name}: {destino.stat().st_size // 1024} KB")
