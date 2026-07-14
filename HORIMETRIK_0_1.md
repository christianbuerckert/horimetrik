# Horimetrik — kanonische Spezifikation

**Version:** 0.24 (Grundtext = 0.1; alle späteren Ergebnisse in den
Anhängen A–J; Versionsgeschichte in CHANGELOG.md)  
**Status:** formaler Arbeitsentwurf; Kernsätze adversarial reviewt (E.4)  
**Datum:** 14. Juli 2026  
**Zweck:** stabile Grundlage für Beweise, Gegenbeispiele, Literaturabgleich und spätere Erweiterungen  
**Hinweis:** Der Dateiname bleibt aus Referenzgründen `HORIMETRIK_0_1.md`; maßgeblich ist die Versionsangabe hier.

## 0. Forschungsdisziplin

Dieses Dokument trennt strikt zwischen vier Klassen von Aussagen:

- **Definition:** wird innerhalb der Horimetrik festgelegt.
- **Satz:** ist bewiesen oder unmittelbar aus bekannten Resultaten abgeleitet.
- **Vermutung:** ist plausibel, aber noch nicht bewiesen.
- **Offene Frage:** besitzt derzeit weder Beweis noch belastbare Vermutung.

Die Horimetrik beansprucht in Version 0.1 keine nachgewiesene mathematische Neuheit. Bekannte Nachbargebiete sind insbesondere Mischbasensysteme, das Fakultätszahlensystem, Inversionsfolgen und Permutationscodes, fallende Fakultätspolynome, endliche Differenzen, ganzzahlige Polynome und direkte Limites. Der vorläufig eigenständige Untersuchungsgegenstand ist ihre Kombination mit einer expliziten Horizontkoordinate und zwei verschiedenen Erweiterungsbegriffen.

---

## 1. Endliche Horizonte

### Definition 1.1, Hori-Horizont

Für \(n\in\mathbb N_0\) sei

\[
H_n=
\left\{
(a_1,\ldots,a_n)\ \middle|\ 0\le a_i\le i
\right\}.
\]

Für \(n=0\) enthält \(H_0\) nur die leere Ziffernfolge \(\varepsilon\).

Die Stelle \(i\) besitzt die Basis \(i+1\). Damit gilt

\[
|H_n|=\prod_{i=1}^{n}(i+1)=(n+1)!.
\]

### Definition 1.2, Wertabbildung

Für \(a=(a_1,\ldots,a_n)\in H_n\) sei

\[
V_n(a)
=
\sum_{i=1}^{n}
a_i\frac{(n+1)!}{(i+1)!}.
\]

Äquivalent kann von links nach rechts ausgewertet werden:

\[
v_0=0,\qquad v_i=(i+1)v_{i-1}+a_i.
\]

Dann ist \(V_n(a)=v_n\).

### Satz 1.3, eindeutige endliche Codierung

\[
V_n:H_n\longrightarrow\{0,\ldots,(n+1)!-1\}
\]

ist bijektiv.

**Beweis** (vollständig, Induktion über \(n\)).
Für \(n=0\) ist \(H_0=\{\varepsilon\}\) und \(V_0(\varepsilon)=0\); die
Behauptung ist trivial.

Sei die Aussage für \(n-1\) bewiesen. Aus der Rekursion in
Definition 1.2 folgt

\[
V_n(a_1,\ldots,a_n)=(n+1)\,V_{n-1}(a_1,\ldots,a_{n-1})+a_n,
\qquad 0\le a_n\le n<n+1 .
\]

**Injektivität:** Sind \(V_n(a)=V_n(b)\), so liefert Division mit Rest
durch \(n+1\) wegen \(0\le a_n,b_n\le n\) eindeutig \(a_n=b_n\) und
\(V_{n-1}(a_1,\ldots,a_{n-1})=V_{n-1}(b_1,\ldots,b_{n-1})\); nach
Induktionsvoraussetzung stimmen auch die übrigen Ziffern überein.

**Bildbereich:** Nach Induktionsvoraussetzung gilt
\(0\le V_{n-1}\le n!-1\), also
\(0\le V_n\le(n+1)(n!-1)+n=(n+1)!-1\).

**Surjektivität:** Es gilt \(|H_n|=(n+1)!\) (Definition 1.1), die
Abbildung ist injektiv und ihr Bild liegt in einer Menge derselben
endlichen Mächtigkeit \((n+1)!\); also ist sie bijektiv. \(\square\)

### Definition 1.4, Codierung

Für \(0\le x<(n+1)!\) bezeichnet

\[
E_n(x)=V_n^{-1}(x)
\]

die eindeutige Codierung von \(x\) in \(H_n\).

---

## 2. Strukturpolynome

### Definition 2.1, fallende Fakultäten

\[
X^{\underline 0}=1,
\qquad
X^{\underline d}=X(X-1)\cdots(X-d+1)
\quad(d\ge1).
\]

### Definition 2.2, Strukturpolynom

Für \(a=(a_1,\ldots,a_n)\in H_n\) sei

\[
P_a(X)
=
\sum_{d=0}^{n-1}a_{n-d}X^{\underline d}.
\]

Die Hori-Ziffern sind damit die Koeffizienten des Polynoms in der Basis
der fallenden Fakultäten, von rechts nach links gelesen.

### Satz 2.3, Auswertungssatz

\[
V_n(a)=P_a(n+1).
\]

**Beweis:** Für \(d=n-i\) gilt

\[
(n+1)^{\underline d}
=
\frac{(n+1)!}{(i+1)!}.
\]

Einsetzen in Definition 2.2 liefert Definition 1.2.

### Beispiel 2.4

\[
0012\in H_4
\]

besitzt

\[
P(X)=X+2
\]

und daher

\[
V_4(0012)=P(5)=7.
\]

---

## 3. Der positive Strukturhalbring

### Definition 3.1

\[
\mathcal S
=
\left\{
P(X)=\sum_{d=0}^{D}c_dX^{\underline d}
\ \middle|\
c_d\in\mathbb N_0
\right\}.
\]

### Satz 3.2, Abschluss

\(\mathcal S\) ist unter gewöhnlicher Polynomaddition und
Polynommultiplikation abgeschlossen.

Für Basiselemente gilt

\[
X^{\underline p}X^{\underline q}
=
\sum_{j=0}^{\min(p,q)}
\binom pj\binom qj j!\,
X^{\underline{p+q-j}}.
\]

Alle Strukturkonstanten sind nichtnegative ganze Zahlen. Damit ist

\[
(\mathcal S,+,\cdot,0,1)
\]

ein kommutativer Halbring.

### Bemerkung 3.3

\(\mathcal S\) ist nicht der vollständige Horiraum. Ein Polynom beschreibt
eine horizonübergreifende Struktur, aber noch keinen konkreten
Auswertungshorizont.

---

## 4. Strukturhorizont und vollständiger Horiraum

### Definition 4.1, minimaler Strukturhorizont

Für

\[
P(X)=\sum c_dX^{\underline d}\in\mathcal S
\]

sei

\[
\sigma(P)=
\begin{cases}
0,&P=0,\\
\max\limits_{c_d>0}(d+c_d),&P\ne0.
\end{cases}
\]

### Satz 4.2

\(P\) ist genau dann als gültige Hori-Ziffernfolge in \(H_n\)
darstellbar, wenn

\[
n\ge\sigma(P).
\]

**Beweis:** Im Horizont \(n\) muss der Koeffizient an
\(X^{\underline d}\) die Ziffernbedingung

\[
c_d\le n-d
\]

erfüllen. Dies ist äquivalent zu \(d+c_d\le n\) für alle \(d\).

### Definition 4.3, vollständiger Horiraum

\[
\mathcal H
=
\left\{
(n,P)\ \middle|\ P\in\mathcal S,\ n\ge\sigma(P)
\right\}.
\]

Der Wert einer Hori-Zahl ist

\[
\operatorname{val}(n,P)=P(n+1).
\]

Der Horizont ist

\[
\operatorname{hor}(n,P)=n.
\]

### Bemerkung 4.4

Eine konkrete Ziffernfolge \(a\in H_n\) und das Paar \((n,P_a)\)
enthalten dieselbe Information.

---

## 5. Zwei Horizonterweiterungen

### Definition 5.1, strukturtreue Erweiterung

\[
Z_n:H_n\longrightarrow H_{n+1},
\qquad
Z_n(a_1,\ldots,a_n)=(0,a_1,\ldots,a_n).
\]

In Polynomkoordinaten:

\[
Z(n,P)=(n+1,P).
\]

Damit gilt

\[
P_{Z_n(a)}=P_a.
\]

Der Wert verändert sich im Allgemeinen:

\[
\operatorname{val}(Z(n,P))=P(n+2).
\]

### Definition 5.2, werttreuer Lift

\[
L_n:H_n\longrightarrow H_{n+1},
\qquad
L_n(a)=E_{n+1}(V_n(a)).
\]

Damit gilt

\[
V_{n+1}(L_n(a))=V_n(a).
\]

Der Lift erhält den Wert, kann aber das Strukturpolynom verändern.

### Beispiel 5.3

\[
0012_{H_4}=7.
\]

Strukturtreu:

\[
Z(0012_{H_4})=00012_{H_5}=8.
\]

Werttreu:

\[
L(0012_{H_4})=00011_{H_5}=7.
\]

### Forschungsprinzip 5.4

Die Horimetrik untersucht insbesondere die Differenz zwischen

- gleicher Struktur in einem größeren Horizont und
- gleichem Wert in einem größeren Horizont.

Diese beiden Begriffe fallen im üblichen Stellenwertsystem bei führenden
Nullen zusammen, im Horiraum jedoch nicht.

---

## 6. Zwei Grenzstrukturen

### Satz 6.1, strukturtreuer direkter Limes

Werden die Horizonte durch die Abbildungen \(Z_n\) verbunden, dann
werden genau Ziffernfolgen identifiziert, die sich nur durch führende
Nullen unterscheiden. Jede Äquivalenzklasse besitzt genau ein
Strukturpolynom aus \(\mathcal S\). Daher gilt als Mengenisomorphie

\[
\varinjlim(H_n,Z_n)\cong\mathcal S.
\]

**Beweis** (vollständig). Für \(m\ge n\) sei
\(Z_{n,m}=Z_{m-1}\circ\cdots\circ Z_n\), also das Voranstellen von
\(m-n\) Nullen. Offensichtlich gilt \(Z_{m,k}\circ Z_{n,m}=Z_{n,k}\);
das System ist gerichtet. Der direkte Limes von Mengen ist
\(\bigsqcup_n H_n/\!\sim\) mit \(a\sim b\) genau dann, wenn beide in
einem gemeinsamen späteren Horizont dasselbe Bild haben.

Für \(a\in H_n\), \(b\in H_m\) mit \(n\le m\) bedeutet das
\(0^{\,k-n}a=0^{\,k-m}b\) für ein \(k\ge m\), was äquivalent zu
\(b=0^{\,m-n}a\) ist. Die Klassen sind also genau die Ziffernfolgen
modulo führender Nullen.

Definiere \(\Phi([a])=P_a\).

*Wohldefiniert:* \(P_{Z_n(a)}=P_a\) nach Definition 5.1, denn eine
vorangestellte Null fügt nur den Koeffizienten 0 am höchsten Grad hinzu.

*Injektiv:* Die Ziffernfolge in \(H_n\) ist die auf Länge \(n\) mit
führenden Nullen aufgefüllte, von rechts gelesene Koeffizientenfolge
von \(P_a\) (Definition 2.2). Aus \(P_a=P_b\) mit \(a\in H_n\),
\(b\in H_m\), \(n\le m\) folgt daher \(b=0^{\,m-n}a\), also
\([a]=[b]\).

*Surjektiv:* Jedes \(P\in\mathcal S\) ist nach Satz 4.2 in
\(H_{\sigma(P)}\) als gültige Ziffernfolge darstellbar. \(\square\)

### Satz 6.2, werttreuer direkter Limes

Werden die Horizonte durch die Lifts \(L_n\) verbunden, dann werden
genau Darstellungen desselben natürlichen Wertes identifiziert. Daher gilt

\[
\varinjlim(H_n,L_n)\cong\mathbb N_0.
\]

**Beweis** (vollständig). Für \(m\ge n\) sei
\(L_{n,m}=E_m\circ V_n\). Wegen \(V_m\circ E_m=\mathrm{id}\) gilt

\[
L_{m,k}\circ L_{n,m}
=E_k\circ V_m\circ E_m\circ V_n
=E_k\circ V_n=L_{n,k},
\]

das System ist gerichtet. Für \(a\in H_n\), \(b\in H_m\) gilt
\(L_{n,k}(a)=L_{m,k}(b)\) für ein gemeinsames \(k\) genau dann, wenn
\(E_k(V_n(a))=E_k(V_m(b))\), und da \(E_k\) injektiv ist (Satz 1.3),
genau dann, wenn \(V_n(a)=V_m(b)\). Die Äquivalenzklassen sind also
genau die Fasern der Wertabbildung.

Definiere \(\Psi([a])=V_n(a)\) für \(a\in H_n\). Nach dem eben
Gezeigten ist \(\Psi\) wohldefiniert und injektiv. Surjektiv ist
\(\Psi\), weil jedes \(x\in\mathbb N_0\) als
\(x=V_{\mu(x)}\bigl(E_{\mu(x)}(x)\bigr)\) auftritt. \(\square\)

### Interpretation 6.3

Dieselben endlichen Mengen \(H_n\) erzeugen durch zwei verschiedene
Einbettungsfamilien zwei verschiedene unendliche Grenzräume:

\[
\text{Strukturerhaltung}\longrightarrow\mathcal S,
\]

\[
\text{Werterhaltung}\longrightarrow\mathbb N_0.
\]

---

## 7. Projektionen und Äquivalenzen

### Definition 7.1, Wertprojektion

\[
\pi_V:\mathcal H\to\mathbb N_0,
\qquad
\pi_V(n,P)=P(n+1).
\]

### Definition 7.2, Strukturprojektion

\[
\pi_S:\mathcal H\to\mathcal S,
\qquad
\pi_S(n,P)=P.
\]

### Definition 7.3, Wertäquivalenz

\[
(n,P)\sim_V(m,Q)
\iff
P(n+1)=Q(m+1).
\]

Dann gilt

\[
\mathcal H/{\sim_V}\cong\mathbb N_0.
\]

### Definition 7.4, Strukturäquivalenz

\[
(n,P)\sim_S(m,Q)
\iff
P=Q.
\]

Dann gilt

\[
\mathcal H/{\sim_S}\cong\mathcal S.
\]

---

## 8. Zwei Kompaktifizierungen

### Definition 8.1, Strukturkompaktifizierung

\[
K_S(n,P)=(\sigma(P),P).
\]

Sie erhält die Struktur und wählt den kleinsten zulässigen
Strukturhorizont.

### Definition 8.2, Minimalhorizont eines Wertes

\[
\mu(x)=\min\{n\in\mathbb N_0\mid x<(n+1)!\}.
\]

### Definition 8.3, Wertkompaktifizierung

\[
K_V(n,P)
=
\left(
\mu(P(n+1)),
P_{E_{\mu(P(n+1))}(P(n+1))}
\right).
\]

Sie erhält den aktuellen Wert und wählt dessen kleinsten
Darstellungshorizont.

### Satz 8.4, Idempotenz

\[
K_S^2=K_S,
\qquad
K_V^2=K_V.
\]

### Satz 8.5, Nichtkommutativität

Im Allgemeinen gilt

\[
K_SK_V\ne K_VK_S.
\]

**Minimales Arbeitsbeispiel:**

\[
h=(4,X+2)\equiv0012_{H_4}.
\]

Zuerst strukturkompakt:

\[
K_S(h)=(2,X+2)\equiv12_{H_2},
\]

dessen Wert 5 ist. Danach bleibt die Wertkompaktifizierung in \(H_2\).

Zuerst wertkompakt:

\[
K_V(h)=(3,X+3)\equiv013_{H_3},
\]

dessen Strukturhorizont bereits 3 ist.

Also

\[
K_VK_S(h)\ne K_SK_V(h).
\]

---

## 9. Horizontdifferenz und Hori-Dimension

### Definition 9.1, Vorwärtsdifferenz

\[
\Delta P(X)=P(X+1)-P(X).
\]

### Satz 9.2, Wertänderung bei strukturtreuer Erweiterung

\[
\operatorname{val}(Z(n,P))-\operatorname{val}(n,P)
=
\Delta P(n+1).
\]

### Satz 9.3, Differenz der fallenden Fakultäten

\[
\Delta X^{\underline d}
=
dX^{\underline{d-1}}.
\]

### Definition 9.4, Hori-Dimension

Für \(P\ne0\):

\[
\dim_H(P)=\deg(P).
\]

Für \(P=0\) kann \(\dim_H(0)=-\infty\) oder gesondert 0 gesetzt werden.
Die Konvention ist vor einer Veröffentlichung festzulegen.

### Satz 9.5

Für \(P,Q\ne0\):

\[
\dim_H(PQ)=\dim_H(P)+\dim_H(Q),
\]

und

\[
\dim_H(P+Q)\le
\max\{\dim_H(P),\dim_H(Q)\}.
\]

### Satz 9.6, natürliche Zahlen als horizontinvariante Strukturen

\[
\Delta P=0
\iff
P\text{ ist konstant}.
\]

Die eingebetteten natürlichen Zahlen sind damit genau die
strukturtreuen Hori-Objekte, deren Wert unter Horizonterweiterung
unverändert bleibt.

---

## 10. Arithmetik, derzeitiger sauberer Stand

Es müssen zwei Ebenen getrennt bleiben.

### 10.1 Strukturarithmetik

Im Halbring \(\mathcal S\) sind

\[
P\boxplus Q=P+Q,
\qquad
P\boxtimes Q=PQ
\]

totale Operationen.

Auf einem festen Horizont \(H_n\) sind diese Operationen nur dann intern
darstellbar, wenn

\[
\sigma(P+Q)\le n
\]

beziehungsweise

\[
\sigma(PQ)\le n.
\]

Andernfalls tritt ein **Strukturüberlauf** auf.

Wird der Horizont anschließend vergrößert, bleibt das Strukturpolynom
erhalten, aber der Auswertungswert verändert sich. Deshalb darf ein
Strukturüberlauf nicht mit werttreuem Integerüberlauf verwechselt werden.

### 10.2 Wertarithmetik

Für Hori-Zahlen \(h,k\) kann der natürliche Ergebniswert gebildet werden:

\[
\pi_V(h)+\pi_V(k),
\qquad
\pi_V(h)\pi_V(k).
\]

Danach ist eine Horizontregel erforderlich. Die kompakte Regel wählt
jeweils \(\mu\) des Ergebnisses. Andere Regeln können Horizontinformation
bewahren, müssen aber auf Assoziativität, Distributivität, neutrale
Elemente und Nullverhalten geprüft werden.

### Offene Hauptfrage 10.3

Welche Horizontselektoren

\[
\rho_+,\rho_\times
\]

erzeugen auf \(\mathcal H\) eine mathematisch interessante Algebra, in der
der Horizont nicht sofort kollabiert, aber möglichst viele klassische
Gesetze streng erhalten bleiben?

---

## 11. Erste Forschungsinvarianten

### Definition 11.1, Kompaktifizierungskommutator

Da \(K_S\) und \(K_V\) nicht kommutieren, kann die Abweichung als Paar
von Horizont- und Wertdifferenzen untersucht werden:

\[
C(h)=\left(K_SK_V(h),K_VK_S(h)\right).
\]

Zu entwickeln sind numerische Invarianten wie

\[
\delta_{\mathrm{hor}}(h)
=
\operatorname{hor}(K_SK_V(h))
-
\operatorname{hor}(K_VK_S(h))
\]

und

\[
\delta_{\mathrm{val}}(h)
=
\operatorname{val}(K_SK_V(h))
-
\operatorname{val}(K_VK_S(h)).
\]

### Definition 11.2, maximale Strukturprodukthöhe

\[
\beta(r,s)
=
\max\left\{
\sigma(PQ)
\ \middle|\
\sigma(P)\le r,\ \sigma(Q)\le s
\right\}.
\]

Da sämtliche Strukturkonstanten der Produktbasis nichtnegativ sind,
wird das Maximum bei den komponentenweise maximalen Polynomen

\[
M_r(X)=\sum_{d=0}^{r-1}(r-d)X^{\underline d}
\]

und \(M_s\) angenommen. Daher

\[
\beta(r,s)=\sigma(M_rM_s).
\]

Erste berechnete Werte:

\[
\begin{array}{c|ccccc}
\beta(r,s)&1&2&3&4&5\\
\hline
1&1&2&3&4&5\\
2&2&6&10&14&18\\
3&3&10&22&36&55\\
4&4&14&36&87&162\\
5&5&18&55&162&407
\end{array}
\]

**Status:** rechnerisch verifiziert für diese kleinen Horizonte, noch
keine geschlossene Formel.

---

## 12. Bekannte Nachbargebiete

Die folgenden Bereiche müssen beim Literaturabgleich dauerhaft
berücksichtigt werden:

1. **Mischbasensysteme und Fakultätszahlensysteme**  
   Sie erklären die Bijektion \(H_n\leftrightarrow[0,(n+1)!-1]\).

2. **Lehmer-Codes und Inversionsfolgen**  
   Sie erklären die enge Verbindung zu Permutationen und die
   Fakultätsmächtigkeit der Horizonte.

3. **Fallende Fakultätsbasis und endliche Differenzen**  
   Sie erklären Strukturpolynome und den Operator \(\Delta\).

4. **Ganzzahlige Polynome und Binomialbasis**  
   Sie liefern einen größeren algebraischen Kontext für Polynome, die
   auf ganzen Zahlen ganzzahlige Werte annehmen.

5. **Kombinatorische Spezies und Polynomfunktoren**  
   Sie könnten eine kategoriale Interpretation der positiven
   Strukturkoeffizienten liefern.

6. **Direkte Limites**  
   Sie sind das korrekte formale Werkzeug für die beiden
   Erweiterungsfamilien \(Z_n\) und \(L_n\).

7. **Graduierte und gefilterte Halbringe**  
   Sie sind mögliche Vergleichsstrukturen für \(\sigma\) und
   \(\dim_H\).

---

## 13. Neuheitsstatus

### Bereits bekannt oder unmittelbar bekannt ableitbar

- jeder einzelne Horizont als Mischbasensystem
- Fakultätsgröße und Permutationsbezug
- fallende Fakultätspolynome
- endliche Differenzen
- Produktformel der fallenden Fakultäten
- direkte Limites als allgemeine Konstruktion

### Bisher kein exakter Literaturtreffer

- der vollständige Raum \(\mathcal H=\{(n,P)\mid n\ge\sigma(P)\}\)
  als gemeinsamer Träger von Wert und Struktur
- die gleichzeitige Verwendung der zwei Einbettungen \(Z_n\) und \(L_n\)
- die zwei verschiedenen Kompaktifizierungen \(K_S\) und \(K_V\)
- die systematische Untersuchung ihres Nichtkommutierens
- Horizontselektoren als Grundlage einer wert- und strukturtragenden
  Arithmetik
- die Funktion \(\beta(r,s)\) in genau dieser horimetrischen Bedeutung

Diese Liste ist kein Neuheitsbeweis. Ein vollständiger Literaturabgleich
ist weiterhin erforderlich.

---

## 14. Nächste Arbeitspakete

### Paket A, Grundlagen beweisen

- vollständiger Beweis von Satz 1.3
- vollständiger Beweis von Satz 6.1 und 6.2
- Prüfung aller Randfälle mit \(H_0\) und Null
- eindeutige Konvention für \(\dim_H(0)\)

### Paket B, Algebra klassifizieren

- sinnvolle Horizontselektoren definieren
- Assoziativität und Kommutativität von Addition prüfen
- Assoziativität der Multiplikation inklusive Null prüfen
- strenge und äquivalenzbasierte Distributivität unterscheiden
- neutrale Elemente und absorbierende Null untersuchen

### Paket C, Kompaktifizierungen

- kleinste Gegenbeispiele systematisch enumerieren
- \(\delta_{\mathrm{hor}}\) und \(\delta_{\mathrm{val}}\) untersuchen
- Fixpunkte von \(K_S\), \(K_V\), \(K_SK_V\) und \(K_VK_S\)
  klassifizieren

### Paket D, Produktstruktur

- \(\beta(r,s)\) für größere Werte berechnen
- Schranken und Asymptotik suchen
- prüfen, ob die Diagonalfolge
  \(1,6,22,87,407,\ldots\) bekannt ist
- direkten Ziffernalgorithmus für Strukturprodukte formulieren
- Strukturüberlauf von werttreuem Überlauf formal trennen

### Paket E, Literatur

- positive Polynome in fallender Fakultätsbasis
- Newton- und Binomialbasen
- kombinatorische Spezies
- direkte Limites von Permutationsräumen
- gefilterte Halbringe und Rees-Konstruktionen
- graded semirings, valuations und rank functions

---

## 15. Referenzen für den Start

- Literatur zu Factoradics, Lehmer-Codes und Inversionsvektoren
- Literatur zur fallenden Fakultätsbasis und diskreten Differenzenrechnung
- Literatur zu Integer-valued Polynomials und der Binomialbasis
- Literatur zu kombinatorischen Spezies und polynomialen Funktoren
- Literatur zu direkten Limites von Mengen und Gruppen

Konkrete Startpunkte aus dem bisherigen Abgleich:

- P. Zawiślak, "The Lehmer factorial norm on \(S_n\)", arXiv:2111.03951
- A. G. Fidalgo, "On combinatorial differential operators on species of structures", arXiv:2305.05059
- M. D. Rus, Arbeit zu factorial powers, arXiv:2501.08762
- A. Diaz-Lopez et al., "Descent polynomials", arXiv:1710.11033
- A. Jiménez-Pastor und M. Petkovšek, "The Factorial-Basis Method...", arXiv:2202.05550

---

## 16. Arbeitsregel

Eine Aussage wird erst aus "Vermutung" in "Satz" verschoben, wenn mindestens
eine der folgenden Bedingungen erfüllt ist:

1. vollständiger handschriftlicher oder maschinenlesbarer Beweis,
2. Ableitung aus einem eindeutig benannten bekannten Satz,
3. bei endlichen Aussagen vollständige Enumeration des relevanten Raums.

Computertests erzeugen Vermutungen und Gegenbeispiele, aber keinen
allgemeinen Beweis.

---

## Anhang A. Ergebnisse vom 13. Juli 2026

Grundlage: `experiments_2026_07_13.py` und `experiments_followup.py`.
In diesem Anhang wird die Wertkoordinate verwendet: Eine Hori-Zahl wird
als Paar \((n,x)\) mit \(n\ge\mu(x)\) geschrieben. Über \(E_n\) ist das
zur Polynomkoordinate \((n,P)\) aus Definition 4.3 äquivalent.

### Satz A.1, Additionshöhe

Für \(r,s\ge1\) gilt

\[
\max\{\sigma(P+Q)\mid \sigma(P)\le r,\ \sigma(Q)\le s\}=r+s.
\]

**Beweis.** Obere Schranke: Ist \(c_d>0\) Koeffizient von \(P\), so gilt
\(c_d\le r-d\); analog für \(Q\). Der Summenkoeffizient bei Grad \(d\)
ist höchstens \((r-d)+(s-d)\), also
\(d+c_d\le r+s-d\le r+s\); trägt nur einer bei, gilt sogar
\(d+c_d\le\max(r,s)\). Erreichbarkeit: Die konstanten Polynome \(P=r\),
\(Q=s\) haben \(\sigma(P)=r\), \(\sigma(Q)=s\) und
\(\sigma(P+Q)=\sigma(r+s)=r+s\). \(\square\)

**Interpretation:** Anders als der Polynomgrad, der bei Addition nie
wächst, kann der Strukturhorizont bei Addition bis auf die Summe der
Ausgangshorizonte steigen. Bereits die Addition ist im Horiraum eine
horizontexpandierende Operation.

### Satz A.2, Fixpunktzählung der Kompaktifizierungen

Für \(n\ge1\) gilt in \(H_n\):

\[
\#\{K_V\text{-Fixpunkte}\}
=\#\{K_S\text{-Fixpunkte}\}
=(n+1)!-n!=n\cdot n!.
\]

**Beweis.** \(K_V\)-Fixpunkte sind genau die \((n,x)\) mit \(\mu(x)=n\),
also \(n!\le x<(n+1)!\); das sind \((n+1)!-n!\) Werte.
\(K_S\)-Fixpunkte sind genau die Elemente mit \(\sigma(P)=n\). Nach
Satz 4.2 entsprechen die Elemente von \(H_n\) bijektiv den Polynomen mit
\(\sigma(P)\le n\), und die mit \(\sigma(P)\le n-1\) entsprechen bijektiv
\(H_{n-1}\), also \(n!\) Stück. Die Differenz ist wieder
\((n+1)!-n!\). \(\square\)

Die beiden Fixpunktmengen sind gleich groß, aber verschieden; ihr
Durchschnitt ist echt kleiner (siehe Datenteil A.6).

### Satz A.3, der konservativ-kompakte Halbring

Auf \(\mathcal H\) seien

\[
(n,x)\oplus(m,y)=(\max(n,m,\mu(x+y)),\,x+y),
\]

\[
(n,x)\otimes(m,y)=(\mu(xy),\,xy).
\]

Dann gilt:

1. \(\oplus\) und \(\otimes\) sind kommutativ und assoziativ.
2. \(\otimes\) distribuiert über \(\oplus\).
3. \((0,0)\) ist neutral für \(\oplus\) und absorbierend für \(\otimes\).
4. Es existiert **kein** neutrales Element für \(\otimes\).
5. \(h\otimes(1,1)=K_V(h)\) für alle \(h\in\mathcal H\).
6. Die wertkompakten Elemente \(\{(\mu(x),x)\}\) sind unter beiden
   Operationen abgeschlossen und bilden mit Eins \((1,1)\) einen zu
   \((\mathbb N_0,+,\cdot)\) isomorphen Halbring.

Damit ist \((\mathcal H,\oplus,\otimes)\) ein kommutativer Halbring ohne
Eins, dessen "Eck" \(\mathcal H\otimes(1,1)\) genau die gewöhnlichen
natürlichen Zahlen sind. Die Wertkompaktifizierung ist keine äußere
Zusatzoperation, sondern innere Multiplikation mit der Eins des Ecks.

**Beweis.**
Vorbemerkung: \(\mu\) ist monoton, denn \(x\le y\) impliziert
\(\mu(x)\le\mu(y)\) direkt aus Definition 8.2.

(1) Kommutativität ist klar. Assoziativität von \(\oplus\): Beide
Klammerungen von \((n,x),(m,y),(k,z)\) liefern den Wert \(x+y+z\) und die
Horizonte
\(\max(n,m,k,\mu(x+y),\mu(x+y+z))\)
beziehungsweise
\(\max(n,m,k,\mu(y+z),\mu(x+y+z))\).
Wegen \(x+y\le x+y+z\) und \(y+z\le x+y+z\) werden die inneren
\(\mu\)-Terme von \(\mu(x+y+z)\) absorbiert; beide Seiten sind
\(\max(n,m,k,\mu(x+y+z))\). Assoziativität von \(\otimes\): beide
Klammerungen ergeben \((\mu(xyz),xyz)\).

(2) \(a\otimes(b\oplus c)=(\mu(x(y+z)),\,x(y+z))\). Andererseits
\((a\otimes b)\oplus(a\otimes c)
=(\max(\mu(xy),\mu(xz),\mu(xy+xz)),\,xy+xz)\).
Wegen \(xy\le xy+xz\) und \(xz\le xy+xz\) ist das Maximum
\(\mu(xy+xz)=\mu(x(y+z))\).

(3) \((n,x)\oplus(0,0)=(\max(n,0,\mu(x)),x)=(n,x)\) wegen
\(n\ge\mu(x)\). \((n,x)\otimes(0,0)=(\mu(0),0)=(0,0)\).

(4) Wäre \((k,e)\) neutral, so folgte \(xe=x\) für alle \(x\), also
\(e=1\), und \(\mu(x)=n\) für alle \((n,x)\). Das scheitert an jedem
nicht wertkompakten Element, etwa \((1,0)\), denn \(\mu(0)=0\ne1\).

(5) \((n,x)\otimes(1,1)=(\mu(x),x)=K_V(n,x)\).

(6) Abgeschlossenheit unter \(\oplus\): Für wertkompakte Operanden ist
der Ergebnishorizont \(\max(\mu(x),\mu(y),\mu(x+y))=\mu(x+y)\) nach
Monotonie. Unter \(\otimes\) ist das Ergebnis per Definition wertkompakt.
Auf den wertkompakten Elementen ist \((1,1)\) neutral nach (5), und
\(x\mapsto(\mu(x),x)\) ist der behauptete Isomorphismus. \(\square\)

**Einordnung:** Das ist die erste vollständig gesetzestreue
Hori-Arithmetik, die Horizontinformation nicht sofort kollabiert: Die
Addition erinnert sich an den größten beteiligten Horizont, die
Multiplikation projiziert auf das kompakte Eck. Die klassische
Arithmetik \(\mathbb N_0\) sitzt darin als Eck-Halbring. Der Preis ist
die fehlende globale Eins; deren Abwesenheit ist kein Defekt, sondern
codiert genau die Tatsache, dass Multiplikation wertkompaktifiziert.

### A.4, widerlegte Vermutungen (Enumeration)

1. **"Wertkompakt impliziert strukturkompakt" ist falsch.**
   Kleinstes Gegenbeispiel: \(012_{H_3}\) mit Wert 6. Es ist
   wertkompakt (\(\mu(6)=3\)), aber \(P=X+2\) hat \(\sigma=2\).
2. **"\#\{wertkompakt, nicht strukturkompakt\} \(=n!/2\)" ist falsch.**
   Die Anzahlen sind für \(n=1,\ldots,9\):
   \(0,0,1,8,60,360,2520,21168,211680\).
   Die Übereinstimmung mit \(n!/2\) bei \(n=5,6,7\) ist zufällig;
   \(n=8\) liefert \(21168\ne20160\).
3. **\(\otimes_{\text{konservativ}}\) mit
   \(\rho_\times=\max(n,m,\mu(xy))\) ist nicht assoziativ.**
   Gegenbeispiel: \(a=(0,0)\), \(b=(2,2)\), \(c=(2,3)\), dann
   \((a\otimes b)\otimes c=(2,0)\), aber
   \(a\otimes(b\otimes c)=(3,0)\).

### A.5, OEIS-Negativbefunde, Stand 13. Juli 2026

Die folgenden Folgen liefern in der OEIS keinen Treffer
(Kontrollabfrage mit A000142 erfolgreich):

- Diagonale \(\beta(r,r)\):
  \(1, 6, 22, 87, 407, 2473, 19527, 170720, 1643913, 18042957,
  233850057, 3239053262\)
- Defektfolge \(D(n)=\#\{x\in[n!,(n+1)!):\sigma(E_n(x))<n\}\):
  \(1, 8, 60, 360, 2520, 21168, 211680\) (ab \(n=3\))
- Beidseitige Fixpunkte \(K_S\) und \(K_V\) in \(H_n\):
  \(4, 17, 88, 540, 3960, 32760\) (ab \(n=2\))

Negativbefunde sind kein Neuheitsbeweis, aber ein starkes Indiz, dass
diese Zählungen bisher nicht als eigenständige Objekte untersucht wurden.

### A.6, Datenlage Kompaktifizierungskommutator (Fortsetzung in Anhang B)

Vollständige Zählung bis \(H_7\) (40320 Elemente):

| \(n\) | Elemente | \(K_S\)-fix | \(K_V\)-fix | beide | \(K_SK_V=K_VK_S\) |
|---|---|---|---|---|---|
| 3 | 24 | 18 | 18 | 17 | 22 |
| 4 | 120 | 96 | 96 | 88 | 108 |
| 5 | 720 | 600 | 600 | 540 | 661 |
| 6 | 5040 | 4320 | 4320 | 3960 | 4645 |
| 7 | 40320 | 35280 | 35280 | 32760 | 37609 |

Kleinstes Nichtkommutieren: \(h=010_{H_3}\) (Wert 4) mit
\(K_SK_V(h)=11_{H_2}\) (Wert 4) und \(K_VK_S(h)=10_{H_2}\) (Wert 3).
Die Horizontdifferenz \(\delta_{\mathrm{hor}}\) liegt im Testbereich
stets in \(\{-1,0,+1\}\); ob das allgemein gilt, ist offen.

---

## Anhang B. Die Exzess-Zerlegung und die Entscheidung von V4

Ergebnisse vom 13. Juli 2026, zweite Sitzung.
Rechnerische Verifikation: `experiments_v4.py`.

### Definition B.1, Exzess

Für \((n,x)\in\mathcal H\) heißt

\[
\varepsilon(n,x)=n-\mu(x)\ \ge 0
\]

der **Exzess**: der Anteil des Horizonts oberhalb des Pflichthorizonts.
Wertkompakte Elemente sind genau die mit Exzess 0.

### Satz B.2, Exzess-Koordinaten

Die Abbildung

\[
\Phi:\mathcal H\longrightarrow\mathbb N_0\times\mathbb N_0,
\qquad
\Phi(n,x)=(x,\ n-\mu(x))
\]

ist bijektiv mit Umkehrung \((x,\varepsilon)\mapsto(\mu(x)+\varepsilon,\ x)\).

**Beweis.** Die Bedingung \(n\ge\mu(x)\) ist äquivalent zu
\(\varepsilon\ge0\); beide Abbildungen sind offensichtlich zueinander
invers. \(\square\)

Der Horiraum ist also als Menge das Paarprodukt aus Wert und Exzess.
Entscheidend ist, dass diese Zerlegung **kanonisch** ist: \(\mu\) ist
durch die Fakultätsschalen intrinsisch gegeben.

### Satz B.3, Produktprinzip

Sei \((\mathbb N_0,\boxplus,\boxtimes)\) ein beliebiger kommutativer
Halbring auf den natürlichen Zahlen mit \(\boxplus\)-neutralem Element
\(0\). Definiere auf \(\mathcal H\) in Exzess-Koordinaten

\[
(x,\varepsilon)\oplus(y,\delta)=(x+y,\ \varepsilon\boxplus\delta),
\qquad
(x,\varepsilon)\otimes(y,\delta)=(xy,\ \varepsilon\boxtimes\delta),
\]

also als Horizontselektoren

\[
\rho_+=\mu(x+y)+(\varepsilon_a\boxplus\varepsilon_b),
\qquad
\rho_\times=\mu(xy)+(\varepsilon_a\boxtimes\varepsilon_b).
\]

Dann gilt:

1. \((\mathcal H,\oplus,\otimes)\) erfüllt **alle** strengen Gesetze:
   Kommutativität, Assoziativität, Distributivität; \((0,0)\) ist
   \(\oplus\)-neutral.
2. Besitzt \(\boxtimes\) ein neutrales Element \(e\), so ist
   \((\mu(1)+e,\ 1)\) Eins von \(\otimes\).
3. Ist \(0\) in \((\mathbb N_0,\boxplus,\boxtimes)\) absorbierend, so
   ist \((0,0)\) in \(\mathcal H\) absorbierend.

**Beweis.** Nach Satz B.2 ist \(\Phi\) eine Bijektion; die Operationen
sind komponentenweise definiert, mit \((\mathbb N_0,+,\cdot)\) im
Wertfaktor und \((\mathbb N_0,\boxplus,\boxtimes)\) im Exzessfaktor.
Ein Produkt zweier kommutativer Halbringe erfüllt alle Gesetze
komponentenweise; neutrale und absorbierende Elemente sind die Paare
der komponentenweisen. Die Selektoren sind gültig, da stets
\(\rho\ge\mu(\text{Ergebniswert})\). \(\square\)

### Korollar B.4, V4 ist widerlegt

Die Starrheitsvermutung V4 („strenge Gesetze erzwingen
\(\rho_\times=\mu\)") ist **falsch**. Zwei explizite Gegenbeispiele:

**Der tropische Exzess-Halbring** \(\mathcal H_{\mathrm{trop}}\),
Exzessfaktor \((\mathbb N_0,\max,+)\):

\[
\rho_+=\mu(x+y)+\max(\varepsilon_a,\varepsilon_b),
\qquad
\rho_\times=\mu(xy)+\varepsilon_a+\varepsilon_b.
\]

Alle Gesetze gelten streng; \((1,1)\) ist Eins (Exzess 0 ist
\(+\)-neutral). Die Null ist **nicht** absorbierend:
\((n,x)\otimes(0,0)=(\varepsilon_a,0)\) — das Gedächtnis überlebt
sogar die Multiplikation mit null. Grund: dem tropischen Faktor fehlt
das absorbierende Element \(-\infty\).

**Der arithmetische Exzess-Halbring** \(\mathcal H_{\mathrm{arith}}\),
Exzessfaktor \((\mathbb N_0,+,\cdot)\):

\[
\rho_+=\mu(x+y)+\varepsilon_a+\varepsilon_b,
\qquad
\rho_\times=\mu(xy)+\varepsilon_a\varepsilon_b.
\]

Dies ist ein vollwertiger kommutativer Halbring **mit Eins**
\((2,1)\) **und absorbierender Null** \((0,0)\), dessen Multiplikation
nicht kompakt ist: zum Beispiel
\((3,2)\otimes(3,2)=(3,4)\) mit \(3>\mu(4)=2\).

### Bemerkung B.5, drei kanonische Arithmetiken

| Struktur | Exzess bei \(\oplus\) | Exzess bei \(\otimes\) | Eins | Null absorb. |
|---|---|---|---|---|
| \(\mathcal H_{A.3}\) (vergessend) | gekoppelt an Werte | wird 0 | nein | ja |
| \(\mathcal H_{\mathrm{trop}}\) (bewahrend) | \(\max\) | \(+\) | \((1,1)\) | nein |
| \(\mathcal H_{\mathrm{arith}}\) (verstärkend) | \(+\) | \(\cdot\) | \((2,1)\) | ja |

Der Halbring aus Satz A.3 ist **keine** Produktstruktur: sein
\(\oplus\)-Exzess

\[
\max(\mu(x)+\varepsilon_a,\ \mu(y)+\varepsilon_b,\ \mu(x+y))-\mu(x+y)
\]

hängt von den Werten ab, nicht nur von den Exzessen. Beispiel: die
Exzess-Eingabe \((1,0)\) liefert für \((1,0)\oplus(1,1)\) den
Ausgangsexzess 0, für \((2,1)\oplus(0,0)\) dagegen 1. A.3 ist damit
die erste echt **gekoppelte** Struktur.

### Bemerkung B.6, Auflösung der tropischen Sackgasse X6

X6 stellte fest, dass \((\max,+)\) auf den *Horizonten* an der
Überlaufvalidität scheitert. Die Exzess-Zerlegung zeigt warum und wie
es richtig geht: Die tropische Arithmetik lebt nicht auf dem Horizont,
sondern auf dem **Exzess**. Der Pflichtanteil \(\mu\) übernimmt die
Validität, der tropische Anteil das Gedächtnis.

### Revidierte Leitfrage V4′

Das Produktprinzip liefert eine ganze Familie gesetzestreuer
Arithmetiken — eine pro Halbringstruktur auf dem Exzess. Ehrlich
eingeordnet: Modulo der Koordinatenwahl \(\Phi\) ist Satz B.3
Standardalgebra (Produkthalbringe); der horimetrische Gehalt ist die
Kanonizität von \(\mu\) und damit von \(\Phi\).

Die eigentliche Klassifikationsfrage lautet jetzt:

**V4′: Welche gesetzestreuen Arithmetiken auf \(\mathcal H\) sind
gekoppelt, das heißt keine Produktstrukturen? Ist die konservativ-
kompakte Familie (A.3 und ihre \(g\)-Varianten auf Teilträgern) im
Wesentlichen die einzige gekoppelte Struktur mit absorbierender Null?**

Zweite neue Frage:

**V8: Für welche Arithmetiken ist die Strukturkompaktifizierung
\(K_S\) ein Homomorphismus?** \(K_V\) ist für alle Produktstrukturen
ein Homomorphismus (Projektion des Exzesses auf 0 ist
halbringverträglich, sofern \(\boxplus,\boxtimes\) die 0 fixieren);
für \(K_S\) ist das offen und vermutlich falsch — \(K_S\) gehört zur
Strukturseite (\(\sigma\)), die in den bisherigen Selektoren gar nicht
vorkommt.

### B.7, Nachtrag: auch V1 ist widerlegt

Die Vermutung V1 (\(\delta_{\mathrm{hor}}\in\{-1,0,+1\}\)) war ein
Artefakt des kleinen Enumerationsbereichs. Kleinstes Gegenbeispiel
(vollständige Suche bis \(H_9\)):

\[
h=(9,\ 720),\qquad 720=6!=10\cdot9\cdot8 .
\]

Im Horizont 9 hat 720 das Strukturpolynom \(X^{\underline 3}\), also
\(\sigma=4\); Strukturkompaktifizierung und anschließende
Wertkompaktifizierung landen bei Horizont 4 (Wert
\(5\cdot4\cdot3=60\), \(\mu(60)=4\)). Umgekehrt ist \(\mu(720)=6\) und
\(\sigma(E_6(720))=6\). Also \(\delta_{\mathrm{hor}}(h)=6-4=+2\).

Vollständige Verteilung bei \(n=9\):
\(\{-1{:}\,16780,\ 0{:}\,3572143,\ +1{:}\,38983,\ +2{:}\,894\}\).
Stichproben bis \(n=21\) zeigen \(+3\) ab \(n=14\) und \(+4\) ab
\(n=20\), aber nie einen Wert unter \(-1\).

**Revidierte Vermutungen:**

- **V1′:** \(\delta_{\mathrm{hor}}(h)\ge-1\) für alle
  \(h\in\mathcal H\) (exhaustiv bis \(H_9\), Stichproben bis \(H_{21}\)).
- **V1″:** \(\sup_{h\in H_n}\delta_{\mathrm{hor}}(h)\to\infty\) für
  \(n\to\infty\); die Asymmetrie zwischen den beiden
  Kompaktifizierungsreihenfolgen ist einseitig unbeschränkt.

Hintergrund der Asymmetrie: \(M_{n-2}(n+1)\ge n!\) ab \(n=15\) — die
Werte kleiner Strukturhorizonte wachsen in die Fakultätsschalen
hinein, wodurch \(K_S\) beliebig weit unter \(\mu\) fallen kann,
während \(K_V\)-Bilder nie weit strukturkomprimierbar sind.

---

## Anhang C. Der Dualitätssatz und das Tiefengesetz des Kommutators

Ergebnisse vom 13. Juli 2026, dritte Sitzung.
Rechnerische Verifikation: `experiments_dualitaet.py`.

### Lemma C.1, Additionsmonotonie von \(\sigma\)

Für \(P,Q\in\mathcal S\) gilt
\(\sigma(P+Q)\ge\max(\sigma(P),\sigma(Q))\).

**Beweis.** Sei \(d^*\) eine Stelle mit
\(\sigma(P)=d^*+c_{d^*}(P)\), \(c_{d^*}(P)>0\). Da alle Koeffizienten
nichtnegativ sind, gilt
\(c_{d^*}(P+Q)\ge c_{d^*}(P)>0\), also
\(\sigma(P+Q)\ge d^*+c_{d^*}(P+Q)\ge\sigma(P)\); symmetrisch für
\(Q\). \(\square\)

(Man beachte den Kontrast zum Polynomgrad: \(\deg\) kann bei Addition
nie über das Maximum steigen, \(\sigma\) kann es — Satz A.1 — aber nie
unter das Maximum fallen.)

### Satz C.2, der strukturseitige Spiegel-Halbring

Auf \(\mathcal H=\{(n,P)\mid n\ge\sigma(P)\}\) seien

\[
(n,P)\boxplus(m,Q)=\bigl(\max(n,m,\sigma(P+Q)),\ P+Q\bigr),
\]

\[
(n,P)\boxtimes(m,Q)=\bigl(\sigma(PQ),\ PQ\bigr).
\]

Dann gilt:

1. \(\boxplus\) und \(\boxtimes\) sind kommutativ und assoziativ,
   \(\boxtimes\) distribuiert über \(\boxplus\).
2. \((0,0)\) ist \(\boxplus\)-neutral und \(\boxtimes\)-absorbierend.
3. Es gibt kein \(\boxtimes\)-neutrales Element.
4. \(h\boxtimes(1,1)=K_S(h)\) für alle \(h\).
5. \(K_S\) ist ein Homomorphismus für \(\boxplus\) und \(\boxtimes\).
6. Die strukturkompakten Elemente bilden einen Unterhalbring, der
   isomorph zum Strukturhalbring \(\mathcal S\) ist, mit Eins \((1,1)\).

**Beweis.**
(1) Kommutativität ist klar. Assoziativität von \(\boxplus\): Beide
Klammerungen liefern das Polynom \(P+Q+R\) und den Horizont
\(\max(n,m,k,\sigma(P+Q),\sigma(P+Q+R))\) beziehungsweise mit
\(\sigma(Q+R)\); nach Lemma C.1 werden die inneren \(\sigma\)-Terme
von \(\sigma(P+Q+R)\) absorbiert. Assoziativität von \(\boxtimes\):
beide Seiten \((\sigma(PQR),PQR)\). Distributivität: Die linke Seite
ist \((\sigma(PQ+PR),PQ+PR)\); rechts steht
\(\max(\sigma(PQ),\sigma(PR),\sigma(PQ+PR))=\sigma(PQ+PR)\) nach
Lemma C.1.
(2) \((n,P)\boxplus(0,0)=(\max(n,0,\sigma(P)),P)=(n,P)\) wegen
\(n\ge\sigma(P)\); \((n,P)\boxtimes(0,0)=(\sigma(0),0)=(0,0)\).
(3) Ein neutrales \((k,E)\) erforderte \(PE=P\) für alle \(P\), also
\(E=1\), und \(\sigma(P)=n\) für alle \((n,P)\); das scheitert an
\((2,1)\), denn \(\sigma(1)=1\ne2\).
(4) \(h\boxtimes(1,1)=(\sigma(P\cdot1),P)=(\sigma(P),P)=K_S(h)\).
(5) Für \(\boxplus\):
\(K_S(a)\boxplus K_S(b)
=(\max(\sigma P,\sigma Q,\sigma(P+Q)),P+Q)
=(\sigma(P+Q),P+Q)=K_S(a\boxplus b)\) nach Lemma C.1. Für
\(\boxtimes\) sind beide Seiten \((\sigma(PQ),PQ)\).
(6) Abschluss nach Lemma C.1 und Definition von \(\boxtimes\); die
Abbildung \(P\mapsto(\sigma(P),P)\) ist der Isomorphismus, und
\((1,1)\) ist Eins, weil auf strukturkompakten Elementen (4) zur
Identität wird. \(\square\)

### Korollar C.3, Dualität und Antwort auf V8

Der Horiraum trägt zwei spiegelbildliche kanonische Halbringe:

| | Wertseite (Satz A.3) | Strukturseite (Satz C.2) |
|---|---|---|
| Addition | konservativ über \(\mu\) | konservativ über \(\sigma\) |
| Multiplikation | kompakt über \(\mu\) | kompakt über \(\sigma\) |
| Eck | \(\mathbb N_0\) | \(\mathcal S\) |
| Projektor | \(K_V(h)=h\otimes(1,1)\) | \(K_S(h)=h\boxtimes(1,1)\) |
| Homomorphismus | \(K_V\) | \(K_S\) |

**Dieselbe Hori-Zahl \((1,1)\)** — die Eins — trägt beide Projektoren,
je nachdem, mit welcher der beiden Multiplikationen sie wirkt. Das
Nichtkommutieren von \(K_S\) und \(K_V\) (Satz 8.5) ist damit das
Nichtkommutieren der beiden Multiplikationen mit demselben Element.
V8 ist positiv beantwortet. \(K_V\) ist kein Homomorphismus des
Spiegels (Gegenbeispiel: \((1,1)\boxplus(2,2)\)), die Dualität ist
also strikt: jede Seite verträgt sich nur mit ihrem eigenen Projektor.

### C.4, auch V1′ ist widerlegt: das Tiefengesetz

Die revidierte Vermutung V1′ (\(\delta_{\mathrm{hor}}\ge-1\)) fällt
ebenfalls — aber erst bei gezielter Konstruktion. Werte
\(x\in[m!,(m+1)!)\) mit kleinem Strukturhorizont existieren ab
\(m=15\) (Anhang B.7); bettet man sie in Horizonte \(n>m\) ein,
entsteht \(\delta_{\mathrm{hor}}=-2\), zum Beispiel bei
\(x=1{.}327{.}252{.}697{.}724\) in \(H_{16}\) (Schale 15).

Definiere die **Schalenlücke**

\[
g(m)=m-\min\{s\mid M_s(m+1)\ge m!\}.
\]

Numerisch bestätigt: Das Minimum von \(\delta_{\mathrm{hor}}\) über
die getesteten Kandidaten der Schale \(m\) ist exakt \(-g(m)\):

\[
g(m)=2\ \text{für}\ 15\le m\le80,
\qquad
g(m)=3\ \text{für}\ 100\le m\le200 .
\]

\(\delta_{\mathrm{hor}}\) ist also vermutlich **beidseitig
unbeschränkt**, aber mit dramatisch verschiedenen Raten: nach oben
schon ab \(n=9\) wachsend, nach unten invers-fakultätisch langsam
(\(-3\) erst um \(m\approx100\)). Die Sprungstellen von \(g\) bilden
eine neue Zählfolge (Bestimmung läuft).

**Revidierte Vermutung V1⁗:**
\(\min_{h\in\text{Schale }m}\delta_{\mathrm{hor}}(h)=-g(m)\) und
\(g(m)\to\infty\).

### C.5, der Seitentreue-Sweep (V4′-Evidenz)

Systematischer Test aller 16 Arithmetiken aus
\(\{\text{Wert-},\text{Struktur-}\}\)Payload \(\times\)
\(\{\text{kompakt},\text{konservativ}\}\)Selektor für Addition und
Multiplikation (`experiments_v4strich.py`, vollständige Tripel bis
\(H_3\)):

- **Überlebende: genau zwei** — der wertseitige Halbring (Satz A.3)
  und sein strukturseitiger Spiegel (Satz C.2).
- Alle acht **gemischten** Kombinationen (Additionsseite ≠
  Multiplikationsseite) scheitern an der Distributivität.
- Kompakte Addition scheitert stets am neutralen Element,
  konservative Multiplikation an der Assoziativität (G4).

Das Muster „konservative Addition, kompakte Multiplikation" ist also
innerhalb dieser Familie **pro Seite eindeutig**, und die Seiten sind
**nicht mischbar**.

**Vermutung V9, Seitentreue:** Jede gesetzestreue gekoppelte
Arithmetik auf \(\mathcal H\) ist seitenrein: ihre Payloads stammen
vollständig von der Wertseite oder vollständig von der Strukturseite.
(Die Produktstrukturen aus Satz B.3 sind wertseitig mit
Exzess-Selektoren; sie mischen ebenfalls keine Seiten.)

Falls V9 zutrifft, wäre das der Starrheitssatz eine Ebene über der
widerlegten V4: nicht die Selektoren sind starr, sondern die
**Identitäten** — jede widerspruchsfreie Hori-Arithmetik muss sich
zwischen Wert und Struktur entscheiden.

### C.6, die Sprungstellenfolge des Tiefengesetzes

Die Schwellen \(m_g=\min\{m\mid g(m)\ge g\}\), also die kleinste
Schale, in der die Kommutator-Tiefe \(-g\) möglich wird
(exakte Berechnung, `experiments`-Hintergrundlauf):

\[
m_1,\ldots,m_6=3,\ 15,\ 84,\ 533,\ 3883,\ 31998 .
\]

Kein OEIS-Treffer (Stand 13.07.2026) — die vierte unbekannte Zählfolge
des Projekts. Auffällig ist die Nähe zu \((g+2)!\):

\[
\frac{m_g}{(g+2)!}=0{,}50,\ 0{,}625,\ 0{,}70,\ 0{,}74,\ 0{,}77,\ 0{,}794
\quad(g=1,\ldots,6),
\]

monoton steigend. Heuristik über den dominanten Term von
\(M_{m-g}(m+1)\): Die Bedingung \(M_{m-g}(m+1)\ge m!\) ist asymptotisch
\(m+1\gtrsim(g+2)!/c_g\) mit \(c_g=1+\tfrac{2}{g+3}+\ldots\to1\).

**Vorhersagetest bestanden:** \(m_6\) wurde vor der Berechnung aus der
Quotientenextrapolation auf \(\approx31930\) und das Intervall
\([30000,32500]\) festgelegt; die anschließende Binärsuche ergab
\(m_6=31998\) (Abweichung 0,2 %). Das Tiefengesetz hat damit seine
zweite bestätigte Vorhersage.

**Vermutung V1⁗-quantitativ:** \(m_g/(g+2)!\to1\); die maximale
negative Tiefe in Schale \(m\) wächst wie die Umkehrfunktion der
Fakultät. Zusammen mit der oberen Seite (V1″, näherungsweise linear
wachsend) ist der Kompaktifizierungskommutator damit vollständig
asymmetrisch quantifiziert: schnelles Wachstum nach oben,
invers-fakultätisches Kriechen nach unten.

---

## Anhang D. Seitentreue: erste Stufe bewiesen, Kern lokalisiert

Ergebnisse vom 13. Juli 2026, fünfte Sitzung.

### Satz D.1, Seitentreue erster Stufe (Klassifikationssatz)

Betrachtet werde die natürliche Familie von Arithmetiken auf
\(\mathcal H\): Das Payload jeder Operation ist wertgetragen
(Werte addieren/multiplizieren) oder strukturgetragen (Polynome
addieren/multiplizieren), der Selektor ist kompakt oder konservativ
über der jeweiligen Seite (\(\mu\) bzw. \(\sigma\)) — insgesamt 16
Arithmetiken.

**Genau zwei davon sind gesetzestreu** (kommutativ, assoziativ,
distributiv, mit \(\oplus\)-neutralem Element): der wertseitige
Halbring (Satz A.3) und sein strukturseitiger Spiegel (Satz C.2).
Insbesondere ist keine seitengemischte Arithmetik dieser Familie
gesetzestreu.

**Beweis.** Die positiven Fälle sind die Sätze A.3 und C.2. Jeder
negative Fall wird durch ein explizites endliches Gegenbeispiel
bewiesen (verifiziert in `experiments_v4strich.py`):

| Addition | Multiplikation | verletzt | Zeuge |
|---|---|---|---|
| kompakt (wert- oder strukturgetragen), beliebige Mult. (8 Fälle) | — | Neutralität | \((1,0)\oplus(0,0)=(0,0)\ne(1,0)\) |
| wert/kons | wert/kons | Distributivität | \(a=(0,0),\ b=c=(1,1)\) |
| wert/kons | **struktur/komp** | Distributivität | \(a=b=(1,1),\ c=(2,5)\) |
| wert/kons | **struktur/kons** | Distributivität | \(a=(0,0),\ b=c=(1,1)\) |
| struktur/kons | **wert/komp** | Distributivität | \(a=b=(1,1),\ c=(2,2)\) |
| struktur/kons | **wert/kons** | Distributivität | \(a=(0,0),\ b=c=(1,1)\) |
| struktur/kons | struktur/kons | Distributivität | \(a=(0,0),\ b=c=(1,1)\) |

Da alle 16 Fälle entschieden sind, ist die Klassifikation vollständig.
\(\square\)

Das Muster des Beweises: Kompakte Addition zerstört stets die
Neutralität (sie vergisst den Horizont des Operanden), konservative
Multiplikation die Assoziativität (G4, die Null), und **jede
Seitenmischung die Distributivität** — der paradigmatische Zeuge ist
\(a=b=(1,1)\), \(c=(2,5)\): links projiziert die strukturgetragene
Eins per \(K_S\) und ändert dabei den Wert von 6 auf 5, rechts
addiert die wertgetragene Addition ehrlich zu 6.

### D.2, Reduktion der vollen Seitentreue (beliebige Selektoren)

Für den Fall „wertgetragene Addition, strukturgetragene
Multiplikation mit strukturbasiertem Selektor
\(T=\tau(P_aP_b)\)" gilt: Das Produkt hängt nur von den
Strukturen ab, und mit
\(\varphi(Q):=Q(\tau(Q)+1)\) erzwingt die Distributivität entlang der
Ketten \(e_m=u\oplus\cdots\oplus u\) die Funktionalgleichung

\[
\varphi(R\cdot Q_m)=m\cdot\varphi(R)
\qquad\text{für alle Strukturen }R\text{ und alle }m,
\]

wobei \(Q_m\) die Struktur von \(e_m\) ist. Daraus folgt bereits:

1. \(\varphi(Q_m)=m\) (mit \(R=1\), da \(\varphi(1)=1\)).
2. \(Q_m\) ist für große \(m\) nicht konstant: Für \(Q_m=m\) wäre
   \(\sigma(mX)=m+1\), also
   \(\varphi(XQ_m)\ge(m+2)m\), im Widerspruch zum linearen
   \(m\,\varphi(X)\).
3. Liegt der Auswertungspunkt von \(XQ_m\) bei oder über dem
   Heimathorizont von \(Q_m\), folgt \(\sigma(Q_m)\) beschränkt und
   damit ein Endlichkeitswiderspruch.

**Warnung in beide Richtungen** (Ehrlichkeitsprotokoll):

- Naive *Unmöglichkeits*argumente scheitern: Die reinen
  Wertgleichungen sind punktweise erfüllbar, teils über
  Pell-Gleichungen — etwa verlangt ein Zweig
  \((h+2)^2-2(t+1)^2=1\), lösbar mit \(h=15\), \(t=11\).
- Naive *Konstruktionen* scheitern: Lineare Strukturen \(X+c\)
  erfordern \(z(z+c)=k\cdot s\), also Teiler von \(k\,s\) im Fenster
  um \(\sqrt{k\,s}\) — die für \(k\) eine große Primzahl fehlen.

**Präzisierte offene Frage V9′:** Existiert eine Funktion
\(\tau:\mathcal S\to\mathbb N\) mit \(\tau\ge\sigma\), sodass
\(\varphi(Q)=Q(\tau(Q)+1)\) die Funktionalgleichungen aller
Distributivitätsketten simultan erfüllt? Die volle Seitentreue ist
damit auf ein diophantisches Konsistenzproblem über dem
Strukturhalbring reduziert. Weder Beweis noch Gegenbeispiel sind
billig; beides wäre ein publizierbares Resultat.

---

## Anhang E. Der Seitentreue-Satz (vollständige Fassung)

Ergebnis vom 13. Juli 2026, sechste Sitzung. Damit ist V9 bewiesen
und die offene Frage V9′ negativ beantwortet.

**Rahmen.** *Gesetzestreu* heißt in dieser Spezifikation:
kommutativ, assoziativ, distributiv, mit \(\oplus\)-neutralem
Element (die pro Fall tatsächlich benötigten schwächeren Axiome
dokumentiert E.4). Eine Operation auf \(\mathcal H\) heißt *wertgetragen*,
wenn der Ergebniswert die gewöhnliche Summe bzw. das gewöhnliche
Produkt der Operandenwerte ist (der Ergebnishorizont ist durch einen
beliebigen gültigen Selektor frei); sie heißt *strukturgetragen*, wenn
das Ergebnisstrukturpolynom die Summe bzw. das Produkt der
Operandenpolynome ist (Horizont wieder frei, \(\ge\sigma\)).
Jedes Element \((n,x)\) bestimmt Wert, Horizont und Strukturpolynom
eindeutig (Satz 1.3 / Bemerkung 4.4).

### Satz E.1, Seitentreue

Es gibt keine seitengemischte gesetzestreue Arithmetik auf
\(\mathcal H\). Genauer:

**(A)** Ist \(\oplus\) wertgetragen und \(\otimes\) strukturgetragen,
so ist bereits die Distributivität allein unerfüllbar — für jede Wahl
der Selektoren.

**(B)** Ist \(\oplus\) strukturgetragen und \(\otimes\) wertgetragen,
so sind Distributivität und Kommutativität von \(\otimes\) zusammen
unerfüllbar — für jede Wahl der Selektoren.

**Beweis von (A).**
Sei \(u=(1,1)\) (Struktur \(1\)) und \(e_1=u\),
\(e_m=e_{m-1}\oplus u\). Da \(\oplus\) wertgetragen ist, gilt
\(\operatorname{val}(e_m)=m\); die Struktur \(Q_m\) von \(e_m\) ist
irgendeine gültige Darstellung von \(m\).

Aus der Distributivität folgt für jedes Element \(a\) durch Induktion

\[
\operatorname{val}(a\otimes e_m)=m\cdot\operatorname{val}(a\otimes u).
\tag{E.1}
\]

*Schritt 1: \(Q_m\) ist konstant.*
Für \(c\ge1\) sei \(a_c=(c,c)\); seine Struktur ist die Konstante
\(c\) (Terminaldarstellung). Da konstante Polynome überall ihren
eigenen Wert annehmen, ist
\(\operatorname{val}(a_c\otimes u)=(c\cdot1)(t+1)=c\) für jeden
Selektorwert \(t\). Mit (E.1):

\[
\operatorname{val}(a_c\otimes e_m)=(c\,Q_m)(y_c+1)=c\,Q_m(y_c+1)=mc,
\]

also \(Q_m(y_c+1)=m\), wobei
\(y_c\ge\sigma(c\,Q_m)=\max_d(d+c\,q_d)\ge c\).
Die Punkte \(y_c+1\) sind also unbeschränkt. Hätte \(Q_m\) Grad
\(\ge1\), wäre es auf dem zulässigen Bereich streng monoton wachsend
und nähme den Wert \(m\) höchstens einmal an — Widerspruch. Also ist
\(Q_m\) konstant, und wegen
\(\operatorname{val}(u\otimes e_m)=Q_m(\cdot)=m\cdot1\) ist
\(Q_m=m\).

*Schritt 2: Konstanten sterben am Multiplikator \(X\).*
Sei \(g=(2,3)\) mit Struktur \(X\). Dann ist
\(r:=\operatorname{val}(g\otimes u)=X(t_g+1)=t_g+1\ge\sigma(X)+1=3\)
eine feste Zahl. Mit (E.1) und \(Q_m=m\):

\[
\operatorname{val}(g\otimes e_m)=(X\cdot m)(T+1)=m\,(T+1),
\qquad T\ge\sigma(mX)=m+1,
\]

also \(\operatorname{val}(g\otimes e_m)\ge m(m+2)\). Andererseits ist
sie \(=m\,r\). Für \(m>r-2\) Widerspruch. \(\square\)

**Beweis von (B).**
Sei \(u=(1,1)\), \(f_1=u\), \(f_m=f_{m-1}\oplus u\). Da \(\oplus\)
strukturgetragen ist, hat \(f_m\) die Struktur \(m\) (Konstante) und
damit den Wert \(m\).

*Schritt 1: Produkte mit \(u\) sind terminal.*
Sei \(g=(2,3)\) und \(A\) die Struktur von \(g\otimes u\) (eine
Darstellung des Wertes \(3\)). Distributivität liefert induktiv
\(P_{g\otimes f_m}=m\cdot A\) (Strukturen addieren sich). Da
\(g\otimes f_m\) ein \(\otimes\)-Ergebnis mit Wert \(3m\) ist, muss
\(m\,A\) den Wert \(3m\) darstellen:

\[
(mA)(T_m+1)=3m
\quad\Longrightarrow\quad
A(T_m+1)=3,
\qquad T_m\ge\sigma(mA)\ge m .
\]

\(A\) nimmt den Wert 3 an unbeschränkt vielen Stellen an, ist also
konstant: \(A=3\).

*Schritt 2: \(g\oplus g\) erschlägt die Terminalität.*
\(f'_2:=g\oplus g\) hat die Struktur \(2X\) und lebt auf einem
Horizont \(H\ge\sigma(2X)=3\); sein Wert ist \(2(H+1)\ge8\).
Distributivität:

\[
u\otimes(g\oplus g)=(u\otimes g)\oplus(u\otimes g).
\]

Rechts steht (mit \(u\otimes g=g\otimes u\) nach Kommutativität und
Schritt 1) die Struktur \(2\cdot3=6\), eine Konstante. Links steht
ein \(\otimes\)-Ergebnis mit Wert \(1\cdot2(H+1)=2(H+1)\); seine
Struktur muss die Konstante 6 sein, also \(2(H+1)=6\), d.h.
\(H=2\) — im Widerspruch zu \(H\ge3\). \(\square\)

### Korollar E.2, vollständige Klassifikation

Zusammen mit den Sätzen A.3, C.2 und D.1 gilt: **Eine
payload-definierte Arithmetik auf \(\mathcal H\) ist genau dann
gesetzestreu, wenn sie seitenrein ist** — und pro Seite existieren
gesetzestreue Selektoren (konservativ-kompakt; auf der Wertseite
zusätzlich die Exzess-Familie aus Satz B.3). Die Vermutung V9 ist
damit **bewiesen**; die Frage V9′ (Existenz eines verwebenden
\(\tau\)) ist **negativ beantwortet** — Fall (A) zeigt, dass kein
solches \(\tau\) existiert, unabhängig von aller Pell-Lösbarkeit
einzelner Zweige.

### Bemerkung E.3, die Quelle der Starrheit

Der Beweis benutzt an beiden entscheidenden Stellen dieselbe
Eigenschaft: \(\sigma(m\cdot P)\) wächst linear in \(m\), weil die
Ziffernschranke \(c_d\le n-d\) große Koeffizienten in große Horizonte
zwingt. Die Starrheit der Identitäten ist also eine direkte
Konsequenz der ältesten Regel der Horimetrik — der Ziffernbedingung
\(0\le a_i\le i\) aus Definition 1.1. Die Regel, mit der alles
begann, ist genau die Regel, die verhindert, dass Wert und Gestalt je
in einer Arithmetik verschmelzen.

### E.4, Review-Protokoll zu Satz E.1 (adversariale Prüfung, 13.07.2026 nachts)

Jede Voraussetzung und jeder Schluss wurde einzeln angegriffen.
Befunde:

**Präzisierung 1 (Herkunft der Schranke \(T_m\ge\sigma(mA)\) in
Fall B):** Der \(\otimes\)-Selektor garantiert nur
\(T_m\ge\mu(3m)\). Die benötigte stärkere Schranke folgt nicht aus
dem Selektor, sondern aus der Elementgültigkeit: Da \(m\,A\) das
Strukturpolynom eines Elements mit Horizont \(T_m\) ist, gilt
\(\sigma(mA)\le T_m\) nach Satz 4.2. Der Beweis ist korrekt, die
Begründung wird hiermit explizit gemacht.

**Präzisierung 2 (minimale Axiome):** Fall A benötigt nur die
*Links*-Distributivität \(a\otimes(b\oplus c)=(a\otimes b)\oplus
(a\otimes c)\); weder Assoziativität noch Kommutativität noch ein
neutrales Element werden verwendet. Fall B benötigt
Links-Distributivität und die Kommutativität von \(\otimes\)
(für \(u\otimes g=g\otimes u\)). Ein *nichtkommutativer* gemischter
Fall B ist durch E.1 nicht ausgeschlossen und bleibt als Randfrage
offen (V10). Für die Standardgesetze ist die Klassifikation
vollständig.

**Geprüfte Angriffe ohne Befund:**

- Existenz aller Zeugen: \(a_c=(c,c)\), \(g=(2,3)\), \(u=(1,1)\)
  liegen in \(\mathcal H\); die Ketten \(e_m\), \(f_m\) sind für
  jede Selektorwahl wohldefinierte Elemente.
- Monotonie: Alle Auswertungspunkte liegen im streng monotonen
  Bereich (\(y\ge\sigma+1\ge\deg+2\)); "unendlich viele Punkte"
  folgt aus \(y_c\ge c\).
- Nullwert-Schlupfloch: Elemente mit Wert 0 werden im Beweis nicht
  benötigt; kein Randfall offen.
- Uniformität: Der Widerspruchsindex (\(m>r-2\) bzw. \(c\) groß)
  hängt vom jeweiligen System ab — für einen Unmöglichkeitsbeweis
  genügt das (jedes System erzeugt seinen eigenen Widerspruch).
- \(Q_m\ne0\): folgt aus \(\operatorname{val}(e_m)=m\ge1\).
- Die Werte-Ebene von Fall B, Schritt 2 liefert den Widerspruch
  sogar ohne Strukturvergleich: RHS-Wert 6, LHS-Wert
  \(2(H+1)\ge8\).

**Ergebnis: Satz E.1 hält dem Review stand.** Neue Randfrage V10:
Existiert eine *nichtkommutative* gemischte Arithmetik vom Typ B?

---

## Anhang F. Schalensprung, Kompaktifizierungsmonoid, Asymptotiksatz

Ergebnisse vom 13. Juli 2026, achte Sitzung. Die Ansätze 1–4 dieses
Anhangs gehen auf Vorschläge des GPT-Agenten zurück; Beweise,
Korrekturen und Verifikation (`experiments_gpt_paket.py`) lokal.

### Satz F.1, Schalensprung-Lemma für die Defektfolge

Für \(a\in H_n\) gilt

\[
\sigma(P_a)<n
\iff
a_i<i\ \text{für alle }i
\iff
a=Z_{n-1}(b)\ \text{für ein }b\in H_{n-1}.
\]

Folglich zählt die Defektfolge genau die Schalenspringer:

\[
D(n)=\#\{\,b\in H_{n-1}\ :\ \operatorname{val}(Z_{n-1}(b))\ge n!\,\},
\]

also die Hori-Zahlen, die durch eine **einzige strukturtreue
Erweiterung** in die nächste Fakultätsschale springen.

**Beweis.** \(\sigma(P_a)=\max_{c_d>0}(d+c_d)\) mit \(c_d=a_{n-d}\).
Es ist \(d+c_d=n\) genau dann, wenn die Ziffer an Position
\(i=n-d\) ihren Maximalwert \(i\) annimmt; wegen \(\sigma\le n\)
(Gültigkeit) ist \(\sigma<n\) äquivalent dazu, dass keine Ziffer
maximal ist. Insbesondere \(a_1<1\), also \(a_1=0\), und
\((a_2,\ldots,a_n)\) erfüllt nach Indexverschiebung genau die
Ziffernbedingung von \(H_{n-1}\); das ist die Nullerweiterung
\(Z_{n-1}\). Einsetzen in die Definition von \(D(n)\) liefert die
Behauptung (numerisch bestätigt für \(n=3,\ldots,8\)). \(\square\)

Damit besitzt V3 eine erzeugende Funktion: mit den Stellengewichten
\(w_i=(n+1)!/(i+1)!\) ist

\[
D(n)=\sum_{k\ge n!}[q^k]\prod_{i=1}^{n}\bigl(1+q^{w_i}+\cdots+q^{(i-1)w_i}\bigr),
\]

ein Schwellenproblem für eine explizite Ziffernsummen-Verteilung.

### Satz F.2, Stabilitätslemma und das Kompaktifizierungsmonoid

**(a) Stabilitätslemma.** Ist \(h\) wertkompakt, so ist auch
\(K_S(h)\) wertkompakt.

**Beweis.** Sei \(h=(m,P)\) mit \(P(m+1)\ge m!\) und \(s=\sigma(P)\).
Angenommen \(P(s+1)<s!\). Für \(s\le t<m\) wächst jeder Term
\(c_d X^{\underline d}\) beim Übergang von \(t+1\) zu \(t+2\) um den
Faktor \((t+2)/(t+2-d)\); wegen \(d\le s-1\le t-1\) (aus
\(d+c_d\le s\), \(c_d\ge1\)) ist dieser höchstens \((t+2)/3\). Also

\[
P(t+2)\le P(t+1)\cdot\frac{t+2}{3}<t!\cdot\frac{t+2}{3}\le(t+1)! ,
\]

da \(t+2\le3(t+1)\). Induktion von \(t=s\) bis \(m-1\) ergibt
\(P(m+1)<m!\), Widerspruch. \(\square\)

**(b) Relation.** Für alle \(h\): \(K_V(h)\) ist wertkompakt, nach
(a) auch \(K_S(K_V(h))\), also fixiert \(K_V\) dieses Element:

\[
K_V\circ K_S\circ K_V=K_S\circ K_V .
\]

**(c) Monoidsatz.** Das von \(S:=K_S\) und \(V:=K_V\) erzeugte
Transformationsmonoid auf \(\mathcal H\) hat genau sechs Elemente

\[
\{\,\mathrm{id},\ S,\ V,\ S{\circ}V,\ V{\circ}S,\ S{\circ}V{\circ}S\,\},
\]

mit den definierenden Relationen \(S^2=S\), \(V^2=V\),
\(V\!SV=SV\). Es gilt \((VS)^2=SVS\); die Idempotenten sind genau die
fünf Elemente außer \(V{\circ}S\).

**Beweis.** Höchstens sechs: Jedes alternierende Wort der Länge
\(\ge4\) enthält das Teilwort \(V\!SV\) und reduziert per (b); Quadrate
reduzieren per Idempotenz. Paarweise Verschiedenheit: explizite
Trennzeugen (vollständige Enumeration bis \(H_7\)); insbesondere
trennt \(h=(6,6)\) die Elemente \(SVS\) und \(VS\):
\(VS(h)=(3,6)\), \(SVS(h)=(2,5)\). \((VS)^2=V(SVS)=(V\!SV)S\cdot\ldots
=SVS\) direkt aus (b); da \(SVS\ne VS\), ist \(VS\) nicht idempotent.
\(\square\)

**Warnung (Methodik):** Bis \(H_4\) wirkt \(VS\) idempotent; der
kleinste Gegenzeuge hat den Wert 6 und lebt in \(H_6\) — zum dritten
Mal in diesem Projekt täuscht ein zu kleiner Testbereich eine
Gesetzmäßigkeit vor.

**Einordnung:** Das abstrakte Monoid
\(\langle s,v\mid s^2=s,\ v^2=v,\ vsv=sv\rangle\) gehört zur
Nachbarschaft der Hecke–Kiselman-Monoide (idempotente Erzeuger mit
gerichteten Absorptionsrelationen; vgl. Kudryavtseva–Mazorchuk,
arXiv:math/0511374, sowie Ganyushkin–Mazorchuk, arXiv:1006.0316); die
konkrete treue Wirkung auf \(\mathcal H\) ist horimetrisch.

### Satz F.3, Asymptotik des Tiefengesetzes

Sei \(m_g=\min\{m:\,M_{m-g}(m+1)\ge m!\}\) (die \(g\)-te
Sprungstelle der Schalenlücke). Mit

\[
c_g:=(g+2)!\sum_{k\ge1}\frac{k}{(g+k+1)!}=1+O(1/g)
\]

gilt

\[
\frac{(g+2)!}{c_g}\ \le\ m_g+1\ \le\ (g+2)!,
\qquad\text{insbesondere}\qquad
\boxed{\ \frac{m_g}{(g+2)!}\longrightarrow1\ }.
\]

**Beweis.** Umindexieren (\(k=s-d\)) liefert die exakte Identität

\[
\frac{M_{m-g}(m+1)}{m!}=(m+1)\sum_{k=1}^{m-g}\frac{k}{(g+k+1)!}=:F(m),
\]

(numerisch in exakter Bruchrechnung bestätigt). \(F\) ist in \(m\)
streng wachsend — beide Faktoren wachsen —, die Schwelle also
wohldefiniert und die Schalenlücke monoton (das rechtfertigt
nachträglich die Sprungstellen-Suche). Für \(m+1\ge(g+2)!\) ist
bereits der Term \(k=1\) groß genug: \(F(m)\ge(m+1)/(g+2)!\ge1\).
Umgekehrt ist \(F(m)\le(m+1)\,c_g/(g+2)!\), also \(F(m)<1\) für
\(m+1<(g+2)!/c_g\). Die Schranke für \(c_g\): mit \(x=1/(g+3)\) ist

\[
c_g\le1+\sum_{k\ge2}k\,x^{k-1}=1+\frac{x(2-x)}{(1-x)^2}=1+O(1/g).
\qquad\square
\]

**Bemerkung (empirische Schärfe und stehende Vorhersage):**
Numerisch gilt sogar \(m_g\approx(g+2)!/c_g\) auf \(\pm1\) genau:

\[
3{,}5;\ 15{,}8;\ 84{,}6;\ 534{,}0;\ 3883{,}1;\ 31998{,}5
\quad\text{gegen}\quad
3,\ 15,\ 84,\ 533,\ 3883,\ 31998 .
\]

Daraus die dritte stehende Vorhersage des Tiefengesetzes:
\(m_7\approx294875\) (noch nicht verifiziert; Rechnung teuer, aber
machbar). Der konjekturale Teil von V1⁗ reduziert sich damit auf die
Gleichheit \(\min\delta_{\mathrm{hor}}=-g(m)\); die Asymptotik der
Sprungstellen ist jetzt Satz.

### F.4, der Interchange-Defekt (neue Front)

Für \(h\in H_n\) führen zwei Wege nach \(H_{n+2}\): erst
strukturtreu erweitern, dann werttreu liften — oder umgekehrt.
Der **Interchange-Defekt**

\[
\Omega(h)=\operatorname{val}(L_{n+1}Z_n(h))-\operatorname{val}(Z_{n+1}L_n(h))
=P(n+2)-P'(n+3),
\quad P'=\text{struct}(P(n+1),\,n+1),
\]

misst die Nichtvertauschbarkeit der beiden **Wachstums**operationen.
Vollständige Enumeration bis \(H_7\):

\[
\Omega\ge0\ \text{überall};\qquad
\max_{H_1..H_7}\Omega=0,1,6,43,351,2873,26443;\qquad
\#\{\Omega=0\}=2,5,13,23,61,111,274 .
\]

**Vermutung V11:** \(\Omega(h)\ge0\) für alle \(h\) — „erst wachsen,
dann liften dominiert erst liften, dann wachsen." Beide neuen Folgen
sind ohne OEIS-Treffer (Nummern fünf und sechs des Projekts). Offen:
Charakterisierung von \(\Omega=0\), Maximalwachstum, Zusammenhang mit
\(\delta_{\mathrm{hor}}\); als Werkzeug kommen lokale
Mischbasen-Umwandlungen und die mengentheoretische
Yang-Baxter-Gleichung in Frage (arXiv:2405.19798).

### F.5, Nachtrag: dritte Vorhersage exakt bestätigt, Folge bis g=12

Die Identität aus Satz F.3 erlaubt die Sprungstellenberechnung in
exakter Bruchrechnung mit zertifizierten Restgliedern — ohne
Riesenfakultäten (`experiments_m7.py`). Ergebnis:

\[
m_7=294875
\]

— die stehende Vorhersage (\(\approx294875\)) war **exakt** richtig.
Die zertifizierte Gesamtfolge:

\[
3,\ 15,\ 84,\ 533,\ 3883,\ 31998,\ 294875,\ 3006206,\ 33603002,\
408733041,\ 5375410231,\ 76013015079
\]

mit Quotienten \(m_g/(g+2)!=0{,}50,\ldots,0{,}872\) monoton steigend
(konsistent mit \(\to1\), Satz F.3). Das Tiefengesetz hat damit drei
bestätigte Vorhersagen, die dritte auf den Punkt.

### Satz F.6, die Ziffernformel für die Schalenspringer

Sei \(d=(d_1,\ldots,d_n)\) die \(H_n\)-Ziffernfolge von \(n!\) und
\(P\) die erste Position mit maximaler Ziffer (\(d_P=P\)), bzw.
\(P=n\), falls keine existiert. Dann gilt für die Nicht-Springer
\(N(n)=n!-D(n)\):

\[
N(n)\;=\;\sum_{p=1}^{P}\min(d_p,\,p)\cdot\frac{n!}{p!}\,.
\]

**Beweis.** \(N(n)\) zählt die Ziffernfolgen mit \(a_i\le i-1\)
(Inversionssequenzen) und Wert \(<n!\). Da die Wertabbildung
bijektiv ist (Satz 1.3), zerlegen wir nach der ersten Position
\(p\), an der sich \(a\) von \(d\) unterscheidet: Der Präfix muss
mit \(d\) übereinstimmen — möglich nur, solange \(d_j\le j-1\),
also bis ausschließlich zur ersten maximalen Ziffer —, an der
Stelle \(p\) muss \(a_p<d_p\) und \(a_p\le p-1\) gelten
(\(\min(d_p,p)\) Möglichkeiten), und der Suffix ist frei innerhalb
der Kappen (\(\prod_{j>p}j=n!/p!\) Möglichkeiten), wobei jeder
solche Suffix strikt unterhalb bleibt, weil der volle Suffixraum
das Intervall \([0,w_p)\) bijektiv füllt. Jeder Nicht-Springer wird
so genau einmal gezählt. \(\square\)

**Verifikation:** exakt für \(n=3,\ldots,10\)
(`experiments`-Lauf, Loop-Iteration 4).

**Korollar (Auflösung des \(n!/2\)-Phänomens).** Die Koinzidenz
\(N(n)=n!/2\) für \(n=5,6,7\) ist eine Aussage über die
Ziffernbilder der Fakultäten in ihrer eigenen Schale:
\(120=(0,1,0,0,0)\) und \(5040=(0,0,3,0,0,0,0)\) sind
Ein-Ziffern-Darstellungen mit \(d_p\cdot n!/p!=n!/2\), und bei
\(720=(0,0,3,2,0,6)\) summieren sich die Terme zufällig zu
\(6!/2\). Ab \(n=8\) reißt das Muster, weil \(8!\) ein dichteres
Ziffernbild hat.

**Reduktion von V3:** Die Defektfolge ist damit vollständig auf die
**Eigen-Darstellung der Fakultäten** zurückgeführt: die Frage nach
\(D(n)\) ist jetzt die Frage nach den Ziffern von \(n!\) im
Horizont \(n\) — ein neues, schärferes Untersuchungsobjekt
(z.\,B. \(10!=(0,0,2,0,5,3,1,4,0,10)\); auffällig viele führende
Nullen: \(d_1=d_2=0\) ab \(n\ge6\), da \(n!<w_2\)).

### F.7, der V11-Angriff: Rekursionsformel und Monotonie

Sei \(z_n(x):=P(n+2)\) für \(P=\operatorname{struct}(x,n)\) — der
Wert nach einer Nullerweiterung. V11 ist äquivalent zu:
\(z_n(x)\) ist für festes \(x\) nichtwachsend in \(n\).

**Lemma F.7a (Rekursionsformel).** Für \(x=q(n+1)+r\),
\(0\le r\le n\):

\[
z_n(x)=r+(n+2)\,z_{n-1}(q).
\]

**Beweis.** Aus der Ziffernrekursion (Satz 1.3) folgt für die
Strukturpolynome \(P_{n,x}(X)=r+X\cdot P_{n-1,q}(X-1)\), denn der
Koeffizientenshift um einen Grad ist in der fallenden
Fakultätsbasis die Multiplikation mit \(X\) bei gleichzeitiger
Argumentverschiebung (\(X^{\underline d}=X\cdot(X-1)^{\underline{d-1}}\)).
Auswerten bei \(X=n+2\). \(\square\)

**Lemma F.7b (strikte Monotonie).** \(z_n(x)<z_n(x+1)\).

**Beweis.** Induktion über \(n\). Ohne Übertrag (\(r<n\)) wächst
\(z\) um genau 1. Beim Übertrag (\(r=n\), \(x+1=(q+1)(n+1)\)) ist

\[
z_n(x+1)-z_n(x)=(n+2)\bigl(z_{n-1}(q+1)-z_{n-1}(q)\bigr)-n
\ge(n+2)-n=2>0
\]

nach Induktionsvoraussetzung. \(\square\)

**Protokoll des Induktionsversuchs für V11.** Die Rekursionsformel
legt eine Induktion über \(n\) nahe. Im Zweig gleicher Quotienten
verlangt sie die Verschärfung
\(W_n(x)=x+(n+2)z_{n-1}(x)-(n+3)z_n(x)\ge0\) — diese ist
**falsch** (Minimum \(-187\) bei \(n=7\), \(x=416\); Enumeration bis
\(H_7\)). Da V11 selbst bis \(H_8\) exhaustiv bestätigt ist, muss
die korrekte Invariante die Kopplung der beiden Divisionsreste
(\(x\) mod \(n+1\) gegen \(x\) mod \(n+2\)) einbeziehen; der Zweig
gleicher Quotienten tritt nur für \(x\bmod(n+2)=r-q\ge0\) auf.
**Offen**, aber jetzt mit exaktem Werkzeug: V11 ist auf eine
elementare Ungleichung über die Rekursion F.7a reduziert.

### F.8, Satz: die Interchange-Positivität (V11 bewiesen)

**Lemma F.8a (Superadditivität).** \(z_n(y+s)\ge z_n(y)+s\) für
\(s\ge0\). *(Direkt aus der strikten Monotonie F.7b: jeder
Einzelschritt hebt \(z_n\) um mindestens 1.)*

**Lemma F.8b (Multiplikationslemma).** Für \(c\ge\ell+2\) und
\(cy<(\ell+1)!\) gilt

\[
z_\ell(c\,y)\;\ge\;(c+1)\,z_\ell(y).
\]

**Beweis.** Induktion über \(\ell\); die Basisfälle sind leer bzw.
trivial. Sei \(y=q(\ell+1)+r\) und \(cr=s(\ell+1)+u\) mit
\(0\le u\le\ell\); dann ist \(cy=(cq+s)(\ell+1)+u\), also nach der
Rekursionsformel F.7a

\[
z_\ell(cy)=u+(\ell+2)\,z_{\ell-1}(cq+s).
\]

Mit Superadditivität und der Induktionsvoraussetzung (Regime bleibt
erhalten: \(c\ge\ell+2>(\ell-1)+2\); Gültigkeit: \(cq<\ell!\)):

\[
z_{\ell-1}(cq+s)\ \ge\ (c+1)\,z_{\ell-1}(q)+s .
\]

Es bleibt \(u+(\ell+2)s\ge(c+1)r\) zu zeigen. Schreibe
\(c=\ell+1+e\) mit \(e\ge1\); dann ist
\(u=cr\bmod(\ell+1)=er\bmod(\ell+1)\), und die Ungleichung ist
äquivalent zu \(r\,(c-\ell-1)\ge u\), also zu \(er\ge er\bmod(\ell+1)\)
— wahr. \(\square\)

Die Regime-Grenze \(c\ge\ell+2\) ist scharf: Für \(c=\ell+1\)
beträgt das numerische Minimum der Differenz \(-1\), darunter
\(-9,-59,-319,\ldots\) (gestaffelt; Enumeration).

**Satz F.8c (Interchange-Positivität, vormals V11).** Für alle
\(h\in\mathcal H\):

\[
\Omega(h)=\operatorname{val}(LZh)-\operatorname{val}(ZLh)\ \ge\ 0 .
\]

**Beweis.** Äquivalent ist \(z_{n+1}(x)\le z_n(x)\) für
\(x<(n+1)!\). Sei \(x=q'(n+2)+r'\). Dann

\[
z_{n+1}(x)
=r'+(n+3)\,z_n(q')
\ \overset{\text{F.8b}, c=n+2}{\le}\
r'+z_n\bigl((n+2)q'\bigr)
\ \overset{\text{F.8a}}{\le}\
z_n\bigl(q'(n+2)+r'\bigr)=z_n(x).
\qquad\square
\]

„Erst die Struktur wachsen lassen, dann den Wert liften, liefert
nie weniger als umgekehrt" ist damit ein Satz. Der gescheiterte
erste Anlauf (F.7, Rest-Kopplung) wurde durch den multiplikativen
Zugang umgangen: Nicht die Reste beider Divisionen mussten
gekoppelt werden, sondern die Multiplikation mit \(n+2\) musste als
eigenständiges Lemma isoliert werden. Offen bleiben die
Gleichheitsfälle (\(\Omega=0\); Zählfolge \(2,5,13,23,61,111,274,564\))
und das Maximalwachstum.

---

## Anhang G. Die Cantor-Koordinate und die dritte Erweiterung

Anlass: das erste externe Mini-Review (Kollege von Christian,
13.07.2026). Kernbeobachtung des Reviewers, numerisch bestätigt:

### Satz G.1, Faktorisierung über den Fakultätsbruch

Für \(a\in H_n\) sei \(F(a)=\sum_{i=1}^n a_i/(i+1)!\in[0,1)\)
(endlicher Cantor-Fakultätsbruch). Dann gilt

\[
V_n(a)=(n+1)!\cdot F(a).
\]

**Beweis.** Termweise: \(a_i\,(n+1)!/(i+1)!=(n+1)!\cdot a_i/(i+1)!\).
\(\square\)

### Satz G.2, die dritte Erweiterung

Sei \(R_n(a_1,\ldots,a_n)=(a_1,\ldots,a_n,0)\) das **Rechts-Anhängen**
einer Null. Dann gilt:

1. \(F(R(a))=F(a)\) — \(R\) ist **bruchtreu**;
2. \(\operatorname{val}(R(a))=(n+2)\cdot\operatorname{val}(a)\) —
   der Wert skaliert exakt homogen;
3. \(F\) ist **nicht** \(Z\)-invariant (Beispiel:
   \(F(12)=5/6\), \(F(012)=1/4\)) und \(P\) ist nicht
   \(R\)-invariant — Bruch und Gestalt sind verschiedene Identitäten;
4. \(\varinjlim(H_n,R_n)\) ist als Menge die Menge der endlichen
   Fakultätsbrüche in \([0,1)\).

**Beweis.** (1) Die neue Ziffer 0 trägt nichts bei; alle alten
Ziffern behalten Position und Nenner. (2) Aus G.1:
\(\operatorname{val}(R(a))=(n+2)!\,F(a)=(n+2)\operatorname{val}(a)\).
(3) Beispiele. (4) Unter \(R\) werden genau Ziffernfolgen
identifiziert, die sich um angehängte Nullen unterscheiden; jede
Klasse trägt genau einen endlichen Bruch, und jeder solche Bruch
tritt auf. \(\square\)

### Einordnung G.3

Der Horiraum trägt damit **drei** natürliche Erweiterungen mit drei
verschiedenen Invarianten und drei verschiedenen Grenzräumen:

| Erweiterung | invariant | Wertdynamik | Grenzraum |
|---|---|---|---|
| \(L\) (Lift) | Wert | \(\times1\) | \(\mathbb N_0\) |
| \(Z\) (links Null) | Gestalt \(P\) | \(P(n+2)/P(n+1)\), ungleichmäßig | \(\mathcal S\) |
| \(R\) (rechts Null) | Bruch \(F\) | \(\times(n+2)\), homogen | endliche Cantor-Brüche |

Das Review las die Basenleiter links verankert (dann ist \(F\) die
Invariante und die Erweiterung \(R\)); unsere Konvention verankert
rechts (dann ist \(P\) die Invariante und die Erweiterung \(Z\)).
Beide Lesarten sind legitim — und verschieden: Der Einwand „im Kern
seit Cantor bekannt" trifft die \(R\)-Welt (Satz G.2.4 IST Cantors
Bruchsystem), aber nicht die \(Z\)-Welt, deren Grenzraum der
Strukturhalbring ist, und nicht das Zusammenspiel (Dualität,
Seitentreue, Tiefengesetz). Die Heuristik des Reviewers zur
Starrheit („Multiplikation skaliert quadratisch") beschreibt korrekt,
warum *wertgetragene* Multiplikation nicht horizontstabil sein kann —
sie erklärt aber nicht, warum die *strukturseitige* Multiplikation
(Satz C.2) sehr wohl gesetzestreu ist. Der Seitentreue-Satz ist
feiner als die Homogenitätsheuristik.

### G.4, Satz: dreiseitige Seitentreue, Teil 1 (V12 zu zwei Dritteln)

Eine Operation heiße **bruchgetragen**, wenn der Ergebnisbruch
\(F\) Summe bzw.\ Produkt der Operandenbrüche ist (Horizont frei,
sofern der Wert \(F\cdot(h+1)!\) ganzzahlig und die Darstellung
gültig ist). Bruchprodukte sind stets endlich darstellbar (die
Nenner teilen Fakultäten).

**Satz G.4a (kein reiner Bruchhalbring).** Bruchgetragene Addition
ist nicht total: Für \(u=(1,1)\) ist \(F(u)+F(u)=1\notin[0,1)\),
und kein Element von \(\mathcal H\) hat Bruch \(\ge1\). Damit
scheitert jede Arithmetik mit bruchgetragener Addition an der
Totalität — insbesondere existiert keine reine Bruchseite und keine
Mischung mit Bruch-Addition. \(\square\)

**Satz G.4b (Wert-Addition verträgt sich nicht mit
Bruch-Multiplikation).** Ist \(\oplus\) wertgetragen und
\(\otimes\) bruchgetragen, so ist die Links-Distributivität für
jede Selektorwahl unerfüllbar.

**Beweis.** Ketten \(e_m=e_{m-1}\oplus u\) mit \(\val(e_m)=m\),
Horizont \(N_m\ge\mu(m)\), also \(F(e_m)=m/(N_m+1)!\) (Satz G.1).
Distributivität liefert induktiv
\(\val(a\otimes e_m)=m\cdot w\) mit \(w=\val(a\otimes u)\).
Andererseits ist
\(\val(a\otimes e_m)=F_a\cdot\frac{m}{(N_m+1)!}\cdot(h_m+1)!\),
also

\[
F_a\cdot\frac{(h_m+1)!}{(N_m+1)!}=w\qquad\text{für alle }m .
\]

Sei \(a=u\), also \(F_a=1/2>0\); dann ist \(w\) ein positives
Ganzes (\(w=F_uF_u(h+1)!\ge1\)). Der Fakultätsquotient
\((h_m+1)!/(N_m+1)!=w/F_a\) ist eine feste Zahl \(>1\), also
\((N_m+2)\cdots(h_m+1)=w/F_a\) mit \(h_m>N_m\); aber die linke
Seite ist \(\ge N_m+2\), und \(N_m\ge\mu(m)\to\infty\).
Widerspruch. (Die Fälle \(h_m=N_m\) bzw.\ \(h_m<N_m\) erzwingen
\(w=F_a<1\) bzw.\ \(w<F_a\), beides unmöglich für ganzes
\(w\ge1\).) \(\square\)

**Offen bleibt genau ein Fall (V12-Rest):** \(\oplus\)
strukturgetragen mit \(\otimes\) bruchgetragen. Dort liefert die
Kette nur die Bedingung
\(A(T+1)/(T+1)!=F_a/(N_m+1)!\) für die feste Struktur
\(A=P_{a\otimes u}\) — eine Diophantische Familie, die durch
polynomiale Identitäten der Form
\(C\cdot A(X{+}k{+}1)=(X{+}2)\cdots(X{+}k{+}1)\) im Prinzip
erfüllbar sein könnte. Das schnelle Argument greift nicht; der Fall
braucht eine eigene Untersuchung (analog zur Pell-Episode bei V9′:
punktweise Lösbarkeit ist noch keine Systemlösbarkeit).

### G.5, Satz: der Trilogie-Schlussstein (V12 vollständig bewiesen)

**Satz G.5a.** Ist \(\oplus\) strukturgetragen und \(\otimes\)
bruchgetragen, so ist die Links-Distributivität für jede Selektorwahl
unerfüllbar.

**Beweis.** Ketten \(f_m=f_{m-1}\oplus u\) (Strukturen addieren):
\(f_m\) hat die konstante Struktur \(m\), Horizont
\(N_m\ge\sigma(m)=m\), Wert \(m\), Bruch \(m/(N_m+1)!\).
Links-Distributivität liefert induktiv
\(P_{u\otimes f_m}=m\cdot A\) mit \(A:=P_{u\otimes u}\ne0\),
\(d:=\deg A\). Als \(\otimes\)-Ergebnis hat \(u\otimes f_m\) den
Bruch \(F_u\cdot m/(N_m+1)!=m/(2(N_m+1)!)\); als Element
\((T_m,\,mA)\) hat es den Bruch \(m\,A(T_m{+}1)/(T_m{+}1)!\).
Gleichsetzen und Kürzen von \(m\):

\[
2\,A(T_m{+}1)\;=\;\frac{(T_m{+}1)!}{(N_m{+}1)!}
\;=\;(T_m{+}1)^{\underline{\,k_m}},
\qquad k_m:=T_m-N_m .
\]

Dabei ist \(k_m\ge1\) (sonst wäre \(2A(T_m{+}1)\le1\), aber
\(A(T_m{+}1)\ge1\)). Das Produkt der \(k\) Faktoren ist mindestens
\((N_m+k_m/2)^{k_m/2}\), während
\(2A(T_m{+}1)\le C\,(N_m+k_m+1)^{d}\); wegen \(N_m\ge m\to\infty\)
folgt \(k_m\le 2d+1\) für große \(m\). Ein Wert \(k^*\) tritt also
unendlich oft auf, und die Polynome \(2A(Y)\) und
\(Y^{\underline{k^*}}\) stimmen an unendlich vielen Stellen
\(Y=T_m{+}1\) überein — sie sind identisch. Dann hätte \(A\) in der
fallenden Fakultätsbasis den Koeffizienten \(1/2\); die
Koeffizienten von \(A\) sind aber Ziffern eines Elements, also
ganze Zahlen. Widerspruch. \(\square\)

(Für beliebige Multiplikatoren \(a\) statt \(u\) läuft dasselbe
Argument mit \(c=(n_a{+}1)!/v_a\) anstelle der \(2\); wegen
\(v_a<(n_a{+}1)!\) ist stets \(c>1\), und \(Y^{\underline{k}}/c\)
liegt nie in \(\mathcal S\).)

**Korollar G.5b (dreiseitige Seitentreue, vollständig).**
Zusammen mit Satz S18 (Wert/Gestalt-Mischungen), Satz G.4a (keine
totale Bruch-Addition) und Satz G.4b (Wert-\(\oplus\) mit
Bruch-\(\otimes\)) gilt: **Auf \(\mathcal H\) existieren genau zwei
Familien gesetzestreuer payload-definierter Arithmetiken — die
wertseitige und die strukturseitige. Die dritte Identität, der
Cantor-Bruch, trägt keine eigene Arithmetik und lässt sich mit
keiner der beiden anderen Seiten verweben.** V12 ist bewiesen;
die Seitentreue ist eine Trilogie. \(\square\)

**Bemerkung.** Die drei Beweise benutzen drei verschiedene Waffen
derselben Bauart: \(\sigma(mX)=m{+}1\) (Ziffernschranke, S18),
konstante Fakultätsquotienten (G.4b) und die halbzahlige
Koeffizienten-Obstruktion (G.5a) — jedes Mal zwingt die Endlichkeit
der Horizonte eine diskrete Größe, gleichzeitig konstant zu bleiben
und zu wachsen.

### E.5, Satz: der nichtkommutative Mischfall (V10 geschlossen)

**Satz E.5.** Ist \(\oplus\) strukturgetragen und \(\otimes\)
wertgetragen, und gelten \emph{beide} Distributivgesetze (wie in
jedem — auch nichtkommutativen — Halbring), so ist das System
unerfüllbar. Kommutativität, Assoziativität und neutrale Elemente
werden nicht benötigt.

**Beweis.** Ketten \(f_m=f_{m-1}\oplus u\) wie in E.1(B). Die
\emph{Rechts}-Distributivität liefert induktiv
\(P_{f_m\otimes a}=m\cdot A'_a\) mit \(A'_a:=P_{u\otimes a}\); da
\(f_m\otimes a\) den Wert \(m\cdot\operatorname{val}(a)\) hat und
\(T'_m\ge\sigma(mA'_a)\ge m\to\infty\), nimmt \(A'_a\) den Wert
\(\operatorname{val}(a)\) an unbeschränkt vielen Stellen an und ist
konstant: \(A'_a=\operatorname{val}(a)\). Insbesondere ist
\(P_{u\otimes g}=3\) — genau die Aussage, für die E.1(B) die
Kommutativität brauchte. Das Finale läuft wörtlich wie dort: Die
\emph{Links}-Distributivität gibt
\(u\otimes(g\oplus g)=(u\otimes g)\oplus(u\otimes g)\) mit Struktur
\(2\cdot3=6\), also Wert 6; links steht
\(1\cdot2(H{+}1)\ge8\). Widerspruch. \(\square\)

**Damit ist die Seitentreue axiomatisch abgeschlossen:** Fall A
stirbt an der Links-Distributivität allein (E.1), Fall B an
beidseitiger Distributivität (E.5) bzw.\ Links-Distributivität plus
Kommutativität (E.1); die Bruchfälle an Totalität,
Fakultätsquotient und Halbkoeffizient (G.4/G.5). Offen bleibt nur
die Kuriosität eines \emph{einseitig} distributiven Mischsystems
vom Typ B — das liegt außerhalb jeder Halbring-Axiomatik.

### F.9, Satz: die Gleichheitsfälle der Interchange-Positivität

**Satz F.9a (Charakterisierung).** Für \(h=(n,x)\) mit
\(x=q'(n{+}2)+r'\) gilt \(\Omega(h)=0\) genau dann, wenn

1. \((q'\bmod(n{+}1))+r'\le n\) — die Superadditivität ist
   übertragsfrei scharf — und
2. \(z_n((n{+}2)q')=(n{+}3)\,z_n(q')\) — das Multiplikationslemma
   ist scharf.

**Beweis.** \(\Omega(h)=0\) heißt Gleichheit in der zweigliedrigen
Kette des Beweises von Satz F.8c, also Scharfheit beider
Ungleichungen. Die Superadditivität über \(r'\) Einzelschritte ist
genau dann scharf, wenn kein Schritt einen Übertrag auslöst; der
Schritt \(x\mapsto x+1\) erhöht \(z_n\) um genau 1 bei letzter
Ziffer \(<n\) und um mindestens 2 sonst (Beweis von F.7b), und die
letzte Ziffer von \((n{+}2)q'\) ist \(q'\bmod(n{+}1)\). Bedingung 2
ist die Definition der Scharfheit. \(\square\)
(Numerisch exakt bestätigt bis \(H_7\). Die weitere Entfaltung von
Bedingung 2 in explizite Ziffernbedingungen — pro Ebene wächst der
Exzess \(e=c-\ell-1\) um eins, verlangt \(e\cdot r\le\ell\) und
Übertragsfreiheit — ist skizziert, aber noch nicht verifiziert
ausformuliert.)

**Korollar F.9b (Zählformel).** Mit \(N=(n{+}1)!\):

\[
\#\{\Omega=0\ \text{auf}\ H_n\}
=\sum_{\substack{0\le q'\le(N-1)/(n+2)\\ z_n((n+2)q')=(n+3)z_n(q')}}
\Bigl(\min\bigl(n-(q'\bmod(n{+}1)),\ N-1-q'(n{+}2)\bigr)+1\Bigr).
\]

Exakt bestätigt für \(n=1,\ldots,8\)
(\(2,5,13,23,61,111,274,564\)). Die sechste Zählfolge des Projekts
ist damit auf die Zählung der scharfen Quotienten reduziert.

### F.10, Satz: die Gleichheit im Tiefengesetz

**Satz F.10.** Für jede Schale \(m\ge3\) gilt

\[
\min_{\mu(\mathrm{val}(h))=m}\ \delta_{\mathrm{hor}}(h)\;=\;-g(m),
\qquad g(m)=m-\min\{s: M_s(m{+}1)\ge m!\}.
\]

**Beweis.** \emph{Schranke:} Sei \(h=(n,x)\) mit \(\mu(x)=m\). Für
\(P=\operatorname{struct}(x,m)\) gilt koeffizientenweise
\(P\le M_{\sigma(P)}\), also \(x=P(m{+}1)\le M_{\sigma(P)}(m{+}1)\);
wegen \(x\ge m!\) folgt \(\sigma(P)\ge s_{\min}(m)\) — der linke
Term von \(\delta\) ist mindestens \(s_{\min}\). Für
\(P_n=\operatorname{struct}(x,n)\) ist die Auswertung monoton
(nichtnegative Koeffizienten, \(\sigma\le n\)), also
\(P_n(\sigma{+}1)\le P_n(n{+}1)=x<(m{+}1)!\) — der rechte Term ist
höchstens \(m\). Zusammen \(\delta\ge s_{\min}-m=-g(m)\).

\emph{Annahme:} Sei \(x^*=M_{s_{\min}}(m{+}1)\in[m!,(m{+}1)!)\) und
\(h^*=(x^*,x^*)\) die Terminaldarstellung (konstante Struktur
\(x^*\), strukturkompakt). Dann fixiert \(K_S\) das Element, also
ist der rechte Term \(\mu(x^*)=m\); der linke ist
\(\sigma(\operatorname{struct}(x^*,m))=\sigma(M_{s_{\min}})
=s_{\min}\) (Bijektivität). Also
\(\delta(h^*)=-g(m)\). \(\square\)

(Numerisch bestätigt: Zeugen \(x^*=6,33,202,1419,11358,102229\) für
\(m=3,\ldots,8\) treffen exakt \(-g(m)\); für \(m=3\) ist der Zeuge
die Hausgeist-Zahl \((6,6)\).)

**Damit ist die untere Seite des Tiefengesetzes vollständig Satz:**
Sprungstellen exakt (\(m_g=\min\{m:g(m)\ge g\}\), Folge
\(3,15,84,\ldots\)), Asymptotik \(m_g/(g{+}2)!\to1\) (Satz F.3) und
Gleichheit \(\min\delta=-g(m)\) (dieser Satz). Offen bleibt allein
die obere Seite V1″ (Wachstumsrate von \(\sup\delta\)).

### F.11, Satz: Reduktion der β-Asymptotik auf ein explizites Maximum

**Satz F.11.** Mit \(M(r):=\max_{0\le t\le r-1} \binom{r-1}{t}^2 (r-1-t)!\) gilt

\[
\ln\beta(r,r)\;=\;\ln M(r)\;+\;O(\log r).
\]

**Beweis.** \emph{Untere Schranke:} In der Produktformel der
fallenden Fakultäten liefert das Tripel \((p,q,j)=(r{-}1,r{-}1,r{-}1{-}t)\)
zum Koeffizienten bei Grad \(d=r{-}1{+}t\) den Beitrag
\((r{-}p)(r{-}q)\binom pj\binom qj j!=\binom{r-1}{t}^2(r{-}1{-}t)!\);
da alle Beiträge nichtnegativ sind, ist
\(c_{r-1+t}(M_r^2)\ge\binom{r-1}{t}^2(r{-}1{-}t)!\) und
\(\beta(r,r)\ge\max_d(d+c_d)\ge M(r)\).
\emph{Obere Schranke:} Jeder Beitrag ist
\(\le r^2\binom{r-1}{j}^2 j!\le r^2 M(r)\) (Binomialkoeffizienten
wachsen im oberen Argument), und pro Grad gibt es höchstens \(r^3\)
Tripel; also \(c_d\le r^5 M(r)\) und
\(\beta(r,r)\le 2r+r^5M(r)\). Logarithmieren. \(\square\)

Numerisch ist die Einzelterm-Näherung sogar auf Faktor \(<4\) genau
(bis \(r=40\) geprüft); das Maximum liegt bei \(t^*\approx\sqrt r\).

**Vermutung V2′ (mit Beweisskizze).** Die Auswertung von \(M(r)\)
per Stirling (Optimierung \(t=c\sqrt r\), Maximum bei \(c=1\)) legt

\[
\ln\frac{\beta(r,r)}{r!}\;=\;\bigl(2+o(1)\bigr)\sqrt r
\]

nahe. Die Konvergenz ist logarithmisch langsam; gemessen:
\(\ln(\beta/r!)/\sqrt r=0{,}92,\ 0{,}97,\ 1{,}05,\ 1{,}12\) für
\(r=50,60,80,100\), konsistent steigend gegen die
Vergleichskurve \(2-\ln r/\sqrt r\). Die vollständige
Stirling-Ausarbeitung steht aus.

**Nachtrag zur oberen Tiefengesetz-Seite:** Der \(\sigma\le9\)-Sweep
bestätigt die Schwellen \(+3\) ab 14 und \(+4\) ab 20 als robust
gegen Vertiefung; \(+5\) rückte von 30 auf spätestens 26. Stand der
oberen Sprungstellen: \(9\) (exhaustiv), \(\le14,\ \le20,\ \le26\).

### F.9c, Satz: die vollständige Ziffernentfaltung der Scharfheit

**Satz F.9c.** Sei \(c\ge\ell+2\), \(cy<(\ell+1)!\), \(y=q(\ell+1)+r\)
und \(e=c-\ell-1\). Dann gilt (für \(y=0\) trivial wahr; \(y\ge1\)
erzwingt \(\ell\ge2\) per Gültigkeit):

\[
\operatorname{tight}(\ell,c,y)
\iff
e\,r\le\ell
\;\wedge\;
(cq\bmod\ell)+r\le\ell-1
\;\wedge\;
\operatorname{tight}(\ell-1,c,q).
\]

**Beweis.** Die Beweiskette von Satz F.8b ist exakt
\(z_\ell(cy)=u+(\ell+2)z_{\ell-1}(cq+s)\) gefolgt von drei
Abschätzungen; Gleichheit gilt genau bei Scharfheit aller drei.
Die arithmetische Abschätzung ist scharf genau bei
\(er=er\bmod(\ell+1)\), also \(er\le\ell\) (dann \(s=r\), \(u=er\)).
Die Superadditivität über die \(r\) Einzelschritte von \(cq\) aus
ist scharf genau bei durchgehender Übertragsfreiheit, also
\((cq\bmod\ell)+r\le\ell-1\) (Einzelschrittlemma aus F.7b, Basis
\(\ell\) auf Ebene \(\ell-1\)). Die dritte Abschätzung ist die
Definition von \(\operatorname{tight}(\ell-1,c,q)\). \(\square\)
(Exhaustiv verifiziert für \(\ell\le7\), \(c\le\ell+6\); der in F.9
vermerkte fehlerhafte erste Entfaltungsversuch ist damit ersetzt.)

**Korollar (Ziffernkriterium für \(\Omega=0\)).** Mit Satz F.9a ist
\(\Omega(n,x)=0\) durch einen einzigen Abstieg durch die
Ziffernentwicklung entscheidbar: Übertragsfreiheit
\((q'\bmod(n{+}1))+r'\le n\) plus die F.9c-Kette für
\((n,\,n{+}2,\,q')\) — pro Ebene zwei Ungleichungen, der Exzess
\(e\) wächst dabei um eins pro Ebene.

### F.12, Satz: die β-Asymptotik (V2′ bewiesen)

**Satz F.12.** \(\ \ln\dfrac{\beta(r,r)}{r!}=2\sqrt r+O(\log r).\)

**Beweis.** Nach Satz F.11 genügt dieselbe Aussage für
\(M(r)=\max_t\binom{s}{t}^2(s-t)!\) mit \(s:=r-1\); es ist
\(\binom st^2(s-t)!/r!=\dfrac{s!}{r\,t!^2\,(s-t)!}\).

\emph{Obere Schranke.} Mit den Stirling-Schranken
\(\ln s!\le s\ln s-s+O(\log s)\), \(\ln t!\ge t\ln t-t\),
\(\ln(s{-}t)!\ge(s{-}t)\ln(s{-}t)-(s{-}t)\) folgt für jedes \(t\)

\[
\ln\frac{s!}{t!^2(s-t)!}\;\le\;-h(t)+O(\log s),
\qquad
h(t):=2t\ln t-t+(s{-}t)\ln(s{-}t)-s\ln s .
\]

Aus der Konkavität des Logarithmus ist
\((s{-}t)\ln(s{-}t)\ge s\ln s-t(\ln s+1)\), also
\(h(t)\ge t\,(2\ln t-\ln s-2)=:\varphi(t)\); die Funktion
\(\varphi\) hat ihr Minimum bei \(t=\sqrt s\) mit Wert
\(-2\sqrt s\). Also \(\ln(M(r)/r!)\le2\sqrt s+O(\log s)\).

\emph{Untere Schranke.} Wähle \(t=\lceil\sqrt s\rceil\). Mit
\(\binom st\ge(s-t)^t/t!\) und \(\ln t!\le t\ln t-t+O(\log t)\):

\[
\ln\frac{\binom st^2(s-t)!}{r!}
=\ln\binom st-\ln t!-\ln r
\ \ge\ t\ln\frac{s-t}{t^2}+2t-O(\log r)
\ =\ 2\sqrt s-O(\log r),
\]

da \((s-t)/t^2=1-O(1/\sqrt s)\), also
\(t\ln((s-t)/t^2)=-O(1)\). \(\square\)

(Numerik: Die Kernungleichung \(h(t)\ge-2\sqrt s\) hält mit
Sicherheitsabstand \(\approx\tfrac12\) bis \(s=10^4\); der gemessene
Abstand \(2\sqrt r-\ln(\beta/r!)\approx\tfrac32\ln r+2{,}3\) liegt
im \(O(\log r)\)-Fenster und benennt die vermutete Feinstruktur:
\(\ln(\beta/r!)=2\sqrt r-\tfrac32\ln r+O(1)\), offen.)

### F.13, Satz: die Ein-Ziffern-Fakultäten, vollständig

**Satz F.13.** \(n!\) ist genau dann eine Ein-Ziffern-Zahl in seiner
eigenen Schale \(H_n\), wenn

\[
n=\frac{(i+1)!}{d}-1
\qquad\text{für ganze }i\ge1,\ 1\le d\le i;
\]

die Ziffer ist dann \(d\) an Position \(i\). Pro Position \(i\) gibt
es **genau \(i\)** solche Fakultäten.

**Beweis.** Ist \(n!\) eine Einzelziffer \(d\) an Position \(i\), so
gilt \(n!=d\,(n+1)!/(i+1)!\), also \(d=(i+1)!/(n+1)\), und die
Ziffernschranke verlangt \(d\le i\). Umgekehrt: Für
\(n+1=(i+1)!/d\) mit \(1\le d\le i\) teilt \(d\) die Zahl
\((i+1)!\) automatisch (da \(d\le i<i+1\)), und

\[
d\cdot\frac{(n+1)!}{(i+1)!}
=d\cdot\frac{(n+1)\,n!}{(i+1)!}
=d\cdot\frac{(i+1)!/d}{(i+1)!}\cdot n!
=n! ,
\]

sodass die (eindeutige) Ziffernentwicklung von \(n!\) genau die
Einzelziffer \(d\) an Position \(i\) ist; die Positionsgültigkeit
folgt aus \(n+1\ge(i+1)!/i\ge i+1\). Die Zählung: \(d\) durchläuft
bijektiv \(1,\ldots,i\). \(\square\)

Vorhersagetest (Nr. 5–9 des Projekts, alle exakt): Position
\(i=5\) liefert \(n=143,179,239,359,719\) — sämtlich bestätigt.
Die Folge der Ein-Ziffern-Fakultäten

\[
2,\ 5,\ 7,\ 11,\ 23,\ 29,\ 39,\ 59,\ 119,\ 143,\ 179,\ 239,\ 359,\
719,\ 839,\ \ldots
\]

ist die **achte** OEIS-unbekannte Folge des Projekts — und die
erste mit vollständig geschlossener Beschreibung schon bei der
Entdeckung. Über Satz F.6 (Ziffernformel) liefert F.13 zugleich
exakte \(N(n)\)-Werte für alle diese \(n\):
\(N((i{+}1)!/d-1)=d\cdot\bigl((i{+}1)!/d-1\bigr)!/i!\)\,.

### F.14, Satz: obere Schranke für die Reihenfolge-Gleichgültigen

**Satz F.14.** Für die Anzahl der Elemente mit \(\Omega=0\) auf
\(H_n\) gilt

\[
\#\{\Omega=0\}\;\le\;(n{+}1)\prod_{\ell=1}^{n}
\Bigl(\Bigl\lfloor\tfrac{\ell}{n+1-\ell}\Bigr\rfloor+1\Bigr)
\;\le\;\frac{(n{+}1)^{\,n+1}}{n!},
\qquad\text{also}\quad
\ln\#\{\Omega=0\}\le n+O(\log n).
\]

**Beweis.** Nach Satz F.9a ist jedes solche Element durch
\((q',r')\) mit scharfem \(q'\) und \(r'\le n\) bestimmt (höchstens
\(n{+}1\) Werte für \(r'\)). Nach Satz F.9c erzwingt die Scharfheit
auf Ebene \(\ell\) die Bedingung \((n{+}1{-}\ell)\,r_\ell\le\ell\),
also \(r_\ell\le\lfloor\ell/(n{+}1{-}\ell)\rfloor\) für jede Ziffer
von \(q'\); die Ziffern bestimmen \(q'\) eindeutig. Für die
geschlossene Form: mit \(j=n{+}1{-}\ell\) ist
\(\lfloor\ell/j\rfloor+1\le(\ell+j)/j=(n{+}1)/j\), also ist das
Produkt höchstens \((n{+}1)^n/n!\); Stirling gibt
\(\ln\bigl((n{+}1)^{n+1}/n!\bigr)=n+O(\log n)\). \(\square\)

**Korollar.** Der Anteil der reihenfolge-gleichgültigen Elemente an
\(H_n\) ist höchstens \((n{+}1)^{n+1}/(n!\,(n{+}1)!)\), fällt also
wie \(e^{-(1+o(1))\,n\ln n}\): Gleichgültigkeit gegenüber der
Wachstumsreihenfolge ist asymptotisch extrem selten.
(Daten: \(\ln\#\{\Omega=0\}\approx0{,}8\,n\) — die Schranke trifft
die Größenordnung; eine untere Schranke erfordert eine
übertragsbewusste Konstruktion und ist offen.)

---

## Anhang H. Das Horizontkalkül (14. Juli 2026)

Anlass: GPT-Vorschlag vom 14.07.2026 („Horizontkalkül"). Von den vier
dort vorgeschlagenen Sätzen waren zwei bereits Bestand (Satz 1 =
S9/S15, Satz 2 = Reduktionsargument der Definition 11.2). Neu und
hier bewiesen: das allgemeine Extremalprinzip und der
Differenzüberlauf. Rechnerische Verifikation:
`experiments_horizontkalkuel.py` (exhaustiv über alle \((r+1)!\)
Elemente bis \(r=8\)).

### Definition H.0, Horizontkalkül

Für einen \(k\)-stelligen Operator \(T\) auf dem Strukturhalbring
\(\mathcal S\) sei

\[
\Gamma_T(r_1,\ldots,r_k)
=
\max\{\sigma(T(P_1,\ldots,P_k)) \mid \sigma(P_i)\le r_i\}.
\]

Bekannt sind \(\Gamma_+(r,s)=r+s\) (S9/S15) und
\(\Gamma_\times(r,s)=\beta(r,s)=\sigma(M_rM_s)\) (Def. 11.2) mit dem
maximal gefüllten Polynom \(M_r(X)=\sum_{d=0}^{r-1}(r-d)X^{\underline d}\).

### Satz H.1, Extremalprinzip (S39)

Sei \(T\) ein \(k\)-stelliger Operator auf \(\mathcal S\), der
**koeffizientenmonoton** ist: aus \(P\preceq P'\) (koeffizientenweise
\(\le\)) folgt \(T(\ldots,P,\ldots)\preceq T(\ldots,P',\ldots)\) in
jedem Argument. Dann gilt

\[
\Gamma_T(r_1,\ldots,r_k)=\sigma\bigl(T(M_{r_1},\ldots,M_{r_k})\bigr).
\]

Insbesondere ist jeder aus Addition, Multiplikation und der
Horizontableitung \(\Delta\) zusammengesetzte Operator
koeffizientenmonoton (alle Strukturkonstanten sind nichtnegativ).

**Beweis.** \(\sigma(P)=\max_{c_d>0}(d+c_d)\) ist monoton bezüglich
\(\preceq\). \(\sigma(P)\le r\) ist äquivalent zu \(c_d\le r-d\) für
alle \(d\), also zu \(P\preceq M_r\). Monotonie von \(T\) liefert
\(T(P_1,\ldots,P_k)\preceq T(M_{r_1},\ldots,M_{r_k})\), Monotonie von
\(\sigma\) die Ungleichung \(\le\); da \(\sigma(M_{r_i})=r_i\), wird
die Schranke bei \((M_{r_1},\ldots,M_{r_k})\) angenommen. Zur
Zusatzaussage: \(+\) und \(\Delta\) sind koeffizientenweise linear mit
nichtnegativen Konstanten (\(\Delta X^{\underline d}=d\,X^{\underline{d-1}}\));
für \(\times\) sind die Linearisierungskoeffizienten
\(\binom pj\binom qj j!\) nichtnegativ, und Bilinearität überträgt
die Monotonie. Kompositionen monotoner Operatoren sind monoton.
\(\square\)

Das ist die Verallgemeinerung des Reduktionsarguments aus Definition
11.2: Der Suchraum der Größe \((r_1+1)!\cdots(r_k+1)!\) kollabiert
auf ein einziges kanonisches Produkt. Rechnerisch bestätigt auch für
den zusammengesetzten Operator \(T(P,Q)=\Delta(PQ)\) (\(r,s\le3\),
exhaustiv).

### Satz H.2, Differenzüberlauf (S40)

Für \(r\ge2\) gilt

\[
\Gamma_\Delta(r)
=\max_{\sigma(P)\le r}\sigma(\Delta P)
=\left\lfloor\frac{(r+1)^2}{4}\right\rfloor-1 .
\]

Ein einzelner Koeffizient genügt als Zeuge: \(P=(r-d)\,X^{\underline d}\)
mit \(d=\lfloor(r+1)/2\rfloor\).

**Beweis.** Nach H.1 ist \(\Gamma_\Delta(r)=\sigma(\Delta M_r)\).
\(\Delta M_r\) hat die Koeffizienten \(b_k=(k+1)(r-k-1)\) für
\(k=0,\ldots,r-2\), also

\[
\sigma(\Delta M_r)
=\max_{0\le k\le r-2}\bigl[k+(k+1)(r-k-1)\bigr]
=\max_{0\le k\le r-2}(k+1)(r-k)-1 .
\]

Mit \(u=k+1\in\{1,\ldots,r-1\}\) ist \(u(r+1-u)\) maximal bei
\(u=\lfloor(r+1)/2\rfloor\) mit Wert \(\lfloor(r+1)^2/4\rfloor\)
(Produkt zweier Zahlen mit fester Summe \(r+1\)); der Randfall
\(u\le r-1\) ist für \(r\ge2\) erfüllt. Für den Ein-Koeffizienten-Zeugen:
\(P=(r-d)X^{\underline d}\) hat \(\sigma(P)=r\) und
\(\sigma(\Delta P)=d-1+d(r-d)=d(r+1-d)-1\), maximal bei
\(d=\lfloor(r+1)/2\rfloor\) mit demselben Wert. \(\square\)

Werte: \(\Gamma_\Delta(2\ldots8)=1,3,5,8,11,15,19\) (exhaustiv
bestätigt bis \(r=8\)).

**Einordnung.** \(\Delta\) senkt den Grad um eins, kann den
Strukturhorizont aber quadratisch erhöhen: Grad misst Dimension,
\(\sigma\) misst Kapazität — eine Gradfiltration sieht diesen Effekt
nicht. Zusammen mit \(\Gamma_+=r+s\) (linear) und
\(\Gamma_\times=\beta\) (im Wesentlichen fakultätisch, S36) hat jede
Grundoperation ihr eigenes exaktes Wachstumsgesetz.

### Bemerkung H.3, intrinsische Differenzformel

Aus der Newton-Entwicklung \(c_d=\Delta^dP(0)/d!\) folgt

\[
\sigma(P)=\max_{\Delta^dP(0)>0}\Bigl(d+\frac{\Delta^dP(0)}{d!}\Bigr),
\qquad
\sigma(P)\le r\iff 0\le\Delta^dP(0)\le(r-d)\,d!\ \text{für alle }d .
\]

Der Strukturhorizont ist damit ohne Ziffern und ohne Basiswechsel
beschreibbar: eine **Kapazitätshöhe** auf dem Halbring der
nichtnegativen Newton-Polynome. Er ist *keine* Bitkomplexität
(\(\sigma(10^{100})=10^{100}\)): Er misst unär interpretierte
kombinatorische Kapazität, nicht Speicherbedarf.

### Einordnung H.4, Literaturlage

Additiv ist \((\mathcal F_r)_r\) mit
\(\mathcal F_r=\{P:\sigma(P)\le r\}\), \(|\mathcal F_r|=(r+1)!\),
eine klassisch verträgliche Filtration
(\(\mathcal F_r+\mathcal F_s\subseteq\mathcal F_{r+s}\), scharf);
multiplikativ ist sie **nichtlinear** mit optimalem Wachstumsgesetz
\(\beta\). Eine etablierte Höhenfunktion \(\max_d(d+c_d)\) auf
Newton-Koeffizienten wurde in der gezielten Suche (GPT, 14.07.2026)
nicht gefunden — kein Neuheitsbeweis, aber die Vermutung „nur eine
bekannte Standardhöhe unter anderem Namen" hat sich nicht bestätigt.
Klassische Höhen (\(\max|c_d|\), Grad-plus-log-Höhe) koppeln Grad und
Koeffizient nicht lokal; es gilt
\(\max(\deg P+1,H(P))\le\sigma(P)\le\deg P+H(P)\) für
\(H(P)=\max_d c_d\), \(P\neq0\).

### Satz H.5, Kompositionsabschluss (S41)

\(\mathcal S\) ist unter Komposition abgeschlossen: für
\(P,Q\in\mathcal S\) ist \(P\circ Q\in\mathcal S\). Ferner ist
\(\circ\) in beiden Argumenten koeffizientenmonoton; mit Satz H.1
folgt

\[
\Gamma_\circ(r,s)
=\max\{\sigma(P\circ Q)\mid \sigma(P)\le r,\ \sigma(Q)\le s\}
=\sigma(M_r\circ M_s).
\]

**Beweis.** Wegen
\(P\circ Q=\sum_d c_d(P)\,(Q)^{\underline d}\) mit
\((Q)^{\underline d}=Q(Q-1)\cdots(Q-d+1)\) und der Abgeschlossenheit
von \(\mathcal S\) unter Addition und \(\mathbb N_0\)-Vielfachen
genügt es, \((Q)^{\underline d}\in\mathcal S\) zu zeigen.

Schreibe \(Q=\sum_k a_kX^{\underline k}\) mit \(a_k\in\mathbb N_0\)
und wähle paarweise disjunkte endliche Mengen \(T_k\) mit
\(|T_k|=a_k\) („Schablonen der Stelligkeit \(k\)"). Für
\(x\in\mathbb N_0\) sei eine **Q-Struktur** auf \([x]\) ein Paar
\((t,\varphi)\) aus einer Schablone \(t\in T_k\) und einer Injektion
\(\varphi\colon[k]\hookrightarrow[x]\); ihre Anzahl ist
\(\sum_k a_k\,x^{\underline k}=Q(x)\). Also zählt
\(Q(x)^{\underline d}\) die \(d\)-Tupel paarweise verschiedener
Q-Strukturen auf \([x]\).

Klassifiziere die Tupel nach der Vereinigung \(U\subseteq[x]\) der
Bilder aller beteiligten Injektionen. Die Anzahl \(N_m\) der Tupel,
deren Bildvereinigung eine feste \(m\)-Menge **ganz ausschöpft**,
hängt nur von \(m\) ab, und es gilt für alle \(x\in\mathbb N_0\)

\[
Q(x)^{\underline d}=\sum_m N_m\binom xm ,
\]

also als Polynomidentität. Die symmetrische Gruppe \(S_m\) wirkt auf
den ausschöpfenden Tupeln durch Umbenennung der Grundmenge,
\(\pi\cdot(t,\varphi)=(t,\pi\circ\varphi)\). **Diese Wirkung ist
frei:** Fixiert \(\pi\) jedes Tupelglied, so fixiert \(\pi\) jedes
Bild punktweise, wegen der Ausschöpfung also ganz \([m]\), d.\,h.
\(\pi=\mathrm{id}\). (Strukturen der Stelligkeit 0 stören nicht: Sie
tragen nichts zur Vereinigung bei, die Ausschöpfung wird von den
übrigen geleistet.) Folglich \(m!\mid N_m\), und

\[
(Q)^{\underline d}=\sum_m \frac{N_m}{m!}\,X^{\underline m}
\]

hat Koeffizienten in \(\mathbb N_0\) — Positivität **und**
Ganzzahligkeit in einem Zug.

Monotonie: In \(P\) ist \(\circ\) eine
\(\mathbb N_0\)-Linearkombination der \((Q)^{\underline d}\in\mathcal S\).
In \(Q\): Aus \(a_k\le a_k'\) folgt \(T_k\subseteq T_k'\); jedes
Tupel von Q-Strukturen ist dann eines von Q′-Strukturen mit gleicher
Bildvereinigung, also \(N_m\le N_m'\) termweise und
\((Q)^{\underline d}\preceq(Q')^{\underline d}\). \(\square\)

Rechnerisch bestätigt: Abschluss und Extremalprinzip exhaustiv für
\(r,s\le4\) (alle \((r{+}1)!\,(s{+}1)!\) Paare), Abschluss zusätzlich
für 300 Zufallspaare bis \(\sigma=8\)
(`experiments_komposition.py`).

Erste Werte (man beachte die Asymmetrie, z.\,B.
\(\Gamma_\circ(3,4)=88\ne251=\Gamma_\circ(4,3)\)):

\[
\begin{array}{c|cccc}
\Gamma_\circ(r,s)&1&2&3&4\\
\hline
1&1&1&1&1\\
2&3&4&5&6\\
3&5&9&23&88\\
4&7&18&251&6541
\end{array}
\]

Die Diagonale

\[
\Gamma_\circ(r,r)=1,\ 4,\ 23,\ 6541,\ 477149751,\
26594371862819905,\ \ldots
\]

ist OEIS-unbekannt (Negativbefund 14.07.2026) — die **neunte
Zählfolge** des Projekts. Ihre Asymptotik ist offen (empirisch
\(\ln\Gamma_\circ(r,r)\) etwa von der Ordnung \(r^2\log r\); keine
Vermutung mit Beweisanspruch).

### Satz H.6, Shift-Überlauf (S42)

Für den Verschiebeoperator \(E\,P(X)=P(X{+}1)\) gilt

\[
\Gamma_E(r)=r+\left\lfloor\frac{r^2}{4}\right\rfloor
=\Gamma_\Delta(r{+}1)\qquad(r\ge1).
\]

**Beweis.** \(E\) ist linear mit nichtnegativen Konstanten
(\((X{+}1)^{\underline d}=X^{\underline d}+d\,X^{\underline{d-1}}\),
Spezialfall von H.5), also gilt H.1:
\(\Gamma_E(r)=\sigma(E\,M_r)\). \(E\,M_r\) hat die Koeffizienten
\(c_k=(r{-}k)+(k{+}1)(r{-}k{-}1)\) für \(k\le r{-}2\) und
\(c_{r-1}=1\), also
\(k+c_k=r+(k{+}1)(r{-}k{-}1)\); das Produkt zweier Zahlen mit Summe
\(r\) ist maximal \(\lfloor r^2/4\rfloor\). Die zweite Gleichheit
ist die Identität
\(r+\lfloor r^2/4\rfloor=\lfloor(r{+}2)^2/4\rfloor-1\). \(\square\)

Verschieben kostet exakt so viel wie Ableiten einen Horizont höher —
und die Wertfolge \(1,3,5,8,11,15,19,\ldots\) ist die klassische
Viertelquadrat-Folge A024206. Ehrlichkeitsvermerk: Damit sind die
**Wertfolgen** von \(\Gamma_\Delta\) und \(\Gamma_E\) bekannte
Zahlen; neu sind die Gesetze, nicht die Folgen. Die
Kompositions-Diagonale dagegen ist auch als Folge neu.

### Einordnung H.7, Literaturlage der Komposition

Das stetige Analogon ist klassisch: Absolut monotone Funktionen
(alle Ableitungen \(\ge0\)) sind unter Komposition abgeschlossen
(Faà di Bruno / Bernstein). Satz H.5 ist die diskrete
**Gitterverschärfung**: Er liefert nicht nur die Positivität aller
Differenzenordnungen, sondern die Teilbarkeit \(m!\mid N_m\) — also
Abgeschlossenheit im \(\mathbb N_0\)-Gitter der fallenden
Fakultätsbasis, nicht bloß im Binomialgitter. Für diese
Gitterfassung samt Kapazitätskalkül \(\Gamma_\circ\) wurde bei
gezielter Suche (14.07.2026) kein Literaturtreffer gefunden; wie
immer ist das kein Neuheitsbeweis.

---

## Anhang I. Die Zählbreite: eine #P-Interpretation der Strukturpolynome (14. Juli 2026)

Anlass: GPT-Einordnung vom 14.07.2026, hier geprüft, präzisiert und
mit Literatur unterlegt. Numerische Gegenprobe der Zählsemantik:
`experiments_komposition.py`-Umfeld (200 Zufallstests, Skript im
Chat-Protokoll; Kernidentitäten trivial nachrechenbar).

### I.1 Einbettung in die binomial-guten Polynome

Wegen \(X^{\underline d}=d!\binom Xd\) hat jedes
\(P=\sum_d c_dX^{\underline d}\in\mathcal S\) in der Binomialbasis
die Koeffizienten \(b_d=c_d\,d!\in\mathbb N_0\). Polynome mit
\(b_d\in\mathbb N_0\) heißen in der Zählkomplexität
**binomial-good** (Ikenmeyer–Pak, *What is in #P and what is not?*,
FOCS 2022, arXiv:2204.13149): Für univariate \(\varphi\) gilt dort
\(\varphi(\#P)\subseteq\#P\) genau dann, wenn alle
Binomialbasis-Koeffizienten in \(\mathbb N_0\) liegen.

Also: \(\mathcal S\subsetneq\) binomial-good — **echte** Teilklasse
(\(\binom X2\) ist binomial-good, aber \(c_2=\tfrac12\notin\mathbb N_0\)).
Die Teilbarkeit \(d!\mid b_d\) ist genau der Unterschied zwischen
**geordneten Tupeln** und ungeordneten Auswahlen: binomial-good
zählt gefärbte Teilmengen, \(\mathcal S\) zählt gefärbte geordnete
Tupel.

### Satz I.2, Hori-#P-Satz (S43)

Ist \(f\in\#P\) und \(P\in\mathcal S\), so ist \(P\circ f\in\#P\).

**Beweis (elementar, ohne die allgemeine Theorie).** Sei \(f(x)\)
die Anzahl der Zeugen von \(x\) unter einem polynomiellen
Verifizierer \(V\). Neue Maschine: Rate
\(d\in\{0,\ldots,\deg P\}\), rate eine Variante
\(\ell\in\{1,\ldots,c_d\}\), rate \(d\) Zeugenkandidaten
\(w_1,\ldots,w_d\); akzeptiere, wenn alle \(w_i\) von \(V\)
akzeptiert werden und paarweise verschieden sind. Da \(\deg P\)
fest ist, bleibt alles polynomiell, und die Anzahl akzeptierender
Pfade ist exakt
\(\sum_d c_d\,f(x)^{\underline d}=P(f(x))\). \(\square\)

(Die Aussage folgt auch aus der bekannten binomial-good-Richtung
von Ikenmeyer–Pak; der obige Beweis ist selbständig und zeigt die
Zählsemantik direkt.)

### I.3 Die Zählsemantik der Hori-Operationen

- **Ein Term \(c_dX^{\underline d}\):** \(c_d\) Varianten
  („Farben") geordneter \(d\)-Tupel verschiedener Zeugen.
- **Addition** = disjunkte Vereinigung von Zählkonstruktionen.
- **Multiplikation** = Kopplung zweier Konstruktionen; die
  Linearisierungskoeffizienten \(\binom pj\binom qj j!\) zählen
  exakt die Überlappungsmuster zweier Zeugengruppen
  (\(j\) gemeinsame Zeugen, Positionswahl, Zuordnung). Das
  \(\beta\)-Wachstum misst also die Explosion der
  Überlappungsmuster.
- **Horizontableitung:** \((n{+}1)^{\underline d}-n^{\underline d}
  =d\,n^{\underline{d-1}}\) zählt die Strukturen, die ein **neuer
  Zeuge** ermöglicht (\(d\) Positionen mal Rest-Tupel). \(\Delta\)
  ist der Operator des marginalen Zeugen-Zuwachses; der
  Differenzüberlauf (S40) besagt: Ein zusätzlicher Zeuge senkt die
  Tupelordnung, kann die Variantenvielfalt aber quadratisch
  aufblähen.
- **Strukturhorizont:** Zeichnet man das Koeffizientenbrett
  (Spalte \(d\) mit \(c_d\) Kästchen), so ist
  \(\sigma(P)=\max(d+c_d)\) die kleinste **Treppe**, in die das
  Brett passt — in der Zählsemantik das Maximum aus
  „wie viele Zeugen gleichzeitig" plus „wie viele Varianten davon":
  die **Zählbreite** (Arbeitsbegriff; engl. etwa *witness-gadget
  width*).

### I.4 Die endliche Hierarchie

\(\mathcal C_r=\{P\in\mathcal S:\sigma(P)\le r\}\) ist eine endliche,
vollständig aufzählbare Familie von \#P-Abschlussoperatoren mit
\(|\mathcal C_r|=(r+1)!\), und das Horizontkalkül (Anhang H) wird zu
einem Kapazitätskalkül für Zähloperatoren:
\(\mathcal C_r+\mathcal C_s\subseteq\mathcal C_{r+s}\),
\(\Delta(\mathcal C_r)\subseteq\mathcal C_{\Gamma_\Delta(r)}\),
\(\mathcal C_r\mathcal C_s\subseteq\mathcal C_{\beta(r,s)}\),
\(\mathcal C_r\circ\mathcal C_s\subseteq\mathcal C_{\Gamma_\circ(r,s)}\)
— jeweils optimal (Extremalprinzip).

### I.5 Einordnung und Abgrenzung

**Bekannt:** die qualitative Schicht — binomial-good als (bewiesene
univariate) Charakterisierung der \#P-Abschlussoperationen; die
fallende Fakultätsbasis in der Rook-Theorie (z.\,B.
arXiv:2312.10855). **Offenbar neu:** die quantitative Schicht — die
Höhe \(\max(d+c_d)\), die \((r+1)!\)-Hierarchie \(\mathcal C_r\)
und ihre optimalen Wachstumsgesetze. **Ausdrücklich kein
Anspruch:** Die *Binomial Basis Conjecture* (alle polynomiellen
\#P-Abschlussoperationen relativieren; schon die univariate Fassung
impliziert P\(\ne\)NP) bleibt von alledem unberührt — die
Hori-Operatoren liegen auf der gut verstandenen, relativierenden
Seite. Der mögliche Beitrag ist bescheidener und präziser: aus der
qualitativen Klassifikation („erlaubt / nicht erlaubt") erstmals
eine endliche quantitative Hierarchie („Zählbreite \(r\)") zu
machen.

---

## Anhang J. Einordnung: Inversionsfolgen, Gitter, Operatorrechnung (14. Juli 2026)

Anlass: GPT-Einordnung vom 14.07.2026, hier geprüft (Kernidentitäten
exhaustiv, `experiments_einordnung.py`) und mit verifizierten
Literaturtiteln unterlegt. Dies ist der Schlussstein: die Verortung
der Horimetrik auf bekanntem Boden.

### Satz J.1, Inversionsfolgen-Bijektion (S44)

Für \(a\in H_n\) setze \(e=(0,a_1,\ldots,a_n)\). Dann gilt
\(0\le e_j<j\) für \(j=1,\ldots,n{+}1\) — \(e\) ist eine
**Inversionsfolge** der Länge \(n{+}1\). Die Abbildung
\(\pi\mapsto(e_j)\), \(e_j=|\{i<j:\pi_i>\pi_j\}|\), ist die
klassische Bijektion zu \(S_{n+1}\). Somit
\(H_n\cong\{\text{Inversionsfolgen der Länge }n{+}1\}\cong S_{n+1}\).

Der Strukturhorizont wird zur Permutationsstatistik: mit
\(c_d=e_{n-d+1}\) ist
\[
\sigma(P_a)=n-\min_{e_j>0}\bigl((j{-}1)-e_j\bigr),
\]
und die Niveaus sind exakt abzählbar,
\[
|\{a\in H_n:\sigma(P_a)\le r\}|=(r{+}1)!,\qquad
|\{a\in H_n:\sigma(P_a)=r\}|=r\cdot r!\quad(r\ge1).
\]
(Beweis siehe Buch, Anhang B; exhaustiv bestätigt bis \(n=6\).)

**Offen (V13):** Entspricht \(\sigma\) unter der Bijektion einer
klassischen Permutationsstatistik? Die Extremfälle \(e_j=j-1\) sind
in der Literatur als *tight entries* bekannt (Inversionsfolgen-Muster,
arXiv:1510.05434); \(\sigma\) verfeinert das zum minimalen Abstand
zur oberen Schranke.

### J.2, Gitterstruktur

Koordinatenweiser Vergleich macht \(H_n\) zu einem Produkt
endlicher Ketten, also einem **distributiven Gitter**;
\(\min,\max\) sind stellenweise. \(\mathcal F_r=\{P:\sigma(P)\le r\}\)
ist das **Hauptideal** \(\{P:P\le M_r\}\) unter der randvollen
Gestalt, und \(\sigma(P)\) ist die kleinste Stufe der Kette
\(M_1\le M_2\le\cdots\), deren Ideal \(P\) enthält — die
ordnungstheoretische Fassung des Extremalprinzips. Dieselbe Ordnung
auf Inversionscodes ist die *middle order* zwischen schwacher und
Bruhat-Ordnung (arXiv:2405.08943). Anschlussfragen (offen): Sind
\(Z,L,K_V,K_S\) monoton? Ist der Kommutator ein Gitterdefekt?

### J.3, Operatorrechnung und Nachbargebiete

Die fallenden Fakultäten sind die Hausbasis der finiten
Operatorrechnung (\(\Delta\) als Delta-Operator; umbrale Algebra,
arXiv:2407.16348); Strukturpolynome und Horizontableitung sind dort
verortet. Der horimetrische Zusatz ist das **Kapazitätskalkül**
\(\Gamma_T\) (Anhang H) — eine Buchhaltung über etablierten
Operatoren. Als Forschungsprogramm notiert, nicht ausgeführt:
\(s\)-Inversionsfolgen und Lecture-Hall-Polytope (allgemeine
Kapazitätsprofile \(0\le a_i<s_i\); Type-B: arXiv:1310.5313,
Level-Algebren: arXiv:1710.10892) als mögliche „\(s\)-Horimetrik";
Rook-Theorie (welche Gestalten sind Rook-Polynome von Brettern?);
kombinatorische Spezies als gemeinsame Sprache der
Zählinterpretationen (arXiv:2305.05059).

### Einordnung J.4, die drei Ausgänge

Ein unbekannter Grundraum wäre verdächtig (schlecht gesucht); eine
bekannte vollständige Theorie wäre ein Ende (alte Mathematik neu
angemalt). Die Horimetrik landet im dritten, besten Fall: **bekannter
Grundraum (Inversionsfolgen / Permutationscodes in einem bekannten
Gitter, geschrieben in der Hausbasis der Differenzenrechnung), darauf
neue Operationen und neue Sätze** (zwei Wachstums- und zwei
Aufräumbegriffe, Seitentreue, Kapazitäts- und Zählbreitenkalkül).
Damit ist die Theorie mathematisch eingeordnet — der natürliche
Abschluss des Buchprojekts.
