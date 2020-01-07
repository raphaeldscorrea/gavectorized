# -*- coding: utf-8 -*-

import numpy as np

class Fitness():
    def __init__(self):
        self.distance_matrix = distance_matrix = np.random.random((80, 80))
        
    def calculate(self, individual):
        shift_individual = np.hstack([individual[1:len(individual)], individual[0]]) 
        total_distance = sum(map(lambda x,y: self.distance_matrix[x][y], individual, shift_individual))
        return(-total_distance)
