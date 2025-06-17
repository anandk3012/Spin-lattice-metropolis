import numpy as np
import matplotlib.pyplot as plt
from spin_lattice import generate_spin_lattice
from utils import sum_lattice_spins as sum_m, generate
from metropolis import metropolis
from observables import lattice_energy, lattice_magnetization, boltzmann_probability


# Define our constants
N = 10 # No of atoms
K = [0.01, 0.1, 1, 10, 100] # Boltzmann Constant
T = [0.01, 0.1, 1, 10, 100] # Boltzmann Constant

J = 0.7 # Coupling Constant for interaction between neighbouring atoms in Spin lattice

iters=8000
K_b_T = [k*t for k, t in zip(K, T)]

print(K_b_T)


# # Define (N x N) Grid
# spin_lattice = generate_spin_lattice(N)

# # Run the Metropolis algorithm which randomly flips the spins
# min_energy_spin_lattice, spin_lattice_energies = metropolis(N, spin_lattice, K, T, J, iters) 

# # Average and Max energy of the configurations
# avg_en = sum(spin_lattice_energies)/len(spin_lattice_energies)
# max_en = max(spin_lattice_energies)

# print(f'Average energy = {avg_en}\n\n')
# print(f'Max energy = {max_en}\n\n')



# # Moving average of energy vs iters plot (Energy Variation with Temperature)
# T = [0.01, 0.1, 1, 10, 100]

# x_var=np.linspace(1,100,99)

# m=spin_lattice
# for index, i in enumerate(T):
#   l1=[]
#   e=0
#   for j in range(1,100):
#     m,ene=metropolis(N, m, K, i, J, 1)
#     e+=ene[0]
#     l1.append(e/j)
#   plt.plot(x_var, l1, label=f"K={i}")

# plt.legend()
# plt.show()


# # Magnetisation plots

# T = [0.01, 0.1, 1, 10, 100 , 1000]

# plt.figure()  # Create a new figure
# mag=[]

# for i in T:
#     sum=0
#     for j in range(20):
#         ma, spin_lattice_energies = metropolis(N, spin_lattice, K, i, J, iters)
#         sum+=abs(sum_m(ma))
#     mag.append(sum)

# plt.plot(T, mag, label=f'Temperature={i}')
# plt.xlabel('Iteration (j)')
# plt.ylabel('Magnetization')
# plt.title('Magnetization vs Iteration')
# plt.legend()  # Show legend
# plt.grid(True)
# plt.show()