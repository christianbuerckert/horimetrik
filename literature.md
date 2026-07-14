# Literaturmatrix

| Quelle | Bekannter Baustein | Abgrenzung zur Horimetrik |
|---|---|---|
| Knuth, TAOCP Bd. 2, Abschn. 4.1; Wikipedia "Factorial number system" | Fakultätszahlensystem, Mischbasen, Bijektion auf \([0,n!)\) | Basen dort von der niederwertigen Seite wachsend; kein intrinsischer Horizont, führende Nullen wertneutral |
| Lehmer-Codes / Inversionsvektoren (Standardkombinatorik) | Ziffernbedingung \(0\le a_i\le i\), Bijektion zu Permutationen, \((n+1)!\)-Mächtigkeit | Erklärt die Größe von \(H_n\), aber nicht die horizonabhängige Auswertung \(P(n+1)\) |
| Graham/Knuth/Patashnik, Concrete Mathematics, Kap. 2 | Fallende Fakultäten, \(\Delta X^{\underline d}=dX^{\underline{d-1}}\), Newton-Reihen | Liefert Werkzeug für Strukturpolynome und Satz 9.2; keine Horizontkoordinate, keine Positivitätsbeschränkung \(c_d\le n-d\) |
| Produktformel \(X^{\underline p}X^{\underline q}=\sum_j\binom pj\binom qj j!X^{\underline{p+q-j}}\) (Standard) | Strukturkonstanten des Halbrings \(\mathcal S\) | Bekannt; neu ist nur die Frage nach \(\sigma\)-Wachstum (\(\beta\)) unter der Ziffernschranke |
| Cahen/Chabert, Integer-Valued Polynomials | Binomial-/Newtonbasis ganzzahliger Polynome | Dort Ring über \(\mathbb Z\) bzw. \(\mathbb Q\); Horimetrik nutzt nur den positiven Kegel und bewertet an einem laufenden Punkt |
| Direkte Limites (Standardalgebra) | \(\varinjlim\)-Konstruktion für Satz 6.1/6.2 | Werkzeug, kein Inhalt; die Pointe ist die Nichtvertauschbarkeit der beiden Einbettungsfamilien \(Z\) und \(L\) |
| Tropische Halbringe (max,+) | Kandidatenstruktur für Horizontselektoren | Scheitert am Wertüberlauf der Addition, siehe lab-notes 13.07.2026 und Vermutung V4 |
| OEIS-Abgleich 13.07.2026 | — | \(\beta(r,r)\), \(D(n)\), \(F(n)\) ohne Treffer; Negativbefund, kein Beweis |
| Rigo/Stipulanti, „Revisiting regular sequences in light of rational base numeration systems", arXiv:2103.16966 | Abstrakte Numerationssysteme: führende Nullen ändern über die Radix-Ordnung den Wert | Nächster bekannter Nachbar der Nullen-Semantik; dort formale Sprachen/Automaten, keine Halbringe, keine Dualität, kein Seitentreue-Analogon (Tiefencheck 13.07.2026) |
| Factorial-Arithmetik-Literatur (u.a. MDPI Appl. Sci. 14(19):8588, 2024) | Addition/Subtraktion auf Factoradic-Ziffern | Reine Ziffernalgorithmen im festen System; kein Horizont als Objektbestandteil |
| Mathlib `Polynomial.Pochhammer` | Fallende/steigende Fakultäten formalisiert in Lean 4 | Ansatzpunkt für eine spätere Formalisierung von Satz S18 |
| Peirce-Zerlegung / Ecken idempotenter Elemente (Standard-Ringtheorie) | „Eck"-Sprache für e·R·e | Analogie für K_V = ⊗(1,1); bei uns Halbringe ohne Eins und ZWEI Multiplikationen zum selben Element — kein direktes Vorbild gefunden |
| Kudryavtseva/Mazorchuk, „On Kiselman's semigroup", arXiv:math/0511374; Ganyushkin/Mazorchuk, „On Kiselman quotients of 0-Hecke monoids", arXiv:1006.0316 (Zuordnung korrigiert nach GPT-Review 13.07.) | Monoide aus idempotenten Erzeugern mit Absorptionsrelationen | Nachbarschaft des Kompaktifizierungsmonoids (Satz S21); exakte Identifikation des Typs \(\langle s,v\mid s^2{=}s, v^2{=}v, vsv{=}sv\rangle\) offen |
| D. Simon, „Mixed radix numeration bases: Horner's rule, Yang-Baxter equation and Furstenberg's conjecture", arXiv:2405.19798 | Basiswechsel als lokale euklidische Divisionen; YBE bei drei Wechseln | Kandidatenwerkzeug für den Interchange-Defekt Ω (V11, Anhang F.4) |
| Cantor, Fakultätsbasis für Brüche (Cantor-Reihen) | endliche Brüche Σ aᵢ/(i+1)!, Ziffernschranke 0 ≤ aᵢ ≤ i | Externes Review (13.07.2026) identifizierte V = (n+1)!·F — korrekt (Satz G.1); Cantors Welt ist der R-Limes (bruchtreu, rechts verankert), NICHT der Z-Limes (gestalttreu, links verankert); Dualität/Seitentreue/Tiefengesetz bleiben davon unberührt |

## Zählkomplexität (ergänzt 14.07.2026)

- **Ikenmeyer, Pak: "What is in #P and what is not?"** (FOCS 2022,
  arXiv:2204.13149) — binomial-good-Polynome (nichtneg. ganzzahlige
  Binomialbasis-Koeffizienten) = die relativierenden polynomiellen
  #P-Abschlussoperationen; univariate Richtung bewiesen
  (φ(#P)⊆#P ⟺ α_i∈ℕ); Binomial-Basis-Vermutung, univariate Fassung
  ⟹ P≠NP. **Bezug:** 𝓢 ⊊ binomial-good via b_d=c_d·d!; unser S43
  ist die geordnete Teilklasse mit Elementarbeweis. Was dort NICHT
  steht: die Höhe max(d+c_d), endliche (r+1)!-Hierarchien,
  Wachstumsgesetze.
- **Rook-Theorie** (z. B. arXiv:2312.10855) — fallende Fakultäten
  als Koeffizientenbasis von Rook-Polynomen, Normalordnung in
  Weyl-Algebren. Nachbargebiet für die Brett/Treppen-Geometrie von σ.
