"""V4'-Sweep: Lassen sich Wert- und Strukturseite verweben?

Getestet werden alle 16 Arithmetiken aus
  Addition:        Payload {Wert, Struktur} x Selektor {kompakt, konservativ}
  Multiplikation:  Payload {Wert, Struktur} x Selektor {kompakt, konservativ}

"Gemischt" = Additionsseite != Multiplikationsseite (8 Kandidaten).
Bekannt gesetzestreu: Wert/kons + Wert/komp (A.3),
Struktur/kons + Struktur/komp (C.2), sowie die kollabierenden
kompakt/kompakt-Varianten je Seite.

Gesetze: Assoziativitaet beider Operationen, Distributivitaet,
(0,0) als Additionsneutral. Kommutativitaet ist bauartbedingt.
"""

from __future__ import annotations

from itertools import product
from math import factorial

from horimetrik_reference import (
    add_structures,
    multiply_structures,
    structure_sigma as sigma,
    minimal_value_horizon as mu,
)
from experiments_v1_probe import eval_falling, structure_of

_struct_cache: dict = {}


def struct(a):
    if a not in _struct_cache:
        _struct_cache[a] = tuple(structure_of(a[1], a[0]))
    return _struct_cache[a]


def make_op(payload: str, selector: str, kind: str):
    """kind in {add, mul}, payload in {wert, struktur}, selector in {komp, kons}."""

    def op(a, b):
        (n, x), (m, y) = a, b
        if payload == "wert":
            v = x + y if kind == "add" else x * y
            base = mu(v)
            h = base if selector == "komp" else max(n, m, base)
            return (h, v)
        p, q = struct(a), struct(b)
        s = add_structures(p, q) if kind == "add" else multiply_structures(p, q)
        base = sigma(s)
        h = base if selector == "komp" else max(n, m, base)
        return (h, eval_falling(list(s), h + 1))

    return op


def elements_up_to(max_horizon: int):
    return [
        (n, x)
        for n in range(max_horizon + 1)
        for x in range(factorial(n + 1))
        if mu(x) <= n
    ]


def check(addf, mulf, elems):
    zero = (0, 0)
    for a in elems:
        if addf(a, zero) != a:
            return f"neutral+ verletzt bei {a}"
    for a, b, c in product(elems, repeat=3):
        if addf(addf(a, b), c) != addf(a, addf(b, c)):
            return f"assoz+ verletzt bei {(a, b, c)}"
        if mulf(mulf(a, b), c) != mulf(a, mulf(b, c)):
            return f"assoz* verletzt bei {(a, b, c)}"
        if mulf(a, addf(b, c)) != addf(mulf(a, b), mulf(a, c)):
            return f"distrib verletzt bei {(a, b, c)}"
    return None


if __name__ == "__main__":
    elems = elements_up_to(3)
    print(f"Sweep ueber 16 Arithmetiken, Testraum H<=3 ({len(elems)} Elemente, alle Tripel)")
    print(f"{'Addition':<18} {'Multiplikation':<18} {'Seiten':<9} Ergebnis")
    survivors = []
    for ap, asel, mp, msel in product(
        ("wert", "struktur"), ("komp", "kons"), ("wert", "struktur"), ("komp", "kons")
    ):
        addf = make_op(ap, asel, "add")
        mulf = make_op(mp, msel, "mul")
        mixed = "GEMISCHT" if ap != mp else "rein"
        result = check(addf, mulf, elems)
        label_a = f"{ap}/{asel}"
        label_m = f"{mp}/{msel}"
        verdict = "GESETZESTREU" if result is None else result
        if result is None:
            survivors.append((label_a, label_m, mixed))
        print(f"{label_a:<18} {label_m:<18} {mixed:<9} {verdict}")
    print()
    print("Ueberlebende:", survivors)
    mixed_survivors = [s for s in survivors if s[2] == "GEMISCHT"]
    print(
        "Gemischte Ueberlebende: "
        + (str(mixed_survivors) if mixed_survivors else "KEINE — Seitentreue-Befund")
    )
