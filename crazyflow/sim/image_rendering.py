from mujoco import MjvCamera
import numpy as np

class Camera():
    def __init__(self):
        raise NotImplementedError

    def place(self):
        raise NotImplementedError

    def capture(self) -> np.ndarray:
        raise NotImplementedError