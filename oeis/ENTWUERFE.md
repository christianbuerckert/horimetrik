# OEIS-Einreichungsentwürfe (neun Folgen)

**Stand 14.07.2026:** Alle neun Folgen, feldgenau nach dem
OEIS-Einreichungsformular gegliedert. **Schnellster Weg:** In
`internal/folge1.txt` … `folge9.txt` liegt jede Folge fertig im
OEIS-\*internal format\* (%-Zeilen, erzeugt und formal geprüft von
`programme/experiments_oeis_internal.py`) — Datei öffnen, alles
kopieren, in das große Textfeld von „Submitting a New Sequence“
einfügen, fertig. Die Blöcke unten sind die Feld-für-Feld-Variante
derselben Inhalte (NAME / DATA / OFFSET /
COMMENTS / REFERENCES / LINKS / FORMULA / EXAMPLE / PROG /
CROSSREFS / KEYWORD) — Inhalte einfach in die jeweiligen
Formularfelder kopieren. MAPLE/MATHEMATICA bleiben leer, AUTHOR
füllt das System (Christian Felix Bürckert). Die b-Files in
`bfiles/` erzeugt und verifiziert
`programme/experiments_oeis_bfiles.py`; laut Formular werden sie
**nach** der Freischaltung per Edit nachgereicht (Format der
LINKS-Zeile steht jeweils dabei).

**Formular-Regeln, hier eingehalten:** DATA kommagetrennt und unter
260 Zeichen (Rest ins b-File); COMMENTS und FORMULA sagen explizit,
was bewiesen und was nur beobachtet ist; Einträge sind englisch und
jargonfrei. Alle Einträge wiederholen die Grundkonstruktion, da
OEIS-Einträge self-contained sein müssen.

**Grundkonstruktion (Baukasten):** digit sequences (a_1,...,a_n)
with 0 <= a_i <= i, value V(a) = Sum_{i=1..n} a_i\*(n+1)!/(i+1)!,
structure polynomial P(X) = Sum_d a_{n-d}\*X_(d) in the falling
factorial basis X_(d) = X\*(X-1)\*...\*(X-d+1), and
sigma(P) = max over nonzero coefficients c_d of (d + c_d).

---

## Folge 1 (zuerst einreichen, stärkster Eintrag): Sprungstellen

**NAME:**
a(g) is the least m such that Sum_{d=0}^{m-g-1} (m-g-d) * (m+1)!/(m+1-d)! >= m!.

**DATA:**
3,15,84,533,3883,31998,294875,3006206,33603002,408733041,5375410231,76013015079,1150206933969,18545538085994,317435032141745,5748797568046347,109827594310217168,2207457411249752035,46565493803467062165,1028649317126730207600

**OFFSET:** 1

**COMMENTS:**
In the Horimetrik framework (a positional number system with decreasing bases; see LINKS) this is the sequence of "jump positions of the depth law" (Sprungstellen des Tiefengesetzes).
Arises in the mixed-radix positional system with decreasing bases (digit i has base i+1, so the most significant digit is binary): a(g) is the first "factorial shell" [m!, (m+1)!) containing a value whose digit-polynomial support height sigma lies g below the shell index; equivalently, the first shell where the commutator of the two natural compactification operators of that system reaches depth -g.
The defining sum satisfies the identity S(m,g)/m! = (m+1) * Sum_{k=1}^{m-g} k/(g+k+1)!, which makes distant terms computable.
Proved: (g+2)!/c(g) <= a(g)+1 <= (g+2)! with c(g) = (g+2)! * Sum_{k>=1} k/(g+k+1)! = 1 + O(1/g), hence a(g)/(g+2)! -> 1.

**REFERENCES:** (leer)

**LINKS:**
Christian Felix Bürckert, <a href="https://github.com/christianbuerckert/horimetrik">Horimetrik — Zahlen mit Horizont (book, proofs, and programs, in German)</a>
Christian Felix Bürckert, <a href="https://github.com/christianbuerckert/horimetrik/blob/main/buch/main.pdf">Horimetrik - Zahlen mit Horizont (book PDF, in German)</a>
Christian Felix Bürckert, <a href="https://github.com/christianbuerckert/horimetrik/blob/main/book/main.pdf">Horimetrik - Numbers with a Horizon (book PDF, English translation)</a>
Christian Felix Bürckert, <a href="https://doi.org/10.5281/zenodo.21400755">Horimetrik - Zahlen mit Horizont / Numbers with a Horizon (archived books and paper, Zenodo)</a>
[Nach Freischaltung per Edit: Christian Felix Bürckert, <a href="/A??????/b??????.txt">Table of g, a(g) for g = 1..20</a>]

**FORMULA:**
a(g) ~ (g+2)! (see COMMENTS for two-sided bounds).

**EXAMPLE:**
For g=1: with M_s(X) = Sum_{d<s} (s-d)*X_(d) in the falling factorial basis, m=3 is the least m with M_{m-1}(m+1) >= m!, since M_2(4) = 2 + 4 = 6 >= 3! = 6, while M_1(3) = 1 < 2! = 2 fails for m=2. So a(1)=3.

**PROG:**
(Python)
```python
from fractions import Fraction
from math import factorial
def a(g, K=400):
    S = [Fraction(0)]
    for k in range(1, K+1):
        S.append(S[-1] + Fraction(k, factorial(g+k+1)))
    tail = Fraction(2*(K+1), factorial(g+K+2))  # certified tail bound
    def ge1(m):
        t = m - g
        if t <= 0: return False
        if t <= K: return (m+1)*S[t] >= 1
        if (m+1)*S[K] >= 1: return True
        assert (m+1)*(S[K]+tail) < 1
        return False
    lo, hi = g+1, factorial(g+2)-1
    while lo < hi:
        mid = (lo+hi)//2
        if ge1(mid): hi = mid
        else: lo = mid+1
    return lo
```

**CROSSREFS:**
Cf. A000142. [Nach A-Nummern-Vergabe: Querverweise auf die übrigen Horimetrik-Folgen ergänzen]

**KEYWORD:** nonn,hard

**b-File:** bfiles/folge1_sprungstellen.txt (g = 1..20)

---

## Folge 2: maximale Produkthöhe von Quadraten

**NAME:**
a(n) = max over d of (d + c_d), where Sum_d c_d*X_(d) is the square of M_n(X) = Sum_{d=0}^{n-1} (n-d)*X_(d), expanded in the falling factorial basis X_(d) = X*(X-1)*...*(X-d+1).

**DATA:**
1,6,22,87,407,2473,19527,170720,1643913,18042957,233850057,3239053262,47820134904,750414817981,12481922930743,223531510857897,4466575128428831,93400807563852114,2040785359707595829,46522111241274345703,1104851095392088611659,27297549612899248588570

**OFFSET:** 1

**COMMENTS:**
In the Horimetrik framework (see LINKS) this is the "maximal product height of squares", beta(n,n) (maximale Produkthoehe von Quadraten).
M_n is the coefficientwise largest polynomial with d + c_d <= n at all occupied positions (the "full number" of the mixed-radix system with decreasing bases). a(n) answers: how large a capacity can the product of two capacity-n structures require. Proved: multiplication is coefficientwise monotone, so the maximum over all pairs is attained at (M_n, M_n) — a single canonical product per term. Products in the falling factorial basis via X_(p)*X_(q) = Sum_j C(p,j)*C(q,j)*j!*X_(p+q-j).
Proved: log(a(n)/n!) = 2*sqrt(n) + O(log n).

**REFERENCES:** (leer)

**LINKS:**
Christian Felix Bürckert, <a href="https://github.com/christianbuerckert/horimetrik">Horimetrik — Zahlen mit Horizont (book, proofs, and programs, in German)</a>
Christian Felix Bürckert, <a href="https://github.com/christianbuerckert/horimetrik/blob/main/buch/main.pdf">Horimetrik - Zahlen mit Horizont (book PDF, in German)</a>
Christian Felix Bürckert, <a href="https://github.com/christianbuerckert/horimetrik/blob/main/book/main.pdf">Horimetrik - Numbers with a Horizon (book PDF, English translation)</a>
Christian Felix Bürckert, <a href="https://doi.org/10.5281/zenodo.21400755">Horimetrik - Zahlen mit Horizont / Numbers with a Horizon (archived books and paper, Zenodo)</a>
[Nach Freischaltung: b-File-Zeile, n = 1..24]

**FORMULA:**
a(n) = n! * exp(2*sqrt(n) + O(log n)).

**EXAMPLE:**
For n=2: M_2(X) = X + 2, and (X+2)^2 = X^2 + 4X + 4 = X_(2) + 5*X_(1) + 4, so a(2) = max(0+4, 1+5, 2+1) = 6.

**PROG:**
(Python)
```python
from math import factorial, comb
def a(n):
    M = {d: n-d for d in range(n)}
    prod = {}
    for p, x in M.items():
        for q, y in M.items():
            for j in range(min(p, q)+1):
                d = p+q-j
                prod[d] = prod.get(d, 0) + x*y*comb(p,j)*comb(q,j)*factorial(j)
    return max(d+c for d, c in prod.items() if c > 0)
```

**CROSSREFS:**
Cf. A000142. [Nach A-Nummern-Vergabe: Querverweise auf die übrigen Horimetrik-Folgen ergänzen]

**KEYWORD:** nonn

**b-File:** bfiles/folge2_beta.txt (n = 1..24)

---

## Folge 3: Schalenspringer

**NAME:**
a(n) is the number of digit sequences (d_1,...,d_n) with 0 <= d_i <= i-1 for all i and Sum_{i=1}^n d_i*(n+1)!/(i+1)! >= n!.

**DATA:**
1,8,60,360,2520,21168,211680,2268000,26611200,319334400,4229184960,61751289600,948063916800,15617892449024,269729632972800,4961839621939200,96302371156992000,1939563545407488000,41361094050756480000,923942970376538112000,21543347282404147200000

**OFFSET:** 3

**COMMENTS:**
In the Horimetrik framework (see LINKS) these are the "shell jumpers" (Schalenspringer).
Equivalently: the number of x < n! that are pushed into the next factorial shell by prepending a single zero digit in the mixed-radix system with decreasing bases (base i+1 at position i; prepending a zero re-weights all positions).
Coincides with n!/2 for n = 5, 6, 7 but not for n = 8 (21168 <> 20160); the proved complement formula (see FORMULA) explains the coincidence: for these three n the formula collapses to a single term equal to n!/2.
The formula is proved; terms verified independently by exhaustive enumeration for n <= 10.

**REFERENCES:** (leer)

**LINKS:**
Christian Felix Bürckert, <a href="https://github.com/christianbuerckert/horimetrik">Horimetrik — Zahlen mit Horizont (book, proofs, and programs, in German)</a>
Christian Felix Bürckert, <a href="https://github.com/christianbuerckert/horimetrik/blob/main/buch/main.pdf">Horimetrik - Zahlen mit Horizont (book PDF, in German)</a>
Christian Felix Bürckert, <a href="https://github.com/christianbuerckert/horimetrik/blob/main/book/main.pdf">Horimetrik - Numbers with a Horizon (book PDF, English translation)</a>
Christian Felix Bürckert, <a href="https://doi.org/10.5281/zenodo.21400755">Horimetrik - Zahlen mit Horizont / Numbers with a Horizon (archived books and paper, Zenodo)</a>
[Nach Freischaltung: b-File-Zeile, n = 3..20]

**FORMULA:**
a(n) = n! - Sum_{p=1}^{P} min(d_p, p) * n!/p!, where (d_1,...,d_n) is the digit sequence of n! in the system above and P is the least p with d_p = p, or n if no such p exists.

**EXAMPLE:**
For n=3: the digit caps are d_1=0, d_2<=1, d_3<=2 with weights 12, 4, 1, so the largest reachable value is 0+4+2 = 6 = 3!; exactly one sequence, (0,1,2), reaches at least 3!. So a(3)=1.

**PROG:**
(Python)
```python
from math import factorial
def a(n):
    x, digits = factorial(n), []
    for base in range(n+1, 1, -1):
        x, r = divmod(x, base)
        digits.append(r)
    d = digits[::-1]  # d[p-1] is digit at position p
    P = n
    for p in range(1, n+1):
        if d[p-1] == p:
            P = p
            break
    return factorial(n) - sum(min(d[p-1], p)*factorial(n)//factorial(p)
                              for p in range(1, P+1))
```

**CROSSREFS:**
Cf. [Folge 7: Komplement], [Folge 4: Fixpunkte].

**KEYWORD:** nonn

**b-File:** bfiles/folge3_schalenspringer.txt (n = 3..40)

---

## Folge 4: beidseitige Fixpunkte

**NAME:**
a(n) = n*n! - b(n), where b(n) is the number of digit sequences (d_1,...,d_n) with 0 <= d_i <= i-1 and Sum_{i=1}^n d_i*(n+1)!/(i+1)! >= n! (b(n) = 0 for n < 3).

**DATA:**
4,17,88,540,3960,32760,301392,3054240,34020000,412473600,5428684800,76722085440,1158744787200,18667051603200,319146745758976,5776956644659200,110280887081164800,2214954536610816000,46718476618125312000,1031548691555141760000,23804073040730830848000

**OFFSET:** 2

**COMMENTS:**
In the Horimetrik framework (see LINKS) these are the "two-sided fixed points" (beidseitige Fixpunkte).
Number of x in [n!, (n+1)!) whose representation at horizon n is fixed by both natural compactifications of the decreasing-base mixed-radix system (value-minimal AND structure-minimal simultaneously). Proved: the shell has n*n! elements; those failing structure-minimality are exactly the b(n) sequences with no digit at its cap.

**REFERENCES:** (leer)

**LINKS:**
Christian Felix Bürckert, <a href="https://github.com/christianbuerckert/horimetrik">Horimetrik — Zahlen mit Horizont (book, proofs, and programs, in German)</a>
Christian Felix Bürckert, <a href="https://github.com/christianbuerckert/horimetrik/blob/main/buch/main.pdf">Horimetrik - Zahlen mit Horizont (book PDF, in German)</a>
Christian Felix Bürckert, <a href="https://github.com/christianbuerckert/horimetrik/blob/main/book/main.pdf">Horimetrik - Numbers with a Horizon (book PDF, English translation)</a>
Christian Felix Bürckert, <a href="https://doi.org/10.5281/zenodo.21400755">Horimetrik - Zahlen mit Horizont / Numbers with a Horizon (archived books and paper, Zenodo)</a>
[Nach Freischaltung: b-File-Zeile, n = 2..20]

**FORMULA:**
a(n) = n*n! - b(n), where b is the shell-jumper count (Folge 3).

**EXAMPLE:**
For n=2: the shell [2,6) has 2*2! = 4 elements and b(2)=0, so all of x = 2,3,4,5 are doubly fixed; e.g. x=4 has digits (1,1), structure polynomial X+1 with sigma = max(0+1,1+1) = 2 = horizon. So a(2)=4.

**PROG:**
(Python) wie Folge 3, dann `n*factorial(n) - b(n)`.

**CROSSREFS:**
Cf. A000142. [Nach A-Nummern-Vergabe: Querverweise auf die übrigen Horimetrik-Folgen ergänzen]

**KEYWORD:** nonn,easy

**b-File:** bfiles/folge4_fixpunkte.txt (n = 2..40)

---

## Folge 5: Interchange-Maxima

**NAME:**
a(n) = max over 0 <= x < (n+1)! of P_x(n+2) - Q_x(n+3), where P_x is the digit polynomial of x at horizon n and Q_x at horizon n+1 (falling factorial basis, digits read in reverse).

**DATA:**
0,1,6,43,351,2873,26443,270291,3370313,41217421,537235479,7419941831

**OFFSET:** 1

**COMMENTS:**
In the Horimetrik framework (see LINKS) these are the "interchange maxima", the maxima of the interchange defect Omega (Interchange-Maxima).
Measures the failure of commutativity between the two growth operations of the decreasing-base mixed-radix system: prepend-zero-then-re-encode versus re-encode-then-prepend-zero.
Proved: P_x(n+2) >= Q_x(n+3) for all x (via a multiplication lemma z(c*y) >= (c+1)*z(y) for c >= l+2, applied exactly at the regime boundary c = n+2), so a(n) >= 0 and the difference is a genuine defect statistic.
Computation via the recursion z_n(x) = (x mod (n+1)) + (n+2)*z_{n-1}(floor(x/(n+1))).

**REFERENCES:** (leer)

**LINKS:**
Christian Felix Bürckert, <a href="https://github.com/christianbuerckert/horimetrik">Horimetrik — Zahlen mit Horizont (book, proofs, and programs, in German)</a>
Christian Felix Bürckert, <a href="https://github.com/christianbuerckert/horimetrik/blob/main/buch/main.pdf">Horimetrik - Zahlen mit Horizont (book PDF, in German)</a>
Christian Felix Bürckert, <a href="https://github.com/christianbuerckert/horimetrik/blob/main/book/main.pdf">Horimetrik - Numbers with a Horizon (book PDF, English translation)</a>
Christian Felix Bürckert, <a href="https://doi.org/10.5281/zenodo.21400755">Horimetrik - Zahlen mit Horizont / Numbers with a Horizon (archived books and paper, Zenodo)</a>
[Nach Freischaltung: b-File-Zeile, n = 1..10]

**FORMULA:** (leer)

**EXAMPLE:**
For n=2 and x=3: at horizon 2 the digits of 3 are (1,0), giving P_3(X) = X and P_3(4) = 4; at horizon 3 the digits are (0,0,3), giving the constant Q_3 = 3. The difference is 4 - 3 = 1, which is maximal on H_2, so a(2)=1.

**PROG:**
(Python)
```python
from math import factorial
def z(n, x):
    if n == 0: return 0
    q, r = divmod(x, n+1)
    return r + (n+2)*z(n-1, q)
def a(n):
    return max(z(n, x) - z(n+1, x) for x in range(factorial(n+1)))
```

**CROSSREFS:**
Cf. A000142. [Nach A-Nummern-Vergabe: Querverweise auf die übrigen Horimetrik-Folgen ergänzen]

**KEYWORD:** nonn,more

**b-File:** bfiles/folge5_omega_max.txt (n = 1..12)

---

## Folge 6: Interchange-Nullzähler

**NAME:**
a(n) = number of 0 <= x < (n+1)! with P_x(n+2) = Q_x(n+3), where P_x is the digit polynomial of x at horizon n and Q_x at horizon n+1 (falling factorial basis, digits read in reverse).

**DATA:**
2,5,13,23,61,111,274,564,1389,2584,6639,13520

**OFFSET:** 1

**COMMENTS:**
In the Horimetrik framework (see LINKS) this is the "interchange zero count" (Interchange-Nullzaehler).
Counts the values for which the two growth orders of the decreasing-base mixed-radix system commute. Proved: the difference P_x(n+2) - Q_x(n+3) is nonnegative, and equality holds exactly when both steps of the positivity proof are sharp (carry-free increments plus a sharp multiplication lemma).
Proved upper bound: a(n) <= (n+1)^(n+1)/n!, so the proportion of commuting values decays at least like exp(-(1+o(1))*n*log n).

**REFERENCES:** (leer)

**LINKS:**
Christian Felix Bürckert, <a href="https://github.com/christianbuerckert/horimetrik">Horimetrik — Zahlen mit Horizont (book, proofs, and programs, in German)</a>
Christian Felix Bürckert, <a href="https://github.com/christianbuerckert/horimetrik/blob/main/buch/main.pdf">Horimetrik - Zahlen mit Horizont (book PDF, in German)</a>
Christian Felix Bürckert, <a href="https://github.com/christianbuerckert/horimetrik/blob/main/book/main.pdf">Horimetrik - Numbers with a Horizon (book PDF, English translation)</a>
Christian Felix Bürckert, <a href="https://doi.org/10.5281/zenodo.21400755">Horimetrik - Zahlen mit Horizont / Numbers with a Horizon (archived books and paper, Zenodo)</a>
[Nach Freischaltung: b-File-Zeile, n = 1..10]

**FORMULA:**
a(n) <= (n+1)^(n+1)/n!.

**EXAMPLE:**
For n=1: both x=0 and x=1 satisfy P_x(3) = Q_x(4) (the constant polynomials 0 and 1), so a(1)=2.

**PROG:**
(Python) — z wie in Folge 5:
```python
def a(n):
    return sum(1 for x in range(factorial(n+1)) if z(n, x) == z(n+1, x))
```

**CROSSREFS:**
Cf. A000142. [Nach A-Nummern-Vergabe: Querverweise auf die übrigen Horimetrik-Folgen ergänzen]

**KEYWORD:** nonn,more

**b-File:** bfiles/folge6_omega_null.txt (n = 1..12)

---

## Folge 7: Nicht-Springer (bewiesene Ziffernformel)

**NAME:**
a(n) is the number of digit sequences (d_1,...,d_n) with 0 <= d_i <= i-1 for all i and Sum_{i=1}^n d_i*(n+1)!/(i+1)! < n!.

**DATA:**
1,2,5,16,60,360,2520,19152,151200,1360800,13305600,159667200,1997835840,25427001600,359610451200,5304897438976,85957795123200,1440534083788800,25342729251840000,493338462769152000,9729848120952960000,200057757401069568000,4308669456480829440000

**OFFSET:** 1

**COMMENTS:**
In the Horimetrik framework (see LINKS) these are the "non-jumpers" (Nicht-Springer).
Complement of Folge 3 within the n! capped digit sequences: a(n) = n! - Folge3(n). Equivalently: the number of x < n! NOT pushed into the next factorial shell by prepending a zero digit in the mixed-radix system with decreasing bases.
Main point is the proved closed digit formula (see FORMULA): the count is read off the digits of n! in its own shell. Verified independently by exhaustive enumeration for n <= 10.

**REFERENCES:** (leer)

**LINKS:**
Christian Felix Bürckert, <a href="https://github.com/christianbuerckert/horimetrik">Horimetrik — Zahlen mit Horizont (book, proofs, and programs, in German)</a>
Christian Felix Bürckert, <a href="https://github.com/christianbuerckert/horimetrik/blob/main/buch/main.pdf">Horimetrik - Zahlen mit Horizont (book PDF, in German)</a>
Christian Felix Bürckert, <a href="https://github.com/christianbuerckert/horimetrik/blob/main/book/main.pdf">Horimetrik - Numbers with a Horizon (book PDF, English translation)</a>
Christian Felix Bürckert, <a href="https://doi.org/10.5281/zenodo.21400755">Horimetrik - Zahlen mit Horizont / Numbers with a Horizon (archived books and paper, Zenodo)</a>
[Nach Freischaltung: b-File-Zeile, n = 1..20]

**FORMULA:**
a(n) = Sum_{p=1}^{P} min(d_p, p) * n!/p!, where (d_1,...,d_n) is the digit sequence of n! at horizon n and P is the least p with d_p = p, or n if no maximal digit exists (via decomposition by the first position where a sequence differs from the digits of n!).

**EXAMPLE:**
For n=3: 3! = 6 has digits (0,1,2) at horizon 3, no digit is at its cap, so P=3 and a(3) = 0*6/1! + 1*6/2! + 2*6/3! = 0 + 3 + 2 = 5. Indeed exactly (0,0,0), (0,0,1), (0,0,2), (0,1,0), (0,1,1) — values 0, 1, 2, 4, 5 — stay below 6.

**PROG:**
(Python)
```python
from math import factorial
def a(n):
    x, digits = factorial(n), []
    for base in range(n+1, 1, -1):
        x, r = divmod(x, base)
        digits.append(r)
    d = digits[::-1]
    P = n
    for p in range(1, n+1):
        if d[p-1] == p:
            P = p
            break
    return sum(min(d[p-1], p)*factorial(n)//factorial(p)
               for p in range(1, P+1))
```

**CROSSREFS:**
Cf. A000142. [Nach A-Nummern-Vergabe: Querverweise auf die übrigen Horimetrik-Folgen ergänzen]

**KEYWORD:** nonn

**b-File:** bfiles/folge7_nichtspringer.txt (n = 1..40)

---

## Folge 8: Ein-Ziffern-Fakultäten

**NAME:**
Numbers n such that n! is a single nonzero digit in the mixed-radix system with decreasing bases (digit i has base i+1, weight (n+1)!/(i+1)!); equivalently n = (i+1)!/d - 1 for integers i >= 1, 1 <= d <= i.

**DATA:**
1,2,5,7,11,23,29,39,59,119,143,179,239,359,719,839,1007,1259,1679,2519,5039,5759,6719,8063,10079,13439,20159,40319,45359,51839,60479,72575,90719,120959,181439,362879,403199,453599,518399,604799,725759,907199,1209599,1814399,3628799,3991679,4435199,4989599

**OFFSET:** 1

**COMMENTS:**
In the Horimetrik framework (see LINKS) these are the "single-digit factorials" (Ein-Ziffern-Fakultaeten).
Exactly i terms arise from each position i (d ranges over 1..i; divisibility is automatic since d <= i). Fully characterized with proof: exactness of n! = d*(n+1)!/(i+1)! forces d = (i+1)!/(n+1), and uniqueness of the digit expansion does the rest.
The characterization supplied nine exact predictions (n = 29, 39, 59, 119 and 143, 179, 239, 359, 719) before computation.

**REFERENCES:** (leer)

**LINKS:**
Christian Felix Bürckert, <a href="https://github.com/christianbuerckert/horimetrik">Horimetrik — Zahlen mit Horizont (book, proofs, and programs, in German)</a>
Christian Felix Bürckert, <a href="https://github.com/christianbuerckert/horimetrik/blob/main/buch/main.pdf">Horimetrik - Zahlen mit Horizont (book PDF, in German)</a>
Christian Felix Bürckert, <a href="https://github.com/christianbuerckert/horimetrik/blob/main/book/main.pdf">Horimetrik - Numbers with a Horizon (book PDF, English translation)</a>
Christian Felix Bürckert, <a href="https://doi.org/10.5281/zenodo.21400755">Horimetrik - Zahlen mit Horizont / Numbers with a Horizon (archived books and paper, Zenodo)</a>
[Nach Freischaltung: b-File-Zeile, 45 Terme]

**FORMULA:**
Sorted values of (i+1)!/d - 1 over i >= 1, 1 <= d <= i.

**EXAMPLE:**
n=5 is a term: 5! = 120 = 1 * 720/3! is the single digit 1 at position 2 of horizon 5 (weight 6!/(2+1)! = 120), i.e. n = (i+1)!/d - 1 with i=2, d=1.

**PROG:**
(Python)
```python
from math import factorial
def upto(limit):
    vals = {factorial(i+1)//d - 1
            for i in range(1, 20) for d in range(1, i+1)}
    return sorted(v for v in vals if v <= limit)
```

**CROSSREFS:**
Cf. A000142. [Nach A-Nummern-Vergabe: Querverweise auf die übrigen Horimetrik-Folgen ergänzen]

**KEYWORD:** nonn,easy

**b-File:** bfiles/folge8_einziffer.txt (78 Terme, bis 6227020799)

---

## Folge 9: maximale Kompositionshöhe

**NAME:**
a(r) is the maximum of max_d (d + c_d(P o Q)) over all polynomials P, Q with nonnegative integer coefficients in the falling factorial basis satisfying max_d (d + c_d) <= r for both; equivalently a(r) = max_d (d + c_d(M_r o M_r)) with M_r(X) = Sum_{d=0}^{r-1} (r-d)*X_(d).

**DATA:**
1,4,23,6541,477149751,26594371862819905,2459443656914751799341550307,704493743642841887982266957869120341803011,1038937998037120725999400773289378882897395371144700639316071

**OFFSET:** 1

**COMMENTS:**
In the Horimetrik framework (see LINKS) this is the "maximal composition height", Gamma_o(r,r) (maximale Kompositionshoehe).
Proved: the semiring of polynomials with nonnegative integer falling-factorial coefficients is closed under composition (via a free symmetric-group action: the count N_m of tuples of injections covering an m-set is divisible by m!). Composition is coefficientwise monotone in both arguments, so the maximum is attained at the componentwise maximal polynomial M_r — a single canonical composition per term.
Empirical (no proof): growth appears to be of order log a(r) ~ r^2 log r.
The analogous maxima for addition, multiplication and forward difference are r+s (trivial), Folge 2, and floor((r+1)^2/4)-1 respectively.

**REFERENCES:** (leer)

**LINKS:**
Christian Felix Bürckert, <a href="https://github.com/christianbuerckert/horimetrik">Horimetrik — Zahlen mit Horizont (book, proofs, and programs, in German)</a>
Christian Felix Bürckert, <a href="https://github.com/christianbuerckert/horimetrik/blob/main/buch/main.pdf">Horimetrik - Zahlen mit Horizont (book PDF, in German)</a>
Christian Felix Bürckert, <a href="https://github.com/christianbuerckert/horimetrik/blob/main/book/main.pdf">Horimetrik - Numbers with a Horizon (book PDF, English translation)</a>
Christian Felix Bürckert, <a href="https://doi.org/10.5281/zenodo.21400755">Horimetrik - Zahlen mit Horizont / Numbers with a Horizon (archived books and paper, Zenodo)</a>
[Nach Freischaltung: b-File-Zeile, r = 1..12]

**FORMULA:**
a(r) = max_d (d + c_d(M_r o M_r)).

**EXAMPLE:**
For r=2: M_2(X) = X + 2, and (M_2 o M_2)(X) = (X+2) + 2 = X + 4, so a(2) = max(0+4, 1+1) = 4.

**PROG:**
(Python)
```python
from math import factorial, comb
def mul(A, B):
    out = {}
    for p, x in A.items():
        for q, y in B.items():
            for j in range(min(p, q)+1):
                d = p+q-j
                out[d] = out.get(d, 0) + x*y*comb(p,j)*comb(q,j)*factorial(j)
    return {d: c for d, c in out.items() if c}
def a(r):
    M = {d: r-d for d in range(r)}
    out, FF = {}, {0: 1}
    for d in range(r):
        c = M.get(d, 0)
        for deg, co in FF.items():
            out[deg] = out.get(deg, 0) + c*co
        if d < r-1:
            Qm = dict(M); Qm[0] = Qm.get(0, 0) - d
            FF = mul(FF, Qm)
    return max(d+c for d, c in out.items() if c > 0)
```

**CROSSREFS:**
Cf. A000142. [Nach A-Nummern-Vergabe: Querverweise auf die übrigen Horimetrik-Folgen ergänzen]

**KEYWORD:** nonn

**b-File:** bfiles/folge9_komposition.txt (r = 1..12)

---

## Vor der Einreichung noch zu tun

- [x] OEIS-Konto registriert (13.07.2026)
- [x] Entwürfe feldgenau ans Einreichungsformular angepasst
      (NAME/DATA/OFFSET/COMMENTS/LINKS/FORMULA/EXAMPLE/PROG/
      CROSSREFS/KEYWORD; 14.07.2026)
- [x] Buch veröffentlicht (GitHub, 14.07.2026): PDF-Link steht in
      allen neun LINKS-Feldern; falls später eine eigene
      Webseiten-URL dazukommt, als weitere %H-Zeile ergänzen
- [x] Termerweiterungen und b-Files generiert und verifiziert
      (`programme/experiments_oeis_bfiles.py`)
- [x] Programme self-contained, DATA-Felder unter 260 Zeichen
- [ ] Nach Freischaltung: b-Files per Edit nachreichen
      (Formular-Hinweis: „Wait until the sequence is approved")
- [ ] Querverweise (CROSSREFS) nach Vergabe der A-Nummern
      wechselseitig eintragen; A-Nummern auch im Buch nachtragen
      (Kapitel 6, Anhang A, Literaturverzeichnis) und im Fachtext
