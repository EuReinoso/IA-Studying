from grafo import Grafo,Vertex,Adjacent
from vetorOrdenado import OrderedVector

class Gulosa:
    def __init__(self,objective):
        self.objective = objective
        self.found = False

    def seach(self,actual):
        print(actual.name, actual.obj_distance)
        actual.visit = True

        if actual == self.objective:
            self.found = True
        else:
            cities = OrderedVector(len(actual.adjacents))
            for adj in actual.adjacents:
                cities.insert(adj.vertex)

            self.seach(cities.valors[0])
    

gulosa = Gulosa(Grafo().bucharest)
gulosa.seach(Grafo().arad)


