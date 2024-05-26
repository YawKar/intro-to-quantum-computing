import unittest
import qiskit as qs  # pyright: ignore [reportMissingTypeStubs]
import qiskit.quantum_info as qsqi  # pyright: ignore [reportMissingTypeStubs]
from typing import cast
import numpy as np


class Tests(unittest.TestCase):
    @staticmethod
    def Bob_decodes(
        state_vector: qsqi.Statevector,
    ) -> dict[str, float]:
        bobs_circuit = qs.QuantumCircuit(2, 2)
        bobs_circuit.cx(0, 1)
        bobs_circuit.h(0)
        state_vector = state_vector.evolve(bobs_circuit)
        return cast(dict[str, float], state_vector.probabilities_dict())

    @staticmethod
    def make_phi_plus_bell_state_circuit() -> qs.QuantumCircuit:
        # Make Phi+ Bell state
        circuit = qs.QuantumCircuit(2, 2)
        circuit.h(0)
        circuit.cx(0, 1)
        return circuit

    def test_Alice_sends_00(self) -> None:
        """
        If Alice wants to send 00 classical bits (0 in decimal) of information, she should not apply anything to her qubit.
        """
        bell_state_circuit = Tests.make_phi_plus_bell_state_circuit()

        state_vector = qsqi.Statevector.from_label("00").evolve(bell_state_circuit)
        possible_states_measurements = Tests.Bob_decodes(state_vector)
        self.assertIn("00", possible_states_measurements)
        self.assertTrue(np.allclose(1.0, possible_states_measurements["00"]))

    def test_Alice_sends_01(self) -> None:
        """
        If Alice wants to send 01 classical bits (1 in decimal) of information, she should apply X gate to her qubit.
        """
        bell_state_circuit = Tests.make_phi_plus_bell_state_circuit()
        bell_state_circuit.z(0)

        state_vector = qsqi.Statevector.from_label("00").evolve(bell_state_circuit)
        possible_states_measurements = Tests.Bob_decodes(state_vector)
        self.assertIn("01", possible_states_measurements)
        self.assertTrue(np.allclose(1.0, possible_states_measurements["01"]))

    def test_Alice_sends_10(self) -> None:
        """
        If Alice wants to send 10 classical bits (2 in decimal) of information, she should apply Z gate to her qubit.
        """
        bell_state_circuit = Tests.make_phi_plus_bell_state_circuit()
        bell_state_circuit.x(0)

        state_vector = qsqi.Statevector.from_label("00").evolve(bell_state_circuit)
        possible_states_measurements = Tests.Bob_decodes(state_vector)
        self.assertIn("10", possible_states_measurements)
        self.assertTrue(np.allclose(1.0, possible_states_measurements["10"]))

    def test_Alice_sends_11(self) -> None:
        """
        If Alice wants to send 11 classical bits (3 in decimal) of information, she should apply X and Z gates to her qubit.
        """
        bell_state_circuit = Tests.make_phi_plus_bell_state_circuit()
        bell_state_circuit.x(0)
        bell_state_circuit.z(0)

        state_vector = qsqi.Statevector.from_label("00").evolve(bell_state_circuit)
        possible_states_measurements = Tests.Bob_decodes(state_vector)
        self.assertIn("11", possible_states_measurements)
        self.assertTrue(np.allclose(1.0, possible_states_measurements["11"]))


def main() -> None:
    unittest.main()


if __name__ == "__main__":
    main()
