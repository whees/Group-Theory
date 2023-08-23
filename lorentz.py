# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 17:37:58 2023

@author: lcuev
"""
import numpy as np
import matplotlib.pyplot as plt

shape = np.shape



def fact(n):
    if n == 0:
        return 1
    else:
        ret = 1
        for i in range(2,n+1):
            ret *= i
        return ret

def mult(A,B):
    n_side = int(shape(A)[0])
    ret = [[0 for i in range(n_side)] for j in range(n_side)]
    for u in range(n_side):
        for v in range(n_side):
            for i in range(n_side):
                ret[u][v] += A[u][i] * B[i][v]
    
    return ret

def act(A,b):
    n_side = int(shape(A)[0])
    ret = [0 for i in range(n_side)]
    for u in range(n_side):
        for v in range(n_side):
            ret[u] += A[u][v] * b[v]
            
    return ret


def exp(A):
    n_side = int(shape(A)[0])
    n_term = 10
    ret = [[0 for i in range(n_side)] for j in range(n_side)]
    dummy = [[int(i == j) for i in range(n_side)] for j in range(n_side)]

    
    for i in range(n_term):
        i_fact = fact(i)
        for u in range(n_side):
            for v in range(n_side):
                ret[u][v] += 1/i_fact * dummy[u][v]
        
        dummy = mult(dummy,A)
    
    
    
    
    return ret


plt.plot([-2,2],[-2,2],c = 'red')     
plt.plot([-2,2],[2,-2],c = 'lime') 

max_x = 2
max_t = 2
n_x = 10
n_t = n_x
xs = [(2 * i / (n_x - 1) - 1) * max_x for i in range(n_x)]
ts = [(2 * i / (n_t - 1) - 1) * max_t for i in range(n_t)]


for x in xs:
    for t in ts:
        b = [t,x]
        
         
        dphi = 0.01
        A = [[0, dphi],[dphi,0]]
        
        
        bp = act(exp(A),b)
        
        
        dx = bp[1] - b[1]
        dt = bp[0] - b[0]
    
        
        plt.quiver(x,t,dx,dt)
    

plt.xlabel('space')
plt.ylabel('time')
        
   
    


