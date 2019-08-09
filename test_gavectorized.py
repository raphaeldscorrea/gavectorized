#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 18:49:44 2019

@author: rodolfodollinger
"""

import unittest 
import support_functions as sup_f



class TestGavectorize(unittest.TestCase):

        
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
    
    
if __name__ == '__main__':
    unittest.main()
    
