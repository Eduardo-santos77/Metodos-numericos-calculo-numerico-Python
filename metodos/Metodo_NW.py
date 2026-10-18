# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 10:12:47 2022

Método de Newton
@author: Carlos Eduardo
"""


import numpy as np

#Função a ser calculada
def f(x):
    return(np.sin(x)- np.exp(x))
    # return(np.cos(np.pi*(x+1)/8) + 0.148*x-0.9062)
    #return(x**2 - x -2)

#Derivada da Função    
def df(x):
    # h = 0.000001
    # return((f(x + h)- f(x))/h)
    return(np.cos(x)- np.exp(x))

 #Tolerância
ni = 100 #Número de interações
TOL = 0.0001
x0 = float(input('Entre com a aproximação inicial: '))
x = 0
i = 1 #Interação

while (np.fabs(f(x0)) > TOL):  #Enquanto o módulo da função for maior que a Tolerância
    x = x0 -f(x0)/df(x0)
    x0 = x
    i = i + 1
    if (i >= ni):
        print('Atenção: Raíz não encontrada')
        break

if(i < ni):
    print("\n\nRaíz %f\nInterações: %i\nf(%f) = %f\n\n"%(x0, i, x0, f(x0)))

