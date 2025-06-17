import numpy as np
from observables import lattice_energy, boltzmann_probability as prob

from utils import generate
# Function to run the Metropolis algorithm which randomly flips the spins
def metropolis(N : int, spin_lattice : list, K : float, T : float, J : float, iters : int):

    i, j = np.random.randint(0, N), np.random.randint(0, N)
    spin_lattice_energy=[] #Energy spin_lattice

    
    for _ in range(iters):
        k = np.random.uniform()
        
        i, j = ( i + generate()) % N, ( j + generate()) % N # Generate two random indices to flip their spins
        temp_lattice = list(np.array(spin_lattice).copy())
        temp_lattice[i][j] = -1 * temp_lattice[i][j] # Flip the spins at that position

        temp_energy = lattice_energy(temp_lattice,J)
        spin_lattice_energy.append(temp_energy) # Calculate and append the new energy of the spin_lattice

        a = min(1,prob(((temp_energy - lattice_energy(spin_lattice,J))),K,T))  # Acceptance probability - If our probability crosses one, this rounds it back to one

        if (k < a) or ((lattice_energy(temp_lattice,J) - lattice_energy(spin_lattice,J)) < 0): #If the acceptance probability is greater than k or if the energy of the spin_lattice decreases, the new spin_lattice is accepted and updated
            spin_lattice = temp_lattice

    return spin_lattice,spin_lattice_energy