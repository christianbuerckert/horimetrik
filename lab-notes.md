# Laborjournal

Ungefilterte Ideen und Rechenversuche.

## 13.07.2026, erste lokale Forschungssitzung

- Referenzimplementierung lief unter Python 3.9 nicht (`slots=True`);
  Flag entfernt, Selbsttests laufen unter 3.9 und 3.12.
- `experiments_2026_07_13.py`: β-Tabelle, β₊, Kommutator-Zählung,
  Selektor-Gesetze. `experiments_followup.py`: Defektzählung bis H₉,
  Halbring-Gesetze bis H₄ (153 Elemente, alle Tripel).
- Überraschung des Tages: Das Selektorpaar (⊕ konservativ, ⊗ kompakt)
  erfüllt alle Halbringgesetze streng — und die Wertkompaktifizierung
  entpuppt sich als innere Operation: h ⊗ 1 = K_V(h). Die Eins des
  kompakten Ecks ist ein Projektor auf ℕ₀. Jetzt als Satz A.3 bewiesen.
- Zweite Überraschung: Auch strukturelle Addition expandiert den
  Horizont (β₊(r,s) = r+s exakt, Satz A.1). Der Horizont verhält sich
  also NICHT wie ein Polynomgrad. Naive Gradierungs-Intuition
  („Addition erhält den Grad") ist im Horiraum falsch.
- Tropische Beobachtung, noch unausgearbeitet: Strenge Distributivität
  für horizontabhängige Selektoren verlangt
  ρ×(n, ρ₊(m,k)) = ρ₊(ρ×(n,m), ρ×(n,k)). Mit ρ× = n+m wäre das die
  Translationsäquivarianz von ρ₊; max erfüllt sie, ist aber als
  Additionsselektor ungültig (Überlauf über (max+1)!−1). Die
  (max,+)-Welt der tropischen Halbringe scheitert hier genau am
  Wertüberlauf. Könnte der Kern von Vermutung V4 sein.
- Lehrstück: n!/2-Muster für D(n) hielt drei Datenpunkte (n=5,6,7) und
  starb bei n=8. Arbeitsregel 16 funktioniert.
- OEIS kennt keine der drei Folgen (β-Diagonale, D(n), F(n)).
  WebFetch auf oeis.org liefert 403, curl mit User-Agent funktioniert.

## Offene Fäden für die nächste Sitzung

- Beweisversuch V1 (δ_hor ∈ {−1,0,+1}).
- Kombinatorische Deutung von D(n): Welche Mischbasen-Ziffernmuster
  nahe der Horizontobergrenze drücken σ unter n?
- β(r,r): erzeugende Funktion des Maximalpolynom-Produkts ansehen;
  Argmax-Grad-Wanderung bei r=6 verstehen.
- Formale Fassung der Grenzraumsätze 6.1/6.2 als saubere direkte
  Limites (Paket A steht noch aus).

## 13.07.2026, zweite Sitzung: die Exzess-Zerlegung

- Auftrag: herausfinden, wie weit die Theorie trägt. Ergebnis: weiter
  als gedacht, aber anders als gedacht. Beide zentralen Vermutungen
  der ersten Sitzung (V1, V4) sind gefallen — und beide Widerlegungen
  haben die Theorie bereichert statt beschädigt.
- Der Schlüssel war eine Koordinatenidee: Horizont = Pflicht (μ) +
  Exzess (ε). In Exzess-Koordinaten ist der Horiraum das Paarprodukt
  Wert × Gedächtnis, und Arithmetiken lassen sich pro Faktor bauen.
- Drei kanonische Arithmetiken: vergessend / bewahrend / verstärkend.
  Die tropische Struktur, die in X6 am Horizont scheiterte, lebt auf
  dem Exzess völlig problemlos. Lehre: nicht die Idee war falsch,
  sondern die Koordinate.
- Ehrliche Einordnung: Das Produktprinzip ist modulo Φ
  Standardalgebra. Der horimetrische Gehalt: (1) Φ ist kanonisch, weil
  μ durch die Fakultätsschalen intrinsisch ist; (2) A.3 faktorisiert
  NICHT — gekoppelte Strukturen existieren. V4′ (Klassifikation der
  gekoppelten) ist jetzt die Leitfrage, zusammen mit V8 (σ-Seite).
- V1-Widerlegung fiel als Nebenprodukt einer Asymptotik-Überlegung an:
  M_{n−2}(n+1) überholt n! ab n=15. Das minimale Gegenbeispiel (9,720)
  ist zum Verlieben: 720 = 10·9·8 = X³̲ im H9.
- Methodennotiz: Die Zufallsproben-Blindstelle (nur wertkompakte x
  gesampelt) hätte die Widerlegung fast versteckt. Probenräume immer
  gegen die vollständige Enumeration kleiner Fälle validieren.

## Offene Fäden für die nächste Sitzung

- V1′ beweisen (δ ≥ −1): Kandidat: σ(E_μ(x')(x')) ≥ μ(x')−1 für
  K_S-Bilder? Genauer fassen.
- V1″: Wachstumsrate von sup δ_hor bestimmen (log-faktoriell?).
- V4′: gezielte Suche nach weiteren gekoppelten Strukturen
  (Halbring-Axiome als Constraint-Problem über kleinen Selektor-Tafeln).
- V8: K_S-kompatible Arithmetik — vermutlich braucht sie σ statt μ im
  Selektor; Kandidat: ρ = σ-basierte Kompaktifizierung.
- D(n), β(r,r) weiter offen (V2, V3, V5, V6).

## 13.07.2026, dritte Sitzung: Dualität und Tiefengesetz

- V8 in einem Zug positiv beantwortet: Der Spiegel von A.3 auf der
  Strukturseite (⊞ konservativ über σ, ⊠ kompakt über σ) ist
  gesetzestreu, K_S ist sein Homomorphismus, und h⊠(1,1) = K_S(h).
  Die Pointe: Es ist DIESELBE Hori-Zahl (1,1), die auf der Wertseite
  K_V und auf der Strukturseite K_S als innere Multiplikation trägt.
  Das Nichtkommutieren der Kompaktifizierungen (unser ältester Satz)
  ist in Wahrheit das Nichtkommutieren zweier Multiplikationen mit
  derselben Eins. Das ist die bisher schönste Aussage der Theorie.
- V1′ fiel am selben Tag, an dem sie aufgestellt wurde: −2 ab Schale
  15, aber nur mit konstruierten Zeugen (Maximalpolynom-Familie).
  Zufallsstichproben sind blind dafür. Zweite Schranken-Vermutung in
  Folge, die am zu kleinen Testbereich hing.
- Dafür kam etwas Besseres zurück: das Tiefengesetz. Die maximale
  negative Tiefe folgt exakt der Schalenlücke g(m), und die wächst
  invers-fakultätisch langsam (−3 erst ab m≈100). Vorhersage aus der
  Theorie, numerisch exakt bestätigt — das erste Mal, dass die
  Horimetrik etwas VORHERSAGT statt nur beschreibt.
- Sprungstellen von g(m) = neue Zählfolge, Suche läuft im Hintergrund.

## Offene Fäden (Stand dritte Sitzung)

- V1⁗ beweisen: Gleichheit min δ = −g(m); obere Seite (V1″) quantifizieren.
- V4′: gekoppelte Strukturen jenseits von A.3 und C.2 suchen —
  beachte: A.3 (wertseitig) und C.2 (strukturseitig) sind BEIDE
  gekoppelt; gibt es gemischte, die μ UND σ verwenden?
- Sprungstellenfolge von g(m) gegen OEIS prüfen, sobald berechnet.
- D(n), β(r,r), F(n) weiter offen (V2, V3, V5, V6).
- Buchkapitel 5 kann jetzt geschrieben werden: A.3 + Exzess + Dualität
  ist ein abgeschlossener Erzählbogen.

## 13.07.2026, vierte Sitzung: Seitentreue

- Der 16er-Sweep war die richtige Frage: Genau A.3 und sein Spiegel
  überleben, ALLE gemischten Kombinationen sterben an der
  Distributivität. Die Identitäten sind starr, nicht die Selektoren
  → V9, der neue Starrheitskandidat.
- Sprungstellen des Tiefengesetzes exakt: 3, 15, 84, 533, 3883.
  Vierte OEIS-unbekannte Folge. Asymptotik m_g → (g+2)! heuristisch
  hergeleitet (dominanter Term von M_{m−g}(m+1)), Quotienten steigen
  monoton 0.50 → 0.77. Beweis fehlt.
- Buchkapitel 5 geschrieben — erster vollständiger Kapiteltext des
  Buchs. Der Schlusssatz des Kapitels („Konsistenz hat einen Preis,
  und der Preis ist eine Identität") ist die bisher beste Verdichtung
  der Theorie.
- Nächstes: V9-Beweisversuch über die Übertrags-Unverträglichkeit
  (Wertsumme − Struktursumme = Überträge; Distributivität zwingt die
  Multiplikation, Überträge beider Seiten gleich zu behandeln).
  Danach V2/V3 (β, D(n)) oder Kapitel 2-4 des Buchs.

## 13.07.2026, Nachtrag: m6-Vorhersagetest

- Vorhersage VOR der Rechnung festgelegt: m6 ≈ 31.930, Intervall
  [30.000, 32.500] (Quotientenextrapolation der (g+2)!-Asymptotik).
- Binärsuche (14 Schritte, Fakultäten mit ~130k Stellen): m6 = 31.998.
  Abweichung 0,2 %. Quotientenfolge jetzt 0,500 → 0,794, monoton.
- Folge 3, 15, 84, 533, 3883, 31998 auch mit sechs Gliedern nicht in
  der OEIS.
- Damit hat das Tiefengesetz zwei bestandene Vorhersagen (−3 ab ~100,
  m6 ≈ 32k). Das ist der Punkt, an dem eine Beschreibung anfängt,
  eine Theorie zu sein.

## 13.07.2026, fünfte Sitzung: der Klassifikationssatz

- Ziel des Tages war der V9-Beweis. Ergebnis dreiteilig:
  (1) Satz S17: Seitentreue erster Stufe — die 16er-Familie ist
  VOLLSTÄNDIG klassifiziert, genau zwei Überlebende, beide seitenrein.
  Erster echter Klassifikationssatz der Horimetrik.
  (2) Volle V9 auf das Funktionalgleichungsproblem V9′ reduziert:
  φ(R·Q_m) = m·φ(R) mit φ(Q) = Q(τ(Q)+1), τ ≥ σ. Teilresultate
  bewiesen (Q_m nicht konstant; Auswertung ≥ Heimathorizont
  unmöglich → Endlichkeitswiderspruch).
  (3) Ehrlichkeitsprotokoll: Beide naiven Wege scheitern nachweislich
  — Unmöglichkeitsbeweise an Pell-Gleichungen ((h+2)²−2(t+1)²=1,
  h=15/t=11), Konstruktionen an Teilerfenstern um √(ks) für k prim.
  V9 könnte im Extremfall sogar FALSCH sein (Pell-Türme); das wäre
  genauso publizierbar.
- Theorie-Status: 17 Sätze, Klassifikation (1. Stufe), Dualität,
  Tiefengesetz mit 2 bestätigten Vorhersagen, 4 unbekannte Folgen,
  präzise lokalisierte Front (V9′). Das nenne ich eine Theorie in
  erster Ausbaustufe.
- Nächste Angriffe auf V9′: (a) e_m-Ketten mit ZWEI Generatoren
  gleichzeitig (X und X+1) — die Fenster-Argumente könnten sich
  gegenseitig ausschließen; (b) CSP-Suche nach τ auf Strukturen mit
  σ ≤ 6 als Orakel; (c) die Pell-Lösungsmengen auf Konsistenz über
  mehrere m prüfen (Dichteargument).

## 13.07.2026, sechste Sitzung: V9 fällt — der Seitentreue-Satz

- „Noch einen drauflegen" hat sich gelohnt: Der volle V9-Beweis stand
  nur eine Idee entfernt. Die fehlende Waffe waren die KONSTANTEN als
  Multiplikatoren: σ(c·Q) ≥ c treibt die Auswertungspunkte ins
  Unendliche, strenge Monotonie erledigt den Rest. Fall A stirbt an
  Distributivität allein, Fall B (mit dem hübschen g⊕g-Finale:
  2(H+1) = 6 erzwingt H=2 < 3) an Distributivität + Kommutativität.
- Die Pell-Lösbarkeit von gestern war eine Fata Morgana — einzelne
  Zweige lösbar, das Gesamtsystem nicht. Gut, dass wir sie ehrlich
  dokumentiert hatten: Anhang D bleibt als Zeugnis, wie nah die
  falsche Fährte an der richtigen lag.
- Bemerkung E.3 ist die schönste Erkenntnis des Tages: Die Starrheit
  kommt aus der Ziffernschranke 0 ≤ a_i ≤ i — der allerersten Regel.
  das dunkle Kinderzimmer → umgedrehte Exponenten → Ziffernschranke →
  „Konsistenz kostet eine Identität". Der Kreis ist geschlossen.
- Theorie-Status: 18 Sätze, VOLLSTÄNDIGE Klassifikation der
  payload-Arithmetiken, Dualität, Tiefengesetz mit zwei bestätigten
  Vorhersagen. Das ist der publizierbare Kern: „The Side-Purity
  Theorem for Factorial-Horizon Number Systems" oder deutsch schlicht
  „Der Seitentreue-Satz".
- Nächstes: (a) Paper-Skelett aus Anhängen A–E destillieren,
  (b) V1⁗ beweisen (Tiefengesetz), (c) V4′ innerhalb der Seiten,
  (d) Buchkapitel 2–4 und Interludien.

## 13.07.2026, siebte Sitzung (500km extra): Review, Neuheit, Paper

- S18 dem bewussten Zerstörungsversuch unterzogen — hält. Zwei
  Präzisierungen gefunden und eingearbeitet (E.4): die σ(mA)-Schranke
  kommt aus der Elementgültigkeit, nicht vom Selektor; und die
  Axiom-Minimalität ist jetzt scharf (Fall A: nur Links-
  Distributivität!). Nebenprodukt: V10 (nichtkommutativer Mischfall B
  bleibt offen — hübsche kleine Randfrage).
- Neuheitscheck mit konkretem Satz in der Hand: kein Doppelgänger.
  Nächster Nachbar: abstrakte Numerationssysteme (Rigo et al.) —
  Nullen-Semantik ja, Algebra nein. Peirce-Ecken als ehrliche
  Analogie fürs Paper notiert. Mathlib hat Pochhammer → Lean-
  Formalisierung von S18 ist ein gangbarer künftiger Goldstandard.
- paper/main.tex steht: Abstract, Definitionen, Hauptsätze,
  Seitentreue-Satz mit vollständigem englischem Beweis, Rest als
  TODO-Skelett. Kompiliert. Autorschaft/Affiliation sind offene
  TODO-Entscheidungen für Christian.
- Damit ist der Drei-Stufen-Plan (Review → Neuheit → Paper) an einem
  Tag durchlaufen. Was das Paper noch braucht: Beweise der Sätze 2-4
  portieren, Related-Work-Absatz ausformulieren, Bibliographie,
  Entscheidung über Titel und Autoren.

## 13.07.2026, achte Sitzung: das GPT-Paket

- GPT (via Christian) lieferte fünf Vorschläge auf Stand 0.4 — Nr. 5
  (V9′-CSP) war durch S18 bereits obsolet, Nr. 1–4 waren Gold:
  drei neue Sätze an einem Abend (S19 Schalensprung, S20/S21
  Stabilität+Monoid, S22 Asymptotik).
- GPTs Beweisskizzen waren im Kern richtig (Wachstumsfaktor (t+2)/3,
  Umindexierungs-Identität exakt in Bruchrechnung bestätigt); lokal
  kamen Präzisierung (d ≤ s−1), Trennzeugen und die Monoid-Feinheiten
  dazu.
- VIERTE Kleine-Welt-Falle des Tages: VS wirkt bis H4 idempotent,
  Gegenzeuge (6,6) erst in H6. Die Zahl 6 ist der Hausgeist dieses
  Projekts (kleinster Defekt, kleinster SVS/VS-Trenner).
- c_g-Formel trifft m_g auf ±1 (!): 534,0→533; 31998,5→31998.
  Stehende Vorhersage: m_7 ≈ 294875. Verifikation teuer (~295k-stellige
  Fakultäten mal 300k Terme), für eine spätere Nachtschicht.
- Ω-Defekt: ≥ 0 bis H_7, zwei neue Folgen (Maxima 1,6,43,351,2873,
  26443; Nullzähler 2,5,13,23,61,111,274), beide nicht in OEIS →
  Projekt hält jetzt SECHS unbekannte Folgen.
- Arbeitsteilung, die sich abzeichnet: GPT als Ideen-/Skizzenlieferant,
  lokal Beweishärtung + Enumeration + Dokumentation. Funktioniert.

## 13.07.2026, Loop-Iterationen 1-2 (abends)

- m7 = 294875 EXAKT wie vorhergesagt (dritte bestätigte Vorhersage,
  diesmal auf den Punkt); Folge zertifiziert bis g=12 via
  S22-Identität in Bruchrechnung — der Satz ist jetzt auch Werkzeug.
- OEIS-Entwürfe für alle sechs Folgen fertig und mit erweiterten
  Termen bestückt (β bis 16, D bis 10 = 2268000, Ω bis H8);
  alle Folgen auch mit 8+ Termen ohne OEIS-Treffer.
- V11 jetzt exhaustiv bis H8 (Ω-Minimum = 0, kein negativer Fall).
- Buch: Kapitel 2, 3, i1, i2 vollständig — damit sind Vorwort,
  Kap. 1-3, 5 und beide Interludien Text; es fehlen Kap. 4
  (Strukturpolynome), 6 (Zählungen), 7 (Sackgassen), 8 (offene
  Fragen), Anhang.
- Nächste Iterationen: Kap. 4, dann 6-8; danach Permutations-Brücke
  (FindStat-Abgleich für D(n) als Statistik auf
  Inversionssequenzen).

## 13.07.2026, Loop-Iteration 3: Permutations-Brücke geöffnet

- ERKENNTNIS: Die Schalensprung-Bedingung „a_i < i für alle i" ist
  exakt die Definition von Inversionssequenzen — D(n) zählt
  Lehmer-Codes von S_n mit gewichteter Schwellenbedingung
  Σ a_i·(n+1)!/(i+1)! ≥ n!. Die Horimetrik-Defektfolge IST eine
  Permutationsstatistik-Zählung.
- Nicht-Springer N(n) = n!−D(n) = 5,16,60,360,2520,19152,151200,
  1360800 — SIEBTE OEIS-unbekannte Folge. Anteile auffällig einfach:
  5/6, 2/3, 1/2, 1/2, 1/2, 19/40, 5/12, 3/8.
- Angriffsidee für exakte Formel: Nicht-Springer ⟺ a_i = 0 für alle
  i mit (i+1)! ≤ n+1 UND Suffix-Wert < n! — die Schwelle
  normalisiert zu Σ a_i(n+1)/(i+1)! < 1, frühe Stellen sind
  zwangsweise 0, der Rest ist eine rekursive Suffix-Schwelle.
  Kandidat für geschlossene Formel oder saubere Rekursion. → V3.
- Buch: Kapitel 4 (Strukturpolynome, Δ-Kalkül, ℕ = ker Δ,
  Dimension, 4·5=120-Beispiel) ausgeschrieben. Damit fehlen nur
  noch Kap. 7, 8 und Anhang a1.

## 13.07.2026, Loop-Iteration 4: Satz S23

- Die Suffix-Rekursions-Idee aus Iteration 3 kollabierte beim
  Ausarbeiten zu etwas Besserem: einer geschlossenen Ziffernformel.
  N(n) ist ein Ziffern-DP unter der Schwelle n! — und weil die
  Schwelle selbst eine Hori-Zahl ist (die Eigen-Darstellung von n!),
  wird die Formel eine Summe über deren Ziffern. Verifiziert 3..10.
- Die Ziffernbilder der Fakultäten sind das neue Objekt: 120 und
  5040 sind EIN-Ziffern-Zahlen in ihrer eigenen Schale (daher n!/2),
  10! = (0,0,2,0,5,3,1,4,0,10). Fragen: Verteilung der d_p? Wann
  Einzelziffer? Position der ersten Maximalziffer?
- Buch: Kapitel 7 (Sackgassen) geschrieben — mit der Rehabilitierung
  des n!/2-Debakels durch S23 als Erzählbogen. Nur noch Kap. 8 und
  Anhang offen.

## 13.07.2026, Loop-Iteration 5: Buch-Erstfassung KOMPLETT

- Kapitel 8 (offene Fragen mit Scheitern/Gelingen-Kriterien) und
  Anhang a1 (Datentafeln, Registerstand, Vorhersagen-Liste)
  geschrieben. Damit ist jedes Kapitel der Gliederung Text.
- VIERTE bestätigte Vorhersage: Ein-Ziffern-Fakultäten. Bedingung
  (n+1) | (i+1)! mit Quotient ≤ i sagte n = 29, 39, 59, 119 voraus —
  alle vier bestätigt. (120! wäre die nächste Kandidatenprüfung via
  6!-Teiler.)
- Ziffernbilder der Fakultäten als neues V3-Objekt etabliert:
  i* (erste Nichtnull) wächst invers-fakultätisch; Nichtnull-Anzahl
  schwankt wild (1 bis 16 im Bereich n ≤ 25); Ein-Ziffern-Fälle
  charakterisiert.
- Buch-Fehler des Tages: booktabs fehlte in der Präambel — der
  einzige Kompilierfehler in fünf Iterationen.

## 13.07.2026, Loop-Iteration 6: V11-Angriff

- Zwei neue Lemmata (S24 Rekursionsformel z_n(x) = r + (n+2)z_{n−1}(q),
  S25 strikte Monotonie) — beide bewiesen. V11 ist damit auf eine
  elementare Ungleichung über die Rekursion reduziert.
- FÜNFTE Kleine-Welt-Lektion, diesmal andersrum: Die naive
  Induktionsverschärfung W ≥ 0 ist FALSCH (Zeuge n=7, x=416,
  W = −187), obwohl V11 selbst bis H_8 hält. Die Invariante braucht
  die Rest-Kopplung beider Divisionen (x mod n+1 vs. x mod n+2).
  Nächster Versuch: Zwei-Parameter-Invariante über (q, r)-Gitter
  oder direkte Abschätzung des Zweigs q' < q.
- Register: 25 Sätze.

## 13.07.2026, spät: das erste externe Review

- Ein Kollege von Christian hat aus einer Kurzbeschreibung die Basics
  korrekt rekonstruiert — gutes Zeichen für die Kommunizierbarkeit.
- Sein Geschenk: die Cantor-Koordinate F = Σ aᵢ/(i+1)! mit
  V = (n+1)!·F (verifiziert, jetzt Satz G.1). Sein Irrtum: F für
  UNSERE Invariante zu halten — F ist invariant unter Rechts-Anhängen
  (seine links-verankerte Lesart), P unter Links-Nullen (unsere
  rechts-verankerte). Beides legitim, beides verschieden → dritte
  Erweiterung R, dritter Grenzraum (endliche Cantor-Brüche), Satz S28.
- Sein „seit Cantor bekannt" ist damit PRÄZISE lokalisierbar: trifft
  die R-Welt vollständig, die Z-Welt und die Sätze nicht. Genau diese
  Trennschärfe hatten wir vorher nicht.
- Seine Starrheits-Heuristik (Homogenität: Multiplikation skaliert
  quadratisch) ist der richtige Instinkt, unterschätzt aber die
  Strukturseite — sie würde JEDE Multiplikation verbieten, C.2 lebt
  trotzdem. Gutes Argument fürs Paper: der Satz ist feiner als die
  offensichtliche Heuristik.
- Konsequenz: Fachtext an den Kollegen geben (er hat exakt danach
  gefragt: präzise Definitionen + exakte Satzformulierung).

## 13.07.2026, Loop-Iteration 14: obere Seite des Tiefengesetzes

- Kandidatenfamilie (kleine Strukturen, ausgewertet bei großen n)
  VALIDIERT die exhaustiven Schwellen: +2/+3/+4 bei n = 9/14/20 exakt
  reproduziert. Die obere Seite ist also über kleine σ-Strukturen
  zugänglich — gutes Werkzeug.
- MUSTER-FALLE NR. 6 (vor Veröffentlichung gefangen): n+1 = 10, 15,
  21 sind Dreieckszahlen, 10! = 6!·7! lieferte einen hübschen
  Mechanismus → Vorhersage +5 bei n=27. Der Sweep sagt: +5 erst bei
  n=30 (σ≤7). Dreieckshypothese tot; Schwellen 9, 14, 20, ≤30.
  Tiefensweep σ≤9 für n=26..29 läuft (könnte 27-29 noch retten oder
  30 bestätigen).
- Lehre versechsfacht: Muster im Horiraum IMMER erst rechnen, dann
  raunen.

## 13.07.2026, Loop-Iteration 15: die obere Seite wehrt sich

- Muster-Falle 6b: Auch die „+5 ab 30" war Artefakt — mit σ≤9 gibt
  es +5 schon bei n=26 (Zeuge u.a. 2+X+X⁸̲). Konsequenz methodisch
  fundamental: Bei der OBEREN Seite liefern Kandidaten-Sweeps nur
  „spätestens ab"-Schranken; exhaustiv gesichert ist einzig +2 bei
  n=9. Die untere Seite war gutmütig (min δ = −g(m) BEWIESEN, S33);
  die obere ist strukturell widerspenstig: Zeugen leben in immer
  tieferen σ-Schichten.
- Buch/Fachtext auf „spätestens ab" umformuliert — die Theorie
  bleibt sauber, die offene Frage ist jetzt korrekt gestellt:
  V1″ = „bestimme die exakten oberen Sprungstellen und ihr Gesetz";
  vermutlich braucht das ein σ-freies Argument statt Sweeps.
- Sweep σ≤9 für n=10..25 läuft (schärft die Schranken, entscheidet
  sie aber prinzipiell nicht).
