import numpy as np

def generate_spin_lattice(N):
    lattice = np.zeros((N,N))
    # Setting up the spin at each point
    for i in range(N):
        for j in range(N):
            k = np.random.uniform()
            if k > 0.5 :
                lattice[i][j] = 1
            else:
                lattice[i][j] = -1
    
    return lattice