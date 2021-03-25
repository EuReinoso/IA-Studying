from individual import Individual
from random import random

class GeneticAlgorithm:
    def __init__(self,population_size):
        self.population_size = population_size
        self.generation = 0
        self.population = []
        self.best_solution = 0

    def population_init(self,spaces,valors,spaces_limit):
        for i in range(self.population_size):
            self.population.append(Individual(spaces,valors,spaces_limit))
        self.best_solution = self.population[0]
    
    def population_order(self):
        self.population = sorted(self.population,
                                key= lambda population:population.grade,
                                reverse = True)
    
    def best_individual(self,individual):
        if individual.grade > self.best_solution.grade:
            self.best_solution = individual

    def population_assessment(self):
        grade = 0
        for individual in self.population:
            grade += individual.grade
        return grade

    def father_select(self,pop_assessment):
        father = -1
        valor = random() * pop_assessment
        total = 0
        i = 0
        while i < len(self.population) and total < valor:
            total += self.population[i].grade
            father += 1
            i += 1
        return father