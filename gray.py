# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 04:04:13 2023

@author: lcuev
"""
import numpy as np
from group_generator import det
import matplotlib.pyplot as plt
from hilbertcurve.hilbertcurve import HilbertCurve

plt.rcParams["figure.figsize"] = [7.00, 7.00]
plt.rcParams["figure.autolayout"] = True

def gray_to_binary(n):
    """Convert Gray codeword to binary and return it."""
 
    mask = n
    while mask != 0:
        mask >>= 1
        n ^= mask
 
    # bin(n) returns n's binary representation with a '0b' prefixed
    # the slice operation is to remove the prefix
    return bin(n)

def binary_to_gray(n):
    """Convert Binary to Gray codeword and return it."""
    n = int(n, 2) # convert to int
    n ^= (n >> 1)
 
    # bin(n) returns n's binary representation with a '0b' prefixed
    # the slice operation is to remove the prefix
    return bin(n)[2:]
        



N = 4
BIT = N ** 2
COMB = 2 ** BIT

n = 2
p = int(BIT / n)
side_length = 2**p
hilbert_curve = HilbertCurve(p, n)


grays = []
image_cells = [[0 for i in range(side_length * 4)] for j in range(side_length * 4)]


for n in range(COMB):
    binary_string = bin(n)
    grays += [binary_to_gray(binary_string)]
    



for n,gray in enumerate(grays):
    xs = [[0 for i in range(4)] for j in range(4)]
    

    for i in range(N):
        for j in range(N):
            pos = N * i + j
            if pos < len(gray):
                xs[i][j] = int(gray[pos])
            else:
                xs[i][j] = 0
                
    x,y = hilbert_curve.point_from_distance(n)
    color = det(xs)
    
    for i in range(4):
        for j in range(4):
            image_cells[4 * x + i][4 * y + j] = color


plt.imsave('hilbert_curve.png',image_cells, cmap = 'Accent', dpi = 300)


    
    

    

                
    
        
    


