#Simulação de genético

"""
O objetivo desse algorítimo vai ser: 
Dada uma lista de vetores alearótios, o resultado da soma de seus componentes
tem que ser o menor possível. Ou seja, o melhor resultado seria [0,0,0,0...]
"""

from random import randint


def gen_vector(min,max,size):
    vector = []
    for i in range(size):
        vector.append(randint(min,max))
    return vector

