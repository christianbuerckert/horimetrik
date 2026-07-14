# Buchplan „Horimetrik — Zahlen mit Horizont"

## Didaktisches Grundprinzip (verbindlich)

1. **Idee vor Formel.** Jedes Konzept wird zuerst ohne Formeln erzählt,
   an der Stelle, an der es im Denkprozess tatsächlich entstanden ist
   (führende Nullen, die plötzlich zählen).
2. **Rückkehrpunkte.** Nach jedem technischen Kapitel folgt ein kurzes
   Interludium „Zurück an die Oberfläche": Was haben wir gerade
   verstanden, in einem Absatz ohne ein einziges Formelzeichen?
3. **Sackgassen gehören ins Buch.** Verworfene Wege (verworfen.md) und
   widerlegte Muster (G3!) werden erzählt, nicht versteckt. Das
   n!/2-Debakel ist ein eigenes Lehrstück über Datenpunkte vs. Beweise.
4. **Jeder Satz hat eine Heimat.** Nichts erscheint im Buch, was nicht
   im REGISTER.md steht; jede Register-Zeile nennt ihr Zielkapitel.

## Kapitelstruktur

| Nr | Datei | Titel | Ebene |
|---|---|---|---|
| 0 | kapitel/00-vorwort.tex | Vorwort: Ein Spiel mit führenden Nullen | Oberfläche |
| 1 | kapitel/01-idee.tex | Die Idee: Zahlen, die wissen, wie viel Platz sie haben | Oberfläche |
| 2 | kapitel/02-horizonte.tex | Endliche Horizonte und Fakultätsschalen | Einstieg Mathematik |
| — | kapitel/i1-oberflaeche.tex | Interludium: Was ein Horizont wirklich ist | Oberfläche |
| 3 | kapitel/03-zwei-erweiterungen.tex | Zwei Arten zu wachsen: Struktur oder Wert | Mathematik |
| 4 | kapitel/04-strukturpolynome.tex | Strukturpolynome und die Horizontableitung | Mathematik tief |
| — | kapitel/i2-oberflaeche.tex | Interludium: Die Lebensgeschichte der Sieben | Oberfläche |
| — | kapitel/i2-oberflaeche.tex | Interludium: Die Lebensgeschichte der Sieben | Oberfläche |
| 5 | kapitel/05-arithmetik.tex | Arithmetik mit Gedächtnis: der Halbring | Mathematik tief |
| 6 | kapitel/06-zaehlungen.tex | Neun Zählfolgen aus der Horimetrik (nennt die OEIS-Einreichungen; A-Nummern nach Vergabe nachtragen) | Mathematik |
| 7 | kapitel/07-sackgassen.tex | Sackgassen: was nicht funktioniert hat und warum | Oberfläche/Mathe gemischt |
| 8 | kapitel/08-offene-fragen.tex | Offene Fragen und ein Forschungsprogramm | Mathematik |
| 9 | kapitel/09-einordnung.tex | Einordnung: Wo die Horimetrik wohnt | Mathematik |
| — | kapitel/literatur.tex | Literatur und Einordnung | — |
| A | kapitel/a1-referenz.tex | Anhang: Referenz, Datentafeln, Registerstand | technisch |
| B | kapitel/a2-beweise.tex | Anhang: Die Beweise | technisch |

## Arbeitsablauf

- Ergebnisse entstehen in Spezifikation/Register, nie zuerst im Buch.
- Buchtext wird kapitelweise geschrieben, sobald der zugehörige
  Registerbestand stabil ist. Kapitel 1 und 2 sind jetzt schon
  schreibbar, Kapitel 5 nach Klärung von V4, Kapitel 6 wächst mit Daten.
- Kompilieren: `cd buch && latexmk -pdf main.tex` (oder `pdflatex` zweimal).
