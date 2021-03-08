import numpy

class OrderedVector:
    def __init__(self,capacity):
        self.capacity = capacity
        self.last_position = -1
        self.valors = numpy.empty(self.capacity,dtype = int)

    def print_valors(self):
        if self.last_position == -1:
            print("Empty Vector")

        else:
            for i in range(self.last_position + 1):
                print(i,"-",self.valors[i])

    def insert(self,val):
        if self.last_position == self.capacity -1:
            print("Full Vector")
            return
        pos = 0
        for i in range(self.last_position + 1):
            pos = i
            if self.valors[i] > val:
                break
            if i == self.last_position:
                pos = i + 1
        
        x = self.last_position
        while x >= pos:
            self.valors[x + 1] = self.valors[x]
            x -= 1

        self.valors[pos] = val
        self.last_position += 1


vector = OrderedVector(5)

vector.insert(2)
vector.insert(7)
vector.insert(1)
vector.insert(4)



vector.print_valors()