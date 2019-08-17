# -*- coding: utf-8 -*-

import numpy as np
import random

class binOperators():
    
    #### MUTATION ####
    
    def bit_inversion_mutation(self, individual, prob_mutation):
        self.random_vector = np.random.uniform(0,1,len(individual))
        
        def mutate_individual(ind, vec_prob, prob_mutation):
            if(vec_prob < prob_mutation):
                return(1-ind)
            else:
                return ind
            
        self.vfunc = np.vectorize(mutate_individual)
        self.new_individual = self.vfunc(individual,self.random_vector, prob_mutation)
        
        return(self.new_individual)
        
    #### CROSSOVER ####
        
    def single_point_crossover(self, parent_1, parent_2, prob_crossover):
        self.random_value = np.random.uniform(0,1,1)
        if(prob_crossover >= self.random_value):
            self.change_position = random.randint(1,len(parent_1)-1)
            
            self.child_1 = np.hstack([parent_1[:self.change_position],parent_2[self.change_position:]])
            self.child_2 = np.hstack([parent_2[:self.change_position],parent_1[self.change_position:]])
            
            return(self.child_1,self.child_2)
        else:
            return(self.parent_1, self.parent_2)
            
    
    def uniform_crossover(self, parent_1, parent_2, prob_crossover):
        self.random_value = np.random.uniform(0,1,1)
        if(prob_crossover >= self.random_value):
            self.random_vector = np.random.choice([0, 1], size=(len(parent_1),))
            
            def create_child(p1,p2,rv):
                if(rv>0):
                    return(p1)
                else:
                    return(p2)
            
            self.vfunc = np.vectorize(create_child)
            self.child_1 = self.vfunc(parent_1,parent_2, self.random_vector)
            self.child_2 = self.vfunc(parent_2,parent_1, self.random_vector)
            
            return(self.child_1,self.child_2)
        else:
            return(self.parent_1, self.parent_2)