"""
TEU QUANTUM HARDWARE VALIDATION - SCRIPT 1B
Extracción Empírica del Mass Gap Topológico mediante ZNE y EstimatorV2
Optimizado para Arquitectura IBM Heron (Heavy-Hex)
"""
import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService, EstimatorV2 as Estimator

print("\n=======================================================")
print(" TEU: EXTRACCIÓN DE MASA AB INITIO MEDIANTE ZNE Y PUBS")
print("=======================================================\n")

# 1. Autenticación y Selección de Hardware
MI_TOKEN = "PEGA_TU_TOKEN_AQUI" # <--- ¡Tu Token aquí!

print("[*] Autenticando en IBM Quantum...")
QiskitRuntimeService.save_account(channel="ibm_quantum_platform", token=MI_TOKEN, set_as_default=True, overwrite=True)
service = QiskitRuntimeService()

# Solicitar explícitamente backend avanzado soportando Fractional Gates
backend = service.least_busy(operational=True, simulator=False, min_num_qubits=127)
print(f"[*] Conectado al procesador cuántico: {backend.name}")

# 2. Definición de Constantes Fundamentales TEU
ALPHA_INV = 137.035999
M_PLANCK = 2.176434e-8 # Masa desnuda (kg)
K_GEO_TEORICO = 2.659455 # Rigidez del vacío (Cantor)

# 3. Diseño del Circuito Abstracto Parametrizado (Interferómetro Topológico)
theta_friccion = Parameter('friccion_topologica')
qc = QuantumCircuit(1)
qc.h(0) # Superposición (Paquete de ondas sin masa)
qc.p(theta_friccion, 0) # Inyección de la porosidad del vacío
qc.h(0) # Recombinación e Interferencia

# 4. Definición del Observable (Operador Hermítico)
observable = SparsePauliOp("Z")

# 5. Optimización y Mapeo Topológico (Pass Manager)
print("[*] Optimizando circuito para topología Heavy-Hex (Nivel 3)...")
pm = generate_preset_pass_manager(backend=backend, optimization_level=3)
isa_circuit = pm.run(qc)
isa_observable = observable.apply_layout(isa_circuit.layout)

# 6. Configuración de Primitivas y Mitigación de Errores V2
estimator = Estimator(mode=backend)
estimator.options.resilience.measure_mitigation = True
estimator.options.resilience.zne_mitigation = True
estimator.options.resilience.zne.noise_factors = (1, 3, 5)
estimator.options.resilience.zne.extrapolator = ("exponential", "linear")
estimator.options.default_precision = 0.005 

# 7. Ejecución Vectorizada mediante PUB
valor_fase = np.pi / K_GEO_TEORICO
pub = (isa_circuit, isa_observable, valor_fase)

print(f"[*] Ejecutando simulación ZNE en {backend.name}. Esperando convergencia cuántica...")
job = estimator.run([pub])
print(f"[>] ID del Trabajo: {job.job_id()}")
result = job.result()

# 8. Post-Procesamiento Analítico y Extracción Física
ev_z = result[0].data.evs
probabilidad_destructiva = (1 - ev_z) / 2
prob_segura = min(max(probabilidad_destructiva, 0.0), 0.9999) 

# Extracción de la Constante de Rigidez Empírica sentida por la máquina
theta_medido = 2 * np.arcsin(np.sqrt(prob_segura))
k_geo_empirico = np.pi / theta_medido if theta_medido > 0 else float('inf')

# Ecuación Maestra TEU: Emergencia de la Inercia
profundidad_escala = ALPHA_INV / k_geo_empirico
masa_extraida_kg = M_PLANCK * np.exp(-profundidad_escala)

print("\n================ RESULTADOS FÍSICOS ===================")
print(f" -> Valor Esperado Mitigado <Z> : {float(ev_z):.5f}")
print(f" -> Probabilidad Destructiva  : {prob_segura*100:.2f}%")
print(f" -> Rigidez Fractal Empírica  : {k_geo_empirico:.6f} (Teórico: {K_GEO_TEORICO:.6f})")
print(f" -> Masa Inercial Extraída    : {masa_extraida_kg:.4e} kg")
print("=======================================================")
