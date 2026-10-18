# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 17:02:00 2023

@author: eduar
"""

import numpy as np
import matplotlib.pyplot as plt

# Dados de exemplo
x = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180])
y = np.array([100, 98, 96, 93, 90, 88, 85, 83, 80, 79 ,76, 73, 70, 67, 64, 60, 57, 55, 51])

# Aplicando o método dos mínimos quadrados
A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]

# Plotando os pontos e a reta ajustada
plt.plot(x, y, 'o', label='Dados originais', markersize=8)
plt.plot(x, m*x + c, 'r', label='Reta ajustada')
plt.legend()
plt.show()

# Imprimindo a equação da reta ajustada
print(f'A equação da reta que melhor se encaixa é y = {m:.2f}x + {c:.2f}')
