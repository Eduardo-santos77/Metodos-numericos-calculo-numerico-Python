# -*- coding: utf-8 -*-
"""
@author: Carlos Eduardo

Método dos Minimos Quadrados 

"""
import numpy as np
from  matplotlib import pyplot as plt

#x = [1.1, 1.7, 2.3, 2.8]
#y = [5.8, 5.1, 4.3, 3.7]
x = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180] #O número de elementos em "x" deve ser igual ao de "y".
y = [100, 95, 93, 88, 85, 80, 76, 70, 64, 62, 59, 52, 47, 30, 23, 18, 13, 8, 2]
#Função
def sistAtdo(x, y, dim):
    m = len(x) 
    A = np.empty((dim, dim))    
    b = np.empty((dim))         
    soma = []                   
    for i in range(0, dim+2):
        aux = 0 
        for k in range(0, m):      
            aux = aux + x[k]**i
        soma.append(aux)
        
    for i in range(0, dim):
        for j in range(i, dim):
            A[i, j] = soma[i+j]
            if (i != j):
                A[j, i] = A[i, j]
            
    b = []
    for i in range(0, dim):
        aux = 0
        for k in range(0, m):
            aux = aux + y[k]*(x[k]**(i))
        b.append(aux)
        
    return A, b
A, b = sistAtdo(x, y, 3)
print("A = ", A)
print("B = ", b)
coef = np.linalg.solve(A, b)
print("Coeficiente = ", coef)

plt.plot(x, y, 'ro')
data = np.linspace(min(x), max(x), 100)
c = coef[::-1].copy()
p = np.poly1d(c)
plt.plot(data, p(data), 'b-')
plt.grid()
plt.xlabel('Tempo decorrido (minutos)')
plt.ylabel('Quantidade de Gelo (%)')
plt.title('Garrafa Normal (pet)')