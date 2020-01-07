# -*- coding: utf-8 -*-
#import sys, os
#sys.path.append(os.path.abspath(os.path.join('..', 'ga_vectorized')))
from ga_vectorized.ga import GA
from ga_vectorized.fitness import Fitness
import numpy as np

  
if __name__ == '__main__':
    population = np.zeros((800, 80))                                                  
    for i in range(0, len(population)):
        population[i,:] = np.random.permutation(np.arange(population.shape[1]))[:population.shape[1]]
    
    population = population.astype(int)
    
    example_4_fitness = Fitness()
    ga_class = GA("perm")
    solution = ga_class.generations(population, 20, example_4_fitness)    

        