# -*- coding: utf-8 -*-
#import sys, os
#sys.path.append(os.path.abspath(os.path.join('..', 'ga_vectorized')))
from ga_vectorized import permOperators, survivorOperators, matingOperators
import numpy as np
import random
import multiprocessing
#from numba import jit
import time

#def get_distances(distance_matrix, x,y):
#    return(distance_matrix[x][y])

def generate_offspring(population, fitness, func_parents_selection, func_crossover, prob_crossover):
    start_off = time.time()
    index_1, index_2 = matingOperators.roulette_selection(fitness, len(population), np.random.uniform(0,1,len(population)))
    roullete_time = time.time()
    
    def get_childs(p1,p2, pc):
        ch1,ch2 = func_crossover(population[p1,], population[p2,])
        return(ch1, ch2)
    
    prob_crossover_vector = np.full((len(population),),prob_crossover)
    children = np.array([get_childs(x,y,z) for x,y,z in zip(index_1,index_2, prob_crossover_vector)]).reshape((len(population),len(population[0])))
    np_array_time = time.time()
    
    #print(roullete_time-start_off)
    #print(np_array_time-roullete_time)
    
    return children

#@jit()
def next_generation(population, prob_crossover, prob_mutation):
    start = time.time()
    fitness = np.array([getFitness(x) for x in population]).reshape((len(population),))

    #p = multiprocessing.Pool(4)
    #population_list = population.tolist()
    #fitness = np.array(p.map(getFitness, population))
    #p.close()
    
    fitness_time = time.time()
    children = generate_offspring(population, fitness, matingOperators.roulette_selection, permOperators.order_crossover, prob_crossover)
    offspring_time = time.time()
    prob_mutation_vector = np.full((len(population),),prob_mutation)
    children_mutated = np.array([permOperators.displacement_mutation(x,y) for x,y in zip(children,prob_mutation_vector)]).reshape((len(population),len(population[0])))
    mutation_time = time.time()
    fitness_children = np.array([getFitness(x) for x in children_mutated]).reshape((len(population),))
    fitness_children_time = time.time()
    new_generation = survivorOperators.fitness_based_replacement(fitness, fitness_children, population, children_mutated)
    end = time.time()
    print(fitness_time-start)
    #print("offspring:")
    print(offspring_time-fitness_time)
    print(mutation_time-offspring_time)
    print(fitness_children_time-mutation_time)
    print(end-fitness_children_time)
    print(end-start)
    
    return(new_generation)
    
def genetic_algorithm(population, generations):
    #distance_matrix = np.random.random((80, 80))
    for i in range(0, generations):
        print(i)
        population.Genes = next_generation(population.Genes, 0.8, 0.05)
        
    return(population.Genes)

class Chromosome:
    def __init__(self, genes, fitness):
        self.Genes = genes
        self.Fitness = fitness


### TEST ####

if __name__ == '__main__':
    population = Chromosome(np.zeros((800, 80)), np.random.randint(10, size=(800,1)))    
    for i in range(0, len(population.Genes)):
        population.Genes[i,:] = np.random.permutation(np.arange(population.Genes.shape[1]))[:population.Genes.shape[1]]
    
    population.Genes = population.Genes.astype(int)
    distance_matrix = np.random.random((80, 80))
    
    def getFitness(individual):
        aux_individual = np.hstack([individual[1:len(individual)], individual[0]])
        
        def get_distances(x,y):
            return(distance_matrix[x][y])
            
        vfunc = np.vectorize(get_distances)
        total_distance = sum(vfunc(individual,aux_individual))
        
        return(-total_distance)

    solution = genetic_algorithm(population,20)
    
    
    
    