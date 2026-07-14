"""Gezielte Folge-Experimente nach dem ersten Lauf vom 13. Juli 2026.

1. Vermutung: #\{wertkompakt, nicht strukturkompakt\} in H_n ist n!/2 fuer n >= 5.
2. Tieferer Gesetzestest fuer das Paar (+konservativ, *kompakt) auf H_0..H_4.
3. Test der Identitaet h (*kompakt) Eins = K_V(h).
"""

from __future__ import annotations

from itertools import product
from math import factorial

from horimetrik_reference import HoriNumber, minimal_value_horizon


def sigma_of_value(value: int, horizon: int) -> int:
    """sigma des Strukturpolynoms von E_horizon(value), ohne Objekt-Overhead."""
    rest = value
    sigma = 0
    for d, base in enumerate(range(horizon + 1, 1, -1)):
        digit = rest % base
        rest //= base
        if digit:
            sigma = max(sigma, d + digit)
    return sigma


def experiment_defect_counts(max_n: int = 9) -> None:
    print("=== Vermutung: wertkompakt ohne strukturkompakt = n!/2 (n >= 5) ===")
    for n in range(1, max_n + 1):
        lo, hi = factorial(n), factorial(n + 1)
        bad = sum(1 for x in range(lo, hi) if sigma_of_value(x, n) < n)
        note = f"n!/2 = {factorial(n) // 2}"
        print(f"  n={n}: {bad:>9}   ({note})" + ("   TREFFER" if bad == factorial(n) // 2 else ""))


def mu(x: int) -> int:
    return minimal_value_horizon(x)


def add_cons(a, b):
    n, x = a
    m, y = b
    return (max(n, m, mu(x + y)), x + y)


def mul_comp(a, b):
    n, x = a
    m, y = b
    return (mu(x * y), x * y)


def mul_add(a, b):
    n, x = a
    m, y = b
    return (n + m, x * y)


def elements_up_to(max_horizon: int):
    return [
        (n, x)
        for n in range(max_horizon + 1)
        for x in range(factorial(n + 1))
        if mu(x) <= n
    ]


def experiment_semiring_laws(max_horizon: int = 4) -> None:
    elems = elements_up_to(max_horizon)
    print(f"=== Gesetzestest (+konservativ, *kompakt) auf {len(elems)} Elementen ===")

    bad = None
    for a, b, c in product(elems, repeat=3):
        if add_cons(add_cons(a, b), c) != add_cons(a, add_cons(b, c)):
            bad = ("+assoc", a, b, c)
            break
        if mul_comp(a, add_cons(b, c)) != add_cons(mul_comp(a, b), mul_comp(a, c)):
            bad = ("distrib", a, b, c)
            break
        if mul_add(mul_add(a, b), c) != mul_add(a, mul_add(b, c)):
            bad = ("*additiv assoc", a, b, c)
            break
    print("  Ergebnis: " + ("alle Gesetze bestanden" if bad is None else f"VERLETZT {bad}"))

    one = (1, 1)
    ok = all(
        mul_comp(h, one)
        == (
            mu((lambda hn: hn.value)(HoriNumber.encode(x, n))),
            x,
        )
        and mul_comp((n, x), one)
        == (
            HoriNumber.encode(x, n).value_compact().horizon,
            HoriNumber.encode(x, n).value_compact().value,
        )
        for (n, x) in elems
        for h in [(n, x)]
    )
    print(f"  Identitaet h * 1 = K_V(h): " + ("bestaetigt" if ok else "WIDERLEGT"))

    zero = (0, 0)
    absorbing = all(mul_comp(a, zero) == zero for a in elems)
    print(f"  Null absorbierend unter *kompakt: " + ("ja" if absorbing else "NEIN"))


if __name__ == "__main__":
    experiment_defect_counts()
    print()
    experiment_semiring_laws()
