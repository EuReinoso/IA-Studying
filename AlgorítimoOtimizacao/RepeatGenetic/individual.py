from random import random

class Individual:
    def __init__(self,spaces,valors,limit):
        self.spaces = spaces
        self.valors = valors
        self.limit = limit
        self.grade = 0
        self.chromosome = []

        for i in range(len(spaces)):
            if random() < 0.5:
                self.chromosome.append('1')
            else:
                self.chromosome.append('0')
    
    def assessment(self):
        grade = 0
        total_space = 0
        for i in range(len(self.chromosome)):
            if self.chromosome[i] == '1':
                grade += self.valors[i]
                total_space += self.spaces[i]
        if total_space > self.limit:
            grade = 1
        
        self.grade = grade

    def crossover(self,other):
        cut = round(random() * len(self.chromosome))

        son1 = other.chromosome[0:cut] + self.chromosome[cut::]
        son2 = self.chromosome[0:cut] + other.chromosome[cut::]

        sons = [Individual(self.spaces,self.valors,self.limit),
                Individual(self.spaces,self.valors,self.limit)]
        
        sons[0].chromosome = son1
        sons[1].chromosome = son2

        return sons
    
    def mutation(self,mutation_rate):
        for i in range(len(self.chromosome)):
            if random() < mutation_rate:
                if self.chromosome[i] == '1':
                    self.chromosome[i] = '0'
                else:
                    self.chromosome[i] = '1'

        return self