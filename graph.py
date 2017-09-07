# Klasa reprezentujaca wierzcholek grafu
class Vertex:
    def __init__(self, val, dlGeo=0.0, szerGeo=0.0):
        self.value = val
        self.dlGeo = dlGeo
        self.szerGeo = szerGeo
        
    def getValue(self):
        return self.value
    
    def getSzerGeo(self):
        return self.szerGeo
    
    def getDlGeo(self):
        return self.dlGeo
    
# Klasa reprezentujaca krawedz miedzy dwoma wierzcholkami w postaci pary
class Edge:
    def __init__(self, v1, v2, w):
        self.first = v1
        self.second = v2
        self.weight = w
        
    def getFirst(self):
        return self.first
    
    def getSecond(self):
        return self.second
    
    def getWeight(self):
        return self.weight

# Klasa reprezentujaca graf nieskierowany jako liste wierzcholkow i liste krawedzi miedzy nimi    
class Graph:
    def __init__(self):
        self.V = dict()
        self.E = list()
        self.countVertex = 0
        self.countEdge = 0
        
    def addVertex(self, v, a, b):
        self.V.update({v:Vertex(v,a,b)})
        self.countVertex += 1
        
    def addEdge(self, v1, v2, w):
        self.E.append(Edge(v1, v2, w))
        self.countEdge += 1