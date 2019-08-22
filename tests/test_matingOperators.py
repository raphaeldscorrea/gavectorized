#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 18:49:44 2019

@author: rodolfodollinger
"""
import sys, os
import unittest 
sys.path.append(os.path.abspath(os.path.join('..', 'src/ga_vectorized')))
import matingOperators as mo
import numpy as np


class TestBinOperators(unittest.TestCase):

        
    def test_roulette_selection(self):
        fitness = np.array([10,11,9,15,9,24,12])
        random_vector = [0.75663808, 0.46919456, 0.96256243]
        
        result = mo.roulette_selection(fitness, 3, random_vector)
        
        self.assertListEqual(list(result[0]), [0])
        self.assertListEqual(list(result[1]), [6,4])
    
    
if __name__ == '__main__':
    unittest.main()
 
    
