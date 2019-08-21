# -*- coding: utf-8 -*-
import numpy as np
import random
import copy

#### MUTATION ####

def swap_mutation(offspring):
    lb = random.randint(0,len(offspring))
    ub = random.randint(lb,len(offspring))
    
    new_offspring = offspring.copy()
    new_offspring[lb] = offspring[ub]
    new_offspring[ub] = offspring[lb]
    
    return(new_offspring)
    
def insert_mutation(offspring):
    pos_1 = random.randint(0,len(offspring))
    pos_2 = random.randint(pos_1,len(offspring))
    
    new_offspring = np.hstack([offspring[:pos_1], offspring[pos_2], offspring[pos_1:pos_2], offspring[pos_2+1:len(offspring)]])
    
    return(new_offspring)
    
def scramble_mutation(offspring):
    lb = random.randint(0,len(offspring))
    ub = random.randint(lb,len(offspring))
    shuffled_positions = offspring[lb:ub]
    random.shuffle(shuffled_positions)
    
    new_offspring = np.hstack([offspring[:lb], shuffled_positions[lb:ub], offspring[ub:len(offspring)]])
    
    return(new_offspring)
    
def inversion_mutation(offspring):
    lb = random.randint(0,len(offspring))
    ub = random.randint(lb,len(offspring))
    positions_to_invert = offspring[lb:ub]
    inverted_positions = positions_to_invert[::-1]
    
    new_offspring = np.hstack([offspring[:lb], inverted_positions, offspring[ub:len(offspring)]])
    
    return(new_offspring)
    
def displacement_mutation(offspring):
    lb = random.randint(0,len(offspring))
    ub = random.randint(lb,len(offspring))
    position = random.randint(0,lb)
    
    new_offspring = np.hstack([offspring[:position], offspring[lb:ub], offspring[position:lb], offspring[ub:len(offspring)]])
    
    return(new_offspring)
    
#### CROSSOVER ####

def pmx(parent_1, parent_2):
    lb = random.randint(0,len(parent_1))
    ub = random.randint(lb,len(parent_1))
    
    #offspring 1
    part_1_offspring_1 = parent_1[lb:ub]
    part_2_offspring_1 = np.hstack([parent_2[:lb], parent_2[ub:len(parent_2)]])
    repeated_elements = np.isin(part_2_offspring_1, part_1_offspring_1)
    
    part_1_offspring_2 = parent_2[lb:ub]
    repeat_elements_parts_1 = np.isin(part_1_offspring_2, part_1_offspring_1, invert=True)
    repeated_values_part_1 = part_1_offspring_2[repeat_elements_parts_1]
    
    part_2_offspring_1_copy = part_2_offspring_1.copy()
    np.place(part_2_offspring_1, repeated_elements, repeated_values_part_1)
    
    final_value = np.hstack([part_2_offspring_1[:lb], part_1_offspring_1,part_2_offspring_1[lb:len(part_2_offspring_1)]])
    
    return(final_value)
    
def order_crossover(parent_1, parent_2):
    lb = random.randint(0,len(parent_1))
    ub = random.randint(lb,len(parent_1))
    
    part_1_offspring_1 = parent_1[lb:ub]
    
    parent_2_reshaped = np.hstack([parent_2[ub:len(parent_2)], parent_2[:ub]])
    index_repeated_elements = np.isin(parent_2_reshaped, part_1_offspring_1, invert=True)
    repeated_values_part_1 = parent_2_reshaped[index_repeated_elements]
    
    new_offspring = np.hstack([repeated_values_part_1[len(parent_2)-ub:len(repeated_values_part_1)], part_1_offspring_1,repeated_values_part_1[:len(parent_2)-ub]])
    
    return(new_offspring)
    
def cycle_crossover(parent_1, parent_2):
    idx_1 = []
    n = 1
    idx = 0
    parent_1 = np.array(parent_1)
    parent_2 = np.array(parent_2)
    indexes = np.array(range(len(parent_1)))
        
    
    def find_element(vector, x):
        idx = np.where(np.array(vector) == x)[0][0]
        return(idx)
    
    def cross_recursion(parent_1, parent_2, n, idx, idx_1):
        if find_element(parent_2, parent_1[idx]) == 0:
            idx_1.append(0)
            return(idx_1)
        idx = find_element(parent_2, parent_1[idx])
        idx_1.append(idx)
        return(cross_recursion(parent_1, parent_2, n, idx, idx_1))

    changes = np.delete(indexes, cross_recursion(parent_1, parent_2, n, idx, idx_1))
    
    child_1 = copy.copy(parent_1)
    child_2 = copy.copy(parent_2)
    child_1[changes] = copy.copy(parent_2[changes])
    child_2[changes] = copy.copy(parent_1[changes])
    
    return(child_1, child_2)