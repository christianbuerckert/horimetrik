# Gegenbeispiele

Jedes Gegenbeispiel ist mit `horimetrik_reference.py` beziehungsweise den
Experimentskripten reproduzierbar.

## G1. Kompaktifizierungen kommutieren nicht (13.07.2026)

Kleinstes Beispiel im gesamten Horiraum: \(h = 010_{H_3}\), Wert 4.

- \(K_S K_V(h) = 11_{H_2}\), Wert 4
- \(K_V K_S(h) = 10_{H_2}\), Wert 3

Es gibt kein Gegenbeispiel unterhalb von \(H_3\) (vollständige Enumeration).

## G2. Wertkompakt impliziert nicht strukturkompakt (13.07.2026)

\(012_{H_3}\), Wert 6: wertkompakt wegen \(\mu(6)=3\), aber das
Strukturpolynom \(X+2\) hat \(\sigma=2\). Damit ist auch
\(K_S K_V = K_V\) als allgemeine Gleichung falsch.

## G3. Die Defektzählung ist nicht \(n!/2\) (13.07.2026)

\(D(n)=\#\{x\in[n!,(n+1)!) : \sigma(E_n(x))<n\}\) stimmt für
\(n=5,6,7\) mit \(n!/2\) überein (60, 360, 2520), bricht aber bei
\(n=8\): \(D(8)=21168\ne20160=8!/2\). Muster aus drei Datenpunkten,
zufällige Koinzidenz. Lehrstück für die Arbeitsregel 16.

## G4. Konservative Multiplikation ist nicht assoziativ (13.07.2026)

\(\rho_\times=\max(n,m,\mu(xy))\), Wertkoordinaten:

\[
((0,0)\otimes(2,2))\otimes(2,3)=(2,0)
\ne
(0,0)\otimes((2,2)\otimes(2,3))=(3,0).
\]

Beide Seiten haben den Wert 0, aber verschiedene Horizonte. Ursache ist
die Null, die den Wert löscht, während der Horizont die Rechengeschichte
behält.

## G5. Distributivität scheitert für fast alle Selektorpaare (13.07.2026)

Vollständige Enumeration bis \(H_3\): Von den neun getesteten Paaren aus
\(\{\text{kompakt},\text{konservativ},\text{additiv}\}^2\) sind nur

- \(\oplus_{\text{kompakt}}\) mit \(\otimes_{\text{kompakt}}\) (kollabiert zu \(\mathbb N_0\)) und
- \(\oplus_{\text{konservativ}}\) mit \(\otimes_{\text{kompakt}}\) (Satz A.3)

streng distributiv. Beispiel-Gegenbeispiel für
\(\oplus_{\text{konservativ}}\) mit \(\otimes_{\text{konservativ}}\):
\(a=(0,0)\), \(b=c=(1,1)\).

## G6. Kein multiplikativ neutrales Element im Halbring aus Satz A.3

\((1,0)\otimes(1,1)=(0,0)\ne(1,0)\). Allgemein gilt
\(h\otimes(1,1)=K_V(h)\); die Eins des kompakten Ecks wirkt auf dem
Gesamtraum als Projektor, nicht als Einheit.

## G7. V1 widerlegt: der Kommutator ist nach oben unbeschränkt (13.07.2026)

Kleinstes Beispiel mit \(|\delta_{\mathrm{hor}}|\ge2\), vollständige
Suche bis \(H_9\): \(h=(9,720)\), also \(720=6!=10\cdot9\cdot8\) im
Horizont 9 mit Strukturpolynom \(X^{\underline 3}\).

- \(K_VK_S\)-Weg: \(\sigma(X^{\underline3})=4\), Wert dort
  \(5\cdot4\cdot3=60\), \(\mu(60)=4\) → Horizont 4.
- \(K_SK_V\)-Weg: \(\mu(720)=6\), \(\sigma(E_6(720))=6\) → Horizont 6.

\(\delta_{\mathrm{hor}}=+2\). Stichproben zeigen \(+3\) ab \(n=14\),
\(+4\) ab \(n=20\); nie unter \(-1\). Siehe V1′/V1″ und Anhang B.7.

## G8. V4 widerlegt: nicht-kompakte gesetzestreue Multiplikationen (13.07.2026)

Der tropische und der arithmetische Exzess-Halbring (Satz B.3/B.4)
erfüllen alle strengen Gesetze mit
\(\rho_\times=\mu(xy)+\varepsilon_a+\varepsilon_b\) beziehungsweise
\(\rho_\times=\mu(xy)+\varepsilon_a\varepsilon_b\). Beide besitzen eine
Eins; der arithmetische zusätzlich eine absorbierende Null. Verifiziert
durch vollständige Tripel-Enumeration bis \(H_4\)
(`experiments_v4.py`). Die frühere Suchfamilie (G5) war schlicht zu
klein.

## G9. V1′ widerlegt: der Kommutator ist auch nach unten unbeschränkt (13.07.2026)

Zufallsstichproben fanden nie \(\delta<-1\) — die Zeugen sind extrem
selten und mussten konstruiert werden: Werte \(x\in[m!,(m+1)!)\) mit
kleinem Strukturhorizont (Maximalpolynom-Familie), eingebettet in
\(n>m\). Erster Zeuge: \(x=1{.}327{.}252{.}697{.}724\) (Schale 15) in
\(H_{16}\), \(\delta_{\mathrm{hor}}=-2\). Ab Schale \(\approx100\)
erreicht dieselbe Konstruktion \(-3\); die Tiefe folgt exakt der
Schalenlücke \(g(m)\) (Anhang C.4, Vermutung V1⁗). Methodische Lehre:
zweimal hintereinander fiel eine Schranken-Vermutung, weil der
Testbereich zu klein war — Schranken im Horiraum immer gegen
konstruierte Extremfälle prüfen, nie nur gegen Stichproben.
