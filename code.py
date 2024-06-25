import numpy as np
import matplotlib.pyplot as plt



# Define our constants
N=10
iterations=8000
K=1
T=1
J_value = 0.7

# Define (N x N) Grid
matrix=np.zeros((N,N))
# Setting up the spin at each point
for i in range(N):
    for j in range(N):
        k=np.random.uniform()
        if k> 0.5 :
            matrix[i][j]=1
        else:
            matrix[i][j]=-1
print(matrix)
print("\n")

# Function to Calculate energy for the configuration
def energy(m, J):
    e = 0
    n = len(m)
    for i in range(n):
        for j in range(n):
            e += m[i][j] * (m[(i + 1) % n][j] + m[i][(j + 1) % n])
    return -J * e

# Probability of that spin configuration
def prob(e,k,T):
    return np.exp(-(e)/(k*T))

# Function to generate random integer between -1 and 1
def generate():
    return np.random.randint(-1,2)

# Find sum of all spins in the matrix for magnetisation calculation
def sum_m(m):
    s=0
    for i in range(len(m)):
        for j in range(len(m)):
            s+=m[i][j]
    return s

# Function to run the Metropolis algorithm which randomly flips the spins
def metropolis(matrix,K,T,iterations):

    i,j=int(9*np.random.uniform()),int(9*np.random.uniform())
    en=[] #Energy matrix

    for _ in range(iterations):

        i,j=(i+generate())%N,(j+generate())%N #Generate two random indices to flip their spins
        w=matrix
        w[i][j] = -1*w[i][j] #Flip the spins at that position

        e=energy(w,J_value)
        en.append(e) #Calculate and append the new energy of the matrix

        a=min(1,prob(((e-energy(matrix,J_value))),K,T))  #Acceptance probability - If our probability crosses one, this rounds it back to one

        k=np.random.uniform()
        if (k < a) or ((energy(w,J_value) - energy(matrix,J_value)) < 0): #If the acceptance probability is greater than k or if the energy of the matrix decreases, the new matrix is accepted and updated
            matrix=w

    return matrix,en

m,en = metropolis(matrix,K,T,iterations)
x = np.linspace(0,iterations+1,iterations)

# Average and Max energy of the configurations
max_en = 0
avg_sum = 0
for e in en:
  if(e > max_en):
    max_en = e
  avg_sum += e

avg_en = avg_sum/len(en)
print(f'Average energy = {avg_en}\n\n')
print(f'Max energy = {max_en}\n\n')

# print(len(x))
plt.figure(figsize=(18,6))
plt.title('Energy vs iterations plot')
plt.plot(x,en)
plt.show()


# Moving average o energy vs iterations plot
T = [0.01, 0.1, 1, 10, 100]
x_var=np.linspace(1,100,99)
m=matrix
for index, i in enumerate(T):
  l1=[]
  e=0
  for j in range(1,100):
    m,ene=metropolis(m,K,i,1)
    e+=ene[0]
    l1.append(e/j)
  plt.plot(x_var, l1, label=f"K={i}")

plt.legend()
plt.show()


# Magnetisation plots

T = [0.01, 0.1, 1, 10, 100 , 1000]

plt.figure()  # Create a new figure
mag=[]

for i in T:
    sum=0
    for j in range(20):
        ma, en = metropolis(matrix, K, i, iterations)
        sum+=abs(sum_m(ma))
    mag.append(sum)

plt.plot(T, mag, label=f'Temperature={i}')
plt.xlabel('Iteration (j)')
plt.ylabel('Magnetization')
plt.title('Magnetization vs Iteration')
plt.legend()  # Show legend
plt.grid(True)
plt.show()
