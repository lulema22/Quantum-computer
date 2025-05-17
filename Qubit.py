import numpy as np

class Qubit:
    def __init__(self, alpha = 1, beta = 0):
        self.state = np.array([alpha, beta], dtype=complex)
        self.normalize()
    def normalize(self):
        norm = np.linalg.norm(self.state)
        if norm == 0:
            raise ValueError("Деление на ноль")
        self.state = self.state / norm
    def gate(self, gate):
        self.state = np.dot(gate, self.state)

    def __str__(self):
        a, b = self.state
        return f"{a:.3f}|0⟩+{b:.3f}|1⟩"
