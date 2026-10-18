"""
@author: Carlos Eduardo

Método de eliminação de Gauss
"""
def elination(A,b):
    n = len(b)    
    
    #Cálculo de pivôs
    for k in list(range(1, n, 1)):
        #Cálculo dos multiplicadores
        for i in list(range(k+1, n+1, 1)):
            m = A[i-1][k-1]/A[k-1][k-1]
            A[i-1][k-1] = 0
            b[i-1] = b[i-1] - m*b[k-1]
            #Atualizar demais valores
            for j in list(range(k+1, n+1, 1)):
                A[i-1][j-1] = A[i-1][j-1]-m*A[k-1][j-1]        
    return A, b

# Resolve o sistema triangular superior
def solverUpperTriangular(U,b):
    n = len(b)
    x = [0]*n
    x[n-1] = b[n-1]/U[n-1][n-1]
    
    for i in list(range(n-1, 0, -1)):
        s = 0
        for j in list(range(i+1, n+1, 1)):
            s = s + U[i-1][j-1]*x[j-1]
            
        x[i-1] = (b[i-1]-s)/(U[i-1][i-1])
        
    return x


Ai = [[0.1, 3.4, 2.2],
      [8.5, 22, 10],
      [1, 20, 12]]
bi = [10.5, 94.5, 61]

#Transformando em sistema equivalente
U, b = elination(Ai, bi)
print("U =",U)
print("b = ",b)
x = solverUpperTriangular(U,b)
print("x =", x)

        
        

