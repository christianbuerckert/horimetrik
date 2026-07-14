"""Gezielte Pruefung von V1 (delta_hor in {-1,0,+1}) bei grossen n.

Beobachtung: M_{n-2}(n+1) waechst wie c*(n+1)! mit c ~ 0.0635, waehrend
n! = (n+1)!/(n+1) faellt. Ab n ~ 15 gibt es also wertkompakte Zahlen,
deren Struktur sigma <= n-2 hat. Frage: reisst das delta_hor aus
{-1,0,+1} heraus?

delta_hor(h) = sigma(E_mu(x)(x)) - mu(val(K_S(h)))
mit h=(n,x), P = Struktur von E_n(x), val(K_S(h)) = P(sigma(P)+1).
"""

from __future__ import annotations

import random
from math import factorial

from horimetrik_reference import minimal_value_horizon as mu


def digits_of(value: int, horizon: int) -> list[int]:
    rest = value
    rev = []
    for base in range(horizon + 1, 1, -1):
        rev.append(rest % base)
        rest //= base
    return list(reversed(rev))


def structure_of(value: int, horizon: int) -> list[int]:
    coeffs = list(reversed(digits_of(value, horizon)))
    while coeffs and coeffs[-1] == 0:
        coeffs.pop()
    return coeffs


def sigma(coeffs) -> int:
    return max((d + c for d, c in enumerate(coeffs) if c > 0), default=0)


def eval_falling(coeffs, x: int) -> int:
    total = 0
    for d, c in enumerate(coeffs):
        term = 1
        for k in range(d):
            term *= x - k
        total += c * term
    return total


def delta_hor(n: int, x: int) -> int:
    # K_S K_V: erst wertkompakt, dann strukturkompakt
    mv = mu(x)
    left = sigma(structure_of(x, mv))
    # K_V K_S: erst strukturkompakt, dann wertkompakt
    coeffs = structure_of(x, n)
    s = sigma(coeffs)
    right = mu(eval_falling(coeffs, s + 1))
    return left - right


def max_poly_value(r: int, at: int) -> int:
    """Wert von M_r an der Stelle 'at'."""
    coeffs = [r - d for d in range(r)]
    return eval_falling(coeffs, at)


def probe():
    print("=== Wann uebersteigt M_{n-2}(n+1) die Schwelle n! ? ===")
    for n in range(5, 26):
        xstar = max_poly_value(n - 2, n + 1)
        marker = "  << ueberschreitet n!" if xstar >= factorial(n) else ""
        print(f"  n={n:>2}: M(n+1) = {xstar}  vs  n! = {factorial(n)}{marker}")

    print()
    print("=== delta_hor: gezielte und zufaellige Proben ===")
    rng = random.Random(2026)
    worst = {}
    for n in range(5, 22):
        lo, hi = 0, factorial(n + 1) - 1  # VOLLER Bereich, auch Exzess-Elemente
        candidates = set()
        # gezielt: Maximalpolynom-Werte kleiner Struktur, falls im Bereich
        for r in range(1, n + 1):
            v = max_poly_value(r, n + 1)
            if lo <= v <= hi:
                candidates.add(v)
                if v - 1 >= lo:
                    candidates.add(v - 1)
        # zufaellig, mit Gewicht auf kleinen Werten (Exzess-Elemente)
        for _ in range(3000):
            candidates.add(rng.randint(lo, hi))
        for k in range(1, min(n, 12)):
            for _ in range(400):
                candidates.add(rng.randint(0, factorial(k + 1) - 1))
        deltas = [delta_hor(n, x) for x in candidates]
        worst[n] = (min(deltas), max(deltas))
        outliers = [x for x in candidates if abs(delta_hor(n, x)) > 1]
        line = f"  n={n:>2}: delta_hor in [{min(deltas):+d}, {max(deltas):+d}] bei {len(candidates)} Proben"
        if outliers:
            x0 = min(outliers, key=lambda x: (abs(delta_hor(n, x)), x))
            line += f"   AUSREISSER z.B. x={x0}, delta={delta_hor(n, x0):+d}"
        print(line)


if __name__ == "__main__":
    probe()
