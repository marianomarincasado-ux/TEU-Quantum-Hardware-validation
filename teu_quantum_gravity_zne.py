"""
TEU QUANTUM HARDWARE VALIDATION - SCRIPT 3 (FINAL HYBRID)
Extracción de la Constante Gravitatoria Universal (G)
Estado de Bell (CNOT) + Purificación ZNE en Arquitectura Heron
"""
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService, EstimatorV2 as Estimator

print("\n=======================================================")
print(" TEU: GRAVEDAD CUÁNTICA EMPÍRICA VÍA CNOT + ZNE PURIFICADO")
print("=======================================================\n")

# 1. Autenticación y Selección de Hardware
MI_TOKEN = "PEGA_TU_TOKEN_AQUI" # <--- ¡Tu Token aquí!

print("[*] Autenticando en IBM Quantum...")
QiskitRuntimeService.save_account(channel="ibm_quantum_platform", token=MI_TOKEN, set_as_default=True, overwrite=True)
service = QiskitRuntimeService()

backend = service.least_busy(operational=True, simulator=False, min_num_qubits=127)
print(f"[*] Conectado al procesador cuántico: {backend.name}")

# 2. Constantes Fundamentales
K_GEO_TEU = 2.659455
ALPHA_INV = 137.035999
M_E = 9.1093837e-31 # Masa electrón (kg)
C_VEL = 299792458.0
HBAR = 1.054571817e-34
G_CODATA = 6.67430e-11

# 3. Construcción del Tensor Gravitatorio TEU
# Utilizamos 2 qubits para simular la interacción conjunta de masas (m_e^2)
qc = QuantumCircuit(2)

# Paso 1: Estado de Bell puro (Entrelazamiento cuántico)
qc.h(0)
qc.cx(0, 1)

# Paso 2: Ambos qubits atraviesan la métrica fractal de Cantor
theta_fase = np.pi / K_GEO_TEU
qc.p(theta_fase, 0)
qc.p(theta_fase, 1)

# Paso 3: Deshacer entrelazamiento para forzar interferencia conjunta
qc.cx(0, 1)
qc.h(0)

# 4. Definición del Observable
# Evaluamos la interferencia destructiva proyectada en el Qubit 0
# "IZ" significa: Identidad en Qubit 1, operador Pauli Z en Qubit 0
observable = SparsePauliOp("IZ")

print("[*] Optimizando circuito para topología Heavy-Hex (Nivel 3)...")
pm = generate_preset_pass_manager(backend=backend, optimization_level=3)
isa_circuit = pm.run(qc)
isa_observable = observable.apply_layout(isa_circuit.layout)

# 5. Configuración de Primitivas y Mitigación Avanzada
estimator = Estimator(mode=backend)
# Habilitamos mitigación de lectura de estado (TREX)
estimator.options.resilience.measure_mitigation = True
# Aplicamos Zero-Noise Extrapolation (ZNE) para limpiar el ruido de la compuerta CNOT
estimator.options.resilience.zne_mitigation = True
estimator.options.resilience.zne.noise_factors = (1, 3, 5)
estimator.options.resilience.zne.extrapolator = ("exponential", "linear")
estimator.options.default_precision = 0.005

# 6. Ejecución Vectorizada (Pub)
pub = (isa_circuit, isa_observable)
print(f"[*] Compilando Gravedad ZNE en {backend.name}. Esperando QPU...")
job = estimator.run([pub])
print(f"[>] ID del Trabajo: {job.job_id()}")
result = job.result()

# 7. Evaluación de la Interferencia Conjunta
ev_z = result[0].data.evs
# Transformación geométrica de valor esperado a probabilidad destructiva
probabilidad_destructiva = (1 - ev_z) / 2
prob_segura = min(max(probabilidad_destructiva, 0.0001), 0.9999)

# 8. Extracción Empírica del Apantallamiento Topológico
k_empirico = np.pi / np.arcsin(np.sqrt(prob_segura))
D_empirico = ALPHA_INV / k_empirico
# El entrelazamiento de 2 masas exige amplificación cuadrática (e^2D)
amplificacion_fractal = np.exp(2 * D_empirico)

# 9. Ecuaciones de Identidad TEU (La Ecuación de Jerarquía)
F_mech = (M_E**2 * C_VEL**3) / HBAR # Fuerza Mecánica del Electrón (0.212 N)
F_P_empirica = F_mech * amplificacion_fractal # Fuerza de Planck Emergente
G_empirica = (C_VEL**4) / F_P_empirica # Constante de Newton Despejada

error_relativo = abs(G_empirica - G_CODATA) / G_CODATA * 100

print("\n================ RESULTADOS FÍSICOS ===================")
print(f" -> Valor Esperado Mitigado <Z>  : {float(ev_z):.5f}")
print(f" -> Probabilidad Destructiva     : {prob_segura*100:.2f}%")
print(f" -> Amplificación Fractal (e^2D) : {amplificacion_fractal:.4e}")
print(f" -> Fuerza de Planck (Empírica)  : {F_P_empirica:.4e} N")
print(f" -> Constante G (Extraída)       : {G_empirica:.5e} m³/kg·s²")
print(f" -> Desviación vs CODATA         : {error_relativo:.2f}%")
print("=======================================================")
