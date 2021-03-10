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
            cities = OrderedVector(len(actual.adjacents),'a')
            for adj in actual.adjacents:
                cities.insert(adj)
        
            if cities.valors[0] != None:
                self.seach(cities.valors[0].vertex)
    

gulosa = Gulosa(Grafo().bucharest)
gulosa.seach(Grafo().arad)