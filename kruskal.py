import graph
import time
from separateSets import SeparableSets

sets = SeparableSets()
def KruskalAlgorithm(G):
    finalEdgeSet = []
    
    for v in G.V:
        sets.createSet(G.V[v])
    
    G.E.sort(key=lambda e: e.getWeight()) # sortowanie krawedziami
    
    for e in G.E:
        set1 = sets.findSet(e.getFirst())
        set2 = sets.findSet(e.getSecond())
        if set1 != set2:
            finalEdgeSet.append(e)
            sets.union(set1, set2)
    
    return finalEdgeSet


def printFinalEdgeSet(finalSet):
    s = 0.0
    e = 0
    out_file = open("min_tree.txt","w")
    for edge in finalSet:
        s += float(edge.getWeight())
        out_file.write(str(edge.getFirst().getDlGeo()) + ';' + str(edge.getFirst().getSzerGeo()) + ';' + str(edge.getSecond().getDlGeo()) + ';' + str(edge.getSecond().getSzerGeo()) + '\n')
    
    print "liczba krawedzi minimalnych: " + str(len(finalSet))
    print "suma wag: " + str(s)
    
    
    





# Tworzymy graf
class Test:
    def __init__(self, krok=1):
        self.graf = graph.Graph() # pusty graf
        self.krok = krok # domyslnie wszystkie wierzcholki
        
    def test(self):
        
        # *********************** Wczytywanie wierzcholkow i krawedzi *************************
        print "Wczytywanie wierzcholkow i krawedzi do grafu..."
        t0 = time.clock()
        import codecs
        vertexListFile = codecs.open('wygenerowaneDane/lista_miast_' + str(self.krok) + '.txt','r','utf8')
        utf8_vertex_file = vertexListFile.read()
        
        lines = utf8_vertex_file.split('\n') # dzielimy plik na linie
        for line in lines:
            if line == "": 
                continue
            words = line.split(';')
            self.graf.addVertex(words[0], float(words[2]), float(words[1]))
        

        
        edgeListFile = codecs.open('wygenerowaneDane/lista_krawedzi_' + str(self.krok) + '.txt', 'r', 'utf8') 
        utf8_edge_file = edgeListFile.read()
        
        lines = utf8_edge_file.split('\n') # dzielimy plik na linie
        for line in lines:
            if line == "": 
                continue
            
            e = line.split('  ')
            self.graf.addEdge(self.graf.V[e[0]], self.graf.V[e[1]], float(e[2].replace(',', '.')))
        
        print "Zakonczono wczytywanie! " + "Czas operacji: " + "%.10f" % float(time.clock()-t0) + " s."
        print "Liczba wierzcholkow: " + str(self.graf.countVertex)
        print "Liczba krawedzi: " + str(self.graf.countEdge)
        
        edges_file = open("edges.dat","w")
        for i in range(self.graf.countEdge):
            edges_file.write(str(self.graf.E[i].getFirst().getDlGeo()) + ';' + str(self.graf.E[i].getFirst().getSzerGeo()) + ';' + str(self.graf.E[i].getSecond().getDlGeo()) + ';' + str(self.graf.E[i].getSecond().getSzerGeo()) + '\n')

        print "Uruchamiam algorytm Kruskala na grafie..."
        t0 = time.clock()
        printFinalEdgeSet(KruskalAlgorithm(self.graf))
        print "Zakonczono. " + "Czas operacji: " + "%.10f" % float(time.clock()-t0)  + " s."


import sys
try:
    if int(sys.argv[1]) > 0 and int(sys.argv[1]) <= 50:
        test = Test(sys.argv[1])
        print "Uzyta wartosc kroku = " + str(sys.argv[1]) + "."
        test.test()
    else:
        raise ValueError
except IndexError:
    print "Nie podano wartosci kroku. Uzyta wartosc domyslna = 1."
    test = Test()
    test.test()
