# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 19:45:11 2022

@author: Carlos Eduardo Almeida Santos
"""
# Esboço dos Gráficos

from  matplotlib import pyplot as plt
import numpy as np


# y = np.sin(x)- np.exp(x)
# y = np.cos(np.pi*(x + 1)/8) + 0.148*x - 0.9062
# y = 2*x**2 - 5 * x + 2

x = np.linspace(-3*np.pi/2, 3*np.pi/2)
y = np.sin(x)- np.exp(x)
plt.plot(x, y, color = 'b')
plt.grid(True)
plt.xlabel('Eixo x')
plt.ylabel('')
plt.title('h(x) = sen(x) -$np.exp(x)$')