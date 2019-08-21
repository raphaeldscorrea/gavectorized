# -*- coding: utf-8 -*-
import numpy as np
from math import ceil,floor

def age_based_replacement(fitness_parents, fitness_children, parents, children, percentage_replacement):
    num_individuals_to_replace = ceil(len(fitness_parents)*percentage_replacement)
    num_individuals_to_keep = len(fitness_parents)-num_individuals_to_replace
    fitness_parents_array = fitness_parents.flatten()
    fitness_children_array = fitness_children.flatten()
    sorted_index_parents = np.array(sorted(range(len(fitness_parents_array)),key=fitness_parents_array.__getitem__, reverse = True))
    sorted_index_children = np.array(sorted(range(len(fitness_children_array)),key=fitness_children_array.__getitem__, reverse = True))
    
    keeped_children = sorted_index_children[0:num_individuals_to_replace,]
    children_selected = children[keeped_children,]
    keeped_parents = sorted_index_parents[0:num_individuals_to_keep,]
    parents_selected = parents[keeped_parents,]
    
    new_generation = np.append(children_selected,parents_selected).reshape((len(parents),len(parents[0])))
    
    return(new_generation)
    
def fitness_based_replacement(fitness_parents, fitness_children, parents, children):
    fitness_parents_array = fitness_parents.flatten()
    fitness_children_array = fitness_children.flatten()
    total_fitness = np.append(fitness_parents_array,fitness_children_array)
    total_population = np.append(parents,children).reshape(((len(parents)+len(parents)),len(children[0])))
    
    sorted_index = np.array(sorted(range(len(total_fitness)),key=total_fitness.__getitem__, reverse = True))
    selected_individuals = sorted_index[0:len(parents),]
    
    new_generation = total_population[selected_individuals,]
    
    return(new_generation)