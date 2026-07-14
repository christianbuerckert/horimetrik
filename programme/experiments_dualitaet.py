"""Zwei Experimente, 13.07.2026, dritte Sitzung.

1. Dualitaetskandidat (beantwortet V8):
   Strukturseitiger Spiegel von Satz A.3 auf Elementen (n, P):
     a [+] b = (max(n, m, sigma(P+Q)), P+Q)     konservative Strukturaddition
     a [*] b = (sigma(PQ), PQ)                  kompakte Strukturmultiplikation
   Erwartung: alle Gesetze streng, K_S ist Homomorphismus,
   h [*] (1,1) = K_S(h) — exakt spiegelbildlich zu A.3, wo
   h (*) (1,1) = K_V(h) gilt. Dieselbe Hori-Zahl "1" traegt beide
   Projektoren, je nach Multiplikation.

2. Angriff auf V1' (delta_hor >= -1):
   Konstruierte Kandidaten: Werte in der Schale [m!, (m+1)!) mit
   kleinem Strukturhorizont (moeglich ab m ~ 15), eingebettet in
   groessere Horizonte n > m.
"""

from __future__ import annotations

import random
from itertools import product
from math import factorial

from horimetrik_reference import (
    add_structures,
    multiply_structures,
    structure_sigma as sigma,
    minimal_value_horizon as mu,
)
from experiments_v1_probe import delta_hor, eval_falling, structure_of


# ---------------------------------------------------------------------------
# Teil 1: der strukturseitige Spiegel-Halbring
# ---------------------------------------------------------------------------

def selems(max_horizon: int):
    """Alle (n, P) mit sigma(P) <= n <= max_horizon, P als Koeffiziententupel."""
    result = []
    for n in range(max_horizon + 1):
        # alle gueltigen Ziffernfolgen in H_n entsprechen bijektiv den P
        for digits in product(*[range(i + 1) for i in range(1, n + 1)]):
            coeffs = tuple(reversed(digits))
            while coeffs and coeffs[-1] == 0:
                coeffs = coeffs[:-1]
            result.append((n, coeffs))
    return result


def sadd(a, b):
    (n, p), (m, q) = a, b
    s = add_structures(p, q)
    return (max(n, m, sigma(s)), s)


def smul(a, b):
    (_, p), (_, q) = a, b
    s = multiply_structures(p, q)
    return (sigma(s), s)


def kS(a):
    n, p = a
    return (sigma(p), p)


def kV(a):
    n, p = a
    v = eval_falling(list(p), n + 1)
    return (mu(v), tuple(structure_of(v, mu(v))))


def teil1(max_horizon: int = 4):
    elems = selems(max_horizon)
    print(f"=== Teil 1: Spiegel-Halbring auf {len(elems)} Elementen (n<={max_horizon}) ===")

    zero = (0, ())
    one = (1, (1,))

    bad = None
    for a, b in product(elems, repeat=2):
        if sadd(a, b) != sadd(b, a) or smul(a, b) != smul(b, a):
            bad = ("kommutativ", a, b)
            break
        if sadd(a, zero) != a:
            bad = ("neutral +", a)
            break
        if kS(sadd(a, b)) != sadd(kS(a), kS(b)):
            bad = ("K_S kein +-Hom", a, b)
            break
        if kS(smul(a, b)) != smul(kS(a), kS(b)):
            bad = ("K_S kein *-Hom", a, b)
            break
        if smul(a, one) != kS(a):
            bad = ("h*1 != K_S(h)", a)
            break
    print("  Paar-Gesetze/K_S-Hom/h*1=K_S: " + ("OK" if bad is None else f"VERLETZT {bad}"))

    kv_bad = next(
        (
            (a, b, tag)
            for a, b in product(elems, repeat=2)
            for op, tag in ((sadd, "+"), (smul, "*"))
            if kV(op(a, b)) != op(kV(a), kV(b))
        ),
        None,
    )
    print(
        "  K_V Homomorphismus des Spiegels: "
        + ("ja (unerwartet!)" if kv_bad is None else f"nein, z.B. {kv_bad[2]} bei {kv_bad[0]},{kv_bad[1]}")
    )

    bad3 = None
    small = selems(min(max_horizon, 3))
    for a, b, c in product(small, repeat=3):
        if sadd(sadd(a, b), c) != sadd(a, sadd(b, c)):
            bad3 = ("assoziativ +", a, b, c)
            break
        if smul(smul(a, b), c) != smul(a, smul(b, c)):
            bad3 = ("assoziativ *", a, b, c)
            break
        if smul(a, sadd(b, c)) != sadd(smul(a, b), smul(a, c)):
            bad3 = ("distributiv", a, b, c)
            break
    print(f"  Tripel-Gesetze (n<=3 vollstaendig): " + ("OK" if bad3 is None else f"VERLETZT {bad3}"))

    absorbing = all(smul(a, zero) == zero for a in selems(3))
    print("  Null absorbierend: " + ("ja" if absorbing else "NEIN"))


# ---------------------------------------------------------------------------
# Teil 2: gezielter Angriff auf V1'
# ---------------------------------------------------------------------------

def random_small_sigma_value(m: int, rng) -> int | None:
    """Zufaelliger Wert x mit mu(x) = m und sigma(E_m(x)) <= m-2.

    Konstruktion: nahe am Maximalpolynom M_{m-2} bleiben, damit der
    Wert die Schwelle m! ueberschreitet.
    """
    coeffs = [m - 2 - d for d in range(m - 2)]
    for d in range(len(coeffs)):
        if coeffs[d] > 0 and rng.random() < 0.35:
            coeffs[d] -= rng.randint(0, min(coeffs[d], 2))
    x = eval_falling(coeffs, m + 1)
    if factorial(m) <= x < factorial(m + 1) and sigma(coeffs) <= m - 2:
        return x
    return None


def teil2():
    print("=== Teil 2: V1'-Angriff mit konstruierten Kandidaten ===")
    rng = random.Random(407)
    global_min = 0
    witness = None
    for m in range(15, 23):
        xs = set()
        # deterministisch: das Maximalpolynom selbst
        x_max = eval_falling([m - 2 - d for d in range(m - 2)], m + 1)
        if factorial(m) <= x_max:
            xs.add(x_max)
        for _ in range(800):
            x = random_small_sigma_value(m, rng)
            if x is not None:
                xs.add(x)
        local_min, local_max = 0, 0
        for x in xs:
            for n in range(m, m + 9):
                d = delta_hor(n, x)
                if d < global_min:
                    global_min, witness = d, (n, x, d)
                local_min = min(local_min, d)
                local_max = max(local_max, d)
        print(
            f"  m={m}: {len(xs)} Kandidaten, delta in [{local_min:+d}, {local_max:+d}]"
        )
    print(
        f"  Globales Minimum: {global_min:+d}"
        + (f"  ZEUGE {witness}" if witness and global_min < -1 else "  (V1' haelt stand)")
    )


if __name__ == "__main__":
    teil1()
    print()
    teil2()
