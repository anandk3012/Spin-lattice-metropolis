# Metropolis-algorithm
---

### Project - Spin interaction

Consider a 2D square lattice of N x N atoms. They have a spin σ = ±1, either pointing up or down. The lattice sites can be labelled with some index. Take (N = 10). The energy of this system is defined as : 
  E = -J * ( ∑ σ_i * σ_j ).
  
Here (σ_i, σ_j) are the spins at nearest neighbor lattice sites i and j. Each neighboring pair is counted only once, each site has four nearest neighbors. Take periodic boundary conditions for the grid.
Start with a random initialization of the spins on the lattice. The probability of finding a particular configuration of spins, denoted by s, depends on its energy E_s by the Boltzmann relation :   
  P(s) ∝ exp(-E_s / (k_B T))
  
Randomly flip spins according to this probability, using the Metropolis algorithm. Continue this till thermal equilibrium is reached, i.e., energy becomes steady.
Try different parameters with J from 0.1 to 0.9, and (k_B*T) from 10^{-2} to 10^{2}. 

Calculate the magnetization in the equilibrated state : 
  M = (∑_i σ_i) / (N^2)

Analyze how the magnetization varies with (k_B * T) and see if there is a phase transition with temperature.

---

## How to Run

This repository contains all code and notebooks required to simulate the 2D Ising model using the Metropolis algorithm. The main logic is implemented in Python scripts, and results can be visualized and explored interactively using the provided Jupyter notebook.

- All simulation and plotting code is in Python files in this directory.
- The main entry point for running experiments and visualizations is the `test.ipynb` Jupyter notebook.
- You can change parameters such as lattice size, temperature, coupling constant, and number of iterations directly in the notebook cells.
- The notebook demonstrates:
  - Lattice visualization
  - Energy convergence for different parameters
  - Magnetization as a function of temperature
  - Animated visualization of spin lattice evolution

**To run the simulation and generate plots/animations:**

1. Open `test.ipynb` in Jupyter Notebook or VS Code.
2. Run all cells sequentially, or modify parameters as needed and rerun.
3. Output plots and animations will be saved in the `plots/` and `animations/` folders.

RUN test.ipynb to run the algorithm and change parameters as