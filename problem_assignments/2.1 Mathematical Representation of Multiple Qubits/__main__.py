import unittest
import qutip as qp  # pyright: ignore [reportMissingTypeStubs]
import numpy as np
from typing import cast


class Tests(unittest.TestCase):
    def test_1_a(self) -> None:
        q1 = qp.Qobj([np.sqrt(3) / 2, 1 / 2])
        q2 = qp.Qobj([1 / np.sqrt(2), 1 / np.sqrt(2)])
        tensor = cast(qp.Qobj, qp.tensor(q1, q2))
        state_probabilities = {
            "|00⟩": np.sqrt(3) / (2 * np.sqrt(2)),
            "|01⟩": np.sqrt(3) / (2 * np.sqrt(2)),
            "|10⟩": 1.0 / (2 * np.sqrt(2)),
            "|11⟩": 1.0 / (2 * np.sqrt(2)),
        }
        self.assertTrue(
            np.allclose(
                tensor.data.to_array(),  # pyright: ignore
                np.array(
                    [
                        state_probabilities["|00⟩"],
                        state_probabilities["|01⟩"],
                        state_probabilities["|10⟩"],
                        state_probabilities["|11⟩"],
                    ]
                ).reshape(-1, 1),
            ),
        )


def main() -> None:
    unittest.main(exit=False)
    print(
        """Task
        1.b) αγ|00⟩ + αδ|01⟩ + βγ|10⟩ + βδ|11⟩
        1.c) α|00⟩ + β|10⟩"""
    )
    print(f"Task 2. {qp.states.ket("001110")=}")


if __name__ == "__main__":
    main()
