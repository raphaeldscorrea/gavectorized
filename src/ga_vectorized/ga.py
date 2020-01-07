
from ga_vectorized import binOperators, permOperators, survivorOperators, matingOperators
import numpy as np

class GA():
    
    def __init__(self, problem_type):
        if(problem_type == "perm"):
            self.crossover_operator = permOperators.order_crossover
            self.mutation_operator = permOperators.displacement_mutation
        else:
            self.crossover_operator = binOperators.single_point_crossover
            self.mutation_operator = binOperators.bit_inversion_mutations
        
        self.mating_operator = matingOperators.roulette_selection
        self.survivor_operator = survivorOperators.fitness_based_replacement
        
        
    def set_parameters(self, mating_operator, crossover_operator, mutation_operator, survivor_operator):
        self.mating_operator = mating_operator
        self.crossover_operator = crossover_operator
        self.mutation_operator = mutation_operator
        self.survivor_operator = survivor_operator
     
        
    def generations(self, population, generations, fitness_class):
        for i in range(0, generations):
            print(i)
            population = self.evaluation(population, 0.8, 0.05, fitness_class)
            
        return(population)
    
    
    def evaluation(self, population, prob_crossover, prob_mutation, fitness_class):
        fitness = np.array([fitness_class.calculate(x) for x in population]).reshape((len(population),))
        children = self.generate_offspring(population, fitness, prob_crossover)
        prob_mutation_vector = np.full((len(population),),prob_mutation)
        children_mutated = np.array([self.mutation_operator(x,y) for x,y in zip(children,prob_mutation_vector)]).reshape((len(population),len(population[0])))
        fitness_children = np.array([fitness_class.calculate(x) for x in children_mutated]).reshape((len(population),))
        new_generation = self.survivor_operator(fitness, fitness_children, population, children_mutated)
        
        return(new_generation)
    
    
    def generate_offspring(self, population, fitness, prob_crossover):
        index_1, index_2 = self.mating_operator(fitness, len(population), np.random.uniform(0,1,len(population)))
        
        def get_childs(p1,p2, pc):
            ch1,ch2 = self.crossover_operator(population[p1,], population[p2,])
            return(ch1, ch2)
        
        prob_crossover_vector = np.full((len(population),),prob_crossover)
        children = np.array([get_childs(x,y,z) for x,y,z in zip(index_1,index_2, prob_crossover_vector)]).reshape((len(population),len(population[0])))

        return children