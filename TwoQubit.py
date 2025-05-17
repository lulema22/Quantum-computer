import numpy as np

from gates import H_tensor


class TwoQubit:
    def __init__(self, alpha = 1, beta = 0, gamma = 0, delta = 0 ):
        self.state = np.array([alpha, beta, gamma, delta], dtype=complex)
        self.normalize()
    def normalize(self):
        norm = np.linalg.norm(self.state)
        if norm == 0:
            raise ValueError("Деление на ноль")
        self.state = self.state / norm
    def gate(self, gate):
        self.state = np.dot(gate, self.state)

    def phase_oracl(self, marks):
        oracl_matrix = np.eye(4, dtype=complex)
        for i in marks:
            oracl_matrix[i, i] = -1
        self.gate(oracl_matrix)

    def oracl_const(self):
        self.phase_oracl([0, 1, 2, 3])

    def oracle_balanced(self):
        self.phase_oracl([1, 2])

    def alg_Grover(self, marks):
        self.gate(H_tensor)
        self.phase_oracl(marks)
        N = 4
        s = np.full((N, 1), 1 / np.sqrt(N), dtype=complex)
        I = np.eye(N, dtype=complex)
        D = 2 * np.dot(s, s.T) - I
        self.gate(D)

