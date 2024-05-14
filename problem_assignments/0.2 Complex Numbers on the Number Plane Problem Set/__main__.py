import unittest
import math
import matplotlib.pyplot as plt
import os


def draw_task_1(figsize: tuple[float, float]) -> None:
    f = plt.figure(figsize=figsize)
    numbers: list[tuple[complex, str]] = [
        (2 + 3j, r"$2+3i$"),
        (
            2 * (math.cos(math.pi / 4) + math.sin(math.pi / 4) * 1j),
            r"$2\cos(\frac{\pi}{4})+i\sin (\frac{\pi}{4}))$",
        ),
        (
            3 * (math.cos(math.pi * 5 / 4) + math.sin(math.pi * 5 / 4) * 1j),
            r"$3e^{5\pi i \ / \ 4}$",
        ),
    ]

    for number, expression in numbers:
        plt.scatter(number.real, number.imag, label=expression)

    plt.legend()

    plt.axhline(y=0, color="black", linestyle="--")
    plt.axvline(x=0, color="black", linestyle="--")
    plt.grid(visible=True, which="both")

    f.savefig(
        os.path.join(os.path.dirname(__file__), "images/task1.png"), bbox_inches="tight"
    )
    plt.close(f)


def draw_task_2(figsize: tuple[float, float]) -> None:
    f = plt.figure(figsize=figsize)
    numbers: list[tuple[complex, str]] = [
        (
            math.cos(7 * math.pi / 8) + 1j * math.sin(7 * math.pi / 8),
            r"$e^{7\pi i \ / \ 8}$",
        ),
        (math.cos(math.pi / 4) + 1j * math.sin(math.pi / 4), r"$e^{\pi i \ / \ 4}$"),
        (
            (math.cos(7 * math.pi / 8) + 1j * math.sin(7 * math.pi / 8))
            * (math.cos(math.pi / 4) + 1j * math.sin(math.pi / 4)),
            r"$e^{7\pi i \ / \ 8}e^{\pi i \ / \ 4}$",
        ),
    ]

    for number, expression in numbers:
        plt.polar(
            [0, math.atan2(number.imag, number.real)],
            [0, math.sqrt(number.imag**2 + number.real**2)],
            marker="o",
            label=expression,
        )

    plt.legend()

    plt.axhline(y=0, color="black", linestyle="--")
    plt.axvline(x=0, color="black", linestyle="--")
    plt.grid(visible=True, which="both")

    f.savefig(
        os.path.join(os.path.dirname(__file__), "images/task2.png"), bbox_inches="tight"
    )
    plt.close(f)


def draw_task_4(figsize: tuple[float, float]) -> None:
    """
    When we multiply a complex number by *i*, we rotate it counter-clockwise by pi/2 radians
    """
    f = plt.figure(figsize=figsize)
    numbers: list[complex] = [1 + 1j, 1j - 1]

    for number in numbers:
        plt.polar(
            [0, math.atan2(number.imag, number.real)],
            [0, math.sqrt(number.imag**2 + number.real**2)],
            marker="o",
            label=str(number),
        )

    plt.legend()

    plt.axhline(y=0, color="black", linestyle="--")
    plt.axvline(x=0, color="black", linestyle="--")
    plt.grid(visible=True, which="both")

    f.savefig(
        os.path.join(os.path.dirname(__file__), "images/task4.png"), bbox_inches="tight"
    )
    plt.close(f)


class Task3(unittest.TestCase):
    def test_representations(self) -> None:
        from typing import TypedDict

        class Test(TypedDict):
            valid: complex
            exponential: str
            polar: complex

        tests: list[Test] = [
            {
                "valid": 1 + 1j,
                "exponential": "sqrt(2) * e ^ (i * pi/4)",
                "polar": math.sqrt(2) * (math.cos(math.pi / 4) + 1j * math.sin(math.pi / 4)),
            },
            {
                "valid": 1j,
                "exponential": "e ^ (i * pi/2)",
                "polar": math.cos(math.pi / 2) + 1j * math.sin(math.pi / 2),
            },
            {
                "valid": -1,
                "exponential": "e ^ (i * pi)",
                "polar": math.cos(math.pi) + 1j * math.sin(math.pi),
            },
        ]

        for i, test in enumerate(tests):
            self.assertAlmostEqual(
                test["valid"],
                test["polar"],
                msg=f"{i} test case is incorrect: {test['exponential']}",
            )


if __name__ == "__main__":
    figsize: tuple[float, float] = (5, 5)
    draw_task_1(figsize)
    draw_task_2(figsize)
    unittest.main(exit=False)  # task3
    draw_task_4(figsize)
