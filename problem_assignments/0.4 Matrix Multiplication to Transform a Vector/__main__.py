import unittest
import numpy as n
from typing import Any


class Test(unittest.TestCase):

    def test_task1(self) -> None:
        tests: dict[str, tuple[Any, n.ndarray[Any, n.dtype[Any]]]] = {
            "a": (
                n.dot(
                    n.array([[0, 1], [5, 2]]),
                    n.array([[3, 2, 2], [1, 0, 4]]),
                ),
                n.array([[1, 0, 4], [17, 10, 18]]),
            ),
            "b": (
                n.dot(
                    n.array([[1, 0], [0, 1]]),
                    n.array([2, 4]).reshape((-1, 1)),
                ),
                n.array([2, 4]).reshape((-1, 1)),
            ),
            "c": (
                n.dot(
                    n.array([1, 1, 2]),
                    n.array([0, 3, 8]).reshape((-1, 1)),
                ),
                n.array([19]),
            ),
        }

        for sample, data in tests.items():
            self.assertTrue(
                n.array_equal(data[0], data[1]), msg=f"{sample} is incorrect"
            )

    def test_task2(self) -> None:
        sample = n.array([1, 2, 3, 4]).reshape((2, 2))
        self.assertTrue(n.allclose(n.eye(2), n.linalg.inv(sample).dot(sample)))

    def test_task3(self) -> None:
        sample = n.array([1, 2, 3, 4]).reshape((2, 2))
        self.assertTrue(n.allclose(sample, n.eye(2).dot(sample)))


if __name__ == "__main__":
    unittest.main()
