import unittest


class TestAssignments(unittest.TestCase):
    def test_simple_operations(self) -> None:
        samples: dict[str, tuple[complex, complex]] = {
            "a": ((2 + 3j) + (8 - 1j), 10 + 2j),
            "b": ((2 + 1j) + (-2 - 4j), -3j),
            "c": ((4 + 4j) + (8 - 4j), 12),
            "d": ((4 + 4j) - (8 - 4j), -4 + 8j),
            "e": ((2 + 3j) * (8 + 1j), 13 + 26j),
            "f": ((4 + 4j) * (8 - 4j), 48 + 16j),
        }
        for sample, (valid, answer) in samples.items():
            self.assertEqual(valid, answer, f"sample '{sample}' is incorrect")

    def test_complex_conjugate(self) -> None:
        samples: dict[str, tuple[complex, complex]] = {
            "a": ((2 + 2j).conjugate(), 2 - 2j),
            "b": ((2 - 2j).conjugate(), 2 + 2j),
            "c": ((1 - 1j).conjugate(), 1 + 1j),
        }
        for sample, (valid, answer) in samples.items():
            self.assertEqual(valid, answer, f"sample '{sample}' is incorrect")


if __name__ == "__main__":
    unittest.main()
