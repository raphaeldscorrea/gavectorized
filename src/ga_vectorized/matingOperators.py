# -*- coding: utf-8 -*-

import numpy as np
import time

def roulette_selection(fitness, num_mating, random_vector):
    total_fitness = sum(fitness)
    
    sorted_fitness = np.array(sorted(fitness, reverse = True))
    sorted_index = np.array(sorted(range(len(fitness)),key=fitness.__getitem__, reverse = True))
    
    def set_prob_fitness(sf, tf):
        return(sf/tf)
    
    vfunc = np.vectorize(set_prob_fitness)
    prob_fitness = vfunc(sorted_fitness,total_fitness)
    cum_fitness = np.cumsum(prob_fitness)
    
    prev_fitness = np.append(0,cum_fitness)
    prev_fitness = prev_fitness[:-1]
    
    def get_mating(rv):
        return((np.abs(cum_fitness - rv)).argmin())
    
    vfunc2 = np.vectorize(get_mating)
    mating_selected = vfunc2(random_vector)
    
    mating_selected_index = sorted_index[mating_selected,]
    
    return(mating_selected_index[:int(len(mating_selected_index)/2)], mating_selected_index[int(len(mating_selected_index)/2):])
    

def ranking_selection(fitness, num_mating, s):
    fitness_array = fitness.flatten()
    sorted_index = np.array(sorted(range(len(fitness_array)),key=fitness_array.__getitem__, reverse = False))
    
    ranking = np.arange(len(fitness))
    mi = len(fitness)
    
    def get_rank_prob(r):
        prob = (2-s)/mi + 2*r*(s-1)/(mi*(mi-1))
        return(prob)
        
    vfunc = np.vectorize(get_rank_prob)
    prob_fitness = vfunc(ranking)
    
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
    