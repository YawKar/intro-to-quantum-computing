import unittest
import numpy as np
from typing import Literal, TypedDict, Any


class Test(unittest.TestCase):

    def test_probabilities_of_measuring_states_of_a_qubit(self) -> None:
        class Exercise(TypedDict):
            current_state: np.ndarray[Any, Any]
            target_state: Literal["|0⟩", "|1⟩"]
            probability_answer: np.float64

        tests: dict[str, Exercise] = {
            "a": {
                "current_state": np.array([np.sqrt(3) / 2, 0.5]),
                "target_state": "|0⟩",
                "probability_answer": np.float64(0.75),
            },
            "b": {
                "current_state": np.array([np.sqrt(3) / 2, 0.5]),
                "target_state": "|1⟩",
                "probability_answer": np.float64(0.25),
            },
            "c": {
                "current_state": np.array([1 / np.sqrt(2), 1 / np.sqrt(2)]),
                "target_state": "|0⟩",
                "probability_answer": np.float64(0.5),
            },
            "d": {
                "current_state": np.array([1 / np.sqrt(2), 1 / np.sqrt(2)]),
                "target_state": "|1⟩",
                "probability_answer": np.float64(0.5),
            },
        }

        for sample, test in tests.items():
            self.assertAlmostEqual(
                test["current_state"][0 if test["target_state"] == "|0⟩" else 1] ** 2,
                test["probability_answer"],
                msg=f"{sample} is incorrect",
                delta=7,
            )

    def test_verify_a_validity_of_a_quantum_state(self) -> None:
        class Exercise(TypedDict):
            state: np.ndarray[Any, Any]
            answer: Literal["Valid", "Invalid"]

        tests: dict[str, Exercise] = {
            "a": {
                "state": np.array([np.sqrt(3) / 2, 0.5]),
                "answer": "Valid",
            },
            "b": {
                "state": np.array([1, 0]),
                "answer": "Valid",
            },
            "c": {
                "state": np.array([np.sqrt(2) / 5, 3 / 5]),
                "answer": "Invalid",  # 2/25 + 9/25 = 11/25 < 1
            },
        }

        for sample, test in tests.items():
            if np.isclose(np.linalg.norm(test["state"], ord=2), 1.0, atol=1e-9):
                self.assertEqual(
                    test["answer"],
                    "Valid",
                    msg=f"{sample} is incorrect",
                )
            else:
                self.assertEqual(
                    test["answer"],
                    "Invalid",
                    msg=f"{sample} is incorrect",
                )


if __name__ == "__main__":
    unittest.main()
