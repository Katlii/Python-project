'''
Given N points in the polynomial with coordinates (x_{1},y_{1}),....,(x_{N},y_{N}).
They are given in the input on N lines, with x_i and y_i separated by a space on each line.
Find the polynomial y=a_{N-1} * x^(N-1)+...+a_{0} * x^0.
that passes through these points.
List its coefficients in order from a_{0} a to a_{N-1}, each on a separate line.
This polynomial is uniquely determined; a small numerical error in the coefficients is allowed
'''


import numpy as np
import math
a=[]
b=[]
import sys
for line in sys.stdin:
    cisla = line.split()
    a.append(cisla[0])
    b.append(cisla[1])
n=len(a)  
A=np.zeros((n,n))
B=np.zeros((n, 1))
for j in range (n):
    for i in range(n):
        A[j][i]=int(a[j])**i
for j in range (n):
        B[j][0]=int(b[j])    

x=np.linalg.solve(A, B)
for i in range(n):
    print(x[i][0])
