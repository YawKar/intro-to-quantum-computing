import qutip as qp  # pyright: ignore[reportMissingTypeStubs]
import numpy as np
import os


def task1() -> None:
    bloch_sphere = qp.Bloch()
    # add the |0⟩ state
    bloch_sphere.add_vectors([[0, 0, 1]], colors=["green"])
    # add the |1⟩ state
    bloch_sphere.add_vectors([[0, 0, -1]], colors=["orange"])
    # add the 1/sqrt(2)|0⟩ + 1/sqrt(2)|1⟩ state
    bloch_sphere.add_vectors([[1, 0, 0]], colors=["blue"])
    # (bonus) add the 1/2|0⟩ + sqrt(3)/2|1⟩ state
    bloch_sphere.add_vectors([[1 / 2, 0, -np.sqrt(3) / 2]], colors=["purple"])
    bloch_sphere.save(
        name=os.path.join(os.path.dirname(__file__), "images/bloch_sphere_0.png")
    )


def task2() -> None:
    print(
        "On the Bloch Sphere, if a qubit is higher up vertically, it means that the qubit has a higher probability to be measured as |0⟩."
    )
    print(
        "On the Bloch Sphere, if a qubit is lower down vertically, it means that the qubit has a higher probability to be measured as |1⟩."
    )


def main() -> None:
    task1()
    task2()


if __name__ == "__main__":
    main()
