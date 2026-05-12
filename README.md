# 1. Anglerverein Schleusingen e.V.

https://github.com/jessica-velasco/av-schleusingen.git

Website des 1. Anglerverein Schleusingen e.V. — einem Angelverein in Schleusingen, Thüringen.

**Live:** [1av-schleusingen.de](https://1av-schleusingen.de)

## Inhalt der Website

| Seite | Beschreibung |
|---|---|
| `index.html` | Startseite |
| `angelkarten.html` | Informationen zu Angelkarten |
| `fotogallerie.html` | Fotogalerie |
| `gewaesser.html` | Vereinsgewässer |
| `kontakt.html` | Kontaktinformationen |
| `mitglied.html` | Mitglied werden |
| `termine.html` | Termine und Veranstaltungen |
| `impressum.html` | Impressum |

## Technik

Statische Website mit Jekyll-Templates (HTML, CSS, JavaScript). Vor lokalen Vorschauen sollten &Auml;nderungen daher immer zuerst mit Jekyll nach `_site/` gebaut werden.

## Lokal starten

F&uuml;r eine korrekte Vorschau nach jeder &Auml;nderung immer den Jekyll-Build ausf&uuml;hren und anschlie&szlig;end das gerenderte Verzeichnis `_site/` per Python-Server bereitstellen:

```bash
bundle install
bundle exec jekyll build
cd _site
python3 -m http.server 8000
```

Dann im Browser [http://127.0.0.1:8000](http://127.0.0.1:8000) aufrufen.

## Hinweise f&uuml;r KI-Agenten

Wenn ein KI-Agent in diesem Repository &Auml;nderungen vornimmt, soll nach jeder inhaltlichen oder visuellen &Auml;nderung dieser Ablauf befolgt werden:

1. `bundle exec jekyll build`
2. `_site/` &uuml;ber `python3 -m http.server 8000` bereitstellen
3. Die Vorschau immer gegen die gebaute Version unter `http://127.0.0.1:8000` pr&uuml;fen, nicht gegen die Rohdateien im Projektwurzelverzeichnis
4. Wenn eine &Auml;nderung auch im &Auml;nderungsprotokoll dokumentiert werden soll, die bestehende Website-Seite `changelog.html` aktualisieren statt eine neue `CHANGELOG.md` oder andere separate Markdown-Chronik anzulegen

## Deployment

Die Seite wird über **GitHub Pages** gehostet. Änderungen am `main`-Branch werden automatisch veröffentlicht.

## Projektstruktur

```
├── css/                   # Stylesheets und zugehörige Bilder
├── images/                # Allgemeine Bilder
├── images_gallerien/      # Fotos für die Galerie
├── images_gewaesser/      # Fotos der Gewässer
├── pdf/                   # Dokumente (z.B. Aufnahmeantrag)
├── CNAME                  # GitHub Pages Custom Domain
└── *.html                 # Seiten der Website
```

## Lizenz

© Anglerverein Schleusingen e.V.
