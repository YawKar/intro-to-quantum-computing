import unittest
import numpy as np


def exponential_to_standard_form(magnitude: float, theta: float) -> complex:
    return magnitude * (np.cos(theta) + 1j * np.sin(theta))


class Tests(unittest.TestCase):
    def test_transpose(self) -> None:
        self.assertTrue(
            np.array_equal(
                np.array([1, 0, 4, 17, 10, 18]).reshape((2, 3)).T,
                np.array([1, 17, 0, 10, 4, 18]).reshape((3, 2)),
            )
        )

    def test_find_conjugate_matrix(self) -> None:
        e2s = exponential_to_standard_form
        a = np.array(
            [
                [3 + 2j, e2s(2, np.pi / 3), 4],
                [1 - 7j, 10, -3j],
            ],
        )
        conjugation_a = np.array(
            [
                [3 - 2j, e2s(2, -np.pi / 3), 4],
                [1 + 7j, 10, 3j],
            ],
        )
        self.assertTrue(
            np.array_equal(a.conjugate(), conjugation_a),
        )

    def test_find_hermitian_adjoint(self) -> None:
        e2s = exponential_to_standard_form
        a = np.array(
            [
                [3 + 2j, e2s(2, np.pi / 3), 4],
                [1 - 7j, 10, -3j],
            ],
        )
        hermitian_adj_a = np.array(
            [
                [3 - 2j, 1 + 7j],
                [e2s(2, -np.pi / 3), 10],
                [4, 3j],
            ],
        )
        self.assertTrue(
            np.array_equal(a.conjugate().T, hermitian_adj_a),
        )

    def test_is_the_matrix_unitary(self) -> None:
        a = np.array([[1, 0], [0, 1j]])
        self.assertTrue(np.array_equal(a.conj().T.dot(a), np.eye(2)))

    def test_is_the_matrix_hermitian(self) -> None:
        a = np.array([[1, 0], [0, 1j]])
        self.assertFalse(
            np.array_equal(
                a.conj().T,
                a,
            )
        )


if __name__ == "__main__":
    unittest.main()
