# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import numpy as np
#import random


parent_1 = np.random.choice([0, 1], size=(10,), p=[1./3, 2./3])
parent_2 = np.random.choice([0, 1], size=(10,), p=[1./3, 2./3])

### CROSSOVER ###
def single_point_crossover(parent_1, parent_2, prob_crossover, random_value, random_position):
    """
        Single point crossover. Create a new generation based on parents.
        Args:
        parents_1/2 (np): input data
        prob_crossover: indicate the propability of crossover for parents
        random_value: Generate a random probability to crossover
        random_position: Indicate a position point for crossover
        Returns:
        new_generation: generated population
    """
    #random_value =  random_prob # np.random.uniform(0,1,1)
    if(prob_crossover >= random_value):
        #change_position =  random_position # random.randint(1,len(parent_1)-1)
        
        child_1 = np.hstack([parent_1[:random_position],parent_2[random_position:]])
        child_2 = np.hstack([parent_2[:random_position],parent_1[random_position:]])
        
        return(child_1,child_2)
    else:
        return(parent_1, parent_2)
        
        
def uniform_crossover(parent_1, parent_2, prob_crossover, random_value, random_vector):
    """
        Uniform_crossover. Create a new generation based on auxiliary vector.
        Args:
        parents_1/2 (np): input data
        prob_crossover: indicate the propability of crossover for parents
        random_value: Generate a random probability to crossover
        random_vector: Auxiliary vector to crossover
        Returns:
        new_generation: generated population
    """
    #random_value = np.random.uniform(0,1,1)
    if(prob_crossover >= random_value):
        #random_vector = np.random.choice([0, 1], size=(len(parent_1),))
        
        def create_child(p1,p2,rv):
            if(rv>0):
                return(p1)
            else:
                return(p2)
        
        vfunc = np.vectorize(create_child)
        child_1 = vfunc(parent_1,parent_2, random_vector)
        child_2 = vfunc(parent_2,parent_1, random_vector)
        
        return(child_1,child_2)
    else:
        return(parent_1, parent_2)
        

### MUTATION ###
def bit_inversion_mutation(individual, prob_mutation, prob_vector):
    """
        bit_inversion_mutation reproduce a mutation action based on a prob vector.
        Args:
        individual (np): input data
        prob_mutation: indicate the propability of mutation for each element in individual vector.
        prob_vector: Generate a random probability vector to mutation
        Returns:
        new_individual: generated new individual after mutation process
    """
    #random_vector = np.random.uniform(0,1,len(individual))
    
    def mutate_individual(ind, vec_prob, prob_mutation):
        if(vec_prob < prob_mutation):
            return(1-ind)
        else:
            return ind
        
    vfunc = np.vectorize(mutate_individual)
    new_individual = vfunc(individual,prob_vector, prob_mutation)
    
    return(new_individual)
    

### MATING SELECTION ###
def roulette_selection(fitness, num_mating):
    fitness_array = fitness.flatten()
    total_fitness = sum(fitness_array)
    
    sorted_fitness = np.array(sorted(fitness_array, reverse = True))
    sorted_index = np.array(sorted(range(len(fitness_array)),key=fitness_array.__getitem__, reverse = True))
    total_fitness = sum(sorted_fitness)
    
    def set_prob_fitness(sf, tf):
        return(sf/tf)
    
    vfunc = np.vectorize(set_prob_fitness)
    prob_fitness = vfunc(sorted_fitness,total_fitness)
    cum_fitness = np.cumsum(prob_fitness)
    
    prev_fitness = np.append(0,cum_fitness)
    prev_fitness = prev_fitness[:-1]
    
    random_vector = np.random.uniform(0,1,num_mating)
    
    def get_mating(rv):
        return(list(map(lambda x: x>rv, cum_fitness)).index(True))
    
    vfunc2 = np.vectorize(get_mating)
    mating_selected = vfunc2(random_vector)
    
    mating_selected_index = sorted_index[mating_selected,]
    
    return(mating_selected_index[:int(len(mating_selected_index)/2)], mating_selected_index[int(len(mating_selected_index)/2):])
        
        
def generate_offspring(population):
    index_1, index_2 = roulette_selection(population.fitness, len(population.fitness))
    parents_1 = population.solution[index_1,]
    parents_2 = population.solution[index_2,]
    
    children = []
    
    for i in len(parents_1):
        child_1, child_2 = single_point_crossover(parents_1[i,], parents_2[i,], 0.8)
        children.append(child_1)
        children.append(child_2)
        
    return children

    
#population = Solution(np.random.randint(2, size=(20,10)), np.random.randint(10, size=(10,1)), np.arange(0,10))
#pop = population.solution
#fitness = population.fitness
#seq = population.seq
#
#class Solution:
#    def __init__(self, solution, fitness, seq):
#        self.solution = solution
#        self.fitness= fitness
#        self.seq= seq
    