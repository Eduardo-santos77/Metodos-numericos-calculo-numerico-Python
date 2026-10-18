# -*- coding: utf-8 -*-
"""

@author: Carlos Eduardo 


Método de interpolação de Newton
"""

import numpy as np
import matplotlib.pyplot as plt

def itpNewton(x, y, xi):
    n = len(x)
    fdd = [[None for x in range(n)] for x in range(n)]
    
    for i in range(n):
        fdd[i][0] = y[i]
        
    for j in range(1, n):
        for i in range(n-j):
            fdd[i][j] = (fdd[i+1][j-1] - fdd[i][j-1])/(x[i+j]- x[i])
    
    xterm = 1
    yint = fdd[0][0]
    for order in range(1, n):
        xterm = xterm*(xi - x[order -1])
        yint = yint + fdd[0][order]*xterm
    return yint

x = [-1, 0, 2]
y = [4, 1, -1]
xp = 0.5
yp = itpNewton(x, y, xp)
t = np.arange(-1.0, 2.0, 0.1)
yt = []
for i in t:
    yt.append(itpNewton(x, y, i))
plt.plot(t, yt, 'b-')
plt.plot(x, y, 'ro')
plt.plot(xp, yp, 'g*')
plt.grid()
plt.show()
    



