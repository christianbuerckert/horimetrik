#!/usr/bin/env python3
"""OEIS-b-File-Generator der Horimetrik (14.07.2026).

Berechnet die neun Zählfolgen des Buchs, verifiziert sie gegen
Brute-Force-Enumeration (kleine Horizonte) und gegen die zuvor
eingecheckten b-Files (Präfix-Abgleich) und schreibt erweiterte
b-Files nach oeis/bfiles/. Grundsatz des Projekts: Formeln werden
nur dort zur Erzeugung benutzt, wo sie bewiesen sind, und auch dann
gegen unabhängige Enumeration geprüft.
"""
from fractions import Fraction
from math import factorial, comb
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BFILE_DIR = os.path.join(os.path.dirname(HERE), "oeis", "bfiles")


# ---------- Bausteine ----------

def encode(x, n):
    """Ziffern (a_1,...,a_n) von x im Horizont H_n (0 <= a_i <= i)."""
    digits = []
    for base in range(n + 1, 1, -1):
        x, r = divmod(x, base)
        digits.append(r)
    assert x == 0, "Wert passt nicht in den Horizont"
    return digits[::-1]


def ff_mul(A, B):
    """Produkt zweier Polynome in der fallenden Fakultätsbasis.

    X_(p) * X_(q) = Sum_j C(p,j) C(q,j) j! X_(p+q-j).
    """
    out = {}
    for p, a in A.items():
        for q, b in B.items():
            ab = a * b
            for j in range(min(p, q) + 1):
                d = p + q - j
                out[d] = out.get(d, 0) + ab * comb(p, j) * comb(q, j) * factorial(j)
    return {d: c for d, c in out.items() if c}


def ff_eval(P, x):
    total = 0
    for d, c in P.items():
        t = 1
        for k in range(d):
            t *= x - k
        total += c * t
    return total


def ff_compose(P, Q):
    """P o Q in der fallenden Fakultätsbasis: Sum_d c_d(P) * (Q)_(d)."""
    out = {}
    FF = {0: 1}  # (Q)_(0) = 1
    maxd = max(P)
    for d in range(maxd + 1):
        c = P.get(d, 0)
        if c:
            for deg, coeff in FF.items():
                out[deg] = out.get(deg, 0) + c * coeff
        if d < maxd:
            Qm = dict(Q)
            Qm[0] = Qm.get(0, 0) - d
            FF = ff_mul(FF, Qm)
    return {d: c for d, c in out.items() if c}


def sigma(P):
    return max((d + c for d, c in P.items() if c > 0), default=0)


def M(r):
    """Maximal gefüllte Gestalt des Horizonts r."""
    return {d: r - d for d in range(r)}


# ---------- Folge 1: Sprungstellen des Tiefengesetzes ----------

def sprungstelle(g, K=400):
    """Kleinstes m mit M_{m-g}(m+1) >= m!, exakt zertifiziert.

    F(m) = (m+1) * Sum_{k=1..m-g} k/(g+k+1)!  (bewiesene Identität);
    Restglied-Schranke Sum_{k>K} k/(g+k+1)! <= 2(K+1)/(g+K+2)!
    (Quotientenkriterium, Faktor <= 1/2). Binäre Suche, da F streng
    wächst; obere Grenze m+1 <= (g+2)! ist bewiesen.
    """
    S = [Fraction(0)]
    for k in range(1, K + 1):
        S.append(S[-1] + Fraction(k, factorial(g + k + 1)))
    tail = Fraction(2 * (K + 1), factorial(g + K + 2))

    def ge1(m):
        t = m - g
        if t <= 0:
            return False
        if t <= K:
            return (m + 1) * S[t] >= 1
        if (m + 1) * S[K] >= 1:
            return True
        assert (m + 1) * (S[K] + tail) < 1, "K zu klein: Rest nicht zertifiziert"
        return False

    lo, hi = g + 1, factorial(g + 2) - 1
    assert ge1(hi)
    while lo < hi:
        mid = (lo + hi) // 2
        if ge1(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


# ---------- Folgen 3/7: Springer und Nicht-Springer ----------

def nichtspringer_formel(n):
    """Bewiesene Ziffernformel: N(n) = Sum_{p=1}^P min(d_p,p) n!/p!,
    d = Ziffern von n! in H_n, P = erste Position mit Maximalziffer
    (d_P = P), sonst P = n."""
    d = encode(factorial(n), n)
    P = n
    for p in range(1, n + 1):
        if d[p - 1] == p:
            P = p
            break
    return sum(min(d[p - 1], p) * factorial(n) // factorial(p)
               for p in range(1, P + 1))


def nichtspringer_brute(n):
    """Enumeration: Ziffernfolgen mit a_i <= i-1 und Wert < n!."""
    v = np.zeros(1, dtype=np.int64)
    for i in range(1, n + 1):
        w = factorial(n + 1) // factorial(i + 1)
        v = (v[:, None] + np.arange(i, dtype=np.int64) * w).ravel()
    return int((v < factorial(n)).sum())


# ---------- Folgen 5/6: Interchange-Maxima und -Nullzähler ----------

def omega_stats(n_max, chunk=8_000_000):
    """(max Omega, #{Omega=0}) auf H_n für n = 1..n_max.

    z_n(x) = r + (n+2) z_{n-1}(q) mit x = q(n+1)+r;
    Omega_n(x) = z_n(x) - z_{n+1}(x) und
    z_{n+1}(x) = x mod (n+2) + (n+3) z_n(x div (n+2)).
    """
    res = {}
    Z = np.array([0, 1], dtype=np.int64)  # z_1
    n = 1
    while True:
        size = factorial(n + 1)
        mx, zc = 0, 0
        for lo in range(0, size, chunk):
            hi = min(lo + chunk, size)
            x = np.arange(lo, hi, dtype=np.int64)
            om = Z[lo:hi] - (x % (n + 2) + (n + 3) * Z[x // (n + 2)])
            assert int(om.min()) >= 0, "Interchange-Positivität verletzt!"
            mx = max(mx, int(om.max()))
            zc += int((om == 0).sum())
        res[n] = (mx, zc)
        if n == n_max:
            return res
        n += 1
        size = factorial(n + 1)
        Znew = np.empty(size, dtype=np.int64)
        for lo in range(0, size, chunk):
            hi = min(lo + chunk, size)
            x = np.arange(lo, hi, dtype=np.int64)
            Znew[lo:hi] = x % (n + 1) + (n + 2) * Z[x // (n + 1)]
        Z = Znew


# ---------- Folge 8: Ein-Ziffern-Fakultäten ----------

def einziffer_formel(max_i):
    """Bewiesene Charakterisierung: n = (i+1)!/d - 1, 1 <= d <= i."""
    vals = {factorial(i + 1) // d - 1
            for i in range(1, max_i + 1) for d in range(1, i + 1)}
    assert len(vals) == max_i * (max_i + 1) // 2, "unerwartete Kollision"
    return sorted(vals)


def einziffer_brute(n_max):
    out = []
    for n in range(1, n_max + 1):
        if sum(1 for t in encode(factorial(n), n) if t) == 1:
            out.append(n)
    return out


# ---------- b-File-Verwaltung ----------

def read_bfile(name):
    path = os.path.join(BFILE_DIR, name)
    if not os.path.exists(path):
        return []
    with open(path) as fh:
        return [(int(a), int(b)) for a, b in
                (line.split() for line in fh if line.strip())]


def write_bfile(name, pairs):
    old = read_bfile(name)
    for o, n in zip(old, pairs):
        assert o == n, f"{name}: Widerspruch zum alten b-File bei {o} vs {n}"
    with open(os.path.join(BFILE_DIR, name), "w") as fh:
        fh.writelines(f"{i} {v}\n" for i, v in pairs)
    print(f"  {name}: {len(pairs)} Terme"
          + (f" (vorher {len(old)})" if old else " (neu)"))


def main():
    print("== Folge 2 (beta) und Folge 9 (Komposition): Kalkül-Selbsttest ==")
    # Unabhängige Prüfung der Basis-Arithmetik durch Auswertung.
    for r in range(1, 6):
        for x in range(r + 1, r + 5):
            assert ff_eval(ff_mul(M(r), M(r)), x) == ff_eval(M(r), x) ** 2
            assert ff_eval(ff_compose(M(r), M(r)), x) == ff_eval(M(r), ff_eval(M(r), x))
    beta = [(r, sigma(ff_mul(M(r), M(r)))) for r in range(1, 25)]
    comp = []
    for r in range(1, 13):
        C = ff_compose(M(r), M(r))
        assert all(c >= 0 for c in C.values()), "Kompositionsabschluss verletzt!"
        comp.append((r, sigma(C)))

    print("== Folgen 3/4/7: Ziffernformel gegen Enumeration (n <= 10) ==")
    for n in range(1, 11):
        f, b = nichtspringer_formel(n), nichtspringer_brute(n)
        assert f == b, f"Ziffernformel weicht ab bei n={n}: {f} != {b}"
    nicht = [(n, nichtspringer_formel(n)) for n in range(1, 21)]
    springer = [(n, factorial(n) - v) for n, v in nicht if factorial(n) - v > 0]
    fix = [(n, n * factorial(n) - (factorial(n) - nichtspringer_formel(n)))
           for n in range(2, 21)]

    print("== Folgen 5/6: Interchange-DP (H_1..H_10) ==")
    st = omega_stats(10)
    om_max = [(n, st[n][0]) for n in sorted(st)]
    om_null = [(n, st[n][1]) for n in sorted(st)]

    print("== Folge 8: Charakterisierung gegen Enumeration (n <= 200) ==")
    fo = einziffer_formel(9)
    br = einziffer_brute(200)
    assert [v for v in fo if v <= 200] == br, "Ein-Ziffern-Abgleich fehlgeschlagen"
    einziffer = list(enumerate(fo, start=1))

    print("== Folge 1: Sprungstellen (binäre Suche, zertifiziert) ==")
    sprung = [(g, sprungstelle(g)) for g in range(1, 17)]

    print("== b-Files schreiben (Präfix-Abgleich gegen Bestand) ==")
    write_bfile("folge1_sprungstellen.txt", sprung)
    write_bfile("folge2_beta.txt", beta)
    write_bfile("folge3_schalenspringer.txt", springer)
    write_bfile("folge4_fixpunkte.txt", fix)
    write_bfile("folge5_omega_max.txt", om_max)
    write_bfile("folge6_omega_null.txt", om_null)
    write_bfile("folge7_nichtspringer.txt", nicht)
    write_bfile("folge8_einziffer.txt", einziffer)
    write_bfile("folge9_komposition.txt", comp)
    print("FERTIG — alle Prüfungen bestanden.")


if __name__ == "__main__":
    main()
