#!/usr/bin/env python3
"""Erzeugt die OEIS-Einreichungen im internal format (14.07.2026).

Eine Datei je Folge unter oeis/internal/, direkt in das
"Submitting a New Sequence"-Textfeld einfügbar. Formatregeln nach
https://oeis.org/eishelp1.html: %S/%T/%U kommagetrennt ohne
Leerzeichen, maximal drei Datenzeilen, %O = (Startindex, Position
des ersten Terms mit Betrag >= 2, sonst 1), %H als
'Author, <a href="...">Titel</a>' auf einer Zeile.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "oeis", "internal")

AUTHOR = "_Christian Felix Bürckert_, Jul 14 2026"
H_PDF = ('%H Christian Felix Bürckert, <a href="https://github.com/'
         'christianbuerckert/horimetrik/blob/main/buch/main.pdf">'
         'Horimetrik - Zahlen mit Horizont (book PDF, in German)</a>')
H_PDF_EN = ('%H Christian Felix Bürckert, <a href="https://github.com/'
            'christianbuerckert/horimetrik/blob/main/book/main.pdf">'
            'Horimetrik - Numbers with a Horizon (book PDF, English '
            'translation)</a>')
H_DOI = ('%H Christian Felix Bürckert, <a href="https://doi.org/10.5281/zenodo.21400755">'
         'Horimetrik - Zahlen mit Horizont / Numbers with a Horizon '
         '(archived books and paper, Zenodo)</a>')
H_REPO = ('%H Christian Felix Bürckert, <a href="https://github.com/'
          'christianbuerckert/horimetrik">Horimetrik (proofs, programs, '
          'and b-files)</a>')


def bf(name):
    with open(os.path.join(ROOT, "oeis", "bfiles", name)) as fh:
        return [int(l.split()[1]) for l in fh if l.strip()]


def fit_terms(terms):
    """So viele Terme, wie in die 260-Zeichen-DATA-Grenze passen."""
    out, total = [], 0
    for t in map(str, terms):
        add = len(t) + (1 if out else 0)
        if total + add > 260:
            break
        out.append(t)
        total += add
    assert len(out) >= 4, "OEIS verlangt mindestens 4 Terme"
    return out


def _chunk(terms, width=90):
    chunks, cur = [], ""
    for t in terms:
        if cur and len(cur) + 1 + len(t) > width:
            chunks.append(cur + ",")
            cur = t
        else:
            cur = (cur + "," + t) if cur else t
    chunks.append(cur)
    return chunks


def datalines(terms):
    """Fuellt DATA bis 260 Zeichen, hoechstens drei Zeilen; passt bei
    Riesentermen die Termzahl an (Rest traegt das b-File)."""
    terms = fit_terms(terms)
    chunks = _chunk(terms)
    while len(chunks) > 3:
        terms = terms[:-1]
        chunks = _chunk(terms)
    assert len(terms) >= 4
    return ["%" + tag + " " + c for tag, c in zip("STU", chunks)]


def second_offset(terms):
    for i, t in enumerate(terms, 1):
        if abs(t) >= 2:
            return i
    return 1


def block(terms, off1, name, comments, formula, example, prog,
          crossref, keyword):
    L = ["%I"]
    L += datalines(terms)
    L.append("%N " + name)
    for c in comments:
        L.append("%C " + c)
    L.append(H_PDF)
    L.append(H_PDF_EN)
    L.append(H_DOI)
    L.append(H_REPO)
    if formula:
        L.append("%F " + formula)
    L.append("%e " + example)
    L.append("%o (Python)")
    for line in prog.strip("\n").split("\n"):
        L.append("%o " + line)
    L.append("%Y " + crossref)
    L.append("%K " + keyword)
    L.append(f"%O {off1},{second_offset(terms)}")
    L.append("%A " + AUTHOR)
    return "\n".join(L) + "\n"


PROG_Z = """from math import factorial
def z(n, x):
    if n == 0: return 0
    q, r = divmod(x, n+1)
    return r + (n+2)*z(n-1, q)"""

PROG_DIGIT = """from math import factorial
def N(n):
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
    return sum(min(d[p-1], p)*factorial(n)//factorial(p) for p in range(1, P+1))"""

SEQS = {}

SEQS["folge1"] = block(
    bf("folge1_sprungstellen.txt"), 1,
    "a(g) is the least m such that Sum_{d=0}^{m-g-1} (m-g-d)*(m+1)!/(m+1-d)! >= m!.",
    ['In the Horimetrik framework (a positional number system with decreasing bases; see LINKS) this is the sequence of "jump positions of the depth law" (Sprungstellen des Tiefengesetzes).',
     'Arises in the mixed-radix positional system with decreasing bases (digit i has base i+1, so the most significant digit is binary): a(g) is the first "factorial shell" [m!, (m+1)!) containing a value whose digit-polynomial support height lies g below the shell index; equivalently, the first shell where the commutator of the two natural compactification operators of that system reaches depth -g.',
     'The defining sum satisfies the identity S(m,g)/m! = (m+1)*Sum_{k=1..m-g} k/(g+k+1)!, which makes distant terms computable.',
     'Proved: (g+2)!/c(g) <= a(g)+1 <= (g+2)! with c(g) = (g+2)!*Sum_{k>=1} k/(g+k+1)! = 1 + O(1/g), hence a(g)/(g+2)! -> 1.'],
    "a(g) ~ (g+2)! (two-sided bounds in COMMENTS).",
    "For g=1: with M_s(X) = Sum_{d<s} (s-d)*X_(d) in the falling factorial basis X_(d) = X*(X-1)*...*(X-d+1), m=3 is the least m with M_{m-1}(m+1) >= m!, since M_2(4) = 2 + 4 = 6 >= 3! = 6, while M_1(3) = 1 < 2! = 2 fails for m=2. So a(1)=3.",
    """from fractions import Fraction
from math import factorial
def a(g, K=400):
    S = [Fraction(0)]
    for k in range(1, K+1):
        S.append(S[-1] + Fraction(k, factorial(g+k+1)))
    tail = Fraction(2*(K+1), factorial(g+K+2))
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
    return lo""",
    "Cf. A000142.",
    "nonn,hard")

SEQS["folge2"] = block(
    bf("folge2_beta.txt"), 1,
    "a(n) = max over d of (d + c_d), where Sum_d c_d*X_(d) is the square of M_n(X) = Sum_{d=0}^{n-1} (n-d)*X_(d), expanded in the falling factorial basis X_(d) = X*(X-1)*...*(X-d+1).",
    ['In the Horimetrik framework (see LINKS) this is the "maximal product height of squares" beta(n,n) (maximale Produkthoehe von Quadraten).',
     'M_n is the coefficientwise largest polynomial with d + c_d <= n at all occupied positions. a(n) answers: how large a capacity can the product of two capacity-n structures require. Proved: multiplication is coefficientwise monotone, so the maximum over all pairs is attained at (M_n, M_n). Products via X_(p)*X_(q) = Sum_j binomial(p,j)*binomial(q,j)*j!*X_(p+q-j).',
     'Proved: log(a(n)/n!) = 2*sqrt(n) + O(log n).'],
    "a(n) = n! * exp(2*sqrt(n) + O(log n)).",
    "For n=2: M_2(X) = X + 2 and (X+2)^2 = X^2 + 4X + 4 = X_(2) + 5*X_(1) + 4, so a(2) = max(0+4, 1+5, 2+1) = 6.",
    """from math import factorial, comb
def a(n):
    M = {d: n-d for d in range(n)}
    prod = {}
    for p, x in M.items():
        for q, y in M.items():
            for j in range(min(p, q)+1):
                d = p+q-j
                prod[d] = prod.get(d, 0) + x*y*comb(p,j)*comb(q,j)*factorial(j)
    return max(d+c for d, c in prod.items() if c > 0)""",
    "Cf. A000142.",
    "nonn")

SEQS["folge3"] = block(
    bf("folge3_schalenspringer.txt"), 3,
    "a(n) is the number of digit sequences (d_1,...,d_n) with 0 <= d_i <= i-1 for all i and Sum_{i=1..n} d_i*(n+1)!/(i+1)! >= n!.",
    ['In the Horimetrik framework (see LINKS) these are the "shell jumpers" (Schalenspringer).',
     'Equivalently: the number of x < n! that are pushed into the next factorial shell by prepending a single zero digit in the mixed-radix system with decreasing bases (base i+1 at position i; prepending a zero re-weights all positions).',
     'Coincides with n!/2 for n = 5, 6, 7 but not for n = 8 (21168 <> 20160); the proved complement formula (see FORMULA) explains the coincidence: for these three n the formula collapses to a single term equal to n!/2.',
     'The formula is proved; terms verified independently by exhaustive enumeration for n <= 10.'],
    "a(n) = n! - Sum_{p=1..P} min(d_p, p)*n!/p!, where (d_1,...,d_n) is the digit sequence of n! in the system above and P is the least p with d_p = p, or n if no such p exists.",
    "For n=3: the digit caps are d_1=0, d_2<=1, d_3<=2 with weights 12, 4, 1, so the largest reachable value is 0+4+2 = 6 = 3!; exactly one sequence, (0,1,2), reaches at least 3!. So a(3)=1.",
    PROG_DIGIT + """
def a(n):
    return factorial(n) - N(n)""",
    "Cf. A000142.",
    "nonn")

SEQS["folge4"] = block(
    bf("folge4_fixpunkte.txt"), 2,
    "a(n) = n*n! - b(n), where b(n) is the number of digit sequences (d_1,...,d_n) with 0 <= d_i <= i-1 and Sum_{i=1..n} d_i*(n+1)!/(i+1)! >= n! (b(n) = 0 for n < 3).",
    ['In the Horimetrik framework (see LINKS) these are the "two-sided fixed points" (beidseitige Fixpunkte).',
     'Number of x in [n!, (n+1)!) whose representation at horizon n is fixed by both natural compactifications of the decreasing-base mixed-radix system (value-minimal AND structure-minimal simultaneously). Proved: the shell has n*n! elements; those failing structure-minimality are exactly the b(n) sequences with no digit at its cap.'],
    "a(n) = n*n! - b(n), where b is the shell-jumper count.",
    "For n=2: the shell [2,6) has 2*2! = 4 elements and b(2)=0, so all of x = 2,3,4,5 are doubly fixed; e.g. x=4 has digits (1,1) and structure polynomial X+1 with max(0+1,1+1) = 2 = horizon. So a(2)=4.",
    PROG_DIGIT + """
def a(n):
    b = factorial(n) - N(n) if n >= 3 else 0
    return n*factorial(n) - b""",
    "Cf. A000142.",
    "nonn,easy")

SEQS["folge5"] = block(
    bf("folge5_omega_max.txt"), 1,
    "a(n) = max over 0 <= x < (n+1)! of P_x(n+2) - Q_x(n+3), where P_x is the digit polynomial of x at horizon n and Q_x at horizon n+1 (falling factorial basis, digits read in reverse).",
    ['In the Horimetrik framework (see LINKS) these are the "interchange maxima", the maxima of the interchange defect (Interchange-Maxima).',
     'Measures the failure of commutativity between the two growth operations of the decreasing-base mixed-radix system: prepend-zero-then-re-encode versus re-encode-then-prepend-zero.',
     'Proved: P_x(n+2) >= Q_x(n+3) for all x (via a multiplication lemma z(c*y) >= (c+1)*z(y) for c >= l+2, applied exactly at the regime boundary c = n+2), so a(n) >= 0.',
     'Computation via the recursion z_n(x) = (x mod (n+1)) + (n+2)*z_{n-1}(floor(x/(n+1))).'],
    "",
    "For n=2 and x=3: at horizon 2 the digits of 3 are (1,0), giving P_3(X) = X and P_3(4) = 4; at horizon 3 the digits are (0,0,3), giving the constant Q_3 = 3. The difference 4 - 3 = 1 is maximal on H_2, so a(2)=1.",
    PROG_Z + """
def a(n):
    return max(z(n, x) - z(n+1, x) for x in range(factorial(n+1)))""",
    "Cf. A000142.",
    "nonn,more")

SEQS["folge6"] = block(
    bf("folge6_omega_null.txt"), 1,
    "a(n) = number of 0 <= x < (n+1)! with P_x(n+2) = Q_x(n+3), where P_x is the digit polynomial of x at horizon n and Q_x at horizon n+1 (falling factorial basis, digits read in reverse).",
    ['In the Horimetrik framework (see LINKS) this is the "interchange zero count" (Interchange-Nullzaehler).',
     'Counts the values for which the two growth orders of the decreasing-base mixed-radix system commute. Proved: the difference P_x(n+2) - Q_x(n+3) is nonnegative, and equality holds exactly when both steps of the positivity proof are sharp (carry-free increments plus a sharp multiplication lemma).',
     'Proved: a(n) <= (n+1)^(n+1)/n!, so the proportion of commuting values decays at least like exp(-(1+o(1))*n*log(n)).'],
    "a(n) <= (n+1)^(n+1)/n!.",
    "For n=1: both x=0 and x=1 satisfy P_x(3) = Q_x(4) (the constant polynomials 0 and 1), so a(1)=2.",
    PROG_Z + """
def a(n):
    return sum(1 for x in range(factorial(n+1)) if z(n, x) == z(n+1, x))""",
    "Cf. A000142.",
    "nonn,more")

SEQS["folge7"] = block(
    bf("folge7_nichtspringer.txt"), 1,
    "a(n) is the number of digit sequences (d_1,...,d_n) with 0 <= d_i <= i-1 for all i and Sum_{i=1..n} d_i*(n+1)!/(i+1)! < n!.",
    ['In the Horimetrik framework (see LINKS) these are the "non-jumpers" (Nicht-Springer).',
     'Equivalently: the number of x < n! NOT pushed into the next factorial shell by prepending a zero digit in the mixed-radix system with decreasing bases. Complement of the shell jumpers within the n! capped digit sequences.',
     'The closed digit formula (see FORMULA) is proved; terms verified independently by exhaustive enumeration for n <= 10.'],
    "a(n) = Sum_{p=1..P} min(d_p, p)*n!/p!, where (d_1,...,d_n) is the digit sequence of n! at horizon n and P is the least p with d_p = p, or n if no maximal digit exists.",
    "For n=3: 3! = 6 has digits (0,1,2) at horizon 3, no digit is at its cap, so P=3 and a(3) = 0*6/1! + 1*6/2! + 2*6/3! = 0 + 3 + 2 = 5. Indeed exactly (0,0,0), (0,0,1), (0,0,2), (0,1,0), (0,1,1) - values 0, 1, 2, 4, 5 - stay below 6.",
    PROG_DIGIT + """
a = N""",
    "Cf. A000142.",
    "nonn")

SEQS["folge8"] = block(
    bf("folge8_einziffer.txt"), 1,
    "Numbers k such that k! is a single nonzero digit in the mixed-radix system with decreasing bases (digit i has base i+1, weight (k+1)!/(i+1)!); equivalently k = (i+1)!/d - 1 for integers i >= 1, 1 <= d <= i.",
    ['In the Horimetrik framework (see LINKS) these are the "single-digit factorials" (Ein-Ziffern-Fakultaeten).',
     'Exactly i terms arise from each position i (d ranges over 1..i; divisibility is automatic since d <= i). Fully characterized with proof: exactness of k! = d*(k+1)!/(i+1)! forces d = (i+1)!/(k+1), and uniqueness of the digit expansion does the rest.',
     'The characterization supplied nine exact predictions (k = 29, 39, 59, 119 and 143, 179, 239, 359, 719) before computation.'],
    "Sorted values of (i+1)!/d - 1 over i >= 1, 1 <= d <= i.",
    "k=5 is a term: 5! = 120 = 1*720/3! is the single digit 1 at position 2 of horizon 5 (weight 6!/3! = 120), i.e. k = (i+1)!/d - 1 with i=2, d=1.",
    """from math import factorial
def upto(limit):
    vals = {factorial(i+1)//d - 1 for i in range(1, 20) for d in range(1, i+1)}
    return sorted(v for v in vals if v <= limit)""",
    "Cf. A000142.",
    "nonn,easy")

SEQS["folge9"] = block(
    bf("folge9_komposition.txt"), 1,
    "a(r) is the maximum of max_d (d + c_d(P o Q)) over all polynomials P, Q with nonnegative integer coefficients in the falling factorial basis satisfying max_d (d + c_d) <= r for both; equivalently a(r) = max_d (d + c_d(M_r o M_r)) with M_r(X) = Sum_{d=0}^{r-1} (r-d)*X_(d).",
    ['In the Horimetrik framework (see LINKS) this is the "maximal composition height" (maximale Kompositionshoehe).',
     'Proved: the semiring of polynomials with nonnegative integer falling-factorial coefficients is closed under composition (via a free symmetric-group action: the count N_m of tuples of injections covering an m-set is divisible by m!). Composition is coefficientwise monotone in both arguments, so the maximum is attained at the componentwise maximal polynomial M_r.',
     'Empirical (no proof): growth appears to be of order log(a(r)) ~ r^2*log(r).',
     'The analogous maxima for addition and forward difference are r+s (trivial) and floor((r+1)^2/4)-1 respectively.'],
    "a(r) = max_d (d + c_d(M_r o M_r)).",
    "For r=2: M_2(X) = X + 2 and (M_2 o M_2)(X) = (X+2) + 2 = X + 4, so a(2) = max(0+4, 1+1) = 4.",
    """from math import factorial, comb
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
    return max(d+c for d, c in out.items() if c > 0)""",
    "Cf. A000142.",
    "nonn")


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, content in SEQS.items():
        # Formalprüfungen nach eishelp1
        lines = content.rstrip("\n").split("\n")
        tags = [l.split()[0] for l in lines]
        for req in ("%I", "%S", "%N", "%K", "%O", "%A"):
            assert req in tags, (name, req)
        data = "".join(l[3:] for l in lines if l[:2] in ("%S", "%T", "%U"))
        assert " " not in data and data.count(",") >= 3, name
        assert sum(1 for t in tags if t == "%N") == 1, name
        with open(os.path.join(OUT, name + ".txt"), "w") as fh:
            fh.write(content)
        print(f"  {name}.txt: {len(lines)} Zeilen, DATA {len(data)} Zeichen")
    print("FERTIG")


if __name__ == "__main__":
    main()
