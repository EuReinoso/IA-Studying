#Simulação de genético

"""
O objetivo desse algorítimo vai ser: 
Dada uma lista de vetores alearótios, o resultado da soma de seus componentes
tem que ser o menor possível. Ou seja, o melhor resultado seria [0,0,0,0...]
"""

from random import randint

MINIMUM = 0
MAXIMUM = 100

INDIVIDUAL_SIZE = 5
POPULATION_SIZE = 5

def gen_vector(min_val,max_val,individual_size):
    vector = []
    for i in range(individual_size):
        vector.append(randint(min_val,max_val))
    return vector

def gen_population(population_size,min_val,max_val,individual_size):
    population = []
    for i in range(population_size):
        population.append(gen_vector(min_val,max_val,individual_size))
    return population

def individual_cost(individual):
    sum = 0
    for i in individual:
        sum += i
    return sum

def print_population(population):
    for individual in population:
        print(individual, individual_cost(individual))

def best_individual(population):
    best = None
    best_sum = 1000
    for individual in population:
        if individual_cost(individual) < best_sum:
            best = individual
            best_sum = individual_cost(individual)
    return best

def mutation(individual):
    vector = individual
    for i in range(len(vector)):
        if randint(1,100) <= 30:
            vector[i] = randint(MINIMUM,MAXIMUM)
    return vector



population = gen_population(POPULATION_SIZE,MINIMUM,MAXIMUM,INDIVIDUAL_SIZE)
print_population(population)

best_individual = best_individual(population)

print(best_individual)
print(mutation(best_individual))

# while individual_cost(best_individual) > 0:
#     print("\nBest:",best_individual, individual_cost(best_individual))





