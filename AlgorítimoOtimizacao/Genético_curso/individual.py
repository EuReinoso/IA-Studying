from random import random

class Individual:
    def __init__(self,spaces,valors,spaces_limit,generation=0):
        self.spaces = spaces
        self.valors = valors
        self.spaces_limit = spaces_limit
        self.generation = generation
        self.grade = 0
        self.total_space = 0
        self.chromosome = []

        for i in range(len(spaces)):
            if random() > 0.5:
                self.chromosome.append("0")
            else:
                self.chromosome.append("1")
    
    def assessment(self):
        total_space = 0
        grade = 0
        for i in range(len(self.chromosome)):
            if self.chromosome[i] == '1':
                total_space += self.spaces[i]
                grade += self.valors[i]

        if total_space > self.spaces_limit:
            grade = 1

        self.total_space = total_space
        self.grade = grade
    
    def crossover(self,other):
        cut = round(random() * len(self.chromosome))

        son1 = other.chromosome[0:cut] + self.chromosome[cut::]
        son2 = self.chromosome[0:cut] + other.chromosome[cut::]

        sons = [Individual(self.spaces,self.valors,self.spaces_limit),
                Individual(self.spaces,self.valors,self.spaces_limit)]
        
        sons[0].chromosome = son1
        sons[1].chromosome = son2

        return sons

