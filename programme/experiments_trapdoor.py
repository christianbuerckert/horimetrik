"""Widerlegung der Delta-Trapdoor-Kryptographie (X9, 14.07.2026).

Gemini-Vorschlag: Einwegfunktion aus Differenzueberlauf + Seitentreue.
GPT-Widerlegung: y = P(N) ist durch fortgesetzte Division mit Rest
eindeutig und polynomial invertierbar, weil die Hori-Schranken
c_d <= r-d < N-d unter den Divisoren bleiben — Satz S1 am
verschobenen Auswertungspunkt. Hier exhaustiv verifiziert.
"""
from itertools import product

def evalP(c, x):
    s = 0
    for d, cd in enumerate(c):
        ff = 1
        for j in range(d):
            ff *= (x - j)
        s += cd * ff
    return s

def decode(y, N, m):
    """Fortgesetzte Division mit Rest: c_d = y_d mod (N-d)."""
    cs = []
    for d in range(m + 1):
        cd = y % (N - d)
        cs.append(cd)
        y = (y - cd) // (N - d)
    return tuple(cs)

assert evalP((2, 1, 2), 7) == 93 and decode(93, 7, 2) == (2, 1, 2)  # GPTs Beispiel

for r in range(1, 7):
    for c in product(*[range(r - d + 1) for d in range(r)]):
        for k in range(6):
            N = r + k + 1
            assert decode(evalP(c, N), N, r - 1) == c, (r, k, c)
print("X9 bestätigt: alle Gestalten bis r=6, Shifts k=0..5 eindeutig")
print("dekodiert — die 'Einwegfunktion' ist in O(m) Divisionen invertierbar.")
