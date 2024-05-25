def task1() -> None:
    solution = """1. Consider the state: |ψ⟩ = (1/√3)(|001⟩ + |011⟩ + |101⟩).
    a.) The probability of measuring the singular left qubit as |0⟩ is the sum of probabilities
        of all quantum states in which the left qubit is |0⟩.

        Therefore, the desired probability equals to:
        |1/√3|001⟩|^2 + |1/√3|011⟩|^2 =
        = 1/3 + 1/3 =
        = 2/3.

    b.) After measuring the left qubit as |0⟩ the third term |101⟩ will be gone and the whole state
        will collapse to |ψ⟩ = A*(1/√3)(|001⟩ + |011⟩), where A is the normalization factor.

        To calculate A we'll use the following equation:
        |A/√3|^2 + |A/√3|^2 = 1 <=>
        <=> A^2/3 + A^2/3 = 1 <=>
        <=> 2*A^2/3 = 1 <=>
        <=> A^2 = 3/2 <=>
        <=> A = √(3/2).

        This leads to the final state:
        |ψ⟩ = A*(1/√3)(|001⟩ + |011⟩) =
        = √(3/2)*(1/√3)(|001⟩ + |011⟩) =
        = 1/√2(|001⟩ + |011⟩).
"""
    print(solution)


def task2() -> None:
    solution = """2. Consider the state: |ψ⟩ = √2/2|000⟩ + √2/4|001⟩ + √5/4|110⟩ + 1/4|111⟩.
    a.) The probability of measuring the singular middle qubit as |1⟩ equals to:
        |√5/4|110⟩|^2 + |1/4|111⟩|^2 =
        = 5/16 + 1/16 =
        = 6/16 =
        = 3/8.

    b.) If we measure the middle qubit as |1⟩ then the whole state will collapse into
        |ψ⟩ = A*(√5/4|110⟩ + 1/4|111⟩), where A is the normalization factor.

        To calculate A we'll use the following equation:
        |A*√5/4|110⟩|^2 + |A*1/4|111⟩|^2 = 1 <=>
        <=> A^2*5/16 + A^2/4 = 1 <=>
        <=> A^2*6/16 = 1 <=>
        <=> A^2 = 16 / 6 <=>
        <=> A = √(8/3) <=>
        <=> A = 2√(2/3).
"""
    print(solution)


def task3() -> None:
    solution = (
        "3. Consider the state |ψ⟩ = 1/2|01⟩ + √3/2|11⟩.\n"
        "   There are no such quantum states in the given superposition state which have their right qubit as |0⟩.\n"
        "   Therefore, the probability of measuring the right qubit as |0⟩ is 0.\n"
        "\n"
        "   We can imagine the given superposition state in the following form to make it clear:\n"
        "   |ψ⟩ = 1/2|01⟩ + √3/2|11⟩ + 0*(|10⟩ + |00⟩).\n"
    )
    print(solution)


def task4() -> None:
    solution = """4. Consider the state: |ψ⟩ = 1/2|00⟩ + √3/2|11⟩.
    a.) If we measure either of qubits as |0⟩, the whole state will collapse into the measured state:
        |ψ⟩ = |00⟩.

    b.) If we measure either of qubits as |1⟩, the whole state will collapse into the measured state:
        |ψ⟩ = |11⟩.
"""
    print(solution)


def main() -> None:
    task1()
    task2()
    task3()
    task4()


if __name__ == "__main__":
    main()
