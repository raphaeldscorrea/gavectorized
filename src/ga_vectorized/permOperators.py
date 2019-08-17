# -*- coding: utf-8 -*-
import numpy as np
import random

class permOperators():
    
    #### MUTATION ####
    
    def swap_mutation(self, offspring):
        self.lb = random.randint(0,len(offspring))
        self.ub = random.randint(self.lb,len(offspring))
        
        self.new_offspring = offspring.copy()
        self.new_offspring[self.lb] = offspring[self.ub]
        self.new_offspring[self.ub] = offspring[self.lb]
        
        return(self.new_offspring)
        
    def insert_mutation(self, offspring):
        self.pos_1 = random.randint(0,len(offspring))
        self.pos_2 = random.randint(self.pos_1,len(offspring))
        
        self.new_offspring = np.hstack([offspring[:self.pos_1], offspring[self.pos_2], offspring[self.pos_1:self.pos_2], offspring[self.pos_2+1:len(offspring)]])
        
        return(self.new_offspring)
        
    def scramble_mutation(self, offspring):
        self.lb = random.randint(0,len(offspring))
        self.ub = random.randint(self.lb,len(offspring))
        self.shuffled_positions = offspring[self.lb:self.ub]
        random.shuffle(self.shuffled_positions)
        
        self.new_offspring = np.hstack([offspring[:self.lb], self.shuffled_positions[self.lb:self.ub], offspring[self.ub:len(offspring)]])
        
        return(self.new_offspring)
        
    def inversion_mutation(self, offspring):
        self.lb = random.randint(0,len(offspring))
        self.ub = random.randint(self.lb,len(offspring))
        self.positions_to_invert = offspring[self.lb:self.ub]
        self.inverted_positions = self.positions_to_invert[::-1]
        
        self.new_offspring = np.hstack([offspring[:self.lb], self.inverted_positions, offspring[self.ub:len(offspring)]])
        
        return(self.new_offspring)
        
    def displacement_mutation(self, offspring):
        self.lb = random.randint(0,len(offspring))
        self.ub = random.randint(self.lb,len(offspring))
        self.position = random.randint(0,self.lb)
        
        self.new_offspring = np.hstack([offspring[:self.position], offspring[self.lb:self.ub], offspring[self.position:self.lb], offspring[self.ub:len(offspring)]])
        
        return(self.new_offspring)
        
    
    #### CROSSOVER ####
    
    def pmx(self, parent_1, parent_2):
        self.lb = random.randint(0,len(parent_1))
        self.ub = random.randint(self.lb,len(parent_1))
        
        #offspring 1
        self.part_1_offspring_1 = parent_1[self.lb:self.ub]
        self.part_2_offspring_1 = np.hstack([parent_2[:self.lb], parent_2[self.ub:len(parent_2)]])
        self.repeated_elements = np.isin(self.part_2_offspring_1, self.part_1_offspring_1)
        
        self.part_1_offspring_2 = parent_2[self.lb:self.ub]
        self.repeat_elements_parts_1 = np.isin(self.part_1_offspring_2, self.part_1_offspring_1, invert=True)
        self.repeated_values_part_1 = self.part_1_offspring_2[self.repeat_elements_parts_1]
        
        self.part_2_offspring_1_copy = self.part_2_offspring_1.copy()
        np.place(self.part_2_offspring_1, self.repeated_elements, self.repeated_values_part_1)
        
        self.final_value = np.hstack([self.part_2_offspring_1[:self.lb], self.part_1_offspring_1,self.part_2_offspring_1[self.lb:len(self.part_2_offspring_1)]])
        
        return(self.final_value)
        
    def order_crossover(self, parent_1, parent_2):
        self.lb = random.randint(0,len(parent_1))
        self.ub = random.randint(self.lb,len(parent_1))
        
        self.part_1_offspring_1 = parent_1[self.lb:self.ub]
        
        self.parent_2_reshaped = np.hstack([parent_2[self.ub:len(parent_2)], parent_2[:self.ub]])
        self.index_repeated_elements = np.isin(self.parent_2_reshaped, self.part_1_offspring_1, invert=True)
        self.repeated_values_part_1 = self.parent_2_reshaped[self.index_repeated_elements]
        
        self.new_offspring = np.hstack([self.repeated_values_part_1[len(parent_2)-self.ub:len(self.repeated_values_part_1)], self.part_1_offspring_1,self.repeated_values_part_1[:len(parent_2)-self.ub]])
        
        return(self.new_offspring)
        
    