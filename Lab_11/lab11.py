class Graph_ES:
    def __init__(self, V = (), E=()):
        self._V = set()
        self._E = set()
        for v in V: self.add_vertex(v)
        for e in E: self.add_edge(e) 

    def __len__(self):
        return len(self._V)

    def __iter__(self):
        return iter(self._V)

    def add_vertex(self, v):
        self._V.add(v)

    def add_edge(self, e):
        self._E.add(e)

    def remove_edge(self, e):
        if not e in self._E:
            raise KeyError('bruh')
        self._E.remove(e)

    def remove_vertex(self, v):
        if v not in self._V:
            raise KeyError('bruh')
        self._V.remove(v)

    def _neighbors(self, v):
        return (w for u,w in self._E if u == v)

class Graph_AS:
    def __init__(self, V = (), E = ()):
        self._V = set()
        self._nbrs = dict()
        for v in V: self.add_vertex(v)
        for e in E: self.add_edge(e)
 
    def __iter__(self):
        return iter(self._V)
    
    def __len__(self):
        return len(self._V)
 
    def add_vertex(self, v):
        self._V.add(v)
    
    def remove_vertex(self, v):
        if v not in self._V:
            raise KeyError('bruh')
        self._V.remove(v)
    
    def add_edge(self, e):
        a, b = e # e = (x, y)
        if a not in self._nbrs:
            self._nbrs[a] = {b}
        else:
            self._nbrs[a].add(b)
    
    def remove_edge(self, e):
       
        a, b = e
        if b not in self._nbrs[a]:
            raise KeyError('bruh')
 
        self._nbrs[a].remove(b)
        if len(self._nbrs[a]) == 0: self._nbrs.pop(a)
    
   
    def _neighbors(self, v):
        return iter(self._nbrs[v])



        