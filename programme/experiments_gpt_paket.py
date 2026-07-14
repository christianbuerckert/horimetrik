"""Verifikation der vier GPT-Vorschlaege vom 13.07.2026 (nachts).

1. Kompaktifizierungsmonoid: Stabilitaetslemma (K_S erhaelt
   Wertkompaktheit), Relation VSV = SV, genau 6 Elemente.
2. D(n)-Umdeutung: sigma(P_a) < n  <=>  alle Ziffern unter Maximum
   <=> a = Z(b); D(n) zaehlt Schalenspringer.
3. Identitaet M_{m-g}(m+1)/m! = (m+1) * sum_{k=1}^{m-g} k/(g+k+1)!.
4. Interchange-Defekt Omega(h) = val(L Z h) - val(Z L h) >= 0.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import factorial

from horimetrik_reference import HoriNumber, minimal_value_horizon as mu
from experiments_v1_probe import eval_falling


def all_h(n):
    for x in range(factorial(n + 1)):
        yield HoriNumber.encode(x, n)


def S(h):
    return h.structure_compact()


def V(h):
    return h.value_compact()


def exp1_monoid(max_n=7):
    print("=== 1. Kompaktifizierungsmonoid ===")
    stab_ok = True
    rel_ok = True
    for n in range(max_n + 1):
        for h in all_h(n):
            k = V(h)
            if V(S(k)) != S(k):
                stab_ok = False
                print(f"  Stabilitaet VERLETZT bei {h.digits} in H{n}")
            if V(S(V(h))) != S(V(h)):
                rel_ok = False
    print(f"  Stabilitaetslemma (S erhaelt wertkompakt): "
          + ("OK bis H%d" % max_n if stab_ok else "VERLETZT"))
    print(f"  Relation VSV = SV: " + ("OK" if rel_ok else "VERLETZT"))

    # Unterscheidbarkeit der sechs Elemente: suche Trennzeugen
    maps = {
        "I": lambda h: h, "S": S, "V": V,
        "SV": lambda h: S(V(h)), "VS": lambda h: V(S(h)),
        "SVS": lambda h: S(V(S(h))),
    }
    names = list(maps)
    separated = {(a, b): None for i, a in enumerate(names) for b in names[i+1:]}
    for n in range(max_n + 1):
        for h in all_h(n):
            for (a, b), w in separated.items():
                if w is None and maps[a](h) != maps[b](h):
                    separated[(a, b)] = (n, h.value)
    missing = [p for p, w in separated.items() if w is None]
    print("  Alle 6 Elemente paarweise verschieden: "
          + ("JA" if not missing else f"NEIN, ununterscheidbar: {missing}"))
    print("  Beispieltrennzeugen:",
          {f"{a}!={b}": w for (a, b), w in list(separated.items())[:4]})

    # Idempotente
    idem = [nm for nm, f in maps.items()
            if all(f(f(h)) == f(h) for n in range(5) for h in all_h(n))]
    print(f"  Idempotente (bis H4): {idem}")


def exp2_defekt(max_n=8):
    print("=== 2. D(n) als Schalensprung ===")
    for n in range(3, max_n + 1):
        # alte Definition
        alt = sum(
            1 for x in range(factorial(n), factorial(n + 1))
            if HoriNumber.encode(x, n).structure_horizon < n
        )
        # neue Definition: b in H_{n-1}, Wert von Z(b) in H_n >= n!
        neu = sum(
            1 for x in range(factorial(n))
            if eval_falling(list(HoriNumber.encode(x, n - 1).structure), n + 1)
            >= factorial(n)
        )
        marker = "OK" if alt == neu else f"ABWEICHUNG {alt} != {neu}"
        print(f"  n={n}: D(n) = {alt} = Schalenspringer {neu}   {marker}")


def exp3_identitaet(max_m=40):
    print("=== 3. GPT-Identitaet fuer M_{m-g}(m+1)/m! ===")
    ok = True
    for g in range(1, 6):
        for m in range(g + 2, max_m, 7):
            s = m - g
            direkt = Fraction(
                eval_falling([s - d for d in range(s)], m + 1), factorial(m)
            )
            formel = (m + 1) * sum(
                Fraction(k, factorial(g + k + 1)) for k in range(1, s + 1)
            )
            if direkt != formel:
                ok = False
                print(f"  ABWEICHUNG bei g={g}, m={m}")
    print("  Identitaet exakt (Bruchrechnung): " + ("OK" if ok else "VERLETZT"))
    # c_g-Werte
    for g in range(1, 8):
        c = factorial(g + 2) * sum(
            Fraction(k, factorial(g + k + 1)) for k in range(1, 60)
        )
        print(f"  c_{g} = {float(c):.6f}   (g+2)!/c = {factorial(g+2)/float(c):.1f}"
              f"   m_g gemessen: {dict(zip(range(1,7),[3,15,84,533,3883,31998])).get(g,'-')}")


def exp4_omega(max_n=7):
    print("=== 4. Interchange-Defekt Omega ===")
    for n in range(1, max_n + 1):
        vals = []
        for h in all_h(n):
            lz = h.zero_extend().lift()          # erst Z, dann L
            zl = h.lift().zero_extend()          # erst L, dann Z
            vals.append(lz.value - zl.value)
        neg = sum(1 for v in vals if v < 0)
        nul = sum(1 for v in vals if v == 0)
        print(f"  H{n}: Omega in [{min(vals)}, {max(vals)}], "
              f"negativ: {neg}, Null: {nul} von {len(vals)}")


if __name__ == "__main__":
    exp1_monoid()
    print()
    exp2_defekt()
    print()
    exp3_identitaet()
    print()
    exp4_omega()
