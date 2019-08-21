# -*- coding: utf-8 -*-

import numpy as np
import random

#### MUTATION ####

def bit_inversion_mutation(individual, prob_mutation):
    random_vector = np.random.uniform(0,1,len(individual))
    
    def mutate_individual(ind, vec_prob, prob_mutation):
        if(vec_prob < prob_mutation):
            return(1-ind)
        else:
            return ind
        
    vfunc = np.vectorize(mutate_individual)
    new_individual = vfunc(individual,random_vector, prob_mutation)
    
    return(new_individual)
    
#### CROSSOVER ####
    
def single_point_crossover(parent_1, parent_2, prob_crossover):
    random_value = np.random.uniform(0,1,1)
    if(prob_crossover >= random_value):
        change_position = random.randint(1,len(parent_1)-1)
        
        child_1 = np.hstack([parent_1[:change_position],parent_2[change_position:]])
        child_2 = np.hstack([parent_2[:change_position],parent_1[change_position:]])
        
        return(child_1,child_2)
    else:
        return(parent_1, parent_2)
        

def uniform_crossover(parent_1, parent_2, prob_crossover):
    random_value = np.random.uniform(0,1,1)
    if(prob_crossover >= random_value):
        random_vector = np.random.choice([0, 1], size=(len(parent_1),))
        
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