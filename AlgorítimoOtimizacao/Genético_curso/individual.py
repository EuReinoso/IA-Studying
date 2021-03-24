from random import random

class Individual:
    def __init__(self,spaces,valors,spaces_limit,generation=0):
        self.spaces = spaces
        self.valors = valors
        self.spaces_limit = spaces_limit
        self.generation = generation
        self.grade = 0
        self.chromosome = []

        for i in range(len(spaces)):
            if random() > 0.5:
                self.chromosome.append("0")
            else:
                self.chromosome.append("1")