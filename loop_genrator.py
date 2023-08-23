# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 02:13:40 2023

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
BLOCK_SIZE = int(COMB / 4)



n = 2
p = int((BIT - 2) / n)
side_length = int((COMB) ** 0.5)
hilbert_curve = HilbertCurve(p, n)


grays = []
image_cells = [[0 for i in range(side_length * 4)] for j in range(side_length * 4)]
image2_cells = [[0 for i in range(side_length * 4)] for j in range(side_length * 4)]


for n in range(COMB):
    binary_string = bin(n)
    grays += [binary_to_gray(binary_string)]


blocks = []

for i in range(4):
    block = []
    for n in range(BLOCK_SIZE):
        block += [grays[i * BLOCK_SIZE + n]]
    blocks += [block]
  
        

counter = 0

for b,block in enumerate(blocks):
    for g,gray in enumerate(block):
        xs = [[0 for i in range(4)] for j in range(4)]
        
    
        for i in range(N):
            for j in range(N):
                pos = N * i + j
                if pos < len(gray) - 1:
                    xs[i][j] = int(gray[pos])
                else:
                    xs[i][j] = 0
                    
        color = det(xs)
                    
        local_x,local_y = hilbert_curve.point_from_distance(g)
        global_x,global_y = 0,0
        
        if b == 0:
            global_x = local_x
            global_y = side_length / 2 - local_y
        elif b == 1:
            global_x = local_x + side_length / 2
            global_y = side_length / 2 - local_y
        elif b == 2:
            global_x =  side_length - local_x - 1
            global_y = local_y + side_length / 2
        elif b == 3:
            global_x = side_length / 2 - local_x -1
            global_y = local_y + side_length / 2
                
        
        for i in range(4):
            for j in range(4):
                image_cells[int(global_x * 4 + i)][int(global_y * 4 + j)] = color
                image2_cells[int(global_x * 4 + i)][int(global_y * 4 + j)] = counter
                
                
        counter += 1


plt.imsave('hilbert_curve.png',image_cells, cmap = 'twilight', dpi = 300)
plt.imsave('hilbert_cirve2.png',image2_cells, cmap = 'twilight', dpi = 300)



    
    

    

                
    
        
    


