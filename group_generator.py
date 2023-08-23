# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 16:58:41 2023

@author: lcuev
"""
import numpy as np
rand = np.random.random

def inverse(xs):
    ret = np.linalg.inv(xs)
    for row in ret:
        for entry in row:
            entry = round(entry,3)
 
    return ret.asarray()


def det(xs):
    ret = np.linalg.det(xs)
    
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
            [[-1,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,-1]],
            [[0,-1,0,0],[1,0,0,0],[0,0,0,-1],[0,0,1,0]]]




for x in members:
    for y in members:
        z = mult4(x,y)
        if z not in members:
            members += [z]
            
            
for x in members:
    print('representation: ', x, '\n')

