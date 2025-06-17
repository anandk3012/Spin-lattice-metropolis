import numpy as np

def lattice_energy(spin_lattice : list, J : float):
    energy = 0 # energy eigenvalue of the spin lattice
    N = len(spin_lattice) # no of atoms
    
    for i in range(N):
        for j in range(N):
            energy += spin_lattice[i][j] * ( spin_lattice[(i + 1) % N][j] + spin_lattice[i][(j + 1) % N] )
    return -J * energy

def boltzmann_probability(energy : float, k : float, T : float):
    return np.exp( -(energy) / (k * T))

def lattice_magnetization(spin_lattice : list):
    magnetization = 0
    N = len(spin_lattice)
    for i in range(N):
        for j in range(N):
            magnetization += spin_lattice[i][j]
            
    return (magnetization/(N**2))
            