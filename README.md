# Computational Physics Lab

**Maintainer:** Alex Morales (AlexPhysEngine)  
**Domain:** Numerical Analysis, Simulation Engines, & Complex Systems.

---

## Overview
This repository hosts a collection of high-performance Python implementations applied to fundamental problems in physics. The goal is to demonstrate the bridge between **theoretical mathematical models** and **efficient algorithmic execution**, moving beyond standard libraries to build custom numerical solvers from scratch.

Current focus areas include **Chaos Theory**, **Molecular Dynamics**, and **Statistical Mechanics**.

## Project Modules

### 1. Non-Linear Dynamics (Chaos)
* **Core Script:** `Lorenz.py`
* **Model:** The Lorenz Attractor (Deterministic Chaos).
* **Engineering:**
    * Manual implementation of **Runge-Kutta 4 (RK4)** for high-precision temporal integration.
    * Analysis of sensitivity to initial conditions (The "Butterfly Effect").
    * 3D Phase-space visualization.

### 2. Molecular Dynamics (N-Body Physics)
* **Status:** *[Active / In Progress]*
* **Model:** Lennard-Jones Gas Simulation.
* **Engineering:**
    * **Verlet Integrator:** Custom logic for stable, energy-conserving particle motion.
    * **Vectorized Physics:** Handling multi-agent interactions using NumPy matrix operations instead of slow iterative loops.

### 3. Statistical Mechanics
* **Status:** *[Planned]*
* **Model:** Ising Model (Ferromagnetism).
* **Engineering:** Monte Carlo simulations using the Metropolis algorithm to study phase transitions.

---

## Technology Stack
* **Language:** Python 3.10+
* **Numerical Computing:** NumPy (Heavy vectorization)
* **Visualization:** Matplotlib, Seaborn
* **Math Backend:** SciPy
