import numpy as np
import matplotlib.pyplot as plt

def logisticMap(r,x):
    return r * x * (1-x)

values = []
parameter = np.linspace(0.05, 4, 3000) # r values we will sub in to logistic map equation

for i in parameter:

    x0 = 0.5 # x for logistic map

    for j in range(1000):
     
     x0 = logisticMap(r=i, x=x0)
     
     if j > 899: # only take 100 later values for plotting
        values.append([i,x0])

values = np.array(values) # turn into an array

plt.scatter(values[:,0],values[:,1], s=0.1, color="black") 
plt.xlabel("Parameter r")

plt.ylabel("Steady State Values of x")
plt.title("Bifurcation Diagram")

plt.show()

