def task1() -> None:
    print(
        "   1.  AND gate is irreversible because there are 3 input pairs that map to 1 output zero, namely: (0, 0), (1, 0), (0, 1).\n"
        "       We are unable to distinguish them by looking only on the zero as a result value.\n"
    )


def task2() -> None:
    print(
        "   2.  We can construct a reversible AND gate by appending one more bit of information like this:\n"
        "       | x | y | c | c XOR (x AND y)\n"
        "       | 0 | 0 | 0 |           0\n"
        "       | 0 | 0 | 1 |           1\n"
        "       | 0 | 1 | 0 |           0\n"
        "       | 0 | 1 | 1 |           1\n"
        "       | 1 | 0 | 0 |           0\n"
        "       | 1 | 0 | 1 |           1\n"
        "       | 1 | 1 | 0 |           1\n"
        "       | 1 | 1 | 1 |           0\n"
    )


def main() -> None:
    task1()
    task2()


if __name__ == "__main__":
    main()
