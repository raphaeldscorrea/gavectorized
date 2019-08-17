# -*- coding: utf-8 -*-
import numpy as np
from math import ceil,floor

class survivorOperators():
    
    def age_based_replacement(self, fitness_parents, fitness_children, parents, children, percentage_replacement):
        self.num_individuals_to_replace = ceil(len(fitness_parents)*percentage_replacement)
        self.num_individuals_to_keep = len(fitness_parents)-self.num_individuals_to_replace
        self.fitness_parents_array = fitness_parents.flatten()
        self.fitness_children_array = fitness_children.flatten()
        self.sorted_index_parents = np.array(sorted(range(len(self.fitness_parents_array)),key=self.fitness_parents_array.__getitem__, reverse = True))
        self.sorted_index_children = np.array(sorted(range(len(self.fitness_children_array)),key=self.fitness_children_array.__getitem__, reverse = True))
        
        self.keeped_children = self.sorted_index_children[0:self.num_individuals_to_replace,]
        self.children_selected = children[self.keeped_children,]
        self.keeped_parents = self.sorted_index_parents[0:self.num_individuals_to_keep,]
        self.parents_selected = parents[self.self.keeped_parents,]
        
        self.new_generation = np.append(self.children_selected,self.parents_selected).reshape((len(parents),len(parents[0])))
        
        return(self.new_generation)
        
    def fitness_based_replacement(self, fitness_parents, fitness_children, parents, children):
        self.fitness_parents_array = fitness_parents.flatten()
        self.fitness_children_array = fitness_children.flatten()
        self.total_fitness = np.append(self.fitness_parents_array,self.fitness_children_array)
        self.total_population = np.append(parents,children).reshape(((len(parents)+len(parents)),len(children[0])))
        
        self.sorted_index = np.array(sorted(range(len(self.total_fitness)),key=self.total_fitness.__getitem__, reverse = True))
        self.selected_individuals = self.sorted_index[0:len(parents),]
        
        self.new_generation = self.total_population[self.selected_individuals,]
        
        return(self.new_generation)