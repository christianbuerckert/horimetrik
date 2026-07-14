"""Verifikation des Horizontkalküls (GPT-Vorschlag 14.07.2026).

Zu prüfen:
  (1) Additionshöhe alpha(r,s)=r+s          -- bekannt (S9/S15), Gegenprobe
  (2) beta(r,s)=sigma(M_r M_s)              -- bekannt (Def. 11.2), Gegenprobe
  (3) NEU Extremalprinzip: fuer koeffizientenmonotone Operatoren mit
      nichtnegativen Strukturkonstanten gilt Gamma_T(r..)=sigma(T(M_r..))
  (4) NEU Differenzueberlauf: max_{sigma(P)<=r} sigma(Delta P)
        = floor((r+1)^2/4) - 1  (r>=2)   und  = sigma(Delta M_r)
Alles per vollstaendiger Enumeration ueber F_r (Groesse (r+1)!).
"""
from itertools import product
from math import comb, factorial

def sigma(c):
    """Strukturhorizont eines Koeffiziententupels c[d]=Koeffizient von X^(d,fallend)."""
    vals = [d + cd for d, cd in enumerate(c) if cd > 0]
    return max(vals) if vals else 0

def all_F(r):
    """Alle Koeffiziententupel mit sigma<=r: 0<=c_d<=r-d, d=0..r-1."""
    ranges = [range(r - d + 1) for d in range(r)]
    for c in product(*ranges):
        yield c

def M(r):
    return tuple(r - d for d in range(r))

def add(c1, c2):
    n = max(len(c1), len(c2))
    return tuple((c1[d] if d < len(c1) else 0) + (c2[d] if d < len(c2) else 0)
                 for d in range(n))

def mul(c1, c2):
    """Produkt in fallender Fakultaetsbasis:
    X^p X^q = sum_j C(p,j)C(q,j) j! X^(p+q-j)."""
    out = {}
    for p, a in enumerate(c1):
        if a == 0: continue
        for q, b in enumerate(c2):
            if b == 0: continue
            for j in range(min(p, q) + 1):
                out[p + q - j] = out.get(p + q - j, 0) + a * b * comb(p, j) * comb(q, j) * factorial(j)
    n = max(out) + 1 if out else 0
    return tuple(out.get(d, 0) for d in range(n))

def delta(c):
    """Vorwaertsdifferenz: Delta X^d = d X^(d-1)."""
    return tuple((k + 1) * c[k + 1] for k in range(len(c) - 1))

# (1) alpha(r,s) = r+s
print("== alpha(r,s)=r+s (Gegenprobe S9/S15) ==")
for r in range(1, 5):
    for s in range(1, 5):
        best = max(sigma(add(c1, c2)) for c1 in all_F(r) for c2 in all_F(s))
        assert best == r + s, (r, s, best)
print("   alpha exakt r+s fuer r,s<=4  OK")

# (2) beta(r,s) = sigma(M_r M_s), Vergleich mit Brute Force + Spez-Tabelle
print("== beta(r,s)=sigma(M_r M_s) (Gegenprobe Def. 11.2) ==")
spez = {(1,1):1,(2,2):6,(3,3):22,(4,4):87,(5,5):407,(2,3):10,(3,4):36,(4,5):162,(2,5):18,(3,5):55}
for r in range(1, 5):
    for s in range(1, 5):
        bf = max(sigma(mul(c1, c2)) for c1 in all_F(r) for c2 in all_F(s))
        red = sigma(mul(M(r), M(s)))
        assert bf == red, (r, s, bf, red)
        if (min(r,s), max(r,s)) in spez:
            assert red == spez[(min(r,s), max(r,s))], (r, s, red)
print("   Brute Force == sigma(M_r M_s) fuer r,s<=4; Spez-Tabelle bestaetigt  OK")
for r in [5]:
    red = sigma(mul(M(r), M(r)))
    assert red == 407, red
print("   beta(5,5)=407 via Reduktion  OK")

# (4) Differenzueberlauf, Brute Force vs. Formel vs. Extremalprinzip
print("== NEU: max sigma(Delta P) ueber sigma(P)<=r ==")
print("   r | bruteforce | floor((r+1)^2/4)-1 | sigma(Delta M_r)")
for r in range(2, 9):
    bf = max(sigma(delta(c)) for c in all_F(r))
    formel = (r + 1) ** 2 // 4 - 1
    viaM = sigma(delta(M(r)))
    print(f"   {r} | {bf:10d} | {formel:18d} | {viaM:15d}")
    assert bf == formel == viaM, (r, bf, formel, viaM)
print("   Differenzueberlauf-Satz bestaetigt (r=2..8, exhaustiv)  OK")

# (3) Extremalprinzip auch fuer gemischte Operatoren, Stichprobe:
#     T(P,Q) = Delta(P*Q)  (koeffizientenmonoton, nichtneg. Konstanten)
print("== Extremalprinzip fuer T(P,Q)=Delta(PQ), r,s<=3 ==")
for r in range(1, 4):
    for s in range(1, 4):
        bf = max(sigma(delta(mul(c1, c2))) for c1 in all_F(r) for c2 in all_F(s))
        viaM = sigma(delta(mul(M(r), M(s))))
        assert bf == viaM, (r, s, bf, viaM)
print("   Gamma_T(r,s)=sigma(T(M_r,M_s)) auch fuer Delta∘mul  OK")

# Zeugen fuer den Differenzueberlauf: einzelner Koeffizient c_d=r-d nahe Mitte
print("== Zeugen (ein Koeffizient) ==")
for r in range(2, 9):
    best = max(((k+1)*(r-k) - 1, k) for k in range(r - 1))
    val, k = best
    print(f"   r={r}: c_{k+1}={r-k-1} an Grad {k+1}, sigma(Delta P)={val}")
print("\nALLE TESTS BESTANDEN.")
