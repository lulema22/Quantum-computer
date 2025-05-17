from Qubit import Qubit
from TwoQubit import TwoQubit
from gates import H, X, Y, Z, CNOT, H_tensor
import numpy as np

def print_state(title, state):
    print(f"\n{title}")
    print(np.round(state.state, 3))

print("Одиночный кубит")
q = Qubit()
print_state("Начальное состояние |0⟩", q)

for gate, name in zip([X, Y, Z, H], ["X","Y","Z","H"]):
    q = Qubit()
    q.gate(gate)
    print_state(f"Применение {name}-гейта", q)

print("Двукубитный")
tq = TwoQubit()
print_state("Начальное состояние |00⟩", tq)

tq.gate(H_tensor)
print_state("После H х H ", tq)

tq.gate(CNOT)
print_state("После CNOT", tq)

tq = TwoQubit()
tq.gate(H_tensor)
tq.phase_oracl([2])
print_state("После phase_oracl([2])", tq)

tq = TwoQubit()
tq.gate(H_tensor)
tq.oracl_const()
print_state("После oracl_const()", tq)

tq = TwoQubit()
tq.gate(H_tensor)
tq.alg_Grover([3])
print_state("После alg_Grover([3])", tq)
