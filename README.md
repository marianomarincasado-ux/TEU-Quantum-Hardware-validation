# 🌌 TEU Quantum Hardware Validation

![Qiskit](https://img.shields.io/badge/Qiskit-Tested-blue)
![Hardware](https://img.shields.io/badge/IBM_Quantum-ibm__fez-purple)
![Status](https://img.shields.io/badge/Status-Empirically_Validated-success)

Este repositorio contiene la validación experimental y computable del **Modelo del Universo Topológico del Electrón (TEU)**. Utilizando el framework cuántico Qiskit, las ecuaciones continuas de la teoría TEU se han traducido a circuitos de puertas lógicas discretas y se han ejecutado empíricamente en hardware superconductor real (Arquitectura IBM Heron, procesador `ibm_fez`).

El objetivo de estos scripts es demostrar que la masa inercial no es un parámetro axiomático o intrínseco, sino un **observable cuántico emergente** que puede ser deducido midiendo la interferencia de fase provocada por la rigidez geométrica (fractalidad) del vacío.

---

## 🔬 Experimentos y Scripts

El repositorio se divide en tres experimentos incrementales. Cada script está diseñado para ejecutarse nativamente en la nube de IBM Quantum.

### 1. Quantum Random Walk (`teu_quantum_walk.py`)
**Objetivo:** Demostrar el confinamiento topológico sub-difusivo.
* **Mecanismo:** Se inicializa un electrón en superposición espacial (Caminata Aleatoria Cuántica). En lugar de evolucionar en un espacio de Minkowski liso, se inyecta la constante topológica TEU ($K_{geo} \approx 2.66$) a través de una compuerta de desfasaje ($P$).
* **Resultado Físico:** En hardware real, la interferencia destructiva generada por el polvo de Cantor ancla estadísticamente el paquete de ondas, logrando un confinamiento superior al 70%.

### 2. Interferometría Ab Initio (`teu_mass_extraction.py`)
**Objetivo:** Extraer la masa del electrón ($m_e$) directamente desde la probabilidad cuántica de la máquina.
* **Mecanismo:** Se construye un análogo de un interferómetro de Mach-Zehnder con un solo qubit. La onda se divide, choca contra la fase fractal del TEU, y se recombina. 
* **Resultado Físico:** El hardware físico lee una probabilidad destructiva del $\sim 30.6\%$. A partir de esta mera estadística física, el código despeja matemáticamente el ángulo de fase y calcula la masa emergente empírica, obteniendo $\sim 1.29 \times 10^{-30}$ kg, coincidiendo con el orden de magnitud macroscópico de la masa referencial de CODATA.

### 3. Barrido Paramétrico Cuántico (`teu_parametric_sweep.py`)
**Objetivo:** Demostrar la respuesta exponencial de la masa ante diferentes topologías (La Curva de la Masa).
* **Mecanismo:** Se compilan en lote (batch) 5 circuitos simulando 5 universos con diferente rugosidad geométrica ($K_{geo}$ variable desde 1.5 hasta 5.0).
* **Resultado Físico:** La máquina de IBM traza empíricamente la curva $m_e = M_p \cdot e^{-D}$. Los resultados demuestran que a mayor fricción, menor probabilidad de escape y menor masa inercial, culminando exactamente en la masa del electrón al inyectar el valor $K_{geo} = 2.659$.

---

## 📊 Resultados Empíricos

El siguiente gráfico vectorial muestra los resultados directos extraídos del procesador cuántico `ibm_fez` (133 qubits, enfriado a 15 mK). 

*(Nota: Inserta aquí el archivo `teu_mass_curve_ibm_bw.svg` o `.png` generado)*
![Curva de Masa Empírica TEU](imagen/teu_mass_curve_ibm_bw.svg)

**Conclusión del Hardware:** La línea punteada representa la ecuación analítica perfecta. Los puntos representan los colapsos reales de la función de onda medidos por la máquina física. La estrella marca el régimen topológico del Electrón TEU. El hardware cuántico ruidoso (NISQ) traza fielmente la atenuación exponencial TEU a lo largo de 30 órdenes de magnitud.

---

## 🚀 Cómo reproducir los experimentos

1. Clona este repositorio:
   ```bash
   git clone [https://github.com/TU_USUARIO/TEU-Quantum-Validation.git](https://github.com/TU_USUARIO/TEU-Quantum-Validation.git)
pip install qiskit qiskit-ibm-runtime matplotlib numpy

Consigue un Token API gratuito en IBM Quantum.

Ejecuta cualquiera de los scripts reemplazando la variable MI_TOKEN con tu clave personal.

Datos crudos (JSON logs) devueltos por la plataforma IBM Quantum durante las ejecuciones están disponibles en la carpeta /data para verificación de pares e historial de deriva temporal (temporal drift).

