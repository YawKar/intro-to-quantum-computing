import qiskit.visualization as qsv  # pyright: ignore [reportMissingTypeStubs]
import qiskit as qs  # pyright: ignore [reportMissingTypeStubs]
from typing import cast, Any


def getTextDrawing(circuit: qs.QuantumCircuit) -> qsv.text.TextDrawing:
    match out := cast(Any, qsv.circuit_drawer(circuit, output="text")):
        case qsv.text.TextDrawing():
            return out
        case _:
            raise ValueError(f"out has unsupported type: {type(out)}")


def task1() -> None:
    q0 = qs.QuantumRegister(1, "α|0⟩ + β|1⟩")
    q1 = qs.QuantumRegister(1, "|1⟩")
    circuit = qs.QuantumCircuit(q0, q1)

    circuit.cz(q0, q1, label="CZ-gate")
    circuit.measure_all()

    drawing = getTextDrawing(circuit)

    solution = (
        "1. It is known that |1⟩ is an eigenvector of the Z-gate since Z|1⟩ = -|1⟩.\n"
        "   Consider the circuit below:\n"
        f"{"".join(map(lambda x: f"   {x}", drawing.single_string().splitlines(True)))}\n"
        "   Prove that phase kickback occurs by showing a relative phase of -1 is applied to the control qubit.\n"
        "\n"
        "   1.  Let's write down the starting superposition state:\n"
        "       |ψ⟩ = α|01⟩ + β|11⟩.\n"
        "   2.  Apply CZ-gate to it:\n"
        "       CZ|ψ⟩ = CZ(α|01⟩ + β|11⟩) =\n"
        "       = αCZ|01⟩ + βCZ|11⟩ =\n"
        "       = α|01⟩ + (-β|11⟩) =\n"
        "       = α|0⟩|1⟩ - β|1⟩|1⟩ =\n"
        "       = (α|0⟩ - β|1⟩) ⊗ |1⟩.\n"
        "   3.  That's how the relative phase of -1 was applied to the control qubit rather than to the target.\n"
    )
    print(solution)


def task2() -> None:
    q0 = qs.QuantumRegister(1, "α|0⟩ + β|1⟩")
    q1 = qs.QuantumRegister(1, "|0⟩")
    circuit = qs.QuantumCircuit(q0, q1)

    circuit.ch(q0, q1)
    circuit.measure_all()

    drawing = getTextDrawing(circuit)

    solution = (
        "2. Does phase kickback occur in the following circuit? Why or why not?\n"
        f"{"".join(map(lambda x: f"   {x}", drawing.single_string().splitlines(True)))}\n"
        "\n"
        "   It doesn't because |0⟩ is not an eigenvector of the Hadamard gate.\n"
        "   1.  Let's write down the starting superposition state:\n"
        "       |ψ⟩ = α|00⟩ + β|10⟩.\n"
        "   2.  Apply CH-gate to it:\n"
        "       CH|ψ⟩ = CH(α|00⟩ + β|10⟩) =\n"
        "       = αCH|00⟩ + βCH|10⟩ =\n"
        "       = α|00⟩ + β|1+⟩.\n"
        "   3.  Now it is impossible to factor this superposition state into a tensor of singular-qubit states.\n"
        "   4.  These qubits are now entangled.\n"
    )
    print(solution)

def main() -> None:
    task1()
    task2()


if __name__ == "__main__":
    main()
