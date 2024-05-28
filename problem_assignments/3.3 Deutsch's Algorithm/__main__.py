import unittest
import qiskit.circuit as qsc  # pyright: ignore [reportMissingTypeStubs]
import qiskit.visualization as qsv  # pyright: ignore [reportMissingTypeStubs]
import qiskit.quantum_info as qsqi  # pyright: ignore [reportMissingTypeStubs]
import numpy as np
from typing import Any, cast


class Tests(unittest.TestCase):

    @staticmethod
    def print_deutsch_and_unitary_circuits(
        deutsch_circuit: qsc.QuantumCircuit, unitary_circuit: qsc.QuantumCircuit
    ) -> None | ValueError | Exception:

        def indent_with_tabs(text: str, indent: int) -> str:
            return "\n".join(
                map(
                    lambda x: (indent * "\t") + x,
                    text.splitlines(),
                )
            )

        try:
            match (
                cast(Any, qsv.circuit_drawer(unitary_circuit, output="text")),
                cast(Any, qsv.circuit_drawer(deutsch_circuit, output="text")),
            ):
                case (
                    qsv.text.TextDrawing() as custom_gate,
                    qsv.text.TextDrawing() as deutsch,
                ):
                    print()
                    print(f"Custom gate: {unitary_circuit.name}")
                    print(indent_with_tabs(custom_gate.single_string(), 1))
                    print(f"Deutsch circuit:")
                    print(indent_with_tabs(deutsch.single_string(), 1))
                case (custom_gate, deutsch):
                    raise ValueError(
                        f"Types aren't supported: ({type(custom_gate)=}, {type(deutsch)=})"
                    )
        except Exception as exc:
            return exc

    @staticmethod
    def make_Deutsch_s_algorithm_circuit(
        function_unitary_circuit: qsc.QuantumCircuit,
    ) -> qsc.QuantumCircuit:
        deutsch_circuit = qsc.QuantumCircuit(2, 1)  # 2 qubits, 1 classical bit
        # |ψ_0⟩ = |00⟩
        deutsch_circuit.x(1)
        # |ψ_1⟩ = |01⟩
        deutsch_circuit.h([0, 1])
        # |ψ_2⟩ = |+-⟩
        deutsch_circuit.compose(
            inplace=True,
            wrap=True,
            other=function_unitary_circuit,
            inline_captures=True,
        )
        # |ψ_3⟩ = U_f|+-⟩ = /* distribute |-⟩ over |+⟩ */ =
        #   = U_f(1/sqrt(2) * (|0-⟩ + |1-⟩)) = /* distribute U_f over states */ =
        #   = 1/sqrt(2) * (U_f|0-⟩ + U_f|1-⟩) = /* apply U_f|x-⟩ = (-1)^f(x) |x-⟩ */ =
        #   = 1/sqrt(2) * ((-1)^f(0) * |0-⟩ + (-1)^f(1) * |1-⟩) = /* factor out |-⟩ and make a tensor */ =
        #   = 1/sqrt(2) * ((-1)^f(0)|0⟩ + (-1)^f(1)|1⟩) ⊗ |-⟩.
        deutsch_circuit.h(0)
        # |ψ_4⟩ = H(1/sqrt(2) * ((-1)^f(0)|0⟩ + (-1)^f(1)|1⟩)) ⊗ |-⟩.
        # after measurement:
        # if `function_unitary_matrix` is constant (e.g. f(0) = f(1) = 0 or 1):
        #   if f(0) = f(1) = 0:
        #       |ψ_5⟩ = H(1/sqrt(2) * (|0⟩ + |1⟩)) ⊗ |-⟩ = H|+⟩ ⊗ |-⟩ = |0-⟩.
        #   elif f(0) = f(1) = 1:
        #       |ψ_5⟩ = H(1/sqrt(2) * (-|0⟩ - |1⟩)) ⊗ |-⟩ = -H(1/sqrt(2) * (|0⟩ + |1⟩)) ⊗ |-⟩ = -H|+⟩ ⊗ |-⟩ = -|0-⟩.
        # elif `function_unitary_matrix` is balanced (e.g. (f(0), f(1)) = (0, 1) or (1, 0))
        #   if f(0) = 0 and f(1) = 1:
        #       |ψ_5⟩ = H(1/sqrt(2) * (|0⟩ - |1⟩)) ⊗ |-⟩ = H|-⟩ ⊗ |-⟩ = |1-⟩.
        #   elif f(0) = 1 and f(1) = 0:
        #       |ψ_5⟩ = H(1/sqrt(2) * (-|0⟩ + |1⟩)) ⊗ |-⟩ = -H(1/sqrt(2) * (|0⟩ - |1⟩)) ⊗ |-⟩ = -H|-⟩ ⊗ |-⟩ = -|1-⟩.
        return deutsch_circuit

    def test_Deutsch_s_algorithm_on_constant_0_function(self) -> None:
        # U_f|x⟩|y⟩ = |x⟩|y ⊗ f(x)⟩ = |x⟩|y ⊗ 0⟩.
        constant_0 = qsc.QuantumCircuit(2, name="Unitary constant 0")
        deutsch_circuit = Tests.make_Deutsch_s_algorithm_circuit(constant_0)

        state_vector = qsqi.Statevector.from_label("00")
        state_vector = state_vector.evolve(deutsch_circuit)

        Tests.print_deutsch_and_unitary_circuits(deutsch_circuit, constant_0)
        self.assertEqual(
            state_vector.measure()[0][1],
            "0",
            "the output qubit shows that the given constant function is not a constant function",
        )
        self.assertTrue(
            state_vector.equiv(
                qsqi.Statevector(
                    [
                        1 / np.sqrt(2),  # 00
                        0,  # 01
                        -1 / np.sqrt(2),  # 10
                        0,  # 11
                    ],
                ),
            ),
            "states in case of constant f(0) = f(1) = 1 differ",
        )

    def test_Deutsch_s_algorithm_on_constant_1_function(self) -> None:
        # U_f|x⟩|y⟩ = |x⟩|y ⊗ f(x)⟩ = |x⟩|y ⊗ 1⟩.
        constant_1 = qsc.QuantumCircuit(2, name="Unitary constant 1")
        constant_1.x(1)
        deutsch_circuit = Tests.make_Deutsch_s_algorithm_circuit(constant_1)

        state_vector = qsqi.Statevector.from_label("00")
        state_vector = state_vector.evolve(deutsch_circuit)

        Tests.print_deutsch_and_unitary_circuits(deutsch_circuit, constant_1)
        self.assertEqual(
            state_vector.measure()[0][1],
            "0",
            "the output qubit shows that the given constant function is not a constant function",
        )
        self.assertTrue(
            state_vector.equiv(
                qsqi.Statevector(
                    [
                        -1 / np.sqrt(2),  # 00
                        0,  # 01
                        1 / np.sqrt(2),  # 10
                        0,  # 11
                    ],
                ),
            ),
            "states in case of constant f(0) = f(1) = 1 differ",
        )

    def test_Deutsch_s_algorithm_on_balanced_identity_function(self) -> None:
        # U_f|x⟩|y⟩ = |x⟩|y ⊗ f(x)⟩ = |x⟩|y ⊗ x⟩.
        # It is balanced because there are 2 cases for f(x) = 1 and 2 cases for f(x) = 0, namely:
        # f(x) = 0 cases:
        #   - U_f|0⟩|0⟩ = |0⟩|0 ⊗ f(x)⟩ = |0⟩|0 ⊗ 0⟩
        #   - U_f|0⟩|1⟩ = |0⟩|1 ⊗ f(x)⟩ = |0⟩|1 ⊗ 0⟩
        # f(x) = 1 cases:
        #   - U_f|1⟩|0⟩ = |1⟩|0 ⊗ f(x)⟩ = |1⟩|0 ⊗ 1⟩
        #   - U_f|1⟩|1⟩ = |1⟩|1 ⊗ f(x)⟩ = |1⟩|1 ⊗ 1⟩
        balanced = qsc.QuantumCircuit(2, name="Unitary balanced identity f(x) = x")
        balanced.cx(0, 1)
        deutsch_circuit = Tests.make_Deutsch_s_algorithm_circuit(balanced)

        state_vector = qsqi.Statevector.from_label("00")
        state_vector = state_vector.evolve(deutsch_circuit)

        Tests.print_deutsch_and_unitary_circuits(deutsch_circuit, balanced)
        self.assertEqual(
            state_vector.measure()[0][1],
            "1",
            "the output qubit shows that the given balanced function is not a balanced function",
        )
        self.assertTrue(
            state_vector.equiv(
                qsqi.Statevector(
                    [
                        0,  # 00
                        1 / np.sqrt(2),  # 01
                        0,  # 10
                        -1 / np.sqrt(2),  # 11
                    ],
                ),
            ),
            "states in case of balanced f(0) != f(1) = 1 differ",
        )

    def test_Deutsch_s_algorithm_on_balanced_not_function(self) -> None:
        # U_f|x⟩|y⟩ = |x⟩|y ⊗ f(x)⟩ = |x⟩|y ⊗ ~x⟩.
        # It is balanced because there are 2 cases for f(x) = 1 and 2 cases for f(x) = 0, namely:
        # f(x) = 1 cases:
        #   - U_f|0⟩|0⟩ = |0⟩|0 ⊗ f(x)⟩ = |0⟩|0 ⊗ 1⟩
        #   - U_f|0⟩|1⟩ = |0⟩|1 ⊗ f(x)⟩ = |0⟩|1 ⊗ 1⟩
        # f(x) = 0 cases:
        #   - U_f|1⟩|1⟩ = |1⟩|1 ⊗ f(x)⟩ = |1⟩|1 ⊗ 0⟩
        #   - U_f|1⟩|0⟩ = |1⟩|0 ⊗ f(x)⟩ = |1⟩|0 ⊗ 0⟩
        balanced = qsc.QuantumCircuit(2, name="Unitary balanced not f(x) = ~x")
        balanced.x(0)
        balanced.cx(0, 1)
        balanced.x(0)
        deutsch_circuit = Tests.make_Deutsch_s_algorithm_circuit(balanced)

        state_vector = qsqi.Statevector.from_label("00")
        state_vector = state_vector.evolve(deutsch_circuit)

        Tests.print_deutsch_and_unitary_circuits(deutsch_circuit, balanced)
        self.assertEqual(
            state_vector.measure()[0][1],
            "1",
            "the output qubit shows that the given balanced function is not a balanced function",
        )
        self.assertTrue(
            state_vector.equiv(
                qsqi.Statevector(
                    [
                        0,  # 00
                        -1 / np.sqrt(2),  # 01
                        0,  # 10
                        1 / np.sqrt(2),  # 11
                    ],
                ),
            ),
            "states in case of balanced f(0) != f(1) = 1 differ",
        )


def main() -> None:
    unittest.main()


if __name__ == "__main__":
    main()
