# -*- coding: utf-8 -*-
#import sys, os
#sys.path.append(os.path.abspath(os.path.join('..', 'ga_vectorized')))
from ga_vectorized import binOperators, survivorOperators, matingOperators
import numpy as np

def getFitness(individual):
    x = 2*individual[0]+4*individual[1]+5*individual[2]-6*individual[3]+4*individual[4]
    y = 2*individual[5]+4*individual[6]-3*individual[7]-2*individual[8]+4*individual[9]
    z = -10*individual[4]-12*individual[9]+5*individual[7]
    
    return(x+y+z)

def generate_offspring(population, fitness, func_parents_selection, func_crossover, prob_crossover):
    index_1, index_2 = func_parents_selection(fitness, len(population))
    
    def get_childs(p1,p2, pc):
        ch1, ch2 = func_crossover(population[p1,], population[p2,], pc)
        return(ch1, ch2)
    
    prob_crossover_vector = np.full((len(population),),prob_crossover)
    children = np.array([get_childs(x,y,z) for x,y,z in zip(index_1,index_2, prob_crossover_vector)]).reshape((len(population),len(population[0])))
    
    return children

def next_generation(population, prob_crossover, prob_mutation):
    fitness = np.array([getFitness(x) for x in population]).reshape((len(population),))
    children = generate_offspring(population, fitness, matingOperators.roulette_selection, binOperators.single_point_crossover, prob_crossover)
    prob_mutation_vector = np.full((len(population),),prob_mutation)
    children_mutated = np.array([binOperators.bit_inversion_mutation(x,y) for x,y in zip(children,prob_mutation_vector)]).reshape((len(population),len(population[0])))
    fitness_children = np.array([getFitness(x) for x in children_mutated]).reshape((len(population),))
    new_generation = survivorOperators.fitness_based_replacement(fitness, fitness_children, population, children_mutated)

    return(new_generation)
    
def genetic_algorithm(population, generations):
    
    for i in range(0, generations):
        population.Genes = next_generation(population.Genes, 0.8, 0.05)
        
    return(population.Genes)

class Chromosome:
    def __init__(self, genes, fitness):
        self.Genes = genes
        self.Fitness = fitness


### TEST ####
        
#population = Chromosome(np.random.randint(2, size=(20,10)), np.random.randint(10, size=(20,1)))    
#solution = genetic_algorithm(population,100)