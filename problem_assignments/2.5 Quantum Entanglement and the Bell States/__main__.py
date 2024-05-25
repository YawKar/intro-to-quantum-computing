def task1() -> None:
    answer = (
        "1. When we call qubits maximally entangled, we mean that the measurement of only one of them instantly gives us the information\n"
        "   about the state of the other one without the requirement to measure it additionally.\n"
    )
    print(answer)


def task2() -> None:
    answer = "2. When we call qubits partially entangled, we mean that the measurement of only one of them affects the state of the other.\n"
    print(answer)


def task3() -> None:
    answer = (
        "3. If we cannot factor the given state into a tensor of independent single-qubit states,\n"
        "   then the state is entangled (i.e. the qubits inside of it).\n"
    )
    print(answer)


def task4() -> None:
    answer = (
        "4. Are the following states entangled?\n"
        "   (a) |ψ⟩ = 1/√2(|01⟩ + |10⟩)\n"
        "       Yes, because if we measure either of qubits we'll instantly deduce the state of the other one.\n"
        "       And no, we can't factor the given superposition state into a tensor of single-qubit states.\n"
        "\n"
        "   (b) |ψ⟩ = 1/√2(|00⟩ + |01⟩)\n"
        "       No, because we can factor the given superposition state into the following tensor:\n"
        "       |ψ⟩ = |0⟩ ⊗ 1/√2(|0⟩ + |1⟩).\n"
        "       Which is, by the way: |0⟩ ⊗ |+⟩.\n"
        "\n"
        "   (c) |ψ⟩ = √3/(2√2)|00⟩ + 1/(2√2)|01⟩ + √3/(2√2)|10⟩ + 1/(2√2)|11⟩\n"
        "       No, because we can factor the given superposition state into the following tensor:\n"
        "       |ψ⟩ = 1/√2(|0⟩ + |1⟩) ⊗ (√3/2|0⟩ + 1/2|1⟩).\n"
        "       Which is, by the way: |+⟩ ⊗ (√3/2|0⟩ + 1/2|1⟩).\n"
        "\n"
        "       How to find these factors:\n"
        "       1.  Consider the general form of a tensor: (a|0⟩ + b|1⟩) ⊗ (c|0⟩ + d|1⟩).\n"
        "           We know that result should equal: ac|00⟩ + ad|01⟩ + bc|10⟩ + bd|11⟩.\n"
        "       2.  We also know the given superposition state: √3/(2√2)|00⟩ + 1/(2√2)|01⟩ + √3/(2√2)|10⟩ + 1/(2√2)|11⟩.\n"
        "       3.  Let's match the letters:\n"
        "           ac = √3/(2√2),\n"
        "           ad = 1/(2√2),\n"
        "           bc = √3/(2√2),\n"
        "           bd = 1/(2√2).\n"
        "       4.  Notice, that ac = bc <=> a = b. Or the other way: ad = bd <=> a = b.\n"
        "       5.  We know that for the (a|0⟩ + b|1⟩) state should hold the following equation:\n"
        "           a^2 + b^2 = 1.\n"
        "       6.  Let's substitute b with a and find out its value:\n"
        "           a^2 + a^2 = 1 <=>\n"
        "           <=> 2a^2 = 1 <=>\n"
        "           <=> a^2 = 1/2 <=>\n"
        "           <=> a = 1/√2. (omit the '-1/√2' solution because global phase doesn't matter.)\n"
        "       7.  ac = √3/(2√2) <=> (substitue a with its newfound value)\n"
        "           c/√2 = √3/(2√2) <=>\n"
        "           c = √3/2.\n"
        "       8.  We know that for the (c|0⟩ + d|1⟩) state should hold the following equation:\n"
        "           c^2 + d^2 = 1.\n"
        "       9.  d = √(1 - c^2) = √(1 - (√3/2)^2) = √(1 - 3/4) = √(1/4) = 1/2.\n"
        "       10. This is the end.\n"
    )
    print(answer)


def main() -> None:
    task1()
    task2()
    task3()
    task4()


if __name__ == "__main__":
    main()
