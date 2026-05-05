from pathlib import Path

from pypdf import PdfWriter
from pypdf.generic import ArrayObject, FloatObject, NameObject


PDF_PATH = Path(__file__).resolve().parents[1] / "pdf" / "Aufnahmeantrag.pdf"
RIGHT_EDGE = 547.0
URL_OLD = b"www.anglerverein-schleusingen.de"
URL_NEW = b"https://1av-schleusingen.de/"
LINE_OLD_AUSSTELLUNGSORT = b"159.666 0 l"
LINE_NEW_AUSSTELLUNGSORT = b"142.237 0 l"
LINE_OLD_UNTERSCHRIFT = b"223.937 0 l"
LINE_NEW_UNTERSCHRIFT = b"204.66 0 l"


def update_content_stream(writer: PdfWriter) -> None:
    page = writer.pages[0]
    content = page.get_contents()
    data = content.get_data()

    replacements = (
        (URL_OLD, URL_NEW),
        (LINE_OLD_AUSSTELLUNGSORT, LINE_NEW_AUSSTELLUNGSORT),
        (LINE_OLD_UNTERSCHRIFT, LINE_NEW_UNTERSCHRIFT),
    )
    for old, new in replacements:
        if old not in data:
            raise ValueError(f"Expected PDF content marker not found: {old!r}")
        data = data.replace(old, new, 1)

    content.set_data(data)
    page.replace_contents(content)


def update_form_field_rectangles(writer: PdfWriter) -> None:
    page = writer.pages[0]

    for annot_ref in page.get("/Annots", []):
        annot = annot_ref.get_object()
        if annot.get("/TU") != "Ausstellungsort":
            continue

        rect = list(annot["/Rect"])
        rect[2] = FloatObject(str(RIGHT_EDGE))
        annot[NameObject("/Rect")] = ArrayObject(rect)
        break


def write_pdf(writer: PdfWriter) -> None:
    with PDF_PATH.open("wb") as target:
        writer.write(target)


def main() -> None:
    writer = PdfWriter(clone_from=PDF_PATH)
    update_content_stream(writer)
    update_form_field_rectangles(writer)
    write_pdf(writer)


if __name__ == "__main__":
    main()
