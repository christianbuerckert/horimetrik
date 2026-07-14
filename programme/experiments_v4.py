"""Entscheidung der Starrheitsfrage V4 durch Exzess-Konstruktionen.

Exzess-Koordinaten: (n, x) <-> (x, eps) mit eps = n - mu(x) >= 0.

Getestete Arithmetiken (Wertteil immer +, *):
  A3     vergessend:  eps_add = max via Horizonte, eps_mul = 0 (Satz A.3)
  TROP   bewahrend:   eps_add = max(ea, eb), eps_mul = ea + eb
  ARITH  verstaerkend: eps_add = ea + eb,     eps_mul = ea * eb

Behauptung: TROP und ARITH erfuellen ALLE strengen Gesetze und haben
eine Eins -> V4 ist widerlegt. ARITH hat zusaetzlich absorbierende Null.
"""

from __future__ import annotations

from itertools import product
from math import factorial

from horimetrik_reference import HoriNumber, minimal_value_horizon as mu


def elements_up_to(max_horizon: int):
    return [
        (n, x)
        for n in range(max_horizon + 1)
        for x in range(factorial(n + 1))
        if mu(x) <= n
    ]


def eps(a):
    return a[0] - mu(a[1])


# --- Arithmetiken -----------------------------------------------------------

def a3_add(a, b):
    (n, x), (m, y) = a, b
    return (max(n, m, mu(x + y)), x + y)


def a3_mul(a, b):
    (_, x), (_, y) = a, b
    return (mu(x * y), x * y)


def trop_add(a, b):
    (_, x), (_, y) = a, b
    return (mu(x + y) + max(eps(a), eps(b)), x + y)


def trop_mul(a, b):
    (_, x), (_, y) = a, b
    return (mu(x * y) + eps(a) + eps(b), x * y)


def arith_add(a, b):
    (_, x), (_, y) = a, b
    return (mu(x + y) + eps(a) + eps(b), x + y)


def arith_mul(a, b):
    (_, x), (_, y) = a, b
    return (mu(x * y) + eps(a) * eps(b), x * y)


PAIRS = {
    "A3    ": (a3_add, a3_mul, None),        # keine Eins erwartet
    "TROP  ": (trop_add, trop_mul, (1, 1)),  # Eins: Exzess 0 beim Wert 1
    "ARITH ": (arith_add, arith_mul, (2, 1)),  # Eins: Exzess 1 beim Wert 1
}


def valid(a) -> bool:
    return a[0] >= mu(a[1])


def check_pair(name, add, mul, unit, elems):
    print(f"--- {name} auf {len(elems)} Elementen ---")
    zero = (0, 0)

    problems = []
    for a, b in product(elems, repeat=2):
        for op, tag in ((add, "+"), (mul, "*")):
            r = op(a, b)
            if not valid(r):
                problems.append(("validitaet " + tag, a, b))
            if op(a, b) != op(b, a):
                problems.append(("kommutativ " + tag, a, b))
        if add(a, zero) != a:
            problems.append(("neutral +", a, zero))
        if problems:
            break

    if not problems:
        for a, b, c in product(elems, repeat=3):
            if add(add(a, b), c) != add(a, add(b, c)):
                problems.append(("assoziativ +", a, b, c))
                break
            if mul(mul(a, b), c) != mul(a, mul(b, c)):
                problems.append(("assoziativ *", a, b, c))
                break
            if mul(a, add(b, c)) != add(mul(a, b), mul(a, c)):
                problems.append(("distributiv", a, b, c))
                break

    print("  Gesetze: " + ("ALLE bestanden" if not problems else f"VERLETZT {problems[0]}"))

    if unit is not None:
        bad = next((a for a in elems if mul(a, unit) != a), None)
        print(f"  Eins {unit}: " + ("neutral" if bad is None else f"NICHT neutral, z.B. {bad}"))
    else:
        # zeige, dass kein Element Eins ist
        has_unit = any(all(mul(a, e) == a for a in elems) for e in elems)
        print("  Eins: " + ("existiert (?)" if has_unit else "existiert nicht (Enumeration)"))

    absorbed = all(mul(a, zero) == zero for a in elems)
    example = next((a for a in elems if mul(a, zero) != zero), None)
    print(
        "  Null absorbierend: "
        + ("ja" if absorbed else f"NEIN, z.B. {example} * (0,0) = {mul(example, zero)}")
    )


def ks(a):
    return_h = HoriNumber.encode(a[1], a[0]).structure_compact()
    return (return_h.horizon, return_h.value)


def check_ks_endomorphism(elems):
    print("--- Ist K_S ein Homomorphismus? (Paarpruefung) ---")
    for name, (add, mul, _) in PAIRS.items():
        bad_add = next(
            (
                (a, b)
                for a, b in product(elems, repeat=2)
                if ks(add(a, b)) != add(ks(a), ks(b))
            ),
            None,
        )
        bad_mul = next(
            (
                (a, b)
                for a, b in product(elems, repeat=2)
                if ks(mul(a, b)) != mul(ks(a), ks(b))
            ),
            None,
        )
        print(
            f"  {name}: K_S(+)-Hom: "
            + ("ja" if bad_add is None else f"NEIN {bad_add}")
            + " | K_S(*)-Hom: "
            + ("ja" if bad_mul is None else f"NEIN {bad_mul}")
        )


def check_kv_endomorphism(elems):
    print("--- Ist K_V ein Homomorphismus? ---")
    kv = lambda a: (mu(a[1]), a[1])
    for name, (add, mul, _) in PAIRS.items():
        bad = next(
            (
                (a, b, tag)
                for a, b in product(elems, repeat=2)
                for op, tag in ((add, "+"), (mul, "*"))
                if kv(op(a, b)) != op(kv(a), kv(b))
            ),
            None,
        )
        print(f"  {name}: " + ("ja, fuer + und *" if bad is None else f"NEIN {bad}"))


if __name__ == "__main__":
    small = elements_up_to(3)   # 33 Elemente, Tripel vollstaendig
    large = elements_up_to(4)   # 153 Elemente, Tripel vollstaendig (dauert)

    for name, (add, mul, unit) in PAIRS.items():
        check_pair(name, add, mul, unit, small)
    print()
    check_ks_endomorphism(small)
    print()
    check_kv_endomorphism(small)
    print()
    print("=== Grosser Lauf (H<=4, alle Tripel) fuer TROP und ARITH ===")
    for name in ("TROP  ", "ARITH "):
        add, mul, unit = PAIRS[name]
        check_pair(name, add, mul, unit, large)
