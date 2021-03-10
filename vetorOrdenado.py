import numpy

class OrderedVector:
    def __init__(self,capacity):
        self.capacity = capacity
        self.last_position = -1
        self.valors = numpy.empty(self.capacity,dtype = object)

    def print_valors(self):
        if self.last_position == -1:
            print("Empty Vector")

        else:
            for i in range(self.last_position + 1):
                print(i,"-",self.valors[i])

    def insert(self,vertex):
        if self.last_position == self.capacity -1:
            print("Full Vector")
            return
        pos = 0
        for i in range(self.last_position + 1):
            pos = i
            if self.valors[i].obj_distance > vertex.obj_distance:
                break
            if i == self.last_position:
                pos = i + 1
        
        x = self.last_position
        while x >= pos:
            self.valors[x + 1] = self.valors[x]
            x -= 1

        self.valors[pos] = vertex
        self.last_position += 1

