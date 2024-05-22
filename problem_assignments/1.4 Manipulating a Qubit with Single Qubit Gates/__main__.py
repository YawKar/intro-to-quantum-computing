import qutip as qp  # pyright: ignore[reportMissingTypeStubs]
import numpy as np
import os
import unittest
from typing import cast, Any


class TestGates(unittest.TestCase):

    def test_xgate_is_sigmax(self) -> None:
        xgate = np.array([[0, 1], [1, 0]])
        self.assertTrue(
            np.array_equal(
                cast(np.ndarray[Any, Any], qp.sigmax().data.to_array()),
                xgate,
            )
        )

    def test_ygate_is_sigmay(self) -> None:
        ygate = np.array([[0, -1j], [1j, 0]])
        self.assertTrue(
            np.array_equal(
                cast(np.ndarray[Any, Any], qp.sigmay().data.to_array()),
                ygate,
            )
        )

    def test_zgate_is_sigmay(self) -> None:
        zgate = np.array([[1, 0], [0, -1]])
        self.assertTrue(
            np.array_equal(
                cast(np.ndarray[Any, Any], qp.sigmaz().data.to_array()),
                zgate,
            )
        )

    def test_xgate_swaps_alpha_and_beta(self) -> None:
        """
        X-gate rotates the given state by Pi radians along the `x` axis
        """
        self.assertTrue(
            np.array_equal(
                (
                    qp.sigmax() * qp.Qobj([1 / 2, np.sqrt(3) / 2])
                ).data.to_array(),  # pyright: ignore [reportUnknownArgumentType]
                qp.Qobj(
                    [np.sqrt(3) / 2, 1 / 2]
                ).data.to_array(),  # pyright: ignore [reportUnknownArgumentType]
            )
        )


def task1(images: str) -> None:
    b = qp.Bloch()
    q = qp.Qobj([1 / 2, np.sqrt(3) / 2])
    applied_x_gate = cast(qp.Qobj, qp.sigmax() * q)
    b.add_arc(q, applied_x_gate, "b--", linewidth=3)
    b.add_states([q, applied_x_gate])
    b.save(name=os.path.join(images, "task1.png"))


def task2(images: str) -> None:
    b = qp.Bloch()
    q = qp.Qobj([1 / 2, np.sqrt(3) / 2])
    applied_y_gate = cast(qp.Qobj, qp.sigmay() * q)
    _middle_point = qp.Qobj([1 / np.sqrt(2), 1j / np.sqrt(2)])
    b.add_arc(q, _middle_point, "b--", linewidth=3)
    b.add_arc(_middle_point, applied_y_gate, "b--", linewidth=3)
    b.add_states([q, applied_y_gate])
    b.save(name=os.path.join(images, "task2.png"))


def task3(images: str) -> None:
    b = qp.Bloch()
    q = qp.Qobj([1 / 2, np.sqrt(3) / 2])
    applied_z_gate = cast(qp.Qobj, qp.sigmaz() * q)
    b.add_arc(q, applied_z_gate, "b--", linewidth=3)
    b.add_states([q, applied_z_gate])
    b.save(name=os.path.join(images, "task3.png"))


def main() -> None:
    unittest.main(exit=False)
    images_folder = os.path.join(os.path.dirname(__file__), "images")
    task1(images_folder)
    task2(images_folder)
    task3(images_folder)


if __name__ == "__main__":
    main()
