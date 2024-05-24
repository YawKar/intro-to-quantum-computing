import unittest
import qiskit.visualization as qsv  # pyright: ignore [reportMissingTypeStubs]
import qiskit.primitives as qsp  # pyright: ignore [reportMissingTypeStubs]
import qiskit.result as qsr  # pyright: ignore [reportMissingTypeStubs]
import qiskit as qs  # pyright: ignore [reportMissingTypeStubs]
import numpy as np
from dataclasses import dataclass
from typing import Any, cast, Literal


class Tests(unittest.TestCase):
    def test_task_1(self) -> None:
        @dataclass
        class Test:
            exercise: str
            v_state: tuple[complex, complex]
            psi_state_probabilities: dict[str, float]

        tests: list[Test] = [
            Test("a", (1, 0), {"00": 1.0}),
            Test("b", (0, 1), {"11": 1.0}),
            Test(
                "c",
                (1 / np.sqrt(2), 1 / np.sqrt(2)),
                {"11": 1 / 2, "00": 1 / 2},
            ),
        ]
        for test in tests:
            q0 = qs.QuantumRegister(1)
            q1 = qs.QuantumRegister(1)
            circuit = qs.QuantumCircuit(q0, q1)
            circuit.initialize(test.v_state, [q0])
            circuit.initialize(0, [q1])
            circuit.cx(q0, q1)
            circuit.measure_all()
            match out := cast(Any, qsv.circuit_drawer(circuit, output="text")):
                case qsv.text.TextDrawing():
                    print(f"{test.exercise}.)")
                    print(out)
                case _:
                    raise ValueError(f"out is not a TextDrawing but: {type(out)}")
            sampler = qsp.Sampler()
            job = sampler.run(circuit, shots=100_000)
            probs = cast(
                qsr.ProbDistribution,
                job.result().quasi_dists[0].nearest_probability_distribution(),
            )
            probs = cast(dict[str, float], probs.binary_probabilities(2))
            self.assertSetEqual(
                set(cast(list[str], probs.keys())),
                set(test.psi_state_probabilities.keys()),
            )
            for state in probs.keys():
                self.assertAlmostEqual(
                    probs[state],
                    test.psi_state_probabilities[state],
                    delta=2,
                )

    def test_task_2(self) -> None:
        @dataclass
        class Test:
            exercise: str
            the_gate_to_use: Literal["C-Hadamard", "CNOT"]
            psi_state_probabilities: dict[str, float]

        tests: list[Test] = [
            Test("a", "C-Hadamard", {"10": 1.0}),
            Test("b", "CNOT", {"11": 1.0}),
        ]
        for test in tests:
            q0 = qs.QuantumRegister(1)
            q1 = qs.QuantumRegister(1)
            circuit = qs.QuantumCircuit(q0, q1)

            circuit.initialize(0, [q0])
            circuit.initialize(0, [q1])
            circuit.x(q1)
            if test.the_gate_to_use == "C-Hadamard":
                circuit.ch(q0, q1)
            elif test.the_gate_to_use == "CNOT":
                circuit.cx(q1, q0)
            circuit.measure_all()

            match out := cast(Any, qsv.circuit_drawer(circuit, output="text")):
                case qsv.text.TextDrawing():
                    print(f"{test.exercise}.)")
                    print(out)
                case _:
                    raise ValueError(f"out is not a TextDrawing but: {type(out)}")
            sampler = qsp.Sampler()
            job = sampler.run(circuit, shots=100_000)
            probs = cast(
                qsr.ProbDistribution,
                job.result().quasi_dists[0].nearest_probability_distribution(),
            )
            probs = cast(dict[str, float], probs.binary_probabilities(2))
            self.assertSetEqual(
                set(cast(list[str], probs.keys())),
                set(test.psi_state_probabilities.keys()),
            )
            for state in probs.keys():
                self.assertAlmostEqual(
                    probs[state],
                    test.psi_state_probabilities[state],
                    delta=2,
                )


def main() -> None:
    unittest.main()


if __name__ == "__main__":
    main()
