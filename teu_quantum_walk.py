from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2
import numpy as np

print("===================================================================")
print(" 🌌 TEU QUANTUM RANDOM WALK: REAL IBM HARDWARE EXECUTION          ")
print("===================================================================")

# 1. AUTENTICACIÓN CON IBM
MI_TOKEN = "PEGA_TU_TOKEN_AQUI" # <--- ¡Pon tu token real aquí!

print("[*] Conectando con los laboratorios de IBM Quantum...")
QiskitRuntimeService.save_account(channel="ibm_quantum_platform", token=MI_TOKEN, set_as_default=True, overwrite=True)
service = QiskitRuntimeService()

# 2. BUSCAR EL ORDENADOR REAL MENOS OCUPADO
print("[*] Buscando el procesador cuántico con menos cola de espera...")
backend_real = service.least_busy(operational=True, simulator=False)
print(f"[>] ¡Conectado! Tu circuito se enviará a la máquina superconductora: {backend_real.name}")

# 3. CREAR EL CIRCUITO TEU
qc = QuantumCircuit(2, 1)
coin = 0
pos = 1
friccion_topologica = np.pi / 2.66 

# Bucle de la caminata (Inyección de la masa)
for step in range(3):
    qc.h(coin)
    qc.p(friccion_topologica, coin) # Tu K_geo (Fricción fractal)
    qc.cx(coin, pos)

qc.measure(pos, 0)
print("\n[>] Circuito compilado. Transpilando para el hardware físico...")

# 4. EJECUTAR EN EL HARDWARE (Sintaxis V2 Corregida)
# Adaptamos el circuito a las puertas de ibm_torino
qc_transpilado = transpile(qc, backend=backend_real)

# Configuramos el Sampler V2 con la nueva sintaxis
sampler = SamplerV2(mode=backend_real)
sampler.options.default_shots = 1024  # Los disparos ahora se configuran aquí

# ¡Enviamos el trabajo!
job = sampler.run([qc_transpilado])

print(f"\n[>] ¡TRABAJO ENVIADO CON ÉXITO! ID del Trabajo (Job ID): {job.job_id()}")
print(f"[*] Ve a tu panel en la web de IBM Quantum (Pestaña 'Jobs') para ver cómo tu código")
print(f"    está haciendo cola para ejecutarse en {backend_real.name}.")
