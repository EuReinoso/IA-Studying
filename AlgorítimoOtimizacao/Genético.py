#Simulação de genético

"""
O objetivo desse algorítimo vai ser: 
Dada uma lista de vetores alearótios, o resultado da soma de seus componentes
tem que ser o menor possível. Ou seja, o melhor resultado seria [0,0,0,0...]
"""
import random,numpy,time

MINIMUM = 0
MAXIMUM = 100

INDIVIDUAL_SIZE = 10
POPULATION_SIZE = 100

def gen_vector(individual_size):
    vector = []
    for i in range(individual_size):
        vector.append(random.randint(MINIMUM,MAXIMUM))
    return vector

def gen_population(population_size,individual_size):
    population = []
    for i in range(population_size):
        population.append(gen_vector(individual_size))
    return population

def individual_cost(individual):
    sum = 0
    for i in individual:
        sum += i
    return sum

def print_population(population):
    for individual in population:
        print(individual, individual_cost(individual))

def best_select(population):
    best = None
    best_sum = 1000
    for individual in population:
        if individual_cost(individual) < best_sum:
            best = individual
            best_sum = individual_cost(individual)
    return best

def mutation(individual):
    vector = []
    for i in range(len(individual)):
        if random.randint(1,100) <= 30: 
            vector.append(random.randint(MINIMUM,MAXIMUM)) 
        else:
            vector.append(individual[i])
    return vector

def gen_new_population(individual):
    population = []
    for i in range(POPULATION_SIZE):
        population.append(mutation(individual))
    return population


population = gen_population(POPULATION_SIZE,INDIVIDUAL_SIZE)
best_individual = best_select(population)

print_population(population)

while individual_cost(best_individual) > 0:
    population = gen_new_population(best_individual)
    best_individual = best_select(population)

    print("\nBest:",best_individual, individual_cost(best_individual))
    time.sleep(1)







