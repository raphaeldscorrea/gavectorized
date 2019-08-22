#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 18:49:44 2019

@author: rodolfodollinger
"""
import sys, os
import unittest 
sys.path.append(os.path.abspath(os.path.join('..', 'src/ga_vectorized')))
import support_functions as sup_f


class TestBinOperators(unittest.TestCase):

        
    def test_single_point_crossover(self):
        parent_1 = [0, 0, 0, 1, 1, 1, 1, 1, 1, 0]
        parent_2 = [1, 1, 0, 1, 0, 1, 0, 0, 0, 1]
        
        childs = sup_f.single_point_crossover(parent_1, parent_2, 0.8, 0.5, 4)
        
        self.assertListEqual(list(childs[0]), [0, 0, 0, 1, 0, 1, 0, 0, 0, 1])
        self.assertListEqual(list(childs[1]), [1, 1, 0, 1, 1, 1, 1, 1, 1, 0])
        
        
    def test_uniform_crossover(self):
        parent_1 = [0, 0, 0, 1, 1, 1, 1, 1, 1, 0]
        parent_2 = [1, 1, 0, 1, 0, 1, 0, 0, 0, 1]
        auxiliary_vector = [1, 1, 0, 1, 0, 0, 0, 1, 1, 0]
        
        childs = sup_f.uniform_crossover(parent_1, parent_2, 0.8, 0.5, auxiliary_vector)
        
        self.assertListEqual(list(childs[0]), [0, 0, 0, 1, 0, 1, 0, 1, 1, 1])
        self.assertListEqual(list(childs[1]), [1, 1, 0, 1, 1, 1, 1, 0, 0, 0])
        
    def test_bit_inversion_mutation(self):
        individual = [0, 0, 0, 1, 1, 1, 1, 1, 1, 0]
        prob_vector = [0.3, 0.55, 0.6, 0.2, 0.8, 0.6, 0.3, 0.4, 0.7, 0.9]
        prob_mutation = 0.5
        
        new_individual = sup_f.bit_inversion_mutation(individual, prob_mutation, prob_vector)
        
        self.assertListEqual(list(new_individual), [1, 0, 0, 0, 1, 1, 0, 0, 1, 0])
    
    
if __name__ == '__main__':
    unittest.main()
    
