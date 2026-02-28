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

Statische Website (HTML, CSS, JavaScript) — kein Build-Prozess erforderlich.

## Lokal starten

Die HTML-Dateien können direkt im Browser geöffnet werden, oder über einen lokalen Webserver:

```bash
# Python 3
python -m http.server 8000

# Node.js
npx http-server
```

Dann im Browser [http://localhost:8000](http://localhost:8000) aufrufen.

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
