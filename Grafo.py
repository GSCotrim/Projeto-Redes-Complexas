from collections import defaultdict


class Grafo(object):

    def __init__(self, arestas, direcionado=True):
        self.arestas = arestas
        self.adj = defaultdict(set)
        self.direcionado = direcionado
        self.adiciona_arestas(arestas)

    def get_vertices(self):
        return list(self.adj.keys())

    # def get_arestas(self):
    #     return [(k, v) for k in self.adj.keys() for v in self.adj.keys()]

    def adiciona_arestas(self, arestas):
        for u, v in arestas:
            self.adiciona_arco(u, v)

    def adiciona_arco(self, u, v):
        self.adj[u].add(v)
        if not self.direcionado:
            self.adj[v].add(u)

    def existe_aresta(self, u, v):
        return u in self.adj and v in self.adj[u]

    def __len__(self):
        return len(self.adj)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.adj))

    def __getitem__(self, v):
        return self.adj[v]
