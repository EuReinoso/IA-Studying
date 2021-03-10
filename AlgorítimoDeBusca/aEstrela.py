from grafo import Grafo,Vertex,Adjacent
from vetorOrdenado import OrderedVector

class AEstrela:
    def __init__(self,objective):
        self.objective = objective
        self.found = False

    def seach(self,actual):
        print(actual.name, actual.obj_distance)
        actual.visit = True

        if actual == self.objective:
            self.found = True
        else:
            cities = OrderedVector(len(actual.adjacents),'estrela')
            for adj in actual.adjacents:
                if adj.vertex.visit == False:
                    adj.vertex.visit = True
                    cities.insert(adj)
        
           
            self.seach(cities.valors[0].vertex)


estrela = AEstrela(Grafo().bucharest)
estrela.seach(Grafo().timisoara)