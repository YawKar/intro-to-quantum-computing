import unittest
from dataclasses import dataclass
import numpy as np
from typing import Any, Optional


@dataclass(frozen=True)
class DiracState:
    alpha: np.float64
    beta: np.float64

    def to_vector(self) -> np.ndarray[Any, np.dtypes.Float64DType]:
        return np.array([self.alpha, self.beta], dtype=np.dtypes.Float64DType)

    def __str__(self) -> str:
        return f"{self.alpha}*|0⟩ + {self.beta}*|1⟩"

    @staticmethod
    def from_str(string: str) -> Optional["DiracState"]:
        try:
            zero_state_term, one_state_term = string.strip().replace(" ", "").split("+")
            zero_state_prob = np.float64(zero_state_term.split("*")[0])
            one_state_prob = np.float64(one_state_term.split("*")[0])
            return DiracState(zero_state_prob, one_state_prob)
        except Exception as exc:
            print(exc)
            return None


class Test(unittest.TestCase):
    def test_convertion_to_dirac_notation(self) -> None:
        random_valid_state: DiracState = DiracState(
            alpha := np.float64(np.random.rand()),
            beta=np.sqrt(1.0 - alpha**2),
        )
        self.assertAlmostEqual(
            (random_valid_state.to_vector() ** 2).sum(),
            1.0,
        )
        self.assertEqual(
            DiracState.from_str(str(random_valid_state)),
            random_valid_state,
        )


if __name__ == "__main__":
    unittest.main()
