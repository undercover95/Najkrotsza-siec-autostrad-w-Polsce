import graph

class SeparableSets:
    
    def __init__(self):
        self.sets = dict()
        
    def createSet(self, item):
        newSet = []
        newSet.append(item)
        
        self.sets[item] = newSet
        
    def findSet(self, item):
        return self.sets[item]
    
    def union(self, set1, set2):
        for i in range(len(set2)):
            set1.append(set2[i])
            self.sets[set2[i]] = set1
        
        
        del set2
    
    def printList(self,v):
        for i in self.sets[v]:
            print i.getValue(),
        print '\n'      
            
class Test:
    def __init__(self):
        self.graf = graph.Graph()
        self.sets = SeparableSets()
        
    def test(self):
        self.graf.addVertex('a')
        self.graf.addVertex('l')
        self.graf.addVertex('g')
        self.graf.addVertex('o')
        self.graf.addVertex('r')
        self.graf.addVertex('y')
        self.graf.addVertex('t')
        self.graf.addVertex('m')
        self.graf.addVertex('u')
        
        self.graf.addEdge(self.graf.V['a'], self.graf.V['g'], 1)
        self.graf.addEdge(self.graf.V['o'], self.graf.V['g'], 2)
        self.graf.addEdge(self.graf.V['g'], self.graf.V['l'], 3)
        self.graf.addEdge(self.graf.V['r'], self.graf.V['y'], 4)
        self.graf.addEdge(self.graf.V['t'], self.graf.V['m'], 5)
        self.graf.addEdge(self.graf.V['m'], self.graf.V['u'], 6)
        self.graf.addEdge(self.graf.V['t'], self.graf.V['u'], 7)
        
        for v in self.graf.V:
            self.sets.createSet(self.graf.V[v])
    
        for e in self.graf.E:
            set1 = self.sets.findSet(e.getFirst())
            set2 = self.sets.findSet(e.getSecond())
            if set1 != set2:
                self.sets.union(set1, set2)
        
        
#test = Test()
#test.test()