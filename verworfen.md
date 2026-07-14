# Verworfene Richtungen

Bewusst beiseitegelegte Ideen mit Begründung und Datum. Nichts hier ist
verboten — aber wer eine dieser Richtungen wieder aufnimmt, muss zuerst
das genannte Hindernis entkräften. Die lehrreichsten Einträge werden im
Buch als Kapitel „Sackgassen" erzählt.

## X1. Hori als allgemeiner Adress- oder Zeigerraum (12.07.2026)

Idee: Hori-Adressen statt IPv6/64-Bit-Zeigern, Horizont als wachsender
Adressraum. Hindernis: Der Horiraum ist innerhalb eines Horizonts
strukturell starr; die Verzweigung ist durch die Tiefe festgelegt.
Adressräume brauchen lokale Elastizität (ungleich wachsende Unterräume).
Rest-Idee, die überlebt hat: Adressierung streng regulärer
Fakultätsbäume (X2-Kontext), als Randnotiz behalten.

## X2. Hori-Heap als schnellere Priority Queue (12.07.2026)

Kindervergleiche kosten ohne Zusatzstruktur \(O(h^2)\) über einen Pfad,
weil der Verzweigungsgrad mit der Tiefe wächst. Kein automatischer
Vorteil gegenüber Binärheap. Wiederaufnahme nur mit konkretem Modell
(SIMD-Vergleich, gecachte Kindminima) und Benchmark-Kriterium.

## X3. P versus NP über den Horiraum (12.07.2026)

Ein Darstellungswechsel ändert keine Komplexitätsklasse. Ausgeklammert,
bis der Horiraum eine bewiesene algorithmische Invariante besitzt, die
sich gegen Standard-Eingabelängen messen lässt.

## X4. Defektformel \(D(n)=n!/2\) (13.07.2026)

Widerlegt bei \(n=8\) (siehe G3). Verworfen als Formel; die Folge selbst
bleibt aktives Forschungsobjekt (V3).

## X5. Konservative Multiplikation \(\rho_\times=\max(n,m,\mu(xy))\) (13.07.2026)

Nicht assoziativ (G4). Die Null löscht den Wert, der Horizont behält
Geschichte — beides zusammen zerstört die Klammerfreiheit. Verworfen als
Halbringkandidat; als Beispiel für „Horizont trägt Rechengeschichte"
didaktisch wertvoll.

## X6. Tropisches Selektorpaar \((\max,+)\) (13.07.2026)

Strenge Distributivität horizontabhängiger Selektoren führt auf die
Translationsäquivarianz \(\rho_+(m+n,k+n)=\rho_+(m,k)+n\), die \(\max\)
erfüllt. Aber \(\rho_+=\max\) ist als Additionsselektor ungültig: die
Wertsumme kann \((\max+1)!-1\) überschreiten. Die tropische Welt
scheitert exakt am Wertüberlauf. Verworfen als direkte Konstruktion;
die Beobachtung speist Vermutung V4.

## X7. „Der Horiraum ist mächtiger als \(\mathbb N\)" (12.07.2026)

Falsch, \(\mathcal H\) ist abzählbar. Der Mehrwert liegt nicht in der
Kardinalität, sondern in Struktur pro Wert (Horizontkoordinate, zwei
Einbettungen, zwei Kompaktifizierungen). Jede Argumentation über
Mächtigkeit ist verworfen.

## X8. Anwendungssuche vor Theorie (12.07.2026)

Entscheidung: Anwendungen (Scheduling, Zustandsräume, Kombinatorik-
Enumeration) werden erst gesucht, wenn Definitionen und Kernsätze
stabil sind. Motivierende Analogien sind im Laborjournal erlaubt, im
Buch nur in den Oberflächenkapiteln.

## Nachtrag zu X6 (13.07.2026): aufgelöst statt verworfen

Die Exzess-Zerlegung (Anhang B) zeigt, dass die tropische Arithmetik
nicht auf dem Horizont, sondern auf dem Exzess \(\varepsilon=n-\mu(x)\)
lebt. Dort gilt \((\max,+)\) uneingeschränkt; der Pflichtanteil
\(\mu\) übernimmt die Überlaufvalidität. X6 bleibt als Warnung vor der
falschen Koordinate bestehen — die Idee selbst war richtig, nur der
Ort war falsch. (Genau das meinte die Arbeitsregel: Die Idee bleibt
bestehen, auch wenn ein Versuch scheitert.)

## X9. Δ-Trapdoor-Kryptographie (14.07.2026; Gemini-Vorschlag, GPT-Widerlegung, hier verifiziert)

**Idee:** Einwegfunktion aus Differenzüberlauf (S40) + Seitentreue
(S18): geheime Gestalt durch k führende Nullen schieben, wertkompakt
auswerten, nackten Wert veröffentlichen; Rückweg angeblich
kapazitätsgesprengt (Anti-Differenzen) und hybride Angriffe durch
Seitentreue versperrt.

**Widerlegung:** \(y=P(N)\) ist durch fortgesetzte Division mit Rest
in \(O(m)\) Divisionen eindeutig invertierbar, weil die
Hori-Schranken \(c_d\le r-d<N-d\) unter den Divisoren bleiben —
das ist Satz S1 am verschobenen Auswertungspunkt; die Gewichte
\(1,N,N(N{-}1),\ldots\) bilden wieder ein Mischbasensystem
(superincreasing-Knapsack-Charakter). Exhaustiv bestätigt
(`experiments_trapdoor.py`: alle Gestalten r≤6, Shifts k≤5).

**Fehlerquellen des Vorschlags:** (1) Strukturtreue Erweiterung
wendet nicht Δ auf P an — P bleibt, nur der Auswertungspunkt
wandert; Δ misst die Wertänderung. (2) Seitentreue verbietet
gemischte *Halbringe*, nicht gemischte *Algorithmen*. (3) Keine
geheime Falltür: Alice weiß nichts, was Eve nicht weiß.

**Lehre:** Die Fakultätsordnung verwirbelt nicht, sie sortiert;
Bijektivität (S1) und kryptographische Härte schließen sich hier
aus. Restperspektive: σ/Γ als Analysewerkzeug für Koeffizienten-
und Rauschwachstum in bestehenden (Gitter-)Konstruktionen —
Messinstrument, nicht Härtequelle.
