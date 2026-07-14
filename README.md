# Horimetrik — Zahlen mit Horizont

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21400755.svg)](https://doi.org/10.5281/zenodo.21400755)

**➔ Das Buch (Deutsch, Original): [`buch/main.pdf`](buch/main.pdf)**
**➔ The book (English translation): [`book/main.pdf`](book/main.pdf)**
**➔ The paper (English preprint): [`paper/main.pdf`](paper/main.pdf)**

Langzeitarchiviert auf Zenodo: [10.5281/zenodo.21400755](https://doi.org/10.5281/zenodo.21400755).

Darum geht es hier — bei Abweichungen ist die deutsche Fassung
maßgeblich.

## Worum es geht

In jedem Stellenwertsystem trägt die Stelle mit dem meisten
Spielraum das meiste Gewicht — eine Ordnung so selbstverständlich,
dass niemand sie ausspricht. Dieses Buch dreht sie um. Aus der
Umkehrung folgt zwangsläufig eine kleine, eigensinnige Theorie:
Zahlenräume, die endlich sind (*Horizonte*), führende Nullen, die
plötzlich den Wert verändern, Zahlen mit drei Identitäten zugleich
(Wert, Gestalt, Bruch) — und als tiefster Satz die *Seitentreue*:
Man kann beweisbar nicht in zwei dieser Identitäten gleichzeitig
rechnen. Am Ende steht eine präzise Landkarte: Die Bewohner dieser
Welt sind wohlbekannte Objekte der Kombinatorik
(Inversionsfolgen), aber die Operationen und Sätze darauf sind
neu — darunter neun Zählfolgen, die bislang in keiner Datenbank
standen.

Erzählt wird ehrlich: mit allen Beweisen (Anhang B), allen neun
Sackgassen (eigenes Kapitel) und formelfreien Rückkehrpunkten nach
jedem technischen Kapitel — wer nur diese liest, versteht trotzdem,
worum es geht. Entstanden im Juli 2026, geschrieben von Christian
Felix Bürckert unter mathematischer Mitarbeit von Claude
(Anthropic, Modell Fable) und mit Ideenbeiträgen von GPT (OpenAI);
die Entstehungsgeschichte — sie beginnt beim Zubettbringen einer
Tochter — erzählt das Vorwort.

## Buch selbst bauen

```sh
cd buch && tectonic main.tex
```

(oder `latexmk -pdf main.tex` mit einer XeLaTeX/LuaLaTeX-fähigen
TeX-Distribution — das Buch nutzt `fontspec`).

## Nebenprodukte

Alles Weitere in diesem Repo ist Werkstatt: die Programme, Daten und
Arbeitsdokumente, aus denen das Buch entstanden ist.

| Pfad | Inhalt |
|---|---|
| `programme/horimetrik_reference.py` | Referenzimplementierung mit Selbsttests (Codierung, Erweiterungen, Kompaktifizierungen, Strukturarithmetik) |
| `programme/experiments_*.py` | Datierte Experimentskripte — Enumeration und Verifikation zu den einzelnen Sätzen (reine Python-3-Standardbibliothek; `experiments_oeis_bfiles.py` braucht NumPy) |
| `oeis/` | Einreichfertige Entwürfe und verifizierte b-Files der neun Zählfolgen des Buchs (A-Nummern werden nach Vergabe nachgetragen) |
| `paper/` | Eigenständiges englisches Preprint: die Hauptresultate mit vollständigen Beweisen im Anhang (12 Seiten) |
| `fachtext/` | Kompakter Fachtext ohne Erzählung — deutsch (`main.pdf`) und englisch (`main-en.pdf`) |
| `HORIMETRIK_0_1.md` | Kanonische Spezifikation (Arbeitsentwurf mit Anhängen A–J) |
| `REGISTER.md` | Ergebnisregister: jede Aussage mit stabiler ID, Status und Zielort im Buch |
| `conjectures.md`, `counterexamples.md`, `verworfen.md` | Vermutungen, Gegenbeispiele, dokumentierte Sackgassen |
| `lab-notes.md`, `CHANGELOG.md` | Arbeitsjournal des Projekts |
| `literature.md` | Literatursichtung mit Abgrenzung |
| `daten/` | Rohdaten einzelner Experimentläufe |

## Lizenz

Zweigeteilt nach Werkart:

- **Buch, Fachtext und alle Dokumente** (alles außer `programme/`):
  [CC BY 4.0](LICENSE) — frei lesen, teilen, zitieren, übersetzen;
  einzige Bedingung ist die Namensnennung
  („Christian Felix Bürckert, *Horimetrik — Zahlen mit Horizont*“)
  und die Kennzeichnung von Änderungen.
- **Programme** (`programme/`): [MIT](programme/LICENSE) — frei
  verwendbar, auch kommerziell, mit Copyright-Hinweis.

## Arbeitsprinzip

Ergebnisse entstehen in Spezifikation und Register, nie zuerst im
Buch. Enumeration erzeugt Vermutungen und Gegenbeispiele, niemals
Sätze — und jede behauptete Schranke muss konstruierte Extremfälle
überleben, nicht nur Stichproben. Auch die Fehlschläge sind Teil des
Projekts: Die Sackgassen haben ein eigenes Buchkapitel.
