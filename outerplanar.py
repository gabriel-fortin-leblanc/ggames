import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

import time
import itertools


def get_attractor(V, E, V0, F0):
    """
    Compute the attractor set.
    Credit : Dietmar Berwanger in "Graph games with perfect information"
    :param V: The set of vertices
    :param E: The set of edges
    :param V0: The set of initial vertices
    :param F0: The set of goal vertices
    :return: The attractor set of the graph
    """

    def propagate(v, W, P, N):
        if W[v]: return

        W[v] = True
        for u in P[v]:
            n[u] -= 1
            if u in V0 or N[u] == 0:
                propagate(u, W, P, N)

    w = {}
    p = {}
    n = {}

    for v in V:
        w[v] = False
        p[v] = set()
        n[v] = 0

    for u, v in E:
        p[v].add(u)
        n[u] += 1

    for v in F0:
        propagate(v, w, p, n)
    return w


def get_game_graph(G, tau):
    pass


T = 1
# Generate vertices
n_between = 2
vertices = ['C1', 'C2', 'C']
vertices.extend([f'L{i}' for i in range(1, n_between + 1)])
vertices.extend([f'R{i}' for i in range(1, n_between + 1)])

# Generate edges
edges = [('C1', 'C'), ('C2', 'C'), (f'L{n_between}', 'C'), (f'R{n_between}', 'C')]
edges.extend([('C1', f'L{i}') for i in range(1, n_between + 1)])
edges.extend([('C2', f'R{i}') for i in range(1, n_between + 1)])
edges.extend([(f'L{i}', f'L{i + 1}') for i in range(1, n_between)])
edges.extend([(f'R{i}', f'R{i + 1}') for i in range(1, n_between)])

G = nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_from(edges)

# Generate Tau
tau = dict()
for u, v in G.edges:
    b = np.random.randint(2, size=T)
    tau[(u, v)] = b
    tau[(v, u)] = b

# Compute the game graph (gg)
vertices_gg = []
edges_gg = []
F0 = set()
V0 = set()
for c1 in vertices:

    if c1 != 'C1' and c1 != 'C2':
        V0.add(('C1', 'C2', c1, False, 0))
    for c2 in vertices:
        for r in vertices:
            for s in [False, True]:
                for t in range(T):
                    vertices_gg.append((c1, c2, r, s, t))
                    if not s:  # Cop's turn
                        # Both cops don't move
                        edges_gg.append(((c1, c2, r, False, t), (c1, c2, r, True, t)))
                        # One of the two cops moves
                        for n in G.neighbors(c1):
                            if tau[(c1, n)][t] == '1':
                                edges_gg.append(((c1, c2, r, False, t), (n, c2, r, True, t)))
                        for n in G.neighbors(c2):
                            if tau[(c2, n)][t] == '1':
                                edges_gg.append(((c1, c2, r, False, t), (c1, n, r, True, t)))
                        # Both cops move
                        for n1 in G.neighbors(c1):
                            if tau[(c1, n1)][t] == '1':
                                for n2 in G.neighbors(c2):
                                    if tau[(c2, n2)][t] == '1':
                                        edges_gg.append(((c1, c2, r, False, t), (n1, n2, r, True, t)))
                    else:  # Robber's turn
                        for n in G.neighbors(r):
                            edges_gg.append(((c1, c2, r, True, t), (c1, c2, n, False, (t + 1) % T)))

                    if c1 == r or c2 == r or (r == 'C1' and c1 != 'C1' and c2 != 'C1') or (
                            r == 'C2' and c1 != 'C2' and c2 != 'C2'):
                        F0.add((c1, c2, r, s, t))

GG = nx.DiGraph()
GG.add_nodes_from(vertices_gg)
GG.add_edges_from(edges_gg)

Attract_flag = get_attractor(GG.nodes, GG.edges, V0, F0)
Attrac = {edge for edge, flag in Attract_flag.items()}
winning = V0.intersection(Attrac)
print(winning)
