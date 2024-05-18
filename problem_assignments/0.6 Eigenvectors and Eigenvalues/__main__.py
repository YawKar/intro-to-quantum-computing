import unittest
import numpy as np
from typing import cast, Any


class Test(unittest.TestCase):

    def test_magnitude_may_change_upon_applying_a_matrix_to_its_eigenvectors(
        self,
    ) -> None:
        identity = np.eye(2)
        eigenvectors = np.linalg.eig(identity).eigenvectors
        for ev in eigenvectors:
            self.assertEqual(
                np.linalg.norm(identity.dot(ev), ord=2),
                np.linalg.norm(ev, ord=2),
            )

        doubler = np.eye(2)
        doubler *= 2
        eigenvectors = np.linalg.eig(doubler).eigenvectors
        for ev in eigenvectors:
            self.assertGreater(
                np.linalg.norm(doubler.dot(ev), ord=2),
                np.linalg.norm(ev, ord=2),
            )

        halver = np.eye(2)
        halver *= 0.5
        eigenvectors = np.linalg.eig(halver).eigenvectors
        for ev in eigenvectors:
            self.assertLess(
                np.linalg.norm(halver.dot(ev), ord=2),
                np.linalg.norm(ev, ord=2),
            )

    def test_find_eigenvalue_of_an_eigenvector(self) -> None:
        matrix = np.array(
            [
                [1, 9],
                [4, 1],
            ]
        )
        eigenvector = np.array([3, 2])
        self.assertTrue(
            np.array_equal(
                7 * np.array([1, 1]),
                matrix.dot(eigenvector) / eigenvector,
            )
        )

    def test_eigenvalue_changes_the_magnitude_of_corresponding_eigenvectors(
        self,
    ) -> None:
        matrix = np.array(
            [
                [1, 2],
                [3, 4],
            ]
        )
        (eval1, eval2), evecs = np.linalg.eig(matrix)

        eval1 = cast(np.float64, eval1)
        evec1 = cast(np.ndarray[Any, np.dtypes.Float64DType], evecs[:, 0])
        self.assertLess(eval1, 1.0)
        self.assertLess(
            np.linalg.norm(matrix.dot(evec1), ord=2),
            np.linalg.norm(evec1, ord=2),
        )

        eval2 = cast(np.float64, eval2)
        evec2 = cast(np.ndarray[Any, np.dtypes.Float64DType], evecs[:, 1])
        self.assertGreater(eval2, 1.0)
        self.assertGreater(
            np.linalg.norm(matrix.dot(evec2), ord=2),
            np.linalg.norm(evec2, ord=2),
        )


if __name__ == "__main__":
    unittest.main()
