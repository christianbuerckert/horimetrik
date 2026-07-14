"""Experimente zu Horimetrik 0.1, Arbeitspakete B, C, D.

Alle Ergebnisse sind Enumerationen oder direkte Berechnungen.
Sie erzeugen Vermutungen und Gegenbeispiele, keine Beweise
(vgl. Arbeitsregel 16 in HORIMETRIK_0_1.md).
"""

from __future__ import annotations

from collections import Counter
from itertools import product
from math import factorial

from horimetrik_reference import (
    HoriNumber,
    add_structures,
    beta,
    maximal_structure,
    minimal_value_horizon,
    multiply_structures,
    structure_sigma,
)


# ---------------------------------------------------------------------------
# Experiment D1: beta(r, s) fuer groessere Horizonte, Diagonale, Argmax-Grad
# ---------------------------------------------------------------------------

def experiment_beta(max_r: int = 12) -> list[int]:
    print("=== D1: beta(r, s), Diagonale und Argmax-Grad ===")
    diagonal = []
    for r in range(1, max_r + 1):
        prod_coeffs = multiply_structures(
            maximal_structure(r), maximal_structure(r)
        )
        sigma = structure_sigma(prod_coeffs)
        argmax_d = max(
            (d for d, c in enumerate(prod_coeffs) if c > 0 and d + c == sigma),
        )
        diagonal.append(sigma)
        print(
            f"  beta({r},{r}) = {sigma:>12}   "
            f"Maximum bei Grad d={argmax_d}, Koeffizient c_d={sigma - argmax_d}"
        )
    print(f"  Diagonalfolge: {diagonal}")
    return diagonal


# ---------------------------------------------------------------------------
# Experiment D2: Additions-Gegenstueck beta_plus(r, s) = sigma(M_r + M_s)
# ---------------------------------------------------------------------------

def experiment_beta_plus(max_r: int = 10) -> None:
    print("=== D2: beta_plus(r, s) = sigma(M_r + M_s) ===")
    all_equal = True
    for r in range(1, max_r + 1):
        for s in range(1, max_r + 1):
            sigma = structure_sigma(
                add_structures(maximal_structure(r), maximal_structure(s))
            )
            if sigma != r + s:
                all_equal = False
                print(f"  Abweichung: beta_plus({r},{s}) = {sigma} != {r + s}")
    if all_equal:
        print(f"  beta_plus(r, s) == r + s fuer alle 1 <= r, s <= {max_r}.")
        print("  Auch strukturelle ADDITION kann den Horizont verdoppeln,")
        print("  anders als der Polynomgrad, der bei Addition nie waechst.")


# ---------------------------------------------------------------------------
# Experiment C1: Kompaktifizierungskommutator, vollstaendige Zaehlung
# ---------------------------------------------------------------------------

def all_hori_numbers(horizon: int):
    for value in range(factorial(horizon + 1)):
        yield HoriNumber.encode(value, horizon)


def experiment_commutator(max_horizon: int = 7) -> None:
    print("=== C1: K_S K_V vs K_V K_S, vollstaendige Zaehlung ===")
    print("  Konvention: 'SV' = erst K_V, dann K_S (also K_S nach K_V).")
    header = (
        "   n | Anzahl | KS-fix | KV-fix | beide | SV==VS | KSKV==KV"
    )
    print(header)
    kskv_always_kv = True
    minimal_diff = None
    for n in range(max_horizon + 1):
        total = ks_fix = kv_fix = both_fix = commute = kskv_is_kv = 0
        for h in all_hori_numbers(n):
            total += 1
            is_ks = h.structure_compact() == h
            is_kv = h.value_compact() == h
            ks_fix += is_ks
            kv_fix += is_kv
            both_fix += is_ks and is_kv
            sv = h.value_compact().structure_compact()
            vs = h.structure_compact().value_compact()
            if sv == vs:
                commute += 1
            elif minimal_diff is None:
                minimal_diff = (h, sv, vs)
            if sv == h.value_compact():
                kskv_is_kv += 1
            else:
                kskv_always_kv = False
        print(
            f"  {n:>2} | {total:>6} | {ks_fix:>6} | {kv_fix:>6} |"
            f" {both_fix:>5} | {commute:>6} | {kskv_is_kv:>8}"
        )
    if minimal_diff:
        h, sv, vs = minimal_diff
        print(f"  Kleinstes Nicht-Kommutieren: h = {h.digits} in H{h.horizon}")
        print(f"    K_S K_V (h) = {sv.digits} in H{sv.horizon}, Wert {sv.value}")
        print(f"    K_V K_S (h) = {vs.digits} in H{vs.horizon}, Wert {vs.value}")
    print(
        "  K_S K_V == K_V (wertkompakt => strukturkompakt): "
        + ("BESTAETIGT im Testbereich" if kskv_always_kv else "WIDERLEGT")
    )


# ---------------------------------------------------------------------------
# Experiment B1: Horizontselektoren fuer Wertarithmetik
# ---------------------------------------------------------------------------
# Ein Element ist ein Paar (n, x) mit n >= mu(x).
# Getestet werden Regeln fuer den Ergebnishorizont.

def mu(x: int) -> int:
    return minimal_value_horizon(x)


SELECTOR_ADD = {
    "kompakt": lambda n, m, x, y: mu(x + y),
    "konservativ": lambda n, m, x, y: max(n, m, mu(x + y)),
    "additiv": lambda n, m, x, y: max(n + m, mu(x + y)),
}

SELECTOR_MUL = {
    "kompakt": lambda n, m, x, y: mu(x * y),
    "konservativ": lambda n, m, x, y: max(n, m, mu(x * y)),
    "additiv": lambda n, m, x, y: n + m,
}


def elements_up_to(max_horizon: int):
    result = []
    for n in range(max_horizon + 1):
        for x in range(factorial(n + 1)):
            if mu(x) <= n:
                result.append((n, x))
    return result


def check_laws(max_horizon: int = 3) -> None:
    print("=== B1: Horizontselektoren, Gesetze per Enumeration ===")
    elems = elements_up_to(max_horizon)
    print(f"  Testraum: alle (n, x) mit n <= {max_horizon}, {len(elems)} Elemente")

    def run(name, op, sel, values_op):
        def apply(a, b):
            n, x = a
            m, y = b
            return (sel(n, m, x, y), values_op(x, y))

        comm_bad = assoc_bad = None
        for a, b in product(elems, repeat=2):
            if apply(a, b) != apply(b, a):
                comm_bad = (a, b)
                break
        for a, b, c in product(elems, repeat=3):
            if apply(apply(a, b), c) != apply(a, apply(b, c)):
                assoc_bad = (a, b, c)
                break
        print(
            f"  {op} [{name:<12}] kommutativ: "
            + ("ja" if comm_bad is None else f"NEIN, z.B. {comm_bad}")
        )
        print(
            f"  {op} [{name:<12}] assoziativ: "
            + ("ja" if assoc_bad is None else f"NEIN, z.B. {assoc_bad}")
        )
        return apply

    adders = {
        name: run(name, "+", sel, lambda x, y: x + y)
        for name, sel in SELECTOR_ADD.items()
    }
    multipliers = {
        name: run(name, "*", sel, lambda x, y: x * y)
        for name, sel in SELECTOR_MUL.items()
    }

    print("  --- strenge Distributivitaet a*(b+c) == a*b + a*c ---")
    for aname, addf in adders.items():
        for mname, mulf in multipliers.items():
            bad = None
            for a, b, c in product(elems, repeat=3):
                if mulf(a, addf(b, c)) != addf(mulf(a, b), mulf(a, c)):
                    bad = (a, b, c)
                    break
            verdict = "ja" if bad is None else f"NEIN, z.B. {bad}"
            print(f"    +[{aname}] mit *[{mname}]: {verdict}")

    print("  --- neutrale Elemente ---")
    for mname, mulf in multipliers.items():
        # Kandidat fuer die Eins: (1, 1), der kompakte Traeger der 1.
        one = (1, 1)
        bad = next(
            (a for a in elems if mulf(a, one) != a or mulf(one, a) != a),
            None,
        )
        print(
            f"    *[{mname}] mit Eins {one}: "
            + ("neutral" if bad is None else f"NICHT neutral, z.B. {bad}")
        )
    for aname, addf in adders.items():
        zero = (0, 0)
        bad = next(
            (a for a in elems if addf(a, zero) != a or addf(zero, a) != a),
            None,
        )
        print(
            f"    +[{aname}] mit Null {zero}: "
            + ("neutral" if bad is None else f"NICHT neutral, z.B. {bad}")
        )


# ---------------------------------------------------------------------------
# Experiment C2: Verteilung des Horizontdefekts delta_hor
# ---------------------------------------------------------------------------

def experiment_delta_distribution(max_horizon: int = 7) -> None:
    print("=== C2: Verteilung von delta_hor = hor(K_S K_V) - hor(K_V K_S) ===")
    for n in range(max_horizon + 1):
        counter = Counter()
        for h in all_hori_numbers(n):
            sv = h.value_compact().structure_compact()
            vs = h.structure_compact().value_compact()
            counter[sv.horizon - vs.horizon] += 1
        dist = ", ".join(
            f"{delta:+d}: {count}" for delta, count in sorted(counter.items())
        )
        print(f"  H{n}: {dist}")


if __name__ == "__main__":
    diagonal = experiment_beta()
    print()
    experiment_beta_plus()
    print()
    experiment_commutator()
    print()
    experiment_delta_distribution()
    print()
    check_laws()
