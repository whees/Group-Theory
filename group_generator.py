# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 16:58:41 2023

@author: lcuev
"""
import numpy as np
rand = np.random.random

def flip():
    ret = int(rand()*2)
    
    return ret

def inverse4(xs):
    ret = [[0 for i in range(4)] for j in range(4)]
    D = det4(xs)
	
    for u in range(4):
        for v in range(4):
            sub_xs = [[0 for i in range(3)] for j in range(3)]
            
            for i in range(3):
                for j in range(3):
                    sub_xs[i][j] = xs[(u + i + 1) % 4][(v + j + 1) % 4];
            
            ret[v][u] = round(det3(sub_xs) / D * -1 ** (int(u != v)),3)
            
    return ret
    

def det2(xs):
    ret = xs[0][0] * xs[1][1] - xs[0][1] * xs[1][0]
    
    return round(ret,3)

def det3(xs):
    ret = 0
    
    for i in range(3):
        sub_xs = [[0 for i in range(2)] for j in range(2)]
        
        for j in range(2):
            for k in range(2):
                sub_xs[j][k] = xs[(i + j + 1) % 3][k + 1]
        
        ret += xs[i][0] * det2(sub_xs)
    
    return round(ret,3)  

def det4(xs):
    ret = 0
    
    for i in range(4):
        sub_xs = [[0 for i in range(3)] for j in range(3)]
        
        for j in range(3):
            for k in range(3):
                sub_xs[j][k] = xs[(i + j + 1) % 4][(k + 1)]
                
        ret += (-1) ** i * xs[i][0] * det3(sub_xs)
        
    return round(ret,3)

def mult4(x,y):
    ret = [[0 for i in range(4)] for j in range(4)]
    
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ret[i][j] += x[i][k] * y[k][j]
            ret[i][j] = round(ret[i][j],3)
    
    return ret

members = [[[int(i == j) for i in range(4)] for j in range(4)],
           [[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]],
            [[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]],
            [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]]




for x in members:
    for y in members:
        z = mult4(x,y)
        if z not in members:
            members += [z]
            print(len(members))
            
            
for x in members:
    print('representation: ', x, '\n')

