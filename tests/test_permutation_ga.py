#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 09:40:06 2019

@author: dollinger
"""
import sys, os
import  unittest
sys.path.append(os.path.abspath(os.path.join('..', 'src/ga_vectorized')))
from permutation_ga import crossover_permutation

# Try to implement crossover operator for permutation problem

class Test_permutation_crossover(unittest.TestCase):
    
    
    def test_crossover(self):
        
        father1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        father2 = [9, 3, 7, 8, 2, 6, 5, 1, 4]
        
        child = crossover_permutation(father1, father2) 
        
        self.assertListEqual(list(child[0]), [1, 3, 7, 4, 2, 6, 5, 8, 9])
        self.assertListEqual(list(child[1]), [9, 2, 3, 8, 5, 6, 7, 1, 4])

if __name__ == '__main__':
    unittest.main()


