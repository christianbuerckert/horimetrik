"""Kompositionsabschluss und Kompositions-Kalkuel (Auftrag Christian, 14.07.2026).

Fragen:
  (K1) Ist S (nichtneg. Koeffizienten in fallender Fakultaetsbasis)
       unter Komposition P∘Q abgeschlossen? (Positivitaet UND
       Ganzzahligkeit der Newton-Koeffizienten)
  (K2) Gilt das Extremalprinzip: Gamma_comp(r,s) = sigma(M_r ∘ M_s)?
  (K3) Gamma_comp-Tabelle und Diagonale (OEIS-Kandidat).
  (K4) Shift-Ueberlauf: Gamma_E(r) = sigma(M_r(X+1)) = r + floor(r^2/4)?
Methodik: Newton-Koeffizienten via Differenzenschema aus Werten;
Brute Force ueber alle (r+1)!(s+1)! Paare fuer kleine r,s.
"""
from fractions import Fraction
from itertools import product
from math import factorial

def sigma(c):
    vals = [d + cd for d, cd in enumerate(c) if cd > 0]
    return max(vals) if vals else 0

def all_F(r):
    for c in product(*[range(r - d + 1) for d in range(r)]):
        yield c

def M(r):
    return tuple(r - d for d in range(r))

def evalP(c, x):
    """P(x) mit Koeffizienten c in fallender Fakultaetsbasis."""
    s = 0
    for d, cd in enumerate(c):
        if cd:
            ff = 1
            for j in range(d):
                ff *= (x - j)
            s += cd * ff
    return s

def newton_coeffs(values):
    """Koeffizienten in fallender Basis aus Werten an 0..deg:
    c_d = Delta^d f(0) / d!  (als Fraction, um Nicht-Ganzzahligkeit zu sehen)."""
    row = [Fraction(v) for v in values]
    out = []
    d = 0
    while row:
        out.append(row[0] / factorial(d))
        row = [row[i + 1] - row[i] for i in range(len(row) - 1)]
        d += 1
    while out and out[-1] == 0:
        out.pop()
    return out

def compose(cP, cQ):
    """Newton-Koeffizienten von P∘Q via Interpolation."""
    degP = max((d for d, v in enumerate(cP) if v), default=0)
    degQ = max((d for d, v in enumerate(cQ) if v), default=0)
    deg = degP * degQ
    vals = [evalP(cP, evalP(cQ, x)) for x in range(deg + 1)]
    return newton_coeffs(vals)

def check_in_S(c):
    """(ganzzahlig?, nichtnegativ?)"""
    return all(f.denominator == 1 for f in c), all(f >= 0 for f in c)

# (K1)+(K2): exhaustiv fuer r,s <= 4
print("== K1/K2: Abschluss + Extremalprinzip, exhaustiv ==")
for r in range(1, 5):
    for s in range(1, 5):
        best = -1
        for cP in all_F(r):
            for cQ in all_F(s):
                comp = compose(cP, cQ)
                ganz, pos = check_in_S(comp)
                assert ganz and pos, ("GEGENBEISPIEL", r, s, cP, cQ, comp)
                sg = sigma([int(f) for f in comp])
                if sg > best:
                    best = sg
        viaM = sigma([int(f) for f in compose(M(r), M(s))])
        assert best == viaM, ("EXTREMAL VERLETZT", r, s, best, viaM)
        print(f"   r={r}, s={s}: alle {factorial(r+1)*factorial(s+1)} Paare in S; "
              f"Gamma_comp={best} = sigma(M_r∘M_s)  OK")

# Zufallstest fuer groessere Horizonte
print("== K1: Zufallstest r,s bis 8 ==")
import random
random.seed(42)  # deterministisch reproduzierbar
for trial in range(300):
    r = random.randint(2, 8); s = random.randint(2, 8)
    cP = tuple(random.randint(0, r - d) for d in range(r))
    cQ = tuple(random.randint(0, s - d) for d in range(s))
    ganz, pos = check_in_S(compose(cP, cQ))
    assert ganz and pos, ("GEGENBEISPIEL", cP, cQ)
print("   300 Zufallspaare bis sigma=8: alle Kompositionen in S  OK")

# (K3): Tabelle + Diagonale
print("== K3: Gamma_comp(r,s) = sigma(M_r∘M_s) ==")
print("   r\\s " + "".join(f"{s:>10d}" for s in range(1, 7)))
diag = []
for r in range(1, 7):
    row = []
    for s in range(1, 7):
        g = sigma([int(f) for f in compose(M(r), M(s))])
        row.append(g)
    diag.append(row[r - 1])
    print(f"   {r}   " + "".join(f"{v:>10d}" for v in row))
print(f"   Diagonale Gamma_comp(r,r): {diag}")
diag7 = sigma([int(f) for f in compose(M(7), M(7))])
diag8 = sigma([int(f) for f in compose(M(8), M(8))])
print(f"   r=7: {diag7},  r=8: {diag8}")

# (K4): Shift E: P(X) -> P(X+1)
print("== K4: Shift-Ueberlauf ==")
for r in range(1, 13):
    shifted = compose(M(r), (1, 1))  # Q = X+1
    viaM = sigma([int(f) for f in shifted])
    # Brute Force fuer kleine r
    if r <= 5:
        bf = max(sigma([int(f) for f in compose(c, (1, 1))]) for c in all_F(r))
        assert bf == viaM, (r, bf, viaM)
    formel = r + r * r // 4
    assert viaM == formel, (r, viaM, formel)
print("   Gamma_E(r) = r + floor(r^2/4) fuer r<=12 (bis r=5 exhaustiv)  OK")
print("   Werte:", [r + r * r // 4 for r in range(1, 13)])

print("\nALLE TESTS BESTANDEN.")
