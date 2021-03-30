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

    def solve(self,mutation_rate):
        for individual in self.population:
            individual.assessment()

        self.population_order()
        self.best_individual(self.population[0])
        print(self.best_solution.chromosome,self.best_solution.grade)

        grade = self.population_assessment()

        new_population = []

        for individual in range(0,self.population_size,2):
            father1 = self.father_select(grade)
            father2 = self.father_select(grade)

            sons = self.population[father1].crossover(self.population[father2])

            new_population.append(sons[0].mutation(mutation_rate))
            new_population.append(sons[1].mutation(mutation_rate))

        self.population = list(new_population)
