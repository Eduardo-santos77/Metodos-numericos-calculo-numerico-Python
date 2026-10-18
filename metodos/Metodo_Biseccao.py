# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 17:26:10 2022

@author: Carlos Eduardo Almeida Santos
"""

# Método de Bisecção

import math as mm

# Definir um intervalo [a,b] e um erro e
a = int(input('Defina o inicio do intervalo da função:' ))
b = int(input('Deifina o final do intervalo da função:' ))
e =  float(input('Defina qual o valor do erro que se deseja verificar:'))

# Difinir uma função
def f(x):
    return x**3-2*x - 1

# Teste do teorema de Bolzano
if f(a)*f(b) < 0:
    while (mm.fabs(b-a)/2 > e):
        xi =(a+b)/2
        if f(xi) == 0:
            print('A raiz da função é:' , xi)
            break

        else:
            if f(a)*f(xi) < 0:
                b = xi
            else:
                a = xi
    print('Valor da Raiz é:' , xi)
    
else:
    print('Não há Raiz nesse intervalo!')