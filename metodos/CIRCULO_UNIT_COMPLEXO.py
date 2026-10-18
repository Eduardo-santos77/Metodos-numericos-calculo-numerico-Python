# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 16:09:21 2023

@author: eduar
"""

import numpy as np
import matplotlib.pyplot as plt

# Definindo o círculo unitário
theta = np.linspace(0, 2*np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)

# Definindo as raízes
num_raizes = 6
k = np.arange(num_raizes)
raizes_x = np.cos(2 * np.pi * k / num_raizes)
raizes_y = np.sin(2 * np.pi * k / num_raizes)

# Plotando o círculo unitário e as raízes
plt.figure(figsize=(6,6))
plt.plot(x, y, label='Círculo Unitário')
plt.scatter(raizes_x, raizes_y, color='r', label='Raízes')
plt.title('Raízes da equação x^6 - 1 = 0 no círculo unitário')
plt.xlabel('Eixo Real')
plt.ylabel('Eixo Imaginário')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
