"""Verifikation der Inversionsfolgen-Einordnung (S44, 14.07.2026).

(1) H_n <-> Inversionsfolgen der Laenge n+1 <-> S_{n+1} (Bijektion)
(2) sigma(P_a) = n - min_{e_j>0}((j-1)-e_j)  mit e=(0,a)
(3) #{a in H_n : sigma(P_a)=r} = r*r!  (r>=1), einmal sigma=0
Alles exhaustiv fuer kleine n.
"""
from itertools import product, permutations
from math import factorial
from collections import Counter

def sigma_of_digits(a):
    n = len(a)
    vals = [d + a[n - 1 - d] for d in range(n) if a[n - 1 - d] > 0]
    return max(vals) if vals else 0

for n in range(1, 5):
    images = set()
    for pi in permutations(range(1, n + 2)):
        e = tuple(sum(1 for i in range(j) if pi[i] > pi[j]) for j in range(n + 1))
        images.add(e)
    expected = {(0,) + a for a in product(*[range(i + 1) for i in range(1, n + 1)])}
    assert images == expected and len(images) == factorial(n + 1)
print("(1) S_{n+1} -> Inversionsfolgen bijektiv auf {0} x H_n (n<=4)  OK")

for n in range(1, 7):
    cnt = Counter()
    for a in product(*[range(i + 1) for i in range(1, n + 1)]):
        e = (0,) + a
        s_vals = [(j - 1) - e[j - 1] for j in range(1, n + 2) if e[j - 1] > 0]
        via_e = n - min(s_vals) if s_vals else 0
        sig = sigma_of_digits(a)
        assert via_e == sig
        cnt[sig] += 1
    assert cnt[0] == 1
    for r in range(1, n + 1):
        assert cnt[r] == r * factorial(r)
print("(2)+(3) sigma-Formel und Niveauzaehlung r*r! exhaustiv (n<=6)  OK")
