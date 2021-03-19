#Simulação de genético

"""
O objetivo desse algorítimo vai ser: 
Dada uma lista de vetores alearótios, o resultado da soma de seus componentes
tem que ser o menor possível. Ou seja, o melhor resultado seria [0,0,0,0...]
"""

from random import randint

MINIMUM = 0
MAXIMUM = 100

INDIVIDUAL_SIZE = 10
POPULATION_SIZE = 10

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

def individual_cost(population,index):
    sum = 0
    for i in population[index]:
        sum += i
    return sum


population = gen_population(POPULATION_SIZE,MINIMUM,MAXIMUM,INDIVIDUAL_SIZE)

print(individual_cost(population,0))

