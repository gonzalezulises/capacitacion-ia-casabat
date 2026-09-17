#!/usr/bin/env python3
"""Lector mínimo de OOXML para las compuertas del curso.

No modifica archivos ni depende de Microsoft Office, LibreOffice, openpyxl o
python-docx. Devuelve JSON estable para que los verificadores Node puedan leer
las fuentes canónicas DOCX y XLSX.
"""
from __future__ import annotations

import json
import re
import sys
import zipfile
from datetime import datetime, timedelta, timezone
from pathlib import Path
from xml.etree import ElementTree as ET

MAIN = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
WORD = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS_X = {"x": MAIN}
NS_W = {"w": WORD}


def _column_index(reference: str) -> int:
    letters = re.match(r"[A-Z]+", reference).group(0)
    value = 0
    for letter in letters:
        value = value * 26 + ord(letter) - 64
    return value - 1


def _shared_strings(book: zipfile.ZipFile) -> list[str]:
    if "xl/sharedStrings.xml" not in book.namelist():
        return []
    root = ET.fromstring(book.read("xl/sharedStrings.xml"))
    return ["".join(node.text or "" for node in item.findall(".//x:t", NS_X))
            for item in root.findall("x:si", NS_X)]


def _date_styles(book: zipfile.ZipFile) -> set[int]:
    if "xl/styles.xml" not in book.namelist():
        return set()
    root = ET.fromstring(book.read("xl/styles.xml"))
    custom = {}
    for num_fmt in root.findall("x:numFmts/x:numFmt", NS_X):
        custom[int(num_fmt.attrib["numFmtId"])] = num_fmt.attrib.get("formatCode", "")
    built_in_dates = set(range(14, 23)) | {27, 30, 36, 45, 46, 47, 50, 57}
    result = set()
    for index, xf in enumerate(root.findall("x:cellXfs/x:xf", NS_X)):
        fmt_id = int(xf.attrib.get("numFmtId", "0"))
        code = re.sub(r'"[^"]*"|\\.', "", custom.get(fmt_id, "")).lower()
        if fmt_id in built_in_dates or ("y" in code and ("m" in code or "d" in code)):
            result.add(index)
    return result


def _excel_date(serial: float) -> str:
    value = datetime(1899, 12, 30, tzinfo=timezone.utc) + timedelta(days=serial)
    return value.date().isoformat()


def read_xlsx(path: Path) -> dict:
    with zipfile.ZipFile(path) as book:
        shared = _shared_strings(book)
        date_styles = _date_styles(book)
        sheet_name = "xl/worksheets/sheet1.xml"
        root = ET.fromstring(book.read(sheet_name))
        rows: list[list[object]] = []
        types: list[list[str]] = []
        max_col = 0
        for row_node in root.findall(".//x:sheetData/x:row", NS_X):
            values: dict[int, object] = {}
            value_types: dict[int, str] = {}
            for cell in row_node.findall("x:c", NS_X):
                col = _column_index(cell.attrib["r"])
                max_col = max(max_col, col + 1)
                kind = cell.attrib.get("t", "n")
                style = int(cell.attrib.get("s", "0"))
                if kind == "inlineStr":
                    value = "".join(node.text or "" for node in cell.findall(".//x:t", NS_X))
                    cell_type = "text"
                else:
                    raw_node = cell.find("x:v", NS_X)
                    raw = "" if raw_node is None else raw_node.text or ""
                    if kind == "s":
                        value = shared[int(raw)] if raw else ""
                        cell_type = "text"
                    elif kind in {"str", "e"}:
                        value, cell_type = raw, "text"
                    elif kind == "b":
                        value, cell_type = raw == "1", "boolean"
                    elif raw == "":
                        value, cell_type = "", "blank"
                    else:
                        number = float(raw)
                        if style in date_styles:
                            value, cell_type = _excel_date(number), "date"
                        else:
                            value = int(number) if number.is_integer() else number
                            cell_type = "number"
                values[col], value_types[col] = value, cell_type
            rows.append([values.get(i, "") for i in range(max_col)])
            types.append([value_types.get(i, "blank") for i in range(max_col)])
        for index in range(len(rows)):
            rows[index].extend([""] * (max_col - len(rows[index])))
            types[index].extend(["blank"] * (max_col - len(types[index])))

    headers = [str(value) for value in rows[0]] if rows else []
    records = [dict(zip(headers, row)) for row in rows[1:]]
    record_types = [dict(zip(headers, row)) for row in types[1:]]
    return {"headers": headers, "rows": records, "types": record_types, "row_count": len(records)}


def _paragraph_text(node: ET.Element) -> str:
    pieces = []
    for item in node.iter():
        if item.tag == f"{{{WORD}}}t": pieces.append(item.text or "")
        elif item.tag == f"{{{WORD}}}tab": pieces.append("\t")
        elif item.tag == f"{{{WORD}}}br": pieces.append("\n")
    return "".join(pieces).strip()


def read_docx(path: Path) -> dict:
    with zipfile.ZipFile(path) as document:
        root = ET.fromstring(document.read("word/document.xml"))
    body = root.find("w:body", NS_W)
    lines = []
    for child in body:
        if child.tag == f"{{{WORD}}}p":
            text = _paragraph_text(child)
            if text: lines.append(text)
        elif child.tag == f"{{{WORD}}}tbl":
            for row in child.findall("w:tr", NS_W):
                cells = [_paragraph_text(cell) for cell in row.findall("w:tc", NS_W)]
                lines.append(" | ".join(cells))
    return {"text": "\n".join(lines), "paragraphs": lines}


def main() -> None:
    if len(sys.argv) != 3 or sys.argv[1] not in {"xlsx", "docx"}:
        raise SystemExit("uso: office_reader.py xlsx|docx archivo")
    kind, filename = sys.argv[1], Path(sys.argv[2])
    result = read_xlsx(filename) if kind == "xlsx" else read_docx(filename)
    json.dump(result, sys.stdout, ensure_ascii=False, separators=(",", ":"))


if __name__ == "__main__":
    main()
