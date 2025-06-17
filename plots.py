import numpy as np
import matplotlib.pyplot as plt

def plot_energy_vs_iters(spin_lattice_energies : list, J : float, iters : int):
 
    x = np.linspace(0,iters+1,iters)
    
    plt.figure(figsize=(18,6))
    plt.title(f'Energy vs iters for J = {J} plot')
    plt.plot(x, spin_lattice_energies)
    plt.ylim(bottom=-200, top=0)
    plt.savefig(f"plots/energy_vs_iters_j_{J}.png")
    plt.show()
    
    return

def plot_magnetization_vs_temp(magnetization : list, temp : list):
    
    plt.figure(figsize=(18,6))
    plt.title('Magnetization vs temp plot')
    plt.plot(temp, magnetization)
    plt.savefig("plots/magnetization_vs_temp.png")
    plt.show()

    return
