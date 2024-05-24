import qiskit.visualization as qsv  # pyright: ignore [reportMissingTypeStubs]
import qiskit.primitives as qsp  # pyright: ignore [reportMissingTypeStubs]
import qiskit as qs  # pyright: ignore [reportMissingTypeStubs]
import numpy as np
from typing import Any, cast, Generator
from contextlib import contextmanager


@contextmanager
def indentation(level: int) -> Generator[str, None, None]:
    yield level * 4 * " "


def print_task1() -> None:

    def a(indentation_level: int) -> None:
        q0 = qs.QuantumRegister(1)
        q1 = qs.QuantumRegister(1)
        circuit = qs.QuantumCircuit(q0, q1)

        circuit.initialize("00", [q0, q1])
        circuit.x(q1)
        circuit.h(q0)
        circuit.h(q1)
        circuit.measure_all()

        match out := cast(Any, qsv.circuit_drawer(circuit, output="text")):
            case qsv.text.TextDrawing():
                with indentation(indentation_level) as indent:
                    print(
                        "\n".join(
                            map(
                                lambda x: indent + x,
                                out.single_string().split("\n"),
                            )
                        )
                    )
                    estimator = qsp.Sampler()
                    shots = 10_000
                    job = estimator.run(circuit, shots=shots)
                    print(f"{indent}With given shots: {shots}")
                    for (
                        state,
                        probability,  # pyright: ignore[reportUnknownVariableType]
                    ) in (
                        job.result().quasi_dists[0].binary_probabilities().items()
                    ):
                        print(f"{indent}|{state}⟩: {probability}")
            case _:
                raise ValueError(f"out's type is not TextDrawing: {type(out)=}")

    def b(indentation_level: int) -> None:
        q0 = qs.QuantumRegister(1)
        circuit = qs.QuantumCircuit(q0)

        circuit.initialize([1 / np.sqrt(2), -1 / np.sqrt(2)], [q0])
        circuit.h(q0)
        circuit.x(q0)
        circuit.measure_all()

        match out := cast(Any, qsv.circuit_drawer(circuit, output="text")):
            case qsv.text.TextDrawing():
                with indentation(indentation_level) as indent:
                    print(
                        "\n".join(
                            map(
                                lambda x: indent + x,
                                out.single_string().split("\n"),
                            )
                        )
                    )
                    estimator = qsp.Sampler()
                    shots = 10_000
                    job = estimator.run(circuit, shots=shots)
                    print(f"{indent}With given shots: {shots}")
                    for (
                        state,
                        probability,  # pyright: ignore[reportUnknownVariableType]
                    ) in (
                        job.result().quasi_dists[0].binary_probabilities().items()
                    ):
                        print(f"{indent}|{state}⟩: {probability}")
            case _:
                raise ValueError(f"out's type is not TextDrawing: {type(out)=}")

    def c(indentation_level: int) -> None:
        q0 = qs.QuantumRegister(1)
        q1 = qs.QuantumRegister(1)
        q2 = qs.QuantumRegister(1)
        circuit = qs.QuantumCircuit(q0, q1, q2)

        circuit.initialize(
            [0, 1],
            [q0],
        )
        circuit.initialize(
            [1, 0],
            [q1],
        )
        circuit.initialize(
            [1 / np.sqrt(2), 1 / np.sqrt(2)],
            [q2],
        )
        circuit.s(q1)
        circuit.x(q2)
        circuit.h(q2)
        circuit.measure_all()

        match out := cast(Any, qsv.circuit_drawer(circuit, output="text")):
            case qsv.text.TextDrawing():
                with indentation(indentation_level) as indent:
                    print(
                        "\n".join(
                            map(
                                lambda x: indent + x,
                                out.single_string().split("\n"),
                            )
                        )
                    )
                    estimator = qsp.Sampler()
                    shots = 10_000
                    job = estimator.run(circuit, shots=shots)
                    print(f"{indent}With given shots: {shots}")
                    for (
                        state,
                        probability,  # pyright: ignore[reportUnknownVariableType]
                    ) in (
                        job.result().quasi_dists[0].binary_probabilities().items()
                    ):
                        print(f"{indent}|{state}⟩: {probability}")
            case _:
                raise ValueError(f"out's type is not TextDrawing: {type(out)=}")

    print("a.)")
    a(1)
    print("b.)")
    b(1)
    print("c.)")
    c(1)


def main() -> None:
    print_task1()


if __name__ == "__main__":
    main()
