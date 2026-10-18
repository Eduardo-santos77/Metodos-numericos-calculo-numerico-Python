# -*- coding: utf-8 -*-
"""

@author: Carlos Eduardo 

Método de Interpolação de Lagrange
"""
import numpy as np 
import matplotlib.pyplot as plt 

def intpLag(xp, x, y, grau):
    yp = 0
    for k in range(0, n+1):
        p = 1
        for j in range(0, n+1):
            if k != j:
                p = p*(xp - x[j])/(x[k] - x[j])

        yp = yp + p * y[k]
    return yp

x = [2.13, 2.78, 3.36]
y = [0.5, 1.57, 0.7]
n = 2
xp = 1.5
yp = intpLag(xp, x, y, n)
t = np.arange(1,4, 0.1)
yt = []
for i in t:
    yt.append(intpLag(i, x, y, n))
plt.plot(t,yt, 'b-')
plt.plot(x, y, 'ro')
plt.plot(xp, yp, 'g*')
plt.grid(True)
plt.xlabel('Eixo x')
plt.ylabel('')
plt.title('Interpolação de Lagrange')