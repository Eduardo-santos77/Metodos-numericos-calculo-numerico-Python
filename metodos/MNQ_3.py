# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 10:21:16 2023
MÉTODO DOS MINÍMOS QUADRADOS
@author: eduardo
"""

import numpy as np
import matplotlib.pyplot as plt

# Etapa 1: Definir os dados de entrada (x e y)
x = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180])
y= np.array([100, 95, 93, 88, 85, 80, 76, 70, 64, 62, 59, 52, 47, 30, 23, 18, 13, 8, 2])#Garrafa Convercional
#y = np.array([100, 98, 96, 93, 90, 88, 85, 83, 80, 79 ,78, 76, 73, 70, 67, 65, 64, 55, 51])#Garrafa térmica

# Etapa 2: Calcular as somas relevantes
n = len(x)  # Número de pontos de dados
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_x_squared = np.sum(x**2)
sum_xy = np.sum(x * y)

# Etapa 3: Calcular os coeficientes do ajuste linear (a e b)
a = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
b = (sum_y - a * sum_x) / n

# Etapa 4: Calcular os valores ajustados usando a e b
y_pred = a * x + b

# Etapa 5: Plotar os dados originais e a linha de ajuste
plt.scatter(x, y, label='Dados Originais', color='blue')
plt.plot(x, y_pred, label='Linha de Ajuste', color='red')
plt.grid()
plt.xlabel('Tempo decorrido (minutos)')
plt.ylabel('Quantidade de Gelo (%)')
plt.title('Garrafa Térmica (Stanley)')
plt.legend()

# Etapa 6: Calcular o erro quadrático médio (RMSE)
error = y - y_pred
rmse = np.sqrt(np.mean(error**2))
print(f'Erro Quadrático Médio (RMSE): {rmse}')

# Etapa 7: Mostrar o gráfico
plt.show()

#Etapa 8: Mostrar a equação da reta que melhor se encaixa
print(f'A equação da reta que melhor se encaixa é y = {a:.2f}x + {b:.2f}')