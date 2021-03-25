from random import random
from individual import Individual

class GeneticAlgorithm:
    def __init__(self,population_size):
        self.population_size = population_size
        self.population = []
        self.best_solution = 0
        self.grade = 0

    def population_init(self,spaces,valors,limit):
        for i in range(self.population_size):
            self.population.append(Individual(spaces,valors,limit))
        self.best_solution = self.population[0]

    def population_order(self):
        self.population = sorted(self.population,
                                key=lambda population:population.grade,
                                reverse = True)
    
    def best_individual(self,individual):
        if individual.grade > self.best_solution.grade:
            self.best_solution = individual

    def population_assessment(self):
        grade = 0
        for individual in self.population:
            grade += individual.grade
        return grade

    def father_select(self,pop_grade):
        father_index = -1
        valor = random() * pop_grade
        total = 0
        i = 0

        while i < len(self.population) and total < pop_grade:
            father_index += 1
            total += self.population[i].grade
            i += 1

        return father_index
