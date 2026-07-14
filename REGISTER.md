# Ergebnisregister der Horimetrik

Zentrale Tafel aller Ergebnisse. Jede Zeile hat eine stabile ID, einen
Status und einen Zielort im Buch. Neue Ergebnisse werden hier
eingetragen, bevor sie irgendwo anders verwendet werden.

Statuscodes: **bewiesen** · **Skizze** (Beweisidee vorhanden, Ausarbeitung
fehlt) · **vermutet** · **widerlegt** · **verworfen** · **offen**

## Definitionen

| ID | Inhalt | Quelle | Buchkapitel |
|---|---|---|---|
| D1 | Horizont \(H_n\), Ziffernbedingung \(0\le a_i\le i\) | Spez. 1.1 | 2 |
| D2 | Wertabbildung \(V_n\), Codierung \(E_n\) | Spez. 1.2/1.4 | 2 |
| D3 | Strukturpolynom \(P_a\) in fallender Fakultätsbasis | Spez. 2.2 | 4 |
| D4 | Strukturhorizont \(\sigma\), vollständiger Horiraum \(\mathcal H=\{(n,P)\mid n\ge\sigma(P)\}\) | Spez. 4.1/4.3 | 4 |
| D5 | strukturtreue Erweiterung \(Z\), werttreuer Lift \(L\) | Spez. 5.1/5.2 | 3 |
| D6 | Kompaktifizierungen \(K_S\), \(K_V\); Minimalhorizont \(\mu\) | Spez. 8.1–8.3 | 5 |
| D7 | Horizontableitung \(\Delta\), Hori-Dimension \(\dim_H\) | Spez. 9.1/9.4 | 4 |
| D8 | Produkthöhenfunktion \(\beta(r,s)\) | Spez. 11.2 | 6 |
| D9 | Defektzählung \(D(n)\), Fixpunktzählung \(F(n)\) | Anhang A.4–A.6 | 6 |
| D10 | Horizontkalkül \(\Gamma_T(r_1,\ldots,r_k)=\max\sigma(T(P_1,\ldots,P_k))\) | Anhang H.0 | 4 |

## Sätze und Lemmata

| ID | Aussage | Status | Quelle | Buchkapitel |
|---|---|---|---|---|
| S1 | \(V_n\) ist Bijektion auf \([0,(n+1)!)\) | bewiesen (13.07.2026) | Spez. 1.3 | 2 |
| S2 | Auswertungssatz \(V_n(a)=P_a(n+1)\) | bewiesen | Spez. 2.3 | 4 |
| S3 | \(\mathcal S\) ist kommutativer Halbring (Produktformel fallender Fakultäten) | bewiesen | Spez. 3.2 | 4 |
| S4 | Darstellbarkeitskriterium \(n\ge\sigma(P)\) | bewiesen | Spez. 4.2 | 4 |
| S5 | Idempotenz \(K_S^2=K_S\), \(K_V^2=K_V\) | bewiesen | Spez. 8.4 | 5 |
| S6 | \(K_SK_V\ne K_VK_S\) (minimal: \(010_{H_3}\)) | bewiesen | Spez. 8.5, G1 | 5 |
| S7 | \(\Delta\)-Kalkül: Wertänderung unter \(Z\) ist \(\Delta P(n+1)\); \(\mathbb N=\ker\Delta\) | bewiesen | Spez. 9.2–9.6 | 4 |
| S8 | Grenzraumsätze: \(\varinjlim Z\cong\mathcal S\), \(\varinjlim L\cong\mathbb N_0\) | bewiesen (13.07.2026) | Spez. 6.1/6.2 | 3 |
| S9 | Additionshöhe: \(\max\sigma(P+Q)=r+s\) | bewiesen | Anhang A.1 | 6 |
| S10 | Fixpunktzählung: je \(n\cdot n!\) für \(K_S\) und \(K_V\) | bewiesen | Anhang A.2 | 5 |
| S11 | Konservativ-kompakter Halbring; \(h\otimes 1=K_V(h)\); \(\mathbb N_0\) als Eck | bewiesen | Anhang A.3 | 5 |
| S12 | Exzess-Koordinaten: \(\mathcal H\cong\mathbb N_0\times\mathbb N_0\) via \((n,x)\mapsto(x,n-\mu(x))\), kanonisch | bewiesen | Anhang B.2 | 5 |
| S13 | Produktprinzip: jede Halbringstruktur auf dem Exzess liefert gesetzestreue Hori-Arithmetik; tropisch \(\to\) Eins ohne absorbierende Null, arithmetisch \(\to\) Eins und absorbierende Null | bewiesen | Anhang B.3/B.4 | 5 |
| S14 | A.3 ist keine Produktstruktur (erste gekoppelte Arithmetik) | bewiesen | Anhang B.5 | 5 |
| S15 | \(\sigma\)-Additionsmonotonie: \(\sigma(P+Q)\ge\max(\sigma P,\sigma Q)\) | bewiesen | Anhang C.1 | 5 |
| S16 | Dualitätssatz: Spiegel-Halbring mit \(h\boxtimes(1,1)=K_S(h)\), \(K_S\) Homomorphismus, Eck \(\cong\mathcal S\); beantwortet V8 positiv | bewiesen | Anhang C.2/C.3 | 5 |
| S17 | **Seitentreue erster Stufe:** In der natürlichen 16er-Familie sind genau A.3 und C.2 gesetzestreu; keine Seitenmischung ist möglich | bewiesen (13.07.2026) | Anhang D.1 | 5 |
| S18 | **Seitentreue-Satz (voll):** keine seitengemischte Arithmetik für BELIEBIGE Selektoren; Fall A stirbt an Distributivität allein, Fall B an Distributivität + Kommutativität; Klassifikation vollständig | bewiesen (13.07.2026) | Anhang E | 5 |
| S19 | Schalensprung-Lemma: \(\sigma(P_a)<n \iff\) keine Ziffer maximal \(\iff a=Z(b)\); \(D(n)\) zählt Schalenspringer; erzeugende Funktion | bewiesen (13.07.2026, GPT-Vorschlag) | Anhang F.1 | 6 |
| S20 | Stabilitätslemma: \(K_S\) erhält Wertkompaktheit; Relation \(VSV=SV\) | bewiesen (13.07.2026, GPT-Vorschlag) | Anhang F.2 | 5 |
| S21 | Kompaktifizierungsmonoid: genau 6 Elemente, 5 Idempotente (\(VS\) nicht!), Hecke–Kiselman-Nachbarschaft | bewiesen (13.07.2026) | Anhang F.2 | 5 |
| S22 | Asymptotiksatz: \(m_g/(g+2)!\to1\) mit expliziten Schranken \((g+2)!/c_g\le m_g+1\le(g+2)!\) | bewiesen (13.07.2026) | Anhang F.3 | 6 |
| S23 | Ziffernformel: \(N(n)=\sum_{p\le P}\min(d_p,p)\,n!/p!\) über die Eigen-Darstellung von \(n!\); löst das \(n!/2\)-Phänomen auf, reduziert V3 auf die Ziffern von \(n!\) | bewiesen (13.07.2026) | Anhang F.6 | 6 |
| S24 | Rekursionsformel \(z_n(x)=r+(n+2)z_{n-1}(q)\) für den Nullerweiterungswert | bewiesen | Anhang F.7a | 8 |
| S25 | \(z_n\) strikt monoton in \(x\) | bewiesen | Anhang F.7b | 8 |
| S26 | Multiplikationslemma: \(z_\ell(cy)\ge(c+1)z_\ell(y)\) für \(c\ge\ell+2\); Regime-Grenze scharf | bewiesen (13.07.2026) | Anhang F.8b | 8 |
| S27 | **Interchange-Positivität** \(\Omega\ge0\) (vormals V11) | bewiesen (13.07.2026) | Anhang F.8c | 8 |
| S28 | Cantor-Koordinate: \(V_n=(n+1)!\,F\); dritte Erweiterung \(R\) (bruchtreu, Wert \(	imes(n+2)\)); \(R\)-Limes = endliche Fakultätsbrüche; drei Identitäten paarweise verschieden | bewiesen (13.07.2026, angestoßen durch externes Review) | Anhang G | 3 |
| S29 | Dreiseitige Seitentreue, Teil 1: kein reiner Bruchhalbring (Bruch-⊕ nie total); Wert-⊕ + Bruch-⊗ unerfüllbar (Fakultätsquotienten-Argument) | bewiesen (13.07.2026) | Anhang G.4 | 8 |
| S30 | **Trilogie-Schlussstein:** Struktur-⊕ + Bruch-⊗ unerfüllbar (Halbkoeffizienten-Obstruktion 2A(Y)=Y^k̲); dreiseitige Seitentreue VOLLSTÄNDIG | bewiesen (13.07.2026) | Anhang G.5 | 5/8 |
| S31 | **V10 geschlossen:** nichtkommutativer Mischfall B unter beidseitiger Distributivität unmöglich (Spiegelkette via Rechts-Distributivität) | bewiesen (13.07.2026) | Anhang E.5 | 5 |
| S32 | Gleichheitsfälle: \(\Omega=0\iff\) Übertragsfreiheit + scharfes Multiplikationslemma; semi-geschlossene Zählformel (exakt n=1..8) | bewiesen (13.07.2026) | Anhang F.9 | 8 |
| S33 | **Tiefengesetz-Gleichheit:** \(\min_{	ext{Schale }m}\delta=-g(m)\); Zeuge = Terminaldarstellung von \(M_{s_{\min}}(m{+}1)\) | bewiesen (13.07.2026) | Anhang F.10 | 6 |
| S34 | β-Reduktionssatz: \(\lneta(r,r)=\ln\max_tinom{r-1}{t}^2(r{-}1{-}t)!+O(\log r)\) | bewiesen (13.07.2026) | Anhang F.11 | 6 |
| S35 | Ziffernentfaltung der Scharfheit: tight-Rekursion mit \(er\le\ell\) + Übertragsfreiheit pro Ebene; O(n)-Ziffernkriterium für \(\Omega=0\) | bewiesen (13.07.2026) | Anhang F.9c | 8 |
| S36 | **β-Asymptotik:** \(\ln(eta(r,r)/r!)=2\sqrt r+O(\log r)\) — elementar (Konkavitätsschranke + Ein-Variablen-Minimum) | bewiesen (13.07.2026) | Anhang F.12 | 6 |
| S37 | Ein-Ziffern-Fakultäten vollständig: \(n=(i{+}1)!/d-1\), \(1\le d\le i\); genau \(i\) pro Position; achte OEIS-unbekannte Folge | bewiesen (13.07.2026) | Anhang F.13 | 8 |
| S38 | Nullzähler-Schranke: \(\#\{\Omega{=}0\}\le(n{+}1)^{n+1}/n!\); Gleichgültigkeit fällt wie \(e^{-(1+o(1))n\ln n}\) | bewiesen (13.07.2026) | Anhang F.14 | 8 |
| S39 | **Extremalprinzip:** für koeffizientenmonotone Operatoren gilt \(\Gamma_T(r_1,\ldots,r_k)=\sigma(T(M_{r_1},\ldots,M_{r_k}))\); verallgemeinert das \(\beta\)-Reduktionsargument | bewiesen (14.07.2026, GPT-Vorschlag) | Anhang H.1 | 4 |
| S40 | **Differenzüberlauf:** \(\Gamma_\Delta(r)=\lfloor(r{+}1)^2/4\rfloor-1\) für \(r\ge2\); \(\Delta\) senkt den Grad, erhöht die Kapazität quadratisch | bewiesen (14.07.2026, exhaustiv bestätigt bis \(r=8\)) | Anhang H.2 | 4 |
| S41 | **Kompositionsabschluss:** \(\mathcal S\) ist unter \(\circ\) abgeschlossen (Positivität + Ganzzahligkeit via freier \(S_m\)-Wirkung); \(\circ\) beidseitig koeffizientenmonoton, also \(\Gamma_\circ(r,s)=\sigma(M_r\circ M_s)\); Diagonale \(1,4,23,6541,\ldots\) = neunte OEIS-unbekannte Folge | bewiesen (14.07.2026, exhaustiv bestätigt \(r,s\le4\)) | Anhang H.5 | 4 |
| S42 | **Shift-Überlauf:** \(\Gamma_E(r)=r+\lfloor r^2/4\rfloor=\Gamma_\Delta(r{+}1)\) — Verschieben kostet wie Ableiten einen Horizont höher | bewiesen (14.07.2026) | Anhang H.6 | 4 |
| S43 | **Hori-#P-Satz:** \(P\circ f\in\#P\) für \(f\in\#P\), \(P\in\mathcal S\) (elementarer Zeugen-Tupel-Beweis; folgt auch aus binomial-good, Ikenmeyer–Pak FOCS 2022); \(\mathcal S\subsetneq\) binomial-good via \(d!\mid b_d\) = geordnet statt ungeordnet; σ = **Zählbreite**, \(\mathcal C_r\) = endliche \#P-Operator-Hierarchie der Größe \((r{+}1)!\) | bewiesen (14.07.2026, GPT-Einordnung) | Anhang I | 4 |
| S44 | **Inversionsfolgen-Einordnung:** \(H_n\cong\) Inversionsfolgen der Länge \(n{+}1\cong S_{n+1}\); \(\sigma(P_a)=n-\min_{e_j>0}((j{-}1)-e_j)\) als Permutationsstatistik; Niveauzählung \(\#\{\sigma=r\}=r\cdot r!\); \(\mathcal F_r\) = Hauptideal unter \(M_r\) im distributiven Gitter (middle order) | bewiesen (14.07.2026, exhaustiv bis \(n=6\)) | Anhang J | 9 |

## Vermutungen

Details in `conjectures.md`.

| ID | Aussage | Status |
|---|---|---|
| V1 | \(\delta_{\mathrm{hor}}\in\{-1,0,+1\}\) | **widerlegt** (G7: \((9,720)\)) |
| V1′ | \(\delta_{\mathrm{hor}}\ge-1\) | **widerlegt** (G9: \(-2\) ab Schale 15, \(-3\) ab \(\approx100\)) |
| V1″ | \(\delta_{\mathrm{hor}}\) nach oben unbeschränkt | vermutet (\(+2/+3/+4\) ab \(n=9/14/20\)) |
| V1⁗ | Tiefengesetz: \(\min_{\text{Schale }m}\delta=-g(m)\), Schalenlücke \(g(m)\to\infty\) invers-fakultätisch langsam | vermutet, bestätigt bis \(m=200\) |
| V2 | Formel/Asymptotik für \(\beta(r,r)\) | offen |
| V3 | kombinatorische Beschreibung von \(D(n)\) | **im Kern gelöst** (S23); Ein-Ziffern-Fälle vollständig (S37); Rest: allgemeine Ziffernstatistik von \(n!\) |
| V4 | Starrheit: strenge Gesetze erzwingen \(\rho_\times=\mu\) | **widerlegt** (G8: Exzess-Halbringe) |
| V4′ | Klassifikation der gekoppelten (Nicht-Produkt-)Arithmetiken | offen, **Leitfrage** |
| V5 | Formel für \(F(n)\) (folgt aus V3) | offen |
| V6 | handliche obere Schranke für \(\beta\) | offen |
| V8 | Existiert eine Arithmetik, für die \(K_S\) Homomorphismus ist? | **beantwortet: ja** (Satz S16, Dualitätssatz) |
| V9 | Seitentreue: gesetzestreue Arithmetiken mischen Wert- und Strukturseite nie | **BEWIESEN** als Satz S18 (Anhang E); V9′ negativ beantwortet |
| V10 | Nichtkommutativer Mischfall B | **beantwortet: NEIN** unter Halbring-Axiomen (Satz S31); nur einseitig-distributive Kuriosität außerhalb der Axiomatik denkbar |
| V11 | Interchange-Defekt: \(\Omega(h)\ge0\) | **BEWIESEN** als Satz S27 (Anhang F.8) |
| V12 | Dreiseitige Seitentreue (Wert/Gestalt/Bruch) | **BEWIESEN** (S29 + S30, Anhang G.4/G.5) — die Seitentreue ist eine Trilogie |
| V13 | Entspricht \(\sigma\) unter der Inversionsfolgen-Bijektion einer klassischen Permutationsstatistik? | offen (S44 gibt Formel + Verteilung \(r\cdot r!\), aber keine Identifikation) |

## Gegenbeispiele

Details in `counterexamples.md`: G1–G6.

## Verworfene Richtungen

Details in `verworfen.md`: X1–X9. Verworfen heißt begründet beiseitegelegt,
nicht vergessen — Kandidaten für das Buchkapitel „Sackgassen".
