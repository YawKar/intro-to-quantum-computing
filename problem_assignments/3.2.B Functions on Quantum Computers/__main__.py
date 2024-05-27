def task1() -> None:
    solution = (
        "1. Consider the given state: |ψ⟩ = 1/√3(|001⟩|0⟩ + |010⟩|0⟩ + |111⟩|0⟩),\n"
        "   and the unitary matrix gate U_f, where the function f : {0, 1}^3 -> {0, 1}.\n"
        "\n"
        "   Apply U_f to the given state |ψ⟩."
        "\n"
        "   Solution:\n"
        "       U_f|ψ⟩ = 1/√3 * U_f(|001⟩|0⟩ + |010⟩|0⟩ + |111⟩|0⟩) =\n"
        "       = 1/√3 * (U_f|001⟩|0⟩ + U_f|010⟩|0⟩ + U_f|111⟩|0⟩) =\n"
        "       = /* let's recall the standard oracle definition U_f|x⟩|y⟩ = |x⟩|y XOR f(x)⟩ */ =\n"
        "       = /* U_f|x⟩|0⟩ = |x⟩|f(x)⟩ */ =\n"
        "       = /* U_f|x⟩|1⟩ = |x⟩|!f(x)⟩ */ =\n"
        "       = 1/√3 * (|001⟩|f(001)⟩ + |010⟩|f(010)⟩ + |111⟩|f(111)⟩).\n"
    )
    print(solution)


def task2() -> None:
    solution = (
        "2. Consider the given state: |ψ⟩ = 1/√3(|001⟩|-⟩ + |010⟩|-⟩ + |111⟩|-⟩),\n"
        "   and the unitary matrix gate U_f, where the function f : {0, 1}^3 -> {0, 1}.\n"
        "\n"
        "   Apply U_f to the given state |ψ⟩."
        "\n"
        "   Solution:\n"
        "       U_f|ψ⟩ = 1/√3 * U_f(|001⟩|-⟩ + |010⟩|-⟩ + |111⟩|-⟩) =\n"
        "       = 1/√3 * (U_f|001⟩|-⟩ + U_f|010⟩|-⟩ + U_f|111⟩|-⟩) =\n"
        "       = /* let's recall the phase oracle definition:\n"
        "            U_f|x⟩|-⟩ = U_f(|x⟩ ⊗ 1/√2(|0⟩ - |1⟩)) =\n"
        "            = U_f * 1/√2(|x⟩|0⟩ - |x⟩|1⟩) =\n"
        "            = 1/√2(U_f|x⟩|0⟩ - U_f|x⟩|1⟩) =\n"
        "            = 1/√2(|x⟩|f(x)⟩ - |x⟩|!f(x)⟩).\n"
        "            Now, if f(x) = 0, then the whole state equals to |x⟩|-⟩.\n"
        "            And if f(x) = 1, then the whole state equals to -|x⟩|-⟩.\n"
        "            So, to wrap it up: U_f|x⟩|-⟩ = (-1)^f(x) * |x⟩|-⟩. */ =\n"
        "       = 1/√3 * ((-1)^f(001)|001⟩|-⟩ + (-1)^f(010)|010⟩|-⟩ + (-1)^f(111)|111⟩|-⟩).\n"
    )
    print(solution)


def main() -> None:
    task1()
    task2()


if __name__ == "__main__":
    main()
