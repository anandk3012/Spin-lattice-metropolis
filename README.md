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

Analyze how the magnetization varies with (k_B*T) and see if there is a phase transition with temperature.

---
