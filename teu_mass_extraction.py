from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2
import numpy as np

print("===================================================================")
print(" 🌌 TEU QUANTUM SWEEP: EXPLORANDO MULTIPLES TOPOLOGÍAS (IBM)      ")
print("===================================================================")

MI_TOKEN = "PEGA_TU_TOKEN_AQUI" # <--- ¡Pon tu token!

QiskitRuntimeService.save_account(channel="ibm_quantum_platform", token=MI_TOKEN, set_as_default=True, overwrite=True)
service = QiskitRuntimeService()

backend_real = service.least_busy(operational=True, simulator=False)
print(f"[>] Conectado al procesador superconductor: {backend_real.name}")

# ===================================================================
# CREAMOS 5 UNIVERSOS DIFERENTES (5 Circuitos)
# ===================================================================
# Diferentes valores de K_geo (desde un espacio más liso a uno más fractal)
topologias_k_geo = [1.5, 2.0, 2.659, 3.5, 5.0]
circuitos = []

for k in topologias_k_geo:
    qc = QuantumCircuit(1, 1)
    # Ángulo de fricción basado en la constante K_geo
    fase = np.pi / k 
    qc.h(0)
    qc.p(fase, 0)
    qc.h(0)
    qc.measure(0, 0)
    circuitos.append(qc)

print(f"\n[>] {len(circuitos)} circuitos compilados (Universo múltiple).")
circuitos_transpilados = transpile(circuitos, backend=backend_real)

# ===================================================================
# EJECUCIÓN FÍSICA EN LOTE (BATCH)
# ===================================================================
DISPAROS = 2048
sampler = SamplerV2(mode=backend_real)
sampler.options.default_shots = DISPAROS

print(f"[*] Disparando electrones en {backend_real.name}...")
job = sampler.run(circuitos_transpilados)
print(f"[>] Trabajo enviado a la cola. ID: {job.job_id()}")
print("[*] (Esperando resultados físicos de la máquina...)")

# Esperamos los resultados
resultados = job.result()

# ===================================================================
# EXTRACCIÓN EMPÍRICA EN MASA (Masa vs Geometría)
# ===================================================================
ALPHA_INV = 137.035999
M_PLANCK = 2.176434e-8

print("\n===================================================================")
print(" 📊 RESULTADOS DEL HARDWARE: LA CURVA DE LA MASA TEU")
print("===================================================================")
print(" K_geo Inyectado |  % Destructivo | Masa Empírica Extraída (kg)")
print("-------------------------------------------------------------------")

for i, k_teorico in enumerate(topologias_k_geo):
    conteos = resultados[i].data.c.get_counts()
    impactos_1 = conteos.get('1', 0)
    prob = impactos_1 / DISPAROS
    
    # Extraemos el ángulo empírico que ha sentido la máquina (protección contra ruido)
    # Evitamos error matemático si el ruido lo saca de rango
    prob_segura = min(prob, 0.9999) 
    k_empirico = np.pi / (2 * np.arcsin(np.sqrt(prob_segura)))
    
    # Calculamos la masa que emerge en este universo específico
    D = ALPHA_INV / k_empirico
    masa = M_PLANCK * np.exp(-D)
    
    marca = " <-- [TEU (Electrón)]" if k_teorico == 2.659 else ""
    print(f" K = {k_teorico:<11} |  {prob*100:>5.1f} %       | {masa:>22.4e}{marca}")

print("===================================================================")
print(" CONCLUSIÓN: Cuanto más alta es la fricción topológica K_geo (fractal),")
print(" menor es la probabilidad de escape, modificando exponencialmente la masa.")
