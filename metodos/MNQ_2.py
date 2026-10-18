# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 17:02:40 2023
Método dos minimos quadrados 2.0
@author: eduar
"""

import numpy as np

# Dados de exemplo (pontos x e y)
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 4, 6])

# Calcula a média de x e y
mean_x = np.mean(x)
mean_y = np.mean(y)

# Calcula as diferenças entre os pontos e a média
diff_x = x - mean_x
diff_y = y - mean_y

# Calcula os coeficientes da regressão linear (a inclinação e a interceptação)
slope = np.sum(diff_x * diff_y) / np.sum(diff_x**2)
intercept = mean_y - slope * mean_x

# Função para prever os valores de y com base na regressão linear
def predict(x):
    return slope * x + intercept

# Imprime os coeficientes da regressão linear
print(f'Inclinação (a): {slope}')
print(f'Interceptação (b): {intercept}')

# Use a função predict() para prever os valores de y com base em novos valores de x
new_x = np.array([6, 7, 8])
predicted_y = predict(new_x)
print(f'Valores previstos de y para novos valores de x: {predicted_y}')
