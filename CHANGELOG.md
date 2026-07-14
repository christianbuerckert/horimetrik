# Changelog

## 0.27, 14. Juli 2026, VERÖFFENTLICHUNG — GitHub-Repo, OEIS einreichfertig, englische Ausgabe

- **Repo öffentlich** (github.com/christianbuerckert/horimetrik):
  Buch als Hauptelement, README mit Buchbeschreibung, Lizenzen
  (Text CC BY 4.0, Programme MIT, Vermerk auf der Titelseite),
  .gitignore; Verzeichnis kuratiert (programme/, daten/;
  TODO.md und LOCAL_AGENT_BRIEF.md entfernt; Vorname der Tochter
  aus allen öffentlichen Texten entfernt — jetzt „meine Tochter")
- **Englische Ausgabe `book/` komplett** (51 Seiten, „Horimetrik —
  Numbers with a Horizon"): alle 15 Kapitel übersetzt; verbindliches
  Glossar (book/GLOSSARY.md, OEIS-Begriffe kanonisch:
  shape, shell, depth law, side fidelity, law-abiding …);
  Titelseiten-Vermerk „German original is authoritative";
  Beweisanhang mit mechanisch verifizierter Formel-Identität
  (665 Mathe-Segmente checksummengleich); gleiche
  Umgebungsnamen wie das Original → Quellen 1:1 vergleichbar
- **OEIS einreichfertig:** ENTWUERFE.md feldgenau nach Formular
  (NAME/DATA/OFFSET/…/KEYWORD, EXAMPLE-Felder mit verifizierten
  Kleinbeispielen); zusätzlich oeis/internal/folge1–9.txt im
  internal format (%-Zeilen, gegen eishelp1.html geprüft,
  Generator programme/experiments_oeis_internal.py); Horimetrik-
  Namen als COMMENTS-Erstzeile (NAME bleibt Definition, OEIS-
  Konvention); LINKS: deutsches PDF, englisches PDF, Repo;
  Einreichstrategie: max. 3 Drafts — zuerst Folge 1 + 3 + 7
- Fachtext nachgezogen (Ein-Ziffern-Anfangsterm 1, „implizieren
  würde", Zeugen-Präzisierung, Überstände beseitigt); Fassung 0.16
  zweisprachig (main.tex / main-en.tex, Mathe-Segmente mechanisch
  identisch verifiziert)
- **Preprint `paper/`** (12 Seiten, englisch, pdflatex-kompatibel):
  Fachtext-Hauptteil plus Tiefengesetz als Satz im Text und
  Appendix A–F mit allen restlichen Beweisen; Autorzeile Christian,
  KI-Mitarbeit in den Acknowledgements; für Peer-Review und ggf.
  spätere arXiv-Einreichung (math.CO/math.RA)

## 0.26, 14. Juli 2026, SIEBEN-PRÜFER-RUNDE — jedes Kapitel adversarial gegengelesen, Beweisanhang vervollständigt

Sieben unabhängige Prüfdurchgänge (je Kapitelgruppe, ein reiner
Beweis-Referee, ein globaler Quervergleich), alle Zahlen unabhängig
nachgerechnet, OEIS und alle arXiv-Referenzen live verifiziert.
Ergebnis: kein einziger Rechen- oder Zahlenfehler; ~30 Befunde zu
Beweisbuchführung, Begriffseinführung und Verweisrichtungen — alle
behoben. Buch kompiliert warnungsfrei (51 Seiten).

- **Tiefengesetz-Beweis (S33) in den Anhang übernommen** (aus Spez.
  F.10): Schranke + Annahme-Teil; zuvor stand der Satz als
  „bewiesen" im Buch, der Beweis aber nur in der Arbeitsdatei
- **Ω endlich definiert** (Interchange-Defekt, in Kap. 6 und Anhang
  B); neuer Satz „Gleichheitsfälle" (S32) mit Einzeiler-Beweis;
  Ziffernentfaltung und Nullzähler-Schranke in den
  Interchange-Abschnitt verschoben (benutzten z_ℓ vor dessen
  Definition); scharfer Quotient definiert, r'≤n begründet,
  „fällt also wie" → „mindestens wie"
- **Falsifizierbare Behauptungen korrigiert:** „der Zeuge ist
  stets…" → „ein Zeuge" (Schale 4 hat 52 Zeugen, kleinster (5,25));
  kleinster Monoid-Gegenzeuge wohnt in Welt **5** ((5,25)), nicht 6
  — (6,6) ist nur wert-kleinster; n!/2-Rehabilitierung erklärt
  jetzt alle drei Terme (720 hat KEINE Ein-Ziffern-Darstellung,
  dort kappt die Maximalziffer die Formel nach einem Summanden)
- **Interludiums-Verweiskette repariert** (i2 war hinter Kap. 4
  gewandert): Kap. 2 „nächstes Interludium"→„eigenes", Kap. 2
  „übernächstes Kapitel"→„nächstes", Kap. 3 „folgendes
  Interludium"→namentlich, i2 „übernächstes"→„nächstes Kapitel"
- **Begriffe vor Gebrauch:** Terminaldarstellung (jetzt in Kap. 3
  definiert), K_V/K_S inline bei Erstauftreten, Horiraum-Trägermenge
  im Satz, Kompaktifizierungsmonoid benannt, „gestalttreu=
  strukturtreu" erklärt, wertgetragen/strukturgetragen glossiert,
  Symbolkollisionen aufgelöst (Exzess-Ops jetzt ⊎/⊙; Beispiel-
  Klausel bei ⊕/⊗), „streng gesetzestreu"→„gesetzestreu",
  Produkthöhe statt „Strukturhöhe"
- **Randfälle:** v₀=0 in D2; „ganzzahlig" in S8; Zulässigkeit nur
  an besetzten Stellen; dim-Additivität P,Q≠0; r·r! nur für
  1≤r≤n; σ-Formel nur für a≠0; Kette ab M₀; (0,0) im
  Stabilitätsbeweis; Induktionsbasis Monotonie-Lemma; i≤n bei
  Ein-Ziffern; Γ_T-Stelligkeit; T_m/t_g/h_m/w sauber eingeführt
- **Zählungen:** 3 (nicht 4) widerlegte Vermutungen; „4
  Vorhersage-Gruppen (12 Einzeltreffer)"; Sackgassen-Bilanz an
  X1–X9 verankert (eine→Satz: tropisch; eine→Fußnote: n!/2);
  Anhang-A-Tabelle mit Indexangaben; REGISTER X1–X8→X1–X9
- **Literatur:** Ikenmeyer–Pak-Annotation um „relativierend"
  präzisiert (sonst würde deren offene Vermutung als Satz
  behauptet); Savage–Schuster (lecture hall) und Chern–Fu–Lin
  (tight entries) als Belege für Kap. 9 ergänzt
- Anhang B jetzt wirklich „nach Kapiteln geordnet" (Kap.-9-Beweis
  ans Ende verschoben); Seitentreue-Anhangssatz ehrlich als
  „Wert-Gestalt-Fälle" etikettiert

## 0.25, 14. Juli 2026, REDAKTIONSRUNDE — externes Gegenlesen eingearbeitet, Buch konsolidiert

Ein externes Gegenlesen aller 52 Seiten fand keine Rechenfehler im
Kern, aber acht echte Übergangs- und Definitionslücken (v. a. dort,
wo neue Ergebnisse in älteren Text eingebaut wurden). Alle Punkte
behoben; das Buch kompiliert warnungsfrei und ist durch den
kompakteren Literaturteil zwei Seiten kürzer (50 statt 52).

- **Schalen ≠ Horizonte (Kap. 2):** Schalen jetzt eigene Notation
  \(S_n=\{x:\mu(x)=n\}\) mit \(S_0=\{0\}\), \(S_1=\{1\}\); Tabelle
  umgestellt, „untere Grenze \(n!\)" auf \(n\ge1\) eingeschränkt.
  Behebt den Widerspruch \(\mu(0)=0\) vs. Tabellenzeile „\(H_1\): 0
  bis 1" und trennt Raum von Neuland
- **Neue Sektion 5.5 „Aufräumen: der Kommutator und das
  Tiefengesetz":** \(K_V,K_S\) erstmals formal im Buch definiert
  (Register D6), Kommutator \(\delta\), Schalenlücke \(g(m)\),
  Tiefengesetz-Gleichheit als Satz (S33), Sprungstellen,
  beidseitige Fixpunkte, Monoid-Hinweis (S21), Hausgeist-Beispiel
  \((6,6)\) durchgerechnet. Damit ist Zählfolge 1 aus dem Buch
  allein rekonstruierbar (zuvor bemängelt)
- **Kap. 5 begradigt:** Halbring-/Gesetzestreu-Konvention jetzt vor
  Satz 5.2 (ohne Pflicht zu Eins und schluckender Null — nötig für
  die tropische Exzessstruktur); Übergang zur Drei-Arithmetiken-
  Tabelle stellt klar, dass der vergessende Halbring KEINE
  Produktkonstruktion ist; „verstärkende Multiplikation vergisst
  nichts" korrigiert (Exzess 0 absorbiert); „genau zwei
  gesetzestreu" ausdrücklich auf die 16er-Familie eingeschränkt
- **\(\sigma(0)=0\)** als Konvention in Definition (Kap. 4) und
  Anhang-B-Präambel verankert
- **Kap. 6 entstaubt:** „siebte Folge"/„die einzige mit bewiesener
  Formel" (veralteter Arbeitsstand) ersetzt; Verweise auf die neue
  Sektion 5.5 ergänzt; Ein-Ziffern-Daten um den trivialen
  Anfangsterm \(n=1\) ergänzt (eigene Charakterisierung, i=1) und
  „fünf" → „neun" Vorhersagen angeglichen
- Registerstand in Anhang A: 38 → **44 bewiesene Sätze** (Register
  ausgezählt), 9 Sackgassen, 9 Zählfolgen
- Einzelkorrekturen: „siebenhundert-zwanzig" (harter Trennstrich),
  „implizierte" → „implizieren würde" (Ikenmeyer–Pak), Cantor „gut
  anderthalb Jahrhunderte", „bunte" → „willkürlich gemischte" Basen
- Layout: `emptypage` (Leerseiten wirklich leer), `parskip` (kein
  Absatzeinzug), Kolumnentitel für Vorwort/Interludien/Literatur
  (\markboth), thebibliography-Doppelüberschrift unterdrückt
- Außerdem heute (vor dem Gegenlesen): Vorwort mit
  Entstehungsgeschichte neu erzählt; X9 wieder eingebaut; OEIS-
  Entwürfe auf neun Folgen erweitert und b-Files verifiziert
  generiert (`programme/experiments_oeis_bfiles.py`); Verzeichnis
  für GitHub aufgeräumt (README, .gitignore, programme/, daten/)

## 0.24, 14. Juli 2026, EINORDNUNG als Schlussstein — das Buch ist rund (GPT-Landkarte, verifiziert)

- **Satz S44 (Inversionsfolgen-Einordnung):** \(H_n\cong\)
  Inversionsfolgen der Länge \(n{+}1\cong S_{n+1}\); Strukturhorizont
  als Permutationsstatistik \(\sigma(P_a)=n-\min_{e_j>0}((j{-}1)-e_j)\);
  Niveauzählung \(\#\{\sigma=r\}=r\cdot r!\); \(\mathcal F_r\) =
  Hauptideal unter \(M_r\) im distributiven Gitter (middle order).
  Exhaustiv bestätigt bis \(n=6\) (`experiments_einordnung.py`)
- **Neues Schlusskapitel 9 „Einordnung: Wo die Horimetrik wohnt"** —
  die drei Ausgänge (unbekannter Grundraum = verdächtig; bekannte
  vollständige Theorie = Ende; bekannter Grundraum + neue Sätze =
  bester Fall), vier Nachbarschaften: Inversionsfolgen/Permutationen
  (bewiesen), distributive Gitter/middle order, finite
  Operatorrechnung, Forschungsprogramm (s-Inversionsfolgen/Lecture-Hall,
  Rook-Theorie, Spezies). Kapitel 8 zu „Zwischenhalt" umgerahmt
- **V13 neu:** Entspricht σ einer klassischen Permutationsstatistik?
  (offen; tight-entries-Verfeinerung)
- Alle sieben GPT-Literaturtitel per arXiv-API verifiziert (nach den
  drei Fehlern vom 13.07. keine Referenz ungeprüft): Corteel–Martinez–
  Savage–Weselcouch 1510.05434, middle order 2405.08943, umbral
  2407.16348 auf die Literaturseite; s-lecture-hall/Rook/Spezies in
  Anhang J + literature.md
- Spezifikation: neuer Anhang J; Buch: Kapitel 9 + Beweis in Anhang B
  + drei Literatureinträge; Fachtext: Einordnungs-Absatz + m_7 in
  Tabelle nachgezogen; conjectures.md V13
- Beim Kompilieren einen Edit-Kollisionsschaden in a2-beweise
  (S43-Header von S44-Dublette überschrieben) gefunden und repariert
- **Bilanz: 44 Sätze, 9 Folgen, 13 Anhänge (A–J). Das Buch ist
  mathematisch eingeordnet und damit rund** — bereit für Christians
  Leserunde

## 0.23, 14. Juli 2026, die Zählbreite: #P-Interpretation (GPT-Einordnung, verifiziert)

- **Satz S43 (Hori-#P-Satz):** \(P\circ f\in\#P\) für \(f\in\#P\),
  \(P\in\mathcal S\) — elementarer Zeugen-Tupel-Beweis (rate Grad,
  Variante, d verschiedene Zeugen); Zählsemantik numerisch
  gegengeprüft (200 Zufallstests + Δ-Deutung)
- Literatur festgenagelt: **Ikenmeyer–Pak, „What is in #P and what
  is not?", FOCS 2022 (arXiv:2204.13149)** — binomial-good-Polynome
  = #P-Abschlussoperationen (univariate Richtung dort bewiesen);
  \(\mathcal S\subsetneq\) binomial-good via \(b_d=c_d\,d!\)
  (geordnete Tupel statt ungeordneter Auswahlen); Binomial-Basis-
  Vermutung (univariat ⟹ P≠NP) bleibt ausdrücklich unberührt
- **Zählsemantik aller Hori-Operationen:** Addition = disjunkte
  Vereinigung; Multiplikation = Kopplung mit Überlappungsmustern
  (Linearisierungskoeffizienten zählen genau diese); Δ = marginale
  Strukturen eines neuen Zeugen; σ = **Zählbreite**
  (Zeugenanzahl + Variantenanzahl; geometrisch: kleinste Treppe
  über dem Koeffizientenbrett); \(\mathcal F_r\) = endliche
  Familie von (r+1)! #P-Abschlussoperatoren; Horizontkalkül =
  optimales Wachstum der Zählbreite
- Spezifikation: neuer Anhang I; Buch: Sektion 4.5 „Was die
  Gestalten zählen" + Beweis in Anhang B + Ikenmeyer–Pak auf der
  Literaturseite; Fachtext: Sektion „Die Zählbreite"; literature.md
  ergänzt (inkl. Rook-Theorie als Nachbargebiet)
- Ehrlichkeitsbilanz: qualitative Schicht bekannt (unser Beweis nur
  eleganter Spezialfall), quantitative Schicht (Höhe, Hierarchie,
  Wachstumsgesetze) offenbar neu — die bisher stärkste externe
  Einordnung der Theorie

## 0.22, 14. Juli 2026, X9: die Krypto-Sackgasse (Gemini-Vorschlag, GPT-Widerlegung, verifiziert)

- Geminis Δ-Trapdoor-Protokoll (Einwegfunktion aus Differenzüberlauf
  + Seitentreue) nach GPTs Widerlegung geprüft und **bestätigt
  widerlegt**: \(y=P(N)\) ist per fortgesetzter Division mit Rest in
  \(O(m)\) invertierbar (\(c_d\le r-d<N-d\)) — Satz S1 am
  verschobenen Auswertungspunkt; exhaustiv verifiziert
  (`experiments_trapdoor.py`, alle Gestalten r≤6, Shifts k≤5)
- Als **X9** in verworfen.md; neue Sackgasse in Buchkapitel 7
  („Verworfene Anwendungsträume") mit den zwei Präzisierungen:
  Seitentreue verbietet gemischte Halbringe, nicht gemischte
  Algorithmen; Einwegfunktionen brauchen ein Geheimnis, die
  Horimetrik hat keins („Die Fakultätsordnung verwirbelt nicht, sie
  sortiert")
- Restperspektive dokumentiert: σ/Γ als Messinstrument für
  Rauschwachstum in bestehender (Gitter-)Kryptographie
- Geminis Beweis-Review des Buchs zur Kenntnis: keine Strukturfehler
  gefunden (Induktionen, Limites, Widerspruchsarchitektur, Monotonie)

## 0.21, 14. Juli 2026, Kompositionsabschluss + neunte Folge (Auftrag Christians via GPT)

- Auftrag: σ als Kapazitätshöhe untersuchen — Abschlussfunktionen für
  Komposition/Substitution herleiten oder widerlegen; Falsifikation
  statt Bestätigung suchen
- **Satz S41 (Kompositionsabschluss):** \(\mathcal S\) ist unter
  \(\circ\) abgeschlossen — Positivität UND d!-Ganzzahligkeit in einem
  Zug via Schablonen-Interpretation + freier \(S_m\)-Wirkung auf
  ausschöpfenden Injektionstupeln (\(m!\mid N_m\)); \(\circ\)
  beidseitig koeffizientenmonoton ⟹ \(\Gamma_\circ(r,s)=\sigma(M_r\circ M_s)\)
  (Anhang H.5); exhaustiv bestätigt r,s≤4, Zufallstest bis σ=8
  (`experiments_komposition.py`)
- **Satz S42 (Shift-Überlauf):** \(\Gamma_E(r)=r+\lfloor r^2/4\rfloor
  =\Gamma_\Delta(r{+}1)\) — Verschieben kostet wie Ableiten einen
  Horizont höher (Anhang H.6)
- **Neunte Zählfolge:** Kompositions-Diagonale
  \(\Gamma_\circ(r,r)=1,4,23,6541,477149751,\ldots\) — OEIS-Negativbefund;
  Entwurf Folge 9 + b-File (10 Terme) in `oeis/`
- Ehrlichkeitsvermerke: \(\Gamma_\Delta\)-/\(\Gamma_E\)-Wertfolgen sind
  die klassische Viertelquadrat-Folge A024206 (Gesetze neu, Folgen
  nicht); stetiges Analogon des Kompositionsabschlusses (absolut
  monotone Funktionen, Faà di Bruno) ist klassisch — S41 ist die
  diskrete Gitterverschärfung; Literatursuche ohne Treffer für die
  Gitterfassung (kein Neuheitsbeweis) (H.7)
- Konsistenz-Kaskade acht→neun: Buch K6-Titel, Steckbrief
  „Kompositions-Explosion", Interludium, Anhang A1-Tabelle,
  Literaturseite, Fachtext (Abstract, Sektion, Tabelle)
- Offener Punkt notiert: Nicht-Springer (Folge 7) hat noch keinen
  eigenen OEIS-Entwurf — Entscheidung vor Einreichung
- Stand: 42 Sätze, 9 Folgen

## 0.20, 14. Juli 2026, das Horizontkalkül (GPT-Anwendungspaket verifiziert)

- GPT-Vorschlagspaket „Horizontkalkül" geprüft: Satz 1 (Additionshöhe)
  und Satz 2 (β-Reduktion auf \(M_rM_s\)) waren bereits Bestand
  (S9/S15 bzw. Def. 11.2); Satz 4 ist die Newton-Umformulierung
  (jetzt Bemerkung H.3). **Echt neu und bewiesen:**
- **Satz S39 (Extremalprinzip):** für koeffizientenmonotone Operatoren
  gilt \(\Gamma_T(r_1,\ldots,r_k)=\sigma(T(M_{r_1},\ldots,M_{r_k}))\) —
  verallgemeinert das β-Reduktionsargument auf beliebige aus
  \(+,\times,\Delta\) zusammengesetzte Operatoren (Anhang H.1)
- **Satz S40 (Differenzüberlauf):**
  \(\Gamma_\Delta(r)=\lfloor(r{+}1)^2/4\rfloor-1\) — Δ senkt den Grad
  und erhöht die Kapazität quadratisch (Anhang H.2); exhaustiv
  bestätigt bis r=8 (`experiments_horizontkalkuel.py`)
- Definition D10 (Horizontkalkül \(\Gamma_T\)); Einordnung als
  „Kapazitätshöhe" auf dem positiven Newton-Halbring (H.3/H.4)
- Spezifikation: neuer Anhang H; Header auf 0.20/14.07. korrigiert
  (stand fälschlich noch auf 0.6)
- Buch: neue Sektion 4.4 „Was Operationen kosten: das Horizontkalkül"
  + Beweise in Anhang B; Oberflächen-Rückkehrpunkt von Kapitel 4
  ergänzt
- Fachtext auf 0.15: Sektion „Das Horizontkalkül", Zählfolgen-Sektion
  von sechs auf acht Folgen nachgezogen (Nicht-Springer,
  Ein-Ziffern-Fakultäten), \(m_7=294875\) als bestätigt vermerkt,
  „Offene Fragen" entstaubt (bewiesene Punkte entfernt, aktuelle
  Fronten eingetragen)
- GPT-Anwendungstriage zur Kenntnis genommen: technische Anwendungen
  (Compiler, DB, KI, Suche) bleiben unbelegt; die mathematische
  Werkzeug-Anwendung (Kapazitätshöhe + Extremalkalkül) ist mit S39/S40
  nun formalisiert

## 0.19, 13. Juli 2026, GPT-Buchreview eingearbeitet — REDAKTIONSSCHLUSS des Tages

- Alle sechs Redaktionspunkte des GPT-Buchreviews umgesetzt:
  (1) „versechsfacht" → „vervielfacht sich nicht unkontrolliert";
  (2) K6-Interludium auf acht Antwortreihen; (3) K1 „beiden zunächst
  sichtbaren Identitäten"; (4) Vorwort-Fußnote zur Gewichtsordnung
  (Exponenten-Titel präzisiert); (5) **Satz 5.8 mit
  Payload-Qualifier** + Transport-Bemerkung (GPTs wichtigster Punkt);
  (6) Halbring-ohne-Eins-Konvention explizit
- **Literaturseite** mit neun annotierten Einträgen (Cantor 1869,
  Knuth, Lehmer, GKP, Cahen–Chabert, Rigo/Stipulanti,
  Kudryavtseva–Mazorchuk + Ganyushkin–Mazorchuk, Simon, OEIS) —
  jeweils mit „was dort NICHT steht"
- **hyperref**: PDF-Lesezeichen, klickbares Inhaltsverzeichnis,
  Metadaten (Titel, Autor, Schlagwörter)
- GPTs Fazit übernommen: keine Ergebnis-Explosion mehr, sondern
  Redaktion — genau das war diese Iteration

## 0.18.2, 13. Juli 2026, Kompilat-Lektüre Teil 2 (Loop-Iteration 22)

- Konsistenz-Sweep über das kompilierte Buch mit drei Treffern:
  Kapitel 6 jetzt „Acht Zählfolgen" (Ein-Ziffern-Fakultäten als
  Steckbrief ergänzt), Kapitel 7 „Kleine-Welt-Falle, sechsmal"
  (Fallen 5+6 vom Tiefengesetz-Abend erzählt), Anhang-Bilanz auf
  8 Folgen
- OEIS-Entwurf Folge 8 (Ein-Ziffern-Fakultäten) + b-File mit 28
  Termen — als einzige Folge mit keyword „easy", weil vollständig
  charakterisiert
- Fachtext braucht keinen Nachtrag (nennt die Folgen nicht einzeln
  über die Tabelle hinaus; Tabelle folgt bei A-Nummern-Vergabe)

## 0.18.1, 13. Juli 2026, Buch-Qualitätsdurchgang (Loop-Iteration 21)

- Kapitel 5 im kompilierten Zustand gegengelesen: drei Nähte
  geschlossen — Abschnitt 5.4 und Schluss-Interludium sprechen jetzt
  konsistent von drei Identitäten (statt zwei, Stand vor der
  dritten Treppe); Interludium endet präzisiert: „zwei Rechenwelten,
  die dritte trägt keine"
- Typografie: alle englischen Anführungszeichen (``…'') auf
  deutsche („…") normalisiert — inkl. Reparatur eines dabei selbst
  verursachten Schadens an der alten ,,…``-Konvention (7 Dateien);
  visuell verifiziert
- Buch kompiliert, 38 Seiten

## 0.18, 13. Juli 2026, Nullzähler-Schranke (Satz S38)

- **Satz S38** (Anhang F.14): #{Ω=0} ≤ (n+1)^{n+1}/n! — die
  Scharfheit würgt die Ziffern ebenenweise ab (untere Ebenen: Ziffer
  null erzwungen); Anteil fällt wie e^{−(1+o(1))·n·ln n}
- Daten treffen die Größenordnung (ln Count ≈ 0,8n vs Schranke
  n + O(log n)); untere Schranke ehrlich offen
- alle drei Dokumente synchronisiert (38 Sätze)

## 0.17, 13. Juli 2026, Ein-Ziffern-Fakultäten vollständig (Satz S37)

- **Satz S37** (Anhang F.13): n! ist Einzelziffer in H_n ⟺
  n = (i+1)!/d − 1 mit 1 ≤ d ≤ i; genau i Fälle pro Position;
  Beweis über Exaktheit + Eindeutigkeit der Entwicklung
- Vorhersagen Nr. 5–9 (n = 143, 179, 239, 359, 719) alle exakt
  bestätigt; Formel = direkte Enumeration bis 150
- ACHTE OEIS-unbekannte Folge: 2, 5, 7, 11, 23, 29, 39, 59, 119,
  143, … — die erste mit geschlossener Beschreibung ab Entdeckung
- alle drei Dokumente synchronisiert (37 Sätze)

## 0.16, 13. Juli 2026, β-ASYMPTOTIK BEWIESEN (Satz S36)

- **Satz S36** (Anhang F.12): ln(β(r,r)/r!) = 2√r + O(log r),
  vollständig elementar — obere Schranke via Konkavität +
  Ein-Variablen-Minimum φ(√s) = −2√s (Kernungleichung numerisch mit
  Abstand ~½ bestätigt bis s=10⁴), untere via t = ⌈√s⌉
- V2 damit im O(log r)-Fenster entschieden; vermutete Feinstruktur
  −(3/2)ln r + O(1) als Restfrage notiert
- alle drei Dokumente synchronisiert (36 Sätze)

## 0.15, 13. Juli 2026, Ziffernentfaltung bewiesen (Satz S35)

- **Satz S35** (Anhang F.9c): vollständige rekursive
  Ziffernentfaltung der Scharfheit — pro Ebene e·r ≤ ℓ plus
  Übertragsfreiheit (cq mod ℓ) + r ≤ ℓ−1, Exzess e wächst um 1;
  exhaustiv verifiziert ℓ ≤ 7. Der fehlerhafte Erstversuch aus
  Iteration 12 ist ersetzt; O(n)-Ziffernkriterium für Ω = 0
- Buch (K8, Anhang B, a1: 35 Sätze) und Fachtext synchronisiert
  (Prozessregel eingehalten)

## 0.14, 13. Juli 2026, β-Reduktionssatz (S34) + robuste obere Schwellen

- **Satz S34** (Anhang F.11): ln β(r,r) = ln max_t C(r−1,t)²(r−1−t)!
  + O(log r) — die β-Asymptotik ist auf ein explizites Maximum
  reduziert (Einzelterm-Dominanz, numerisch Faktor < 4 bis r=40)
- **Vermutung V2′** mit Beweisskizze: ln(β/r!) ~ 2√r; Messwerte bis
  r=100 steigen konsistent (0,92 → 1,12) gegen die Vergleichskurve
- obere Tiefengesetz-Schwellen: 14 und 20 robust unter σ≤9-Vertiefung,
  +5 spätestens 26; Stand: 9 (exhaustiv), ≤14, ≤20, ≤26
- Buch (K6, Anhang B, a1: 34 Sätze) nachgezogen

## 0.13.1, 13. Juli 2026, ehrliche Korrektur der oberen Schwellen

- Tiefensweep (σ≤9): **+5 existiert schon bei n=26** — die „30" des
  flachen Sweeps war ein Artefakt; nur die +2-Schwelle (n=9) ist
  exhaustiv gesichert, alle späteren sind bloße OBERE Schranken
- Buch K8 und Fachtext entsprechend umformuliert („spätestens ab");
  die Dreieckszahlen-Hypothese und die 30 beide als Muster-Fallen
  Nr. 6a/6b im Laborjournal dokumentiert
- Erweiterter Sweep (σ≤9, n=10..25) läuft zur Schärfung der
  Schranken

## 0.13, 13. Juli 2026, TIEFENGESETZ-GLEICHHEIT BEWIESEN (Satz S33)

- **Satz S33** (Anhang F.10): min über Schale m von δ_hor = −g(m),
  exakt. Beweis zweizeilig elegant: Schranke aus
  Koeffizientendominanz (σ ≥ s_min) + Auswertungsmonotonie (μ ≤ m);
  Annahme durch die Terminaldarstellung des Maximalpolynom-Wertes
  (Zeugen 6, 33, 202, 1419, 11358, 102229 — numerisch exakt)
- V1⁗ damit VOLLSTÄNDIG: untere Seite des Tiefengesetzes ist Satz
  (Sprungstellen + Asymptotik + Gleichheit); offen nur noch V1″
  (obere Seite)
- Buch K8, Fachtext, Register (33 Sätze) nachgezogen

## 0.12, 13. Juli 2026, Gleichheitsfälle charakterisiert (Satz S32)

- **Satz S32** (Anhang F.9): Ω = 0 ⟺ Übertragsfreiheit der
  Superadditivität + Scharfheit des Multiplikationslemmas
  (Gleichheitsanalyse der S27-Beweiskette; exakt bis H₇)
- **Korollar**: semi-geschlossene Zählformel für den Nullzähler —
  exakt für alle acht gemessenen Terme (2, 5, 13, …, 564); die
  sechste Zählfolge ist auf die scharfen Quotienten reduziert
- ehrlich vermerkt: die volle Ziffern-Entfaltung von Bedingung 2
  ist skizziert, aber noch nicht verifiziert (erster Versuch wich ab)
- Buch (K6, K8, a1) nachgezogen; Registerstand 32

## 0.11, 13. Juli 2026, V10 GESCHLOSSEN — die Seitentreue ist axiomminimal

- **Satz S31** (Anhang E.5): Auch der nichtkommutative Mischfall B
  ist unmöglich, sobald beide Distributivgesetze gelten (Standard in
  jedem Halbring): Die Rechts-Distributivität spiegelt die Kette und
  erzwingt P_{u⊗a} = val(a)-konstant; das g⊕g-Finale braucht dann
  keine Kommutativität mehr
- V10 beantwortet: NEIN unter Halbring-Axiomen; übrig bleibt nur die
  einseitig-distributive Kuriosität außerhalb der Axiomatik
- Endstand Seitentreue: Fall A stirbt an Links-Distributivität,
  Fall B an beidseitiger Distributivität, Bruchfälle an Totalität/
  Fakultätsquotient/Halbkoeffizient — KEINE Lücke mehr
- Buch (K5-Reichweite, K8-Nachtrag, Anhang B, Registerstand 31) und
  Fachtext nachgezogen

## 0.10.1, 13. Juli 2026, GPT-Review-Korrekturen (alle Punkte umgesetzt)

- **Geltungsbereich Seitentreue präzisiert:** „gesetzestreu" explizit
  definiert (Buch K5 + Spez Anhang E); Reichweiten-Absatz (Fall A nur
  Links-Distributivität, Fall B + Kommutativität, V10 als einzige
  Lücke); Fachtext-Abstract enger formuliert
- ker-Δ präzisiert (Gestalten vs. Elemente); Kompaktifizierung =
  idempotente Retraktion (Fußnoten Buch + Fachtext); Titelei
  korrigiert; K6 → „Sieben Zählfolgen aus der Horimetrik" mit
  Nicht-Springer-Steckbrief; 16er-Bilanz vollständig (2+8+6)
- Literatur: Kudryavtseva–Mazorchuk = math/0511374,
  Ganyushkin–Mazorchuk = 1006.0316, Simon-Titel vollständig,
  Rigo UND Stipulanti

## 0.10, 13. Juli 2026, DIE SEITENTREUE-TRILOGIE (V12 bewiesen)

- **Satz S30** (Anhang G.5): Struktur-⊕ + Bruch-⊗ unerfüllbar —
  Kettengleichung erzwingt 2A(Y) = Y^k̲, also Koeffizient ½;
  Ziffern sind ganz. Wachstumslemma: k ≤ 2·deg(A)+1
- **Korollar G.5b**: dreiseitige Seitentreue VOLLSTÄNDIG — genau
  zwei Rechenwelten (Wert, Gestalt); der Cantor-Bruch trägt keine
  eigene und mischt sich in keine. V12 bewiesen
- drei Beweise, drei Waffen gleicher Bauart (σ-Wachstum,
  Fakultätsquotient, Halbkoeffizient) — Bemerkung in G.5
- Buch: K5 (Trilogie-Absatz), K8 (Nachtrag statt offener Frage),
  Anhang B (Trilogie-Beweis), Registerstand 30

## 0.9, 13. Juli 2026, dreiseitige Seitentreue zu zwei Dritteln (Satz S29)

- **Satz S29** (Anhang G.4): (a) kein reiner Bruchhalbring —
  bruchgetragene Addition ist nie total (F(u)+F(u)=1); (b) Wert-⊕ +
  Bruch-⊗ für beliebige Selektoren unerfüllbar
  (Fakultätsquotienten-Argument: konstanter Quotient > 1 gegen
  N_m → ∞)
- V12-Rest präzise lokalisiert: nur noch Struktur-⊕ + Bruch-⊗,
  samt dokumentierter Warnung (polynomiale Identitäts-Schlupflöcher)
- Buch Kapitel 8 und Registerstand (29 Sätze) aktualisiert

## 0.8.4, 13. Juli 2026, Publikationsstrategie konsolidiert

- Christians Entscheidung: **nur das Buch** wird auf der Webseite
  veröffentlicht und dient als OEIS-Referenz; der Fachtext wird als
  kompakte Satz-Referenz weitergepflegt; das englische arXiv-Skelett
  (paper/) ist gelöscht
- TODO-Pipeline und OEIS-Entwürfe entsprechend umgestellt

## 0.8.3, 13. Juli 2026, die dritte Treppe in Buch und Fachtext (Loop-Iteration 8)

- Buch Kapitel 3: neuer Abschnitt „Die dritte Treppe" — R-Erweiterung,
  Cantor-Bruch, Drei-Treppen-Tabelle, präzise Antwort auf den
  „seit Cantor bekannt"-Einwand
- Buch Kapitel 8: neue offene Frage dreiseitige Seitentreue
- Fachtext: Bemerkung zur Cantor-Koordinate und dritten Erweiterung
  direkt nach den Grenzraumsätzen (beantwortet den Reviewer-Einwand
  im Text selbst)
- **V12 neu**: dreiseitige Seitentreue als neue Leitfrage
- Kollege im Urlaub — Fachtext-Übergabe wartet entspannt

## 0.8.2, 13. Juli 2026, erstes externes Review + Cantor-Koordinate (Satz S28)

- Erstes externes Mini-Review (Kollege): Basics korrekt entschlüsselt,
  Kernbeobachtung V = (n+1)!·F numerisch bestätigt und als Satz G.1
  übernommen
- **Satz S28 / Anhang G**: die DRITTE Erweiterung R (Rechts-Anhängen,
  bruchtreu, Wert ×(n+2), Limes = endliche Cantor-Brüche); drei
  Identitäten (Wert/Gestalt/Bruch) mit paarweise verschiedenen
  Invarianten; Klärung des „seit Cantor bekannt"-Einwands: er trifft
  die R-Welt, nicht die Z-Welt und nicht das Zusammenspiel
- Reviewer-Heuristik zur Starrheit gewürdigt und abgegrenzt: erklärt
  wertgetragene Multiplikation, nicht die gesetzestreue Strukturseite
- 28 Sätze

## 0.8.1, 13. Juli 2026, Beweisanhang im Buch

- **Anhang B „Die Beweise"** (buch/kapitel/a2-beweise.tex): vollständige
  Beweise aller Hauptsätze, nach Kapiteln geordnet — Grenzraumsätze,
  beide Halbringe, Dualität, Seitentreue (komplett), Asymptotiksatz,
  Ziffernformel, Rekursion/Monotonie/Multiplikationslemma/
  Interchange-Positivität (Christians Wunsch: Beweise strukturell im
  Buch, Kapitel bleiben erzählend)
- Kapitel 3 und 5 verweisen jetzt explizit auf den Beweisanhang

## 0.8, 13. Juli 2026, INTERCHANGE-POSITIVITÄT BEWIESEN (Loop-Iteration 7)

- **Satz S27** (vormals V11): Ω(h) ≥ 0 — „erst wachsen, dann liften
  liefert nie weniger" ist bewiesen. Beweiskette: Superadditivität
  (F.8a, aus S25) + **Multiplikationslemma S26**
  (z_ℓ(cy) ≥ (c+1)z_ℓ(y) für c ≥ ℓ+2, Kern: er mod (ℓ+1) ≤ er;
  Regime-Grenze scharf, darunter Minima −1, −9, −59, −319 gestaffelt)
- Der gescheiterte Erstversuch (F.7, Rest-Kopplung) wurde durch den
  multiplikativen Zugang umgangen — dokumentiert als Lehrstück
- Buch (Kap. 6, 8, Anhang) und Fachtext auf Satz-Status
  aktualisiert; Registerstand 27 Sätze
- Offen bleiben: Gleichheitsfälle Ω = 0 (Nullzähler-Folge) und
  Maximalwachstum

## 0.7.1, 13. Juli 2026, V11 auf Rekursion reduziert (Loop-Iteration 6)

- **Lemma S24**: Rekursionsformel z_n(x) = (x mod (n+1)) + (n+2)·z_{n−1}(x div (n+1))
  für den Nullerweiterungswert, mit Beweis (Koeffizientenshift =
  X·P(X−1) in fallender Fakultätsbasis)
- **Lemma S25**: strikte Monotonie von z_n, Beweis per Carry-Induktion
- V11 äquivalent zu „z_n(x) fällt in n"; naive Induktions-
  verschärfung widerlegt (W-Minimum −187 bei n=7, x=416) —
  Invariante braucht Rest-Kopplung; Protokoll in Anhang F.7
- Register: 25 Sätze; V3 als „im Kern gelöst" markiert

## 0.7, 13. Juli 2026, Ziffernformel (Satz S23) + Buch-Erstfassung fast komplett

- **Satz S23** (Loop-Iteration 4): exakte Ziffernformel
  N(n) = Σ_{p≤P} min(d_p, p)·n!/p! über die Eigen-Darstellung von n!
  in H_n; verifiziert n=3..10; löst das n!/2-Phänomen auf und
  reduziert V3 auf die Ziffernbilder der Fakultäten
- Permutations-Brücke geöffnet: D(n) zählt Inversionssequenzen
  (Lehmer-Codes) mit gewichteter Schwelle; siebte OEIS-unbekannte
  Folge N(n)
- Buch: Kapitel 4 (Strukturpolynome), 6 (Sechs Folgen, nennt
  OEIS-Einreichungen), 7 (Sackgassen) ausgeschrieben; es fehlen nur
  Kapitel 8 und Anhang a1
- OEIS: b-Files generiert, Konto beantragt (wartet auf Freischaltung)
- TODO.md als zentrale Aufgabenliste mit Publikations-Pipeline

## 0.6.2, 13. Juli 2026, m₇ exakt bestätigt + OEIS-Entwürfe

- **Dritte Vorhersage des Tiefengesetzes exakt bestätigt:**
  m₇ = 294875 (prognostiziert ≈294875). Sprungstellenfolge
  zertifiziert bis g=12 verlängert (Anhang F.5) — via der
  S22-Identität in exakter Bruchrechnung statt Riesenfakultäten
  (`experiments_m7.py`)
- `oeis/ENTWUERFE.md`: Einreichungsentwürfe für alle sechs Folgen
  (englische Definitionen ohne Projektjargon, Programme, Workflow);
  Einreichung selbst erfordert Christians OEIS-Konto
- Termerweiterungen (β bis 16, D bis 10, Ω bis H₈) im Hintergrund
- Buch: Kapitel 2 und Interludium i1 vollständig ausgeschrieben
  (Loop-Iteration 1)

## 0.6.1, 13. Juli 2026, der Fachtext

- `fachtext/horimetrik-fachtext.pdf`: eigenständiger deutscher
  Fachtext für Christians Webseite (Zuschnitt nach GPT-Empfehlung,
  erweitert um die inzwischen bewiesenen Resultate): drei
  Hauptresultate mit vollständigen Beweisen (Grenzräume, duale
  Projektorhalbringe, voller Seitentreue-Satz), Asymptotiksatz,
  Tabelle der sechs Zählfolgen, Ehrlichkeits-Kapitel (kein
  Neuheitsanspruch über Suchbefund hinaus), offene Fragen,
  Bibliographie
- Publikationsweg laut Christian: zuerst eigene Webseite, arXiv
  optional später; Peer-Review kein Selbstzweck

## 0.6, 13. Juli 2026, das GPT-Paket: drei neue Sätze (Anhang F)

- **Satz S19** (Schalensprung-Lemma, GPT-Vorschlag): \(D(n)\) zählt
  die Ein-Schritt-Schalenspringer unter \(Z\); erzeugende Funktion
  für V3
- **Satz S20/S21** (GPT-Vorschlag): Stabilitätslemma (\(K_S\) erhält
  Wertkompaktheit) ⟹ \(VSV=SV\) ⟹ Kompaktifizierungsmonoid mit genau
  6 Elementen und 5 Idempotenten (\(VS\) nicht — Gegenzeuge (6,6)
  erst in \(H_6\), vierte Kleine-Welt-Falle); Hecke–Kiselman-
  Nachbarschaft (arXiv:1006.0316)
- **Satz S22**: Asymptotik \(m_g/(g+2)!\to1\) vollständig bewiesen
  (exakte Umindexierungs-Identität + Sandwich); empirisch sogar
  \(\pm1\)-scharf; stehende Vorhersage \(m_7\approx294875\);
  V1⁗ damit teilentschieden
- **V11 neu**: Interchange-Defekt \(\Omega\ge0\) (exhaustiv bis
  \(H_7\)); zwei weitere OEIS-unbekannte Folgen (Nr. 5 und 6)
- Header der Spezifikation auf Version 0.6 gebracht (GPT-Hinweis);
  Dateiname bleibt stabil
- Obsolet durch S18: GPT-Vorschlag 5 (V9′-CSP)

## 0.5.1, 13. Juli 2026, Review, Neuheitscheck, Paper-Skelett

- **Adversarialer Review von S18 bestanden** (Anhang E.4): zwei
  Präzisierungen eingearbeitet — (1) die Schranke T_m ≥ σ(mA) folgt
  aus der Elementgültigkeit (Satz 4.2), nicht aus dem Selektor;
  (2) minimale Axiome: Fall A braucht nur Links-Distributivität,
  Fall B zusätzlich ⊗-Kommutativität → neue Randfrage V10
  (nichtkommutativer Mischfall)
- **Neuheits-Tiefencheck:** nächster Nachbar sind abstrakte
  Numerationssysteme (Rigo et al., arXiv:2103.16966 — führende Nullen
  wertsensitiv, aber keine Halbringtheorie); Factoradic-Arithmetik
  existiert nur als Ziffernalgorithmik; kein Seitentreue-Analogon
  gefunden; Peirce-Ecken als Analogie notiert; Mathlib-Pochhammer als
  Formalisierungspfad
- **Paper-Skelett** `paper/main.tex` (englisch): Abstract, Aufbau,
  Hauptsätze formuliert, Seitentreue-Satz mit vollständigem Beweis
  portiert, TODO-Marker für die übrigen Beweise; kompiliert mit
  Tectonic

## 0.5, 13. Juli 2026, DER SEITENTREUE-SATZ (V9 bewiesen)

- **Satz S18** (Anhang E): vollständiger Beweis der Seitentreue für
  BELIEBIGE Selektoren. Fall A (⊕ wert, ⊗ struktur) scheitert an der
  Distributivität allein; Fall B (⊕ struktur, ⊗ wert) an
  Distributivität + Kommutativität. Beweiswaffe: konstante
  Multiplikatoren (σ(c·Q) ≥ c treibt Auswertungspunkte ins
  Unendliche) plus σ(mX) = m+1
- Korollar E.2: vollständige Klassifikation der payload-definierten
  Arithmetiken — gesetzestreu ⟺ seitenrein; V9′ negativ beantwortet
- Bemerkung E.3: Quelle der Starrheit ist die Ziffernschranke aus
  Definition 1.1 — die älteste Regel der Horimetrik
- alle sechs konkreten Beweisschritte numerisch verifiziert
- Buchkapitel 5: Vermutung → Satz, Beweisidee als Erzählung
- Damit sind von den heutigen Leitfragen entschieden: V4 (widerlegt),
  V8 (ja, Dualität), V9 (bewiesen); offen bleiben V1⁗/V1″
  (Tiefengesetz-Beweis), V4′ (gekoppelte Nicht-Produkt-Strukturen
  innerhalb der Seiten), V2/V3/V5/V6 (Zählfolgen)

## 0.4, 13. Juli 2026, der Klassifikationssatz (Seitentreue erster Stufe)

- **Satz S17** (Anhang D.1): vollständige Klassifikation der
  natürlichen 16er-Familie — genau zwei gesetzestreue Arithmetiken
  (A.3 und Spiegel C.2), beide seitenrein; bewiesen über die Sätze
  A.3/C.2 plus explizite Gegenbeispiele für alle 14 übrigen Fälle
- volle Seitentreue V9 auf das diophantische Kernproblem **V9′**
  reduziert (Anhang D.2): Funktionalgleichung
  \(\varphi(R\,Q_m)=m\,\varphi(R)\) für \(\varphi(Q)=Q(\tau(Q)+1)\);
  Teilresultate bewiesen (Q_m nicht konstant; Endlichkeitswiderspruch
  bei Auswertung über Heimathorizont); Pell-Lösbarkeit einzelner
  Zweige und Teilerfenster-Obstruktion dokumentiert
- V8 in conjectures.md als beantwortet nachgetragen (war seit S16 offen
  markiert); m₆-Vorhersagetest (31998) in Anhang C.6 dokumentiert
- Buchkapitel 5 um den Stand der Seitentreue aktualisiert
- Theorie-Status: 17 Sätze, erste Klassifikation, Dualität,
  quantitatives Tiefengesetz mit zwei bestätigten Vorhersagen,
  vier OEIS-unbekannte Zählfolgen, präzise lokalisierte Front (V9′)

## 0.3.1, 13. Juli 2026, Seitentreue und Sprungstellenfolge

- **Seitentreue-Sweep** (Anhang C.5): alle 16 Payload-Selektor-
  Kombinationen getestet; genau zwei Überlebende (A.3 und Spiegel C.2),
  alle 8 gemischten scheitern an der Distributivität → Vermutung V9
  (Seitentreue) als neuer Starrheitskandidat
- **Sprungstellenfolge** (Anhang C.6): \(m_g=3,15,84,533,3883\),
  vierte OEIS-unbekannte Folge; Asymptotik \(m_g\to(g+2)!\) vermutet
  (V1⁗-quantitativ)
- Buchkapitel 5 „Arithmetik mit Gedächtnis" vollständig entworfen
  (Sackgasse G4, Satz A.3, Exzess, Dualität, Seitentreue, drei
  Interludien); Buch kompiliert
- Experimente: `experiments_v4strich.py`

## 0.3, 13. Juli 2026, Dualitätssatz und Tiefengesetz

- **Dualitätssatz** (Anhang C, Sätze S15/S16): Der Horiraum trägt zwei
  spiegelbildliche Halbringe — wertseitig (A.3, Projektor
  \(K_V=\otimes(1,1)\)) und strukturseitig (neu, Projektor
  \(K_S=\boxtimes(1,1)\)). Dieselbe Hori-Zahl Eins trägt beide
  Projektoren; das Nichtkommutieren der Kompaktifizierungen ist das
  Nichtkommutieren der beiden Multiplikationen. **V8 positiv
  beantwortet.**
- Lemma C.1: \(\sigma(P+Q)\ge\max(\sigma P,\sigma Q)\) — \(\sigma\)
  fällt bei Addition nie (Gegenstück zu Satz A.1: es kann aber steigen)
- **V1′ widerlegt** (G9): \(\delta_{\mathrm{hor}}=-2\) ab Schale 15
  (konstruierte Zeugen), \(-3\) ab Schale \(\approx100\); Tiefengesetz
  V1⁗ über die Schalenlücke \(g(m)\) formuliert und bis \(m=200\)
  bestätigt
- Experimente: `experiments_dualitaet.py`

## 0.2, 13. Juli 2026, Exzess-Zerlegung: V1 und V4 entschieden

- Anhang B: Exzess \(\varepsilon=n-\mu(x)\) und kanonische Bijektion
  \(\mathcal H\cong\mathbb N_0\times\mathbb N_0\) (Satz B.2)
- Produktprinzip (Satz B.3): jede Halbringstruktur auf dem Exzess
  liefert eine streng gesetzestreue Hori-Arithmetik
- **V4 widerlegt** (G8): tropischer Exzess-Halbring (Eins, keine
  absorbierende Null) und arithmetischer Exzess-Halbring (Eins UND
  absorbierende Null) haben nicht-kompakte Multiplikation
- drei kanonische Arithmetiken benannt: vergessend (A.3), bewahrend
  (tropisch), verstärkend (arithmetisch); A.3 ist nachweislich keine
  Produktstruktur (B.5) — neue Leitfrage V4′ (gekoppelte Strukturen)
- Sackgasse X6 aufgelöst: \((\max,+)\) lebt auf dem Exzess (B.6)
- **V1 widerlegt** (G7): kleinstes Gegenbeispiel \((9,720)\),
  \(720=10\cdot9\cdot8=X^{\underline3}\) im \(H_9\); Verteilung bei
  \(n=9\) vollständig; neue Vermutungen V1′ (\(\ge-1\)) und V1″
  (unbeschränkt nach oben)
- \(K_V\) ist Homomorphismus aller drei Arithmetiken, \(K_S\) keiner
  — neue Frage V8
- Experimente: `experiments_v4.py`, `experiments_v1_probe.py`

## 0.1.2, 13. Juli 2026, Paket A abgeschlossen

- Satz 1.3 (Bijektivität von \(V_n\)): vollständiger Induktionsbeweis
- Sätze 6.1/6.2 (Grenzraumsätze): vollständige Beweise über gerichtete
  Systeme; \(Z\)-Limes \(\cong\mathcal S\), \(L\)-Limes \(\cong\mathbb N_0\)
- REGISTER: S1 und S8 von "Skizze" auf "bewiesen"
- Werkzeug: Tectonic installiert, Buchgerüst kompiliert erstmals
- REGISTER.md, verworfen.md und buch/ (LaTeX-Gerüst) angelegt

## 0.1.1, 13. Juli 2026, erste lokale Forschungssitzung

- Referenzimplementierung: `slots=True` entfernt, läuft nun ab Python 3.9
- Experimentskripte `experiments_2026_07_13.py` und
  `experiments_followup.py` hinzugefügt
- Anhang A in `HORIMETRIK_0_1.md`: Satz A.1 (Additionshöhe \(r+s\)),
  Satz A.2 (Fixpunktzählung \(n\cdot n!\)), Satz A.3
  (konservativ-kompakter Halbring, \(h\otimes1=K_V(h)\),
  \(\mathbb N_0\) als Eck), jeweils mit vollständigem Beweis
- widerlegt: "wertkompakt ⟹ strukturkompakt", "\(D(n)=n!/2\)",
  Assoziativität der konservativen Multiplikation (siehe
  `counterexamples.md` G1–G6)
- \(\beta(r,r)\) bis \(r=12\) berechnet, Argmax-Grad dokumentiert
- OEIS-Negativbefunde für \(\beta(r,r)\), \(D(n)\), \(F(n)\)
- `conjectures.md` V1–V6 angelegt, `literature.md` Matrix gefüllt

## 0.1, 13. Juli 2026

- endliche Horizonte \(H_n\) formalisiert
- Wertabbildung und Codierung definiert
- Strukturpolynome in fallender Fakultätsbasis eingeführt
- vollständigen Horiraum als Paare \((n,P)\) definiert
- strukturtreue Erweiterung \(Z\) und werttreuen Lift \(L\) getrennt
- Struktur- und Wertkompaktifizierung definiert
- Nichtkommutativität der Kompaktifizierungen dokumentiert
- Horizontdifferenz und Hori-Dimension aufgenommen
- erste Produktfunktion \(eta(r,s)\) definiert
- Referenzimplementierung und Agentenauftrag erstellt
