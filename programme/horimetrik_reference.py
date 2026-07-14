
"""Referenzimplementierung für Horimetrik 0.1.

Die Implementierung ist bewusst klein, exakt und nicht optimiert.
Sie dient zum Prüfen von Beispielen und zum Finden von Gegenbeispielen.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb, factorial
from typing import Iterable, Sequence


Coefficients = tuple[int, ...]  # c[d] ist Koeffizient von X falling d


def trim(coeffs: Iterable[int]) -> Coefficients:
    values = list(coeffs)
    while values and values[-1] == 0:
        values.pop()
    return tuple(values)


def falling(x: int, degree: int) -> int:
    result = 1
    for k in range(degree):
        result *= x - k
    return result


def evaluate_structure(coeffs: Sequence[int], x: int) -> int:
    return sum(c * falling(x, d) for d, c in enumerate(coeffs))


def structure_sigma(coeffs: Sequence[int]) -> int:
    return max((d + c for d, c in enumerate(coeffs) if c > 0), default=0)


def add_structures(a: Sequence[int], b: Sequence[int]) -> Coefficients:
    size = max(len(a), len(b))
    return trim(
        (a[d] if d < len(a) else 0) + (b[d] if d < len(b) else 0)
        for d in range(size)
    )


def multiply_structures(a: Sequence[int], b: Sequence[int]) -> Coefficients:
    """Produkt in der Basis der fallenden Fakultäten.

    (X)_p (X)_q =
      sum_j binom(p,j) binom(q,j) j! (X)_(p+q-j)
    """
    if not a or not b:
        return ()
    result = [0] * (len(a) + len(b) - 1)
    for p, cp in enumerate(a):
        for q, cq in enumerate(b):
            if cp == 0 or cq == 0:
                continue
            for j in range(min(p, q) + 1):
                degree = p + q - j
                result[degree] += (
                    cp * cq * comb(p, j) * comb(q, j) * factorial(j)
                )
    return trim(result)


def delta_structure(coeffs: Sequence[int]) -> Coefficients:
    """Vorwärtsdifferenz: Delta (X)_d = d (X)_(d-1)."""
    if len(coeffs) <= 1:
        return ()
    result = [0] * (len(coeffs) - 1)
    for d in range(1, len(coeffs)):
        result[d - 1] += d * coeffs[d]
    return trim(result)


def minimal_value_horizon(value: int) -> int:
    if value < 0:
        raise ValueError("Nur nichtnegative Werte sind in Version 0.1 erlaubt.")
    horizon = 0
    while value >= factorial(horizon + 1):
        horizon += 1
    return horizon


@dataclass(frozen=True)
class HoriNumber:
    horizon: int
    digits: tuple[int, ...]

    def __post_init__(self) -> None:
        if self.horizon < 0:
            raise ValueError("Der Horizont muss nichtnegativ sein.")
        if len(self.digits) != self.horizon:
            raise ValueError("Ziffernzahl und Horizont stimmen nicht überein.")
        for i, digit in enumerate(self.digits, start=1):
            if not 0 <= digit <= i:
                raise ValueError(
                    f"Ungültige Ziffer {digit} an Position {i}, erlaubt 0..{i}."
                )

    @property
    def value(self) -> int:
        value = 0
        for i, digit in enumerate(self.digits, start=1):
            value = value * (i + 1) + digit
        return value

    @property
    def structure(self) -> Coefficients:
        return trim(reversed(self.digits))

    @property
    def structure_horizon(self) -> int:
        return structure_sigma(self.structure)

    @classmethod
    def encode(cls, value: int, horizon: int) -> "HoriNumber":
        if horizon < 0:
            raise ValueError("Der Horizont muss nichtnegativ sein.")
        capacity = factorial(horizon + 1)
        if not 0 <= value < capacity:
            raise ValueError(
                f"Wert {value} passt nicht in H{horizon}, Kapazität {capacity}."
            )
        rest = value
        reversed_digits: list[int] = []
        for base in range(horizon + 1, 1, -1):
            reversed_digits.append(rest % base)
            rest //= base
        assert rest == 0
        return cls(horizon, tuple(reversed(reversed_digits)))

    @classmethod
    def from_structure(
        cls, coeffs: Sequence[int], horizon: int | None = None
    ) -> "HoriNumber":
        coeffs = trim(coeffs)
        minimum = structure_sigma(coeffs)
        if horizon is None:
            horizon = minimum
        if horizon < minimum:
            raise ValueError(
                f"Struktur benötigt mindestens H{minimum}, erhalten H{horizon}."
            )
        padded = list(coeffs) + [0] * (horizon - len(coeffs))
        digits = tuple(reversed(padded))
        return cls(horizon, digits)

    def zero_extend(self, target_horizon: int | None = None) -> "HoriNumber":
        if target_horizon is None:
            target_horizon = self.horizon + 1
        if target_horizon < self.horizon:
            raise ValueError("Strukturtreue Erweiterung kann nicht verkleinern.")
        return HoriNumber(
            target_horizon,
            (0,) * (target_horizon - self.horizon) + self.digits,
        )

    def lift(self, target_horizon: int | None = None) -> "HoriNumber":
        if target_horizon is None:
            target_horizon = self.horizon + 1
        if target_horizon < self.horizon:
            raise ValueError("Der Lift kann nicht in einen kleineren Horizont gehen.")
        return HoriNumber.encode(self.value, target_horizon)

    def value_compact(self) -> "HoriNumber":
        return HoriNumber.encode(self.value, minimal_value_horizon(self.value))

    def structure_compact(self) -> "HoriNumber":
        return HoriNumber.from_structure(self.structure)

    def structural_add(self, other: "HoriNumber") -> "HoriNumber":
        """Strukturaddition, Ergebnis strukturell kompakt.

        Achtung: Der Ergebniswert bezieht sich auf den neuen Strukturhorizont.
        Dies ist nicht automatisch die Addition der aktuellen Werte.
        """
        return HoriNumber.from_structure(
            add_structures(self.structure, other.structure)
        )

    def structural_multiply(self, other: "HoriNumber") -> "HoriNumber":
        """Strukturmultiplikation, Ergebnis strukturell kompakt.

        Achtung: Der Ergebniswert bezieht sich auf den neuen Strukturhorizont.
        Dies ist nicht automatisch das Produkt der aktuellen Werte.
        """
        return HoriNumber.from_structure(
            multiply_structures(self.structure, other.structure)
        )


def maximal_structure(horizon: int) -> Coefficients:
    if horizon < 0:
        raise ValueError("Der Horizont muss nichtnegativ sein.")
    return tuple(horizon - d for d in range(horizon))


def beta(r: int, s: int) -> int:
    return structure_sigma(
        multiply_structures(maximal_structure(r), maximal_structure(s))
    )


def self_test() -> None:
    h = HoriNumber(4, (0, 0, 1, 2))
    assert h.value == 7
    assert h.structure == (2, 1)

    z = h.zero_extend()
    assert z.digits == (0, 0, 0, 1, 2)
    assert z.value == 8
    assert z.structure == h.structure

    lifted = h.lift()
    assert lifted.digits == (0, 0, 0, 1, 1)
    assert lifted.value == 7

    assert h.structure_compact() == HoriNumber(2, (1, 2))
    assert h.value_compact() == HoriNumber(3, (0, 1, 3))

    x = HoriNumber(3, (0, 1, 0))  # X bei X=4, Wert 4
    xp1 = HoriNumber(3, (0, 1, 1))  # X+1 bei X=4, Wert 5
    product = x.structural_multiply(xp1)
    assert product == HoriNumber(3, (1, 2, 0))
    assert product.value == 20

    # Nichtkommutativität der Kompaktifizierungen
    ks_then_kv = h.structure_compact().value_compact()
    kv_then_ks = h.value_compact().structure_compact()
    assert ks_then_kv != kv_then_ks
    assert ks_then_kv == HoriNumber(2, (1, 2))
    assert kv_then_ks == HoriNumber(3, (0, 1, 3))

    expected = [
        [1, 2, 3, 4, 5],
        [2, 6, 10, 14, 18],
        [3, 10, 22, 36, 55],
        [4, 14, 36, 87, 162],
        [5, 18, 55, 162, 407],
    ]
    actual = [[beta(r, s) for s in range(1, 6)] for r in range(1, 6)]
    assert actual == expected


if __name__ == "__main__":
    self_test()
    print("Alle Horimetrik-0.1-Selbsttests erfolgreich.")
