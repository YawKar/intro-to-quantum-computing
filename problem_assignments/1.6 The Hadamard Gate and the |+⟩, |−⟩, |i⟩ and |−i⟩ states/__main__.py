import unittest
import numpy as np
import qutip as qp  # pyright: ignore [reportMissingTypeStubs]
import os


def from_exponential_form(*, r: float = 1, theta: float) -> complex:
    return r * (np.cos(theta) + 1j * np.sin(theta))


class Tests(unittest.TestCase):
    images_dir = os.path.join(os.path.dirname(__file__), "images")

    def test_1_ab(self) -> None:
        theta = np.pi / 2
        self.assertAlmostEqual(
            from_exponential_form(theta=theta),
            1j,
        )
        i_state = 1 / np.sqrt(2) * qp.Qobj([1, from_exponential_form(theta=theta)])
        b = qp.Bloch()
        b.add_states(i_state)
        b.add_arc(
            1 / np.sqrt(2) * qp.Qobj([1, 1]),
            i_state,
            fmt="b--",
            linewidth=3,
        )
        b.save(os.path.join(Tests.images_dir, "task1_ab"))

    def test_1_cd(self) -> None:
        theta = np.pi
        self.assertAlmostEqual(
            from_exponential_form(theta=theta),
            -1,
        )
        m1_state = 1 / np.sqrt(2) * qp.Qobj([1, from_exponential_form(theta=theta)])
        b = qp.Bloch()
        b.add_states(m1_state)
        b.add_arc(
            1 / np.sqrt(2) * qp.Qobj([1, 1]),
            1 / np.sqrt(2) * qp.Qobj([1, 1j]),
            fmt="b--",
            linewidth=3,
        )
        b.add_arc(
            1 / np.sqrt(2) * qp.Qobj([1, 1j]),
            m1_state,
            fmt="b--",
            linewidth=3,
        )
        b.save(os.path.join(Tests.images_dir, "task1_cd"))

    def test_1_ef(self) -> None:
        theta = 3 * np.pi / 2
        self.assertAlmostEqual(
            from_exponential_form(theta=theta),
            -1j,
        )
        m1j_state = 1 / np.sqrt(2) * qp.Qobj([1, from_exponential_form(theta=theta)])
        b = qp.Bloch()
        b.add_states(m1j_state)
        b.add_arc(
            1 / np.sqrt(2) * qp.Qobj([1, 1]),
            1 / np.sqrt(2) * qp.Qobj([1, 1j]),
            fmt="b--",
            linewidth=3,
        )
        b.add_arc(
            1 / np.sqrt(2) * qp.Qobj([1, 1j]),
            1 / np.sqrt(2) * qp.Qobj([1, -1]),
            fmt="b--",
            linewidth=3,
        )
        b.add_arc(
            1 / np.sqrt(2) * qp.Qobj([1, -1]),
            1 / np.sqrt(2) * qp.Qobj([1, -1j]),
            fmt="b--",
            linewidth=3,
        )
        b.save(os.path.join(Tests.images_dir, "task1_ef"))

    def test_2(self) -> None:
        hadamard = qp.gates.hadamard_transform(1)
        zero_state = qp.Qobj([1, 0])
        one_state = qp.Qobj([0, 1])
        plus_state = 1 / np.sqrt(2) * qp.Qobj([1, 1])
        minus_state = (  # pyright: ignore [reportUnknownVariableType]
            qp.sigmaz() * plus_state
        )
        self.assertTrue(
            np.array_equal(
                hadamard * zero_state,  # type: ignore
                plus_state,
            ),
        )
        self.assertTrue(
            np.array_equal(
                hadamard * one_state,  # type: ignore
                minus_state,  # type: ignore
            ),
        )
        self.assertTrue(
            np.array_equal(
                hadamard * plus_state,  # type: ignore
                zero_state,  # type: ignore
            ),
        )
        self.assertTrue(
            np.array_equal(
                hadamard * minus_state,  # type: ignore
                one_state,  # type: ignore
            ),
        )


def main() -> None:
    unittest.main(exit=False)


if __name__ == "__main__":
    main()
