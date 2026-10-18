# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 14:23:05 2022

@author: Carlos Eduardo Almeida Santos

Método da Bissecção
"""
import numpy as np

#Função a ser calculada
def f(x):
    # return (np.cos(np.pi*(x+1)/8) + 0.148*x-0.9062)
    # return(np.sin(x)- np.exp(x))
    return (x**3 - 2*x - 1)
# Definir um intervalo [a,b] e um erro e.
a = float(input('Entre com o valor "a" do intervalo [a;b]:' ))
b = float(input('Entre com o valkor "b" do intervalo [a;b]:' ))
e =  float(input('Defina qual o valor do erro que se deseja verificar:'))

cont = 0
Ni = 100
c = b - a 

x0 = (a + b)/2

while (c > e or np.fabs(x0)):
    
    if (f(a)*f(x0) < 0):
        b = x0
    if(f(a)*f(x0) > 0):
        a = x0
        
    c = b - a
    x0 = (a + b)/2
    cont = cont + 1
    if (cont >= Ni):
        break

print("\n\nRaíz %f\nInterações: %i\nf(%f) = %f\n\n"%(x0, cont, x0, f(x0)))


