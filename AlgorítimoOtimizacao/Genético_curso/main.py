from product import Product
from geneticAlgorithm import GeneticAlgorithm
import time

POPULATION_SIZE = 5
LIMIT = 3
MUTATION = 0.05

product_list = []
product_list.append(Product("Geladeira Dako", 0.751, 999.90))
product_list.append(Product("Iphone 6", 0.0000899, 2911.12))
product_list.append(Product("TV 55' ", 0.400, 4346.99))
product_list.append(Product("TV 50' ", 0.290, 3999.90))
product_list.append(Product("TV 42' ", 0.200, 2999.00))
product_list.append(Product("Notebook Dell", 0.00350, 2499.90))
product_list.append(Product("Ventilador Panasonic", 0.496, 199.90))
product_list.append(Product("Microondas Electrolux", 0.0424, 308.66))
product_list.append(Product("Microondas LG", 0.0544, 429.90))
product_list.append(Product("Microondas Panasonic", 0.0319, 299.29))
product_list.append(Product("Geladeira Brastemp", 0.635, 849.00))
product_list.append(Product("Geladeira Consul", 0.870, 1199.89))
product_list.append(Product("Notebook Lenovo", 0.498, 1999.90))
product_list.append(Product("Notebook Asus", 0.527, 3999.00))


def gen_lists():
    names = []
    spaces = []
    valors = []
    for product in product_list:
        names.append(product.name)
        spaces.append(product.space)
        valors.append(product.valor)
    return names,spaces,valors


names,spaces,valors = gen_lists()

gen = GeneticAlgorithm(POPULATION_SIZE)
gen.population_init(spaces,valors,LIMIT)

while True:
    for individual in gen.population:
        individual.assessment()

    gen.population_order()
    gen.best_individual(gen.population[0])

    print(gen.best_solution.chromosome, gen.best_solution.grade)
    grade = gen.population_assessment()

    new_population = []

    for individual in range(0,gen.population_size,2):
        father1 = gen.father_select(grade)
        father2 = gen.father_select(grade)

        sons = gen.population[father1].crossover(gen.population[father2])
        new_population.append(sons[0].mutation(MUTATION))
        new_population.append(sons[1].mutation(MUTATION))

    gen.population = list(new_population)
    time.sleep(1)

