from individual import Individual

class geneticAlgorithm:
    def __init__(self,population_size):
        self.population_size = population_size
        self.generation = 0
        self.population = []
        self.best_solution = 0
        self.grade = 0

    def population_init(self,spaces,valors,spaces_limit):
        for i in range(self.population_size):
            self.population.append(Individual(spaces,valors,spaces_limit))
        self.best_solution = self.population[0]
    
    def population_order(self):
        self.population = sorted(self.population,
                                key= lambda population:population.grade,
                                reverse = True)

