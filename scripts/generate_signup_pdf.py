from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "pdf" / "Aufnahmeantrag-modern.pdf"
FONT_DIR = Path("/System/Library/Fonts/Supplemental")
FONT_REGULAR = FONT_DIR / "Arial.ttf"
FONT_BOLD = FONT_DIR / "Arial Bold.ttf"


def register_fonts() -> None:
    pdfmetrics.registerFont(TTFont("FormRegular", str(FONT_REGULAR)))
    pdfmetrics.registerFont(TTFont("FormBold", str(FONT_BOLD)))


def draw_label(c: canvas.Canvas, x: float, y: float, text: str) -> None:
    c.setFont("FormBold", 9)
    c.setFillColor(TEXT)
    c.drawString(x, y, text)


def draw_hint(c: canvas.Canvas, x: float, y: float, text: str) -> None:
    c.setFont("FormRegular", 7)
    c.setFillColor(MUTED)
    c.drawString(x, y, text)


def add_text_field(
    c: canvas.Canvas,
    name: str,
    x: float,
    y: float,
    w: float,
    h: float = 16 * mm / 4.233,
    *,
    value: str = "",
    multiline: bool = False,
) -> None:
    flags = 4096 if multiline else 0
    c.acroForm.textfield(
        name=name,
        x=x,
        y=y,
        width=w,
        height=h,
        value=value,
        fontName="Helvetica",
        fontSize=10,
        textColor=TEXT,
        borderColor=BORDER,
        fillColor=WHITE,
        borderWidth=1,
        forceBorder=True,
        fieldFlags=flags,
    )


PAGE_W, PAGE_H = A4
MARGIN_X = 18 * mm
TOP = PAGE_H - 18 * mm
CONTENT_W = PAGE_W - (2 * MARGIN_X)
TEXT = colors.HexColor("#1f2f3d")
MUTED = colors.HexColor("#5f6f7c")
ACCENT = colors.HexColor("#2c5c4c")
ACCENT_LIGHT = colors.HexColor("#dce9e3")
BORDER = colors.HexColor("#8aa59b")
WHITE = colors.white
BG = colors.HexColor("#f6f6f2")


def section_box(c: canvas.Canvas, x: float, y: float, w: float, h: float, title: str) -> None:
    c.setFillColor(BG)
    c.setStrokeColor(BORDER)
    c.roundRect(x, y - h, w, h, 8, fill=1, stroke=1)
    c.setFillColor(ACCENT)
    c.roundRect(x, y - 18, w, 18, 8, fill=1, stroke=0)
    c.rect(x, y - 18, w, 10, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.setFont("FormBold", 11)
    c.drawString(x + 10, y - 12.5, title)


def generate() -> Path:
    register_fonts()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(OUTPUT), pagesize=A4)
    c.setTitle("Aufnahmeantrag - 1. Anglerverein Schleusingen e.V.")
    c.setAuthor("OpenAI Codex")
    c.setSubject("Digital ausfuellbarer Aufnahmeantrag")

    c.setFillColor(ACCENT)
    c.roundRect(MARGIN_X, TOP - 58, CONTENT_W, 58, 14, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.setFont("FormBold", 22)
    c.drawString(MARGIN_X + 14, TOP - 24, "Aufnahmeantrag")
    c.setFont("FormRegular", 11)
    c.drawString(MARGIN_X + 14, TOP - 40, "1. Anglerverein Schleusingen e.V.")
    c.drawString(MARGIN_X + 14, TOP - 54, "Am Sportplatzteich - Anglerheim - 98553 Schleusingen")

    c.setFont("FormRegular", 10)
    c.setFillColor(TEXT)
    intro_y = TOP - 82
    c.drawString(
        MARGIN_X,
        intro_y,
        "Bitte fuellen Sie die Felder gut lesbar aus und reichen Sie den Antrag unterschrieben beim Verein ein.",
    )
    c.drawString(
        MARGIN_X,
        intro_y - 13,
        "Rueckfragen koennen wir telefonisch oder per E-Mail schneller klaeren als per Post.",
    )

    gutter = 10
    col_w = (CONTENT_W - gutter) / 2

    person_top = TOP - 118
    person_h = 220
    section_box(c, MARGIN_X, person_top, CONTENT_W, person_h, "Persoenliche Angaben")

    left_x = MARGIN_X + 12
    right_x = MARGIN_X + col_w + gutter + 12
    field_w = col_w - 24
    row_gap = 34
    first_row_y = person_top - 48

    personal_left = [
        ("name", "Name", ""),
        ("vorname", "Vorname", ""),
        ("strasse", "Strasse / Hausnummer", ""),
        ("plz_ort", "PLZ / Wohnort", ""),
    ]
    personal_right = [
        ("geburtsdatum", "Geburtsdatum", "TT.MM.JJJJ"),
        ("geburtsort", "Geburtsort", ""),
        ("beruf", "Beruf", "optional"),
        ("telefon", "Telefon / Mobil", "fuer Rueckfragen"),
    ]

    for index, (field_name, label, hint) in enumerate(personal_left):
        y = first_row_y - (index * row_gap)
        draw_label(c, left_x, y, label)
        if hint:
            draw_hint(c, left_x + 92, y, hint)
        add_text_field(c, field_name, left_x, y - 18, field_w)

    for index, (field_name, label, hint) in enumerate(personal_right):
        y = first_row_y - (index * row_gap)
        draw_label(c, right_x, y, label)
        if hint:
            draw_hint(c, right_x + 92, y, hint)
        add_text_field(c, field_name, right_x, y - 18, field_w)

    email_y = first_row_y - (4 * row_gap)
    draw_label(c, left_x, email_y, "E-Mail")
    add_text_field(c, "email", left_x, email_y - 18, CONTENT_W - 24)

    license_top = person_top - person_h - 14
    license_h = 100
    section_box(c, MARGIN_X, license_top, CONTENT_W, license_h, "Angaben zum Fischereischein")

    l_y = license_top - 46
    fields = [
        ("schein_nr", "Fischereischein-Nr.", MARGIN_X + 12, 118),
        ("ausstellung", "Ausstellungsdatum", MARGIN_X + 140, 98),
        ("gueltig_bis", "Gueltig bis", MARGIN_X + 248, 86),
        ("ausstellungsort", "Ausstellungsort", MARGIN_X + 344, 161),
    ]
    for field_name, label, x, width in fields:
        draw_label(c, x, l_y, label)
        add_text_field(c, field_name, x, l_y - 18, width)

    notes_top = license_top - license_h - 14
    notes_h = 144
    section_box(c, MARGIN_X, notes_top, CONTENT_W, notes_h, "Bestaetigung und Hinweise")

    text_x = MARGIN_X + 12
    text_y = notes_top - 38
    body_lines = [
        "Ich bestaetige mit meiner Unterschrift, dass meine Angaben vollstaendig und richtig sind.",
        "Ich besitze einen gueltigen Fischereischein. Mir ist bekannt, dass ueber die Aufnahme der Verein entscheidet.",
        "Die Satzung des 1. Anglerverein Schleusingen e.V. kann beim Verein eingesehen werden.",
    ]
    c.setFont("FormRegular", 9.2)
    c.setFillColor(TEXT)
    for idx, line in enumerate(body_lines):
        c.drawString(text_x, text_y - (idx * 13), line)

    checklist_y = text_y - 52
    c.setFont("FormBold", 9)
    c.drawString(text_x, checklist_y, "Bitte nach Moeglichkeit beifuegen:")
    c.setFont("FormRegular", 9)
    c.drawString(text_x + 8, checklist_y - 16, "- aktuelles Passbild fuer den Sportfischerpass")
    c.drawString(text_x + 8, checklist_y - 29, "- Nachweis ueber die Fischereipruefung oder sonstige Qualifikationen (Kopie)")

    sig_top = notes_top - notes_h - 14
    sig_h = 92
    section_box(c, MARGIN_X, sig_top, CONTENT_W, sig_h, "Ort, Datum und Unterschrift")

    sig_y = sig_top - 46
    sig_fields = [
        ("ort", "Ort", MARGIN_X + 12, 150),
        ("datum", "Datum", MARGIN_X + 174, 90),
        ("unterschrift", "Unterschrift", MARGIN_X + 276, 234),
    ]
    for field_name, label, x, width in sig_fields:
        draw_label(c, x, sig_y, label)
        add_text_field(c, field_name, x, sig_y - 18, width)

    footer_y = 28
    c.setStrokeColor(BORDER)
    c.line(MARGIN_X, footer_y + 20, MARGIN_X + CONTENT_W, footer_y + 20)
    c.setFillColor(MUTED)
    c.setFont("FormRegular", 8)
    c.drawString(MARGIN_X, footer_y + 7, "Kontakt: 0171 / 7362726")
    c.drawRightString(MARGIN_X + CONTENT_W, footer_y + 7, "Website: www.anglerverein-schleusingen.de")

    c.save()
    return OUTPUT


if __name__ == "__main__":
    path = generate()
    print(path)
