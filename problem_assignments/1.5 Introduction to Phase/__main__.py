import os
import qutip as qp  # pyright: ignore [reportMissingTypeStubs]
import numpy as np


def from_exponential_form(theta: float) -> complex:
    return np.cos(theta) + 1j * np.sin(theta)


def task1(images_dir_path: str) -> None:
    bloch = qp.Bloch()
    equal_alpha_beta = 1 / np.sqrt(2)
    relative_phase = from_exponential_form(1.25 * np.pi)
    phased_q = qp.Qobj([equal_alpha_beta, relative_phase * equal_alpha_beta])
    bloch.add_states(phased_q)
    # add arcs for clarity
    _middle_state = qp.Qobj(
        [equal_alpha_beta, from_exponential_form(0.75 * np.pi) * equal_alpha_beta]
    )
    bloch.add_arc(
        qp.Qobj([equal_alpha_beta, equal_alpha_beta]),
        _middle_state,
        fmt="b--",
        linewidth=3,
    )
    bloch.add_arc(
        _middle_state,
        phased_q,
        fmt="b--",
        linewidth=3,
    )

    bloch.save(os.path.join(images_dir_path, "task1.png"))


def task3() -> None:
    print(
        """
Task 3.
    a.) e^(iθ)α|0⟩ + e^(iφ)β|1⟩ <=>
        <=> e^(iθ) * (α|0⟩ + (e^(iθ))^(-1) * e^(iφ)β|1⟩) <=>
        <=> e^(iθ) * (α|0⟩ + e^(-iθ) * e^(iφ)β|1⟩) <=>
        <=> e^(iθ) * (α|0⟩ + e^(-i(φ - θ))β|1⟩) <=>
        <=> e^(iθ) * (α|0⟩ + e^(i(φ - θ))β|1⟩) <=>
        <=> /* omit the global phase e^(iθ) */ <=>
        <=> α|0⟩ + e^(i(φ - θ))β|1⟩.
    b.) e^(πi/2)α|0⟩ + e^(3πi/4)β|1⟩ <=>
        <=> e^(πi/2) * (α|0⟩ + e^(3πi/4) * e^(-πi/2) * β|1⟩) <=>
        <=> e^(πi/2) * (α|0⟩ + e^(3πi/4 - πi/2)β|1⟩) <=>
        <=> e^(πi/2) * (α|0⟩ + e^(πi/4)β|1⟩) <=>
        <=> /* omit the global phase e^(πi/2) */ <=>
        <=> α|0⟩ + e^(πi/4)β|1⟩.
    c.) e^(3πi/2)α|0⟩ - β|1⟩ <=>
        <=> /* use the equation: -1 = e^(πi) */ <=>
        <=> e^(3πi/2)α|0⟩ + e^(πi)β|1⟩ <=>
        <=> e^(3πi/2) * (α|0⟩ + e^(πi) * e^(-3πi/2) * β|1⟩) <=>
        <=> e^(3πi/2) * (α|0⟩ + e^(πi - 3πi/2) * β|1⟩) <=>
        <=> e^(3πi/2) * (α|0⟩ + e^(-πi/2)β|1⟩) <=>
        <=> /* omit the global phase e^(3πi/2) */ <=>
        <=> α|0⟩ + e^(-πi/2)β|1⟩.
        (<=> α|0⟩ + e^(3πi/2)β|1⟩).)
"""
    )


def main() -> None:
    images_dir_path = os.path.join(os.path.dirname(__file__), "images")
    task1(images_dir_path)
    print(
        "Task 2. We can omit the global phase and leave only: e^(iφ)(α|0⟩ + β|1⟩) ≡ α|0⟩ + β|1⟩."
    )
    task3()


if __name__ == "__main__":
    main()
