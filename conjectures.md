# Vermutungen

Status-Codes: **offen**, **gestützt** (Enumeration ohne Gegenbeispiel),
**widerlegt** (dann Verweis auf `counterexamples.md`).

## V1. Horizontdifferenz des Kommutators beschränkt — **widerlegt** (13.07.2026)

Kleinstes Gegenbeispiel \((9,720)\) mit \(\delta_{\mathrm{hor}}=+2\),
siehe G7 und Anhang B.7. Ersetzt durch:

## V1′. Untere Schranke \(-1\) — **widerlegt** (13.07.2026, selbe Sitzung)

Konstruierte Zeugen liefern \(-2\) ab Schale 15, \(-3\) ab Schale
\(\approx100\) (G9). Zufallsstichproben sehen diese Zeugen praktisch
nie. Ersetzt durch V1⁗.

## V1″. Unbeschränktheit nach oben — gestützt

\(\sup_{h\in H_n}\delta_{\mathrm{hor}}(h)\to\infty\).
Beobachtet: \(+2\) ab \(n=9\), \(+3\) ab \(n=14\), \(+4\) ab \(n=20\).

## V1⁗. Tiefengesetz — gestützt, quantitativ

Mit der Schalenlücke \(g(m)=m-\min\{s\mid M_s(m+1)\ge m!\}\) gilt

\[
\min_{h,\ \mathrm{val}(h)\in[m!,(m+1)!)}\delta_{\mathrm{hor}}(h)=-g(m),
\]

und \(g(m)\to\infty\) invers-fakultätisch langsam. Sprungstellen exakt:
\(m_g=3,15,84,533,3883,31998\) (\(g=1,\ldots,6\)), keine OEIS-Treffer.
Quantitative Fassung: \(m_g/(g+2)!\to1\) (Quotienten 0,50 bis 0,794,
monoton; Heuristik in Anhang C.6). Zwei bestandene Vorhersagetests
(\(-3\) ab \(m\approx100\); \(m_6=31998\) bei Vorhersage
\(\approx31930\)). Der Kommutator ist also beidseitig unbeschränkt,
aber mit extrem asymmetrischen Raten. Die Gleichheit (nicht nur
\(\ge-g\)) und die Asymptotik sind noch unbewiesen.

## V2. Diagonale \(\beta(r,r)\) — offen

Werte für \(r=1,\ldots,12\):
\(1, 6, 22, 87, 407, 2473, 19527, 170720, 1643913, 18042957,
233850057, 3239053262\).

- Kein OEIS-Treffer (Stand 13.07.2026, siehe Anhang A.5).
- Der Argmax-Grad wandert: \(d=r-1\) für \(r\le5\), danach \(d\ge r\).
- Gesucht: geschlossene Formel oder Asymptotik. Die Quotienten
  aufeinanderfolgender Werte wachsen etwa linear, was auf
  superexponentielles, grob fakultätsartiges Wachstum hindeutet.

## V3. Defektfolge \(D(n)\) — offen

\(D(n)=\#\{x\in[n!,(n+1)!) : \sigma(E_n(x))<n\}\), also wertkompakt,
aber nicht strukturkompakt:

\(D(3..9) = 1, 8, 60, 360, 2520, 21168, 211680\).

Kein OEIS-Treffer. Auffällig: \(D(9)=10\cdot D(8)\). Gesucht:
kombinatorische Beschreibung, etwa über Ziffernstatistik der
Mischbasendarstellung nahe der oberen Horizontgrenze.

## V4. Starrheit der Horizontselektoren — **widerlegt** (13.07.2026)

Die Exzess-Zerlegung (Anhang B) liefert gesetzestreue Arithmetiken mit
nicht-kompakter Multiplikation, sogar mit Eins und absorbierender Null
(\(\mathcal H_{\mathrm{arith}}\)). Siehe G8 und Satz B.3. Ersetzt durch:

## V4′. Klassifikation der gekoppelten Strukturen — offen, **Leitfrage**

Das Produktprinzip (Satz B.3) erklärt alle Arithmetiken, die in
Exzess-Koordinaten faktorisieren. Der Halbring aus Satz A.3 ist
nachweislich keine Produktstruktur (Bemerkung B.5). Frage: Welche
gekoppelten gesetzestreuen Arithmetiken gibt es? Ist die
konservativ-kompakte Familie im Wesentlichen die einzige gekoppelte
mit absorbierender Null?

## V8. \(K_S\) als Homomorphismus — **positiv beantwortet** (13.07.2026)

Ja: der strukturseitige Spiegel-Halbring (Dualitätssatz, S16/Anhang C.2)
hat \(K_S\) als Homomorphismus, mit \(h\boxtimes(1,1)=K_S(h)\) —
exakt spiegelbildlich zur Wertseite.

## V5. Beidseitige Fixpunkte — offen

\(F(n)=\#\{h\in H_n : K_S(h)=h \text{ und } K_V(h)=h\}\):

\(F(2..7) = 4, 17, 88, 540, 3960, 32760\).

Kein OEIS-Treffer. Es gilt \(F(n) = n\cdot n! - D(n)\).
Eine Formel für \(D(n)\) liefert also auch \(F(n)\).

## V6. Obere Schranke für \(\beta\) — offen

\(\beta(r,s)\le\sigma\)-Wert des Produkts der Maximalpolynome ist per
Konstruktion exakt; gesucht ist eine handliche Schranke der Form
\(\beta(r,s)\le c\cdot\max(r,s)\cdot\min(r,s)!\) oder ähnlich. Der
konstante Koeffizient des Produkts liefert bereits die untere Schranke
\(\beta(r,r)\ge\sum_{j=0}^{r-1}(r-j)^2 j!\).

## V9. Seitentreue — gestützt, **neuer Starrheitskandidat** (13.07.2026)

Jede gesetzestreue gekoppelte Arithmetik auf \(\mathcal H\) ist
seitenrein: Addition und Multiplikation operieren beide auf der
Wertseite oder beide auf der Strukturseite; eine Verwebung beider
Identitäten ist unmöglich.

Evidenz: 16er-Sweep (`experiments_v4strich.py`) — genau zwei
Überlebende (A.3 und C.2), alle acht gemischten Kombinationen
scheitern an der Distributivität. Beweisidee: Distributivität zwingt
das Additions-Payload, mit dem Multiplikations-Payload zu „rechnen";
Wertsummen und Struktursummen unterscheiden sich genau um die
Überträge, und die Multiplikationen der beiden Seiten behandeln
Überträge unverträglich.

### Nachtrag zu V9 (13.07.2026, fünfte Sitzung)

Die **erste Stufe ist bewiesen** (Satz S17/D.1): Innerhalb der
natürlichen 16er-Familie sind genau A.3 und C.2 gesetzestreu. Die
volle Fassung (beliebige Selektoren) ist auf das diophantische
Kernproblem **V9′** reduziert (Anhang D.2): Existiert
\(\tau\ge\sigma\) auf \(\mathcal S\), sodass
\(\varphi(Q)=Q(\tau(Q)+1)\) alle Distributivitäts-Funktional-
gleichungen \(\varphi(R\,Q_m)=m\,\varphi(R)\) simultan erfüllt?
Bekannt: \(Q_m\) nicht konstant (bewiesen), Auswertung über
Heimathorizont unmöglich (bewiesen), Pell-Lösbarkeit einzelner
Zweige, Teilerfenster-Obstruktion für lineare Konstruktionen.

### Abschluss V9 (13.07.2026, sechste Sitzung)

**V9 ist bewiesen** (Satz S18, Anhang E) — für beliebige Selektoren,
nicht nur die natürliche Familie. Fall A (⊕ wert, ⊗ struktur)
scheitert an der Distributivität allein; Fall B (⊕ struktur, ⊗ wert)
an Distributivität plus Kommutativität. Beweiswaffe: konstante
Multiplikatoren treiben die Auswertungspunkte ins Unendliche
(σ(c·Q) ≥ c) und erzwingen konstante Kettenstrukturen; Konstanten
sterben dann an σ(mX) = m+1. **V9′ ist damit negativ beantwortet:**
kein verwebendes τ existiert — die Pell-Lösbarkeit einzelner Zweige
war eine Fata Morgana, die Teilerfenster-Obstruktion der wahre Kern.
Quelle der Starrheit: die Ziffernschranke aus Definition 1.1
(Bemerkung E.3).

### Nachträge 13.07.2026, achte Sitzung (GPT-Paket)

- **V1⁗ teilentschieden:** Die Asymptotik der Sprungstellen
  \(m_g/(g+2)!\to1\) ist jetzt **Satz S22** (Anhang F.3), mit
  empirischer Schärfe \(m_g\approx(g+2)!/c_g\) auf \(\pm1\) und
  stehender Vorhersage \(m_7\approx294875\). Konjektural bleibt nur
  die Gleichheit \(\min\delta_{\mathrm{hor}}=-g(m)\).
- **V3 neu aufgestellt:** Dank Schalensprung-Lemma (Satz S19) ist
  \(D(n)\) jetzt ein Schwellenproblem einer expliziten erzeugenden
  Funktion — Angriff über Grenzverteilung der Ziffernsumme
  (Sattelpunkt) möglich.
- **V11 (neu):** \(\Omega(h)\ge0\) — der Interchange-Defekt der
  beiden Wachstumsoperationen ist einseitig. Exhaustiv bis \(H_7\);
  zwei neue OEIS-unbekannte Folgen (Maxima und Nullzähler,
  Anhang F.4).
- **V10 (neu, Randfrage):** nichtkommutativer Mischfall B.

### V3-Reduktion (13.07.2026, Loop-Iteration 4)

**Satz S23** liefert die exakte Ziffernformel
\(N(n)=\sum_{p\le P}\min(d_p,p)\,n!/p!\) über die Eigen-Darstellung
von \(n!\) in \(H_n\) (verifiziert \(n=3..10\)). V3 ist damit
reduziert auf: **Wie sehen die Ziffern von \(n!\) im Horizont \(n\)
aus?** (Verteilung, Anzahl führender Nullen, Position der ersten
Maximalziffer P). Das n!/2-Phänomen ist aufgelöst (Ein-Ziffern-
Darstellungen von 120 und 5040).

## V12. Dreiseitige Seitentreue — offen (13.07.2026, aus dem externen Review)

Die dritte Identität (Fakultätsbruch F, Satz S28) trägt eigene
Payloads: Brüche addieren, Brüche multiplizieren (Produkte endlicher
Fakultätsbrüche bleiben endlich, da Nenner Fakultäten teilen).
Fragen: (a) Gibt es bruchgetragene gesetzestreue Arithmetiken mit
geeigneten Selektoren? (b) Erweitert sich der Seitentreue-Satz S18
auf alle drei Seiten — ist jede Mischung unter Wert-, Gestalt- und
Bruch-Payloads unmöglich? Die Beweiswaffen aus Anhang E (konstante
Multiplikatoren, σ-Wachstum) haben Bruch-Analoga: F-konstante
Elemente sind die Ein-Ziffern-Brüche a/(i+1)!.


### V12-Fortschritt (13.07.2026, Loop-Iteration 9)

**Zwei Drittel bewiesen (Satz S29, Anhang G.4):** (a) Bruch-Addition
ist nie total → keine reine Bruchseite, keine Mischung mit
Bruch-Addition; (b) Wert-⊕ + Bruch-⊗ stirbt am
Fakultätsquotienten-Argument (konstanter Quotient > 1 unmöglich bei
wachsendem Horizont). **Offen:** Struktur-⊕ + Bruch-⊗ — dort führt
die Kette auf die Diophantische Familie A(T+1)/(T+1)! = F_a/(N_m+1)!
mit möglichen polynomialen Identitäts-Lösungen; braucht eigene
Untersuchung (Pell-Warnung beachten).

## V13 — Ist σ eine klassische Permutationsstatistik? (offen, 14.07.2026)

Unter der Bijektion H_n ≅ Inversionsfolgen der Länge n+1 ≅ S_{n+1}
(Satz S44) wird der Strukturhorizont zur Permutationsstatistik
σ(P_a) = n − min_{e_j>0}((j−1)−e_j), e=(0,a). Verteilung exakt:
#{σ=r} = r·r! (exhaustiv bis n=6). **Offen:** Entspricht σ einer
bereits benannten Permutationsstatistik? Die Extremfälle e_j=j−1
sind die "tight entries" der Inversionsfolgen-Literatur
(arXiv:1510.05434); σ misst den minimalen Abstand irgendeiner Ziffer
zum Anschlag. Anschlussfrage an die middle order (arXiv:2405.08943):
Ist σ eine Rang- oder Höhenfunktion in diesem Gitter?
