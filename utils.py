import numpy as np

# Find sum of all spins in the matrix for magnetisation calculation
def sum_lattice_spins(spin_lattice : list):
    sum = 0
    for i in range(len(spin_lattice)):
        for j in range(len(spin_lattice)):
            sum += spin_lattice[i][j]
    return sum

# Function to generate random integer between -1 and 1
def generate():
    return np.random.randint(-1,2)