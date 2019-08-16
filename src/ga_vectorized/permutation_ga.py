#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 09:44:32 2019

@author: dollinger
"""

import numpy as np
import copy

def crossover_permutation(parent_1, parent_2):
    idx_1 = []
    n = 1
    idx = 0
    parent_1 = np.array(parent_1)
    parent_2 = np.array(parent_2)
    indexes = np.array(range(len(parent_1)))
        
    
    def find_element(vector, x):
        idx = np.where(np.array(vector) == x)[0][0]
        return(idx)
    
    def cross_recursion(parent_1, parent_2, n, idx, idx_1):
        if find_element(parent_2, parent_1[idx]) == 0:
            idx_1.append(0)
            return(idx_1)
        idx = find_element(parent_2, parent_1[idx])
        idx_1.append(idx)
        return(cross_recursion(parent_1, parent_2, n, idx, idx_1))

    changes = np.delete(indexes, cross_recursion(parent_1, parent_2, n, idx, idx_1))
    
    child_1 = copy.copy(parent_1)
    child_2 = copy.copy(parent_2)
    child_1[changes] = copy.copy(parent_2[changes])
    child_2[changes] = copy.copy(parent_1[changes])
    
    return(child_1, child_2)
        

#father1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 11, 15]
#father2 = [9, 3, 7, 8, 2, 6, 5, 1, 4, 15, 10, 11, 12]
#
#import time
#
#start = time.time()
#i = 0
#
#while i <= 10000:
#    saida = crossover_permutation(father1, father2)
#    i += 1
#
#end = time.time()
#
#
#print(end - start)
