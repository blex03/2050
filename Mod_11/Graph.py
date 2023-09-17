from lab10 import PQ_OL
class Graph:
    def __init__(self, V=(), E=()):
        """Initilizes vertices and edges"""
        self._V = set()
        self._nbrs = dict()
        self._nbrsNoWeights = dict()  #A dictionary of edges without the weights
        for v in V: self.add_vertex(v)
        
        if E != ():
            for i, j in E.items():
                for k, l in j.items(): self.add_edge(i, k, l)


    def add_vertex(self, v):
        """Adds given vertex to set of vertices"""
        self._V.add(v)

    def remove_vertex(self, v):
        """removes given vertex from set of vertices"""
        if v not in self._V:
            raise KeyError('Vertex not found')
        self._V.remove(v)

    def add_edge(self, u, v, wt):
        """adds given edge to dictionary of edges"""
        if u not in self._nbrs:
            self._nbrs[u] = {v: wt}
            self._nbrsNoWeights[u] = {v}
        else:
            self._nbrs[u][v] = wt
            self._nbrsNoWeights[u].add(v)
 
    def remove_edge(self, u, v, wt):
        """removes given edge from dictionary of edges"""
        if not u in self._nbrs:
            raise KeyError('Edge not found')
        if not v in self._nbrs[u]:
            raise KeyError('Edge not found')
        if self._nbrs[u][v] != wt:
            raise KeyError('Weight is incorrect')

        del self._nbrs[u][v]
        self._nbrsNoWeights[u].remove(v)

        if len(self._nbrs[u]) == 0: 
            self._nbrs.pop(u)
            self._nbrsNoWeights.pop(u)

    def nbrs(self, v):
        """returns iterator that produces neighboring cities"""
        if v not in self._nbrsNoWeights:
            raise KeyError('Vertex not found')
        return iter(self._nbrsNoWeights[v])



    def fewest_flights(self, city):
        """returns the shortest path with least number of flights to each city"""

        tree = {}
        to_visit = [(None, city)]
        D = {city: 0}
        
        while to_visit:
            a, b = to_visit.pop(0) 
            if b not in tree:
                tree[b] = a 
                for n in self._nbrs[b]:
                    to_visit.append((b, n)) 
                    if n not in D:
                        D[n] = D[b] + 1
        

        return tree, D



    def shortest_path(self, city):
        """returns the shortest path with shortest distance to each city"""
        tree = {city: None}
        D = {u: float('inf') for u in self._V}
        D[city] = 0
        
        tovisit = PQ_OL()

        for u in self._V:
            tovisit.insert(u, D[u])

        
        for u in tovisit:
            for n in self.nbrs(u.item):
                if D[u.item] + self._nbrs[u.item][n] < D[n]:
                    D[n] = D[u.item] + self._nbrs[u.item][n]
                    tree[n] = u.item
                    tovisit.changepriority(n, D[n])
        return tree, D

    def minimum_salt(self, city):
        """returns the shortest path that connects all of the verticies"""

        tree = {city: None}
        D = {u: float('inf') for u in self._V}
        
        D[city] = 0
        
        
        tovisit = PQ_OL()

        for u in self._V:
            tovisit.insert(u, D[u])

        
        #tovisit = PQ_UL
        for u in tovisit:
            for n in self.nbrs(u.item):
                if self._nbrs[u.item][n] < D[n] and self._nbrs[u.item][n] not in D.values():
                    D[n] = self._nbrs[u.item][n]
                    tree[n] = u.item
                    tovisit.changepriority(n, D[n])
        return tree, D



    


Vs = {"New York", "Hartford", "Berlin", "Beijing", "Tokyo"}
Es = {"New York": {"Hartford": 117, "Berlin": 3965}, "Berlin": {"New York": 3965, "Beijing": 4571},  
                   "Beijing": {"Berlin": 4571, "Tokyo": 1300},  "Tokyo": {"Beijing": 1300, "Hartford": 6705},
                   "Hartford": {"Tokyo": 1300, "New York": 117}}
        
g = Graph(Vs, Es)






        


