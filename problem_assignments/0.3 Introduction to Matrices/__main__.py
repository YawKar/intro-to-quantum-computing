import numpy as n
import unittest

class TestMatrices(unittest.TestCase):
    def test_dimensions(self) -> None:
        tests: dict[
            str,
            tuple[n.ndarray[tuple[int, ...], n.dtypes.Float64DType], tuple[int, ...]],
        ] = {
            "a": (
                n.array(
                    [
                        [
                            2.0,
                            -1.0,
                        ],
                        [0.0, 5.0],
                        [1.0, 0.0],
                    ]
                ),
                (3, 2),
            ),
            "b": (
                n.array([[2.0, -1.0, 0.0, 2.0]]),
                (1, 4),
            ),
            "c": (
                n.array(
                    [
                        [
                            -8.0,
                            0.0,
                        ],
                        [3.0, 2.0],
                    ]
                ),
                (2, 2),
            ),
        }

        for test, data in tests.items():
            self.assertTupleEqual(data[0].shape, data[1], msg=f"{test} is incorrect")

    def test_operations(self) -> None:
        tests: dict[
            str,
            tuple[
                n.ndarray[tuple[int, ...], n.dtypes.BoolDType],
                n.ndarray[tuple[int, ...], n.dtypes.BoolDType],
            ],
        ] = {
            "a": (
                n.array([2, 5]).reshape((2, 1)) + n.array([9, 0]).reshape(2, 1),
                n.array([11, 5]).reshape((2, 1)),
            ),
            "b": (
                n.array([4, -3, 0]) - n.array([2, 2, 1]),
                n.array([2, -5, -1]),
            ),
            "c": (
                n.array([[-8, 0], [3, 2]]) + n.array([[2, 0], [0, 1]]),
                n.array([[-6, 0], [3, 3]]),
            ),
            "d": (
                n.array(-2) * n.array([[4, -3, 0], [8, 7, 2]]),
                n.array([[-8, 6, 0], [-16, -14, -4]]),
            ),
            "e": (
                n.array(3) * n.array([[-8, 0], [3, 2]])
                - n.array(0.5) * n.array([[2, 0], [0, 1]]),
                n.array([[-25, 0], [9, 5.5]]),
            ),
        }

        for test, (valid, answer) in tests.items():
            self.assertTrue(n.array_equal(valid, answer), msg=f"{test} is incorrect")


if __name__ == "__main__":
    unittest.main()
