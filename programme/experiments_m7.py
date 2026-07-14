"""Sprungstellen m_g exakt via der Identitaet aus Satz S22.

M_{m-g}(m+1)/m! = (m+1) * T_{m-g},  T_s = sum_{k=1}^{s} k/(g+k+1)!.

Fuer kleine g: exakte endliche Summe, m aufsteigend.
Fuer grosse g: T_s ist im Suchbereich praktisch T_unendlich; wir
zertifizieren mit exakter Partialsumme S_K und Restschranke
R < 2*(K+1)/(g+K+2)!  (Quotienten der Terme sind < 1/2 ab k >= 2).
Alle Vergleiche in exakter Bruchrechnung -> die Ergebnisse sind
bewiesene Werte, keine Naeherungen.
"""

from fractions import Fraction
from math import factorial


def m_g_klein(g: int, limit: int = 200000) -> int:
    t = Fraction(0)
    k = 0
    for m in range(g + 1, limit):
        while k < m - g:
            k += 1
            t += Fraction(k, factorial(g + k + 1))
        if (m + 1) * t >= 1:
            return m
    raise RuntimeError("limit zu klein")


def m_g_gross(g: int, K: int = 300) -> int:
    s_k = sum(Fraction(k, factorial(g + k + 1)) for k in range(1, K + 1))
    rest = Fraction(2 * (K + 1), factorial(g + K + 2))
    # Kandidat: kleinstes m mit (m+1)*T >= 1, T in [s_k, s_k+rest]
    lo = int(1 / (s_k + rest)) - 2   # sicher unterhalb
    hi = int(1 / s_k) + 2            # sicher oberhalb
    for m in range(lo, hi + 2):
        if m - g < K:
            raise RuntimeError("Suchbereich beruehrt Truncation")
        passes_lower = (m + 1) * s_k >= 1                 # sicher JA
        fails_upper = (m + 1) * (s_k + rest) < 1          # sicher NEIN
        if passes_lower:
            return m
        if not fails_upper:
            raise RuntimeError(f"unentscheidbar bei m={m}, K erhoehen")
    raise RuntimeError("kein Treffer im Fenster")


if __name__ == "__main__":
    bekannt = {1: 3, 2: 15, 3: 84, 4: 533, 5: 3883, 6: 31998}
    print("Kreuzvalidierung gegen direkte Bigint-Messungen:")
    for g in range(1, 7):
        m = m_g_klein(g)
        status = "OK" if m == bekannt[g] else f"ABWEICHUNG (erwartet {bekannt[g]})"
        print(f"  m_{g} = {m}   {status}")
    print()
    print("Verlaengerung der Folge (zertifizierte Bruchrechnung):")
    folge = [bekannt[g] for g in range(1, 7)]
    for g in range(7, 13):
        m = m_g_gross(g)
        folge.append(m)
        ratio = m / factorial(g + 2)
        vorhersage = "  << VORHERSAGE-TEST: prognostiziert ~294875" if g == 7 else ""
        print(f"  m_{g} = {m}   m_g/(g+2)! = {ratio:.4f}{vorhersage}")
    print()
    print("Gesamtfolge:", folge)
