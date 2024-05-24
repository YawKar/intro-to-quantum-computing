import qutip as qp  # pyright: ignore [reportMissingTypeStubs]
import numpy as np
from typing import cast
import os
import unittest


def from_exponential_form(*, r: float = 1.0, theta: float) -> complex:
    return r * (np.cos(theta) + 1j * np.sin(theta))


class Tests(unittest.TestCase):
    def test_s_gate_value(self) -> None:
        s_gate = qp.gates.s_gate()
        self.assertTrue(
            np.allclose(
                s_gate.data.to_array(),  # type: ignore
                np.array(
                    [
                        [1, 0],
                        [0, from_exponential_form(theta=np.pi / 2)],
                    ]
                ),
            ),
        )

    def test_s_gate_rotates_by_half_of_pi_radians_along_the_z_axis(self) -> None:
        q = qp.Qobj([p := 1 / np.sqrt(2), p])
        s_gated = cast(qp.Qobj, qp.gates.s_gate() * q)
        self.assertTrue(
            np.allclose(
                s_gated.data.to_array(),  # type: ignore
                np.array([[p := 1 / np.sqrt(2)], [1j * p]]),
            )
        )

    def test_s_dagger_gate_rotates_clockwise_by_half_of_pi_radians_along_the_z_axis(
        self,
    ) -> None:
        q = qp.Qobj([p := 1 / np.sqrt(2), p])
        s_gated = cast(qp.Qobj, qp.gates.s_gate().dag() * q)
        self.assertTrue(
            np.allclose(
                s_gated.data.to_array(),  # type: ignore
                np.array([[p := 1 / np.sqrt(2)], [-1j * p]]),
            )
        )

    def test_t_gate_rotates_by_quarter_of_pi_radians_along_the_z_axis(self) -> None:
        q = qp.Qobj([p := 1 / np.sqrt(2), p])
        s_gated = cast(qp.Qobj, qp.gates.t_gate() * q)
        self.assertTrue(
            np.allclose(
                s_gated.data.to_array(),  # type: ignore
                np.array(
                    [
                        [p := 1 / np.sqrt(2)],
                        [from_exponential_form(theta=np.pi / 4) * p],
                    ]
                ),
            )
        )

    def test_t_dagger_gate_rotates_clockwise_by_quarter_of_pi_radians_along_the_z_axis(
        self,
    ) -> None:
        q = qp.Qobj([p := 1 / np.sqrt(2), p])
        s_gated = cast(qp.Qobj, qp.gates.t_gate().dag() * q)
        self.assertTrue(
            np.allclose(
                s_gated.data.to_array(),  # type: ignore
                np.array(
                    [
                        [p := 1 / np.sqrt(2)],
                        [from_exponential_form(theta=-np.pi / 4) * p],
                    ]
                ),
            )
        )


def draw_s_gate_applications(images_dir_path: str) -> None:
    b = qp.Bloch()
    q1 = qp.Qobj([1 / 2, np.sqrt(3) / 2])
    rotated_by_sgate_once = cast(qp.Qobj, qp.gates.s_gate() * q1)
    rotated_by_sgate_twice = cast(qp.Qobj, qp.gates.s_gate() * rotated_by_sgate_once)
    rotated_by_sgate_thrice = cast(qp.Qobj, qp.gates.s_gate() * rotated_by_sgate_twice)
    b.add_states(
        [q1, rotated_by_sgate_once, rotated_by_sgate_twice, rotated_by_sgate_thrice],
        colors=[["purple"]] * 4,
    )
    b.add_annotation(q1, "q1", fontsize=15)
    b.add_annotation(rotated_by_sgate_once, "s^1", fontsize=15)
    b.add_annotation(rotated_by_sgate_twice, "s^2", fontsize=15)
    b.add_annotation(rotated_by_sgate_thrice, "s^3", fontsize=15)

    b.save(os.path.join(images_dir_path, "s_gate_applications.png"))


def draw_t_gate_applications(images_dir_path: str) -> None:
    b = qp.Bloch()
    q2 = qp.Qobj([1 / 2, np.sqrt(3) / 2])
    rotated_by_tgate_once = cast(qp.Qobj, qp.gates.t_gate() * q2)
    rotated_by_tgate_twice = cast(qp.Qobj, qp.gates.t_gate() * rotated_by_tgate_once)
    rotated_by_tgate_thrice = cast(qp.Qobj, qp.gates.t_gate() * rotated_by_tgate_twice)
    rotated_by_tgate_fource = cast(qp.Qobj, qp.gates.t_gate() * rotated_by_tgate_thrice)
    b.add_states(
        [
            q2,
            rotated_by_tgate_once,
            rotated_by_tgate_twice,
            rotated_by_tgate_thrice,
            rotated_by_tgate_fource,
        ],
        colors=[["green"]] * 5,
    )
    b.add_annotation(q2, "q2", fontsize=15)
    b.add_annotation(rotated_by_tgate_once, "t^1", fontsize=15)
    b.add_annotation(rotated_by_tgate_twice, "t^2", fontsize=15)
    b.add_annotation(rotated_by_tgate_thrice, "t^3", fontsize=15)
    b.add_annotation(rotated_by_tgate_fource, "t^4", fontsize=15)

    b.save(os.path.join(images_dir_path, "t_gate_applications.png"))


def main() -> None:
    images_dir_path = os.path.join(os.path.dirname(__file__), "images")
    draw_s_gate_applications(images_dir_path)
    draw_t_gate_applications(images_dir_path)
    unittest.main()


if __name__ == "__main__":
    main()
