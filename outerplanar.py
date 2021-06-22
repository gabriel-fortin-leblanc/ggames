import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

import math
import time
import itertools


def get_attractor(V, A, V0, F0):
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

    for u, v in A:
        p[v].add(u)
        n[u] += 1

    for v in F0:
        propagate(v, w, p, n)

    return [node for node, in_attractor in w.items() if in_attractor]


def get_game_graph(V, E, tau, k, T = None):
    """
    Compute the game graph where the k-cops and robber game takes place on the
    edge periodic graph (V, E, tau) with a time horizon T.
    :param V: The list of vertices
    :param E: The list of edges
    :param tau: The presence function of the edges in E in dict
    :param k: The number of cops in the game
    :param T: The time horizon which is the least common multiple of the
              values of tau.
    """
    if T is None:
        # Compute the least common multiple.
        pattern_length = map(len, tau.values())
        T = math.prod(pattern_length) // math.gcd(pattern_length)

    V_gg = [], A_gg = []
    V0 = set(), F0 = set()
    capture_flag = False

    for *c, r in itertools.product(V, repeat=k+1):
        V0.add((*c, r, False, 0))

        # All the following nodes are initial ones.
        capture_flag = r in c

        for s in [False, True]:
            for t in range(T):
                V_gg.append((*c, r, s, t))
                if capture_flag:
                    F0.add((*c, r, s, t))

    for u, v in itertools.product(V_gg, repeat=2):
        *c0, r0, s0, t0 = u
        *c1, r1, s1, t1 = v
        if t0 == t1 and not s0 and s1 and r0 == r1:
            # Cop's move
            valid_flag = True
            for i in range(len(c0)):
                if c0[i] != c1[i] and \
                        (c0[i], c1[i]) not in E and \
                        (c1[i], c0[i]) not in E:
                    # It is impossible for a cops to move in
                    # one rounds to a non adjacent vertex.
                    valid_flag = False
                    break
            if valid_flag:
                A_gg.append((u, v))
        
        elif t0 + 1 == t1 and s0 and not s1 and c0 == c1:
            # Robber's move
            if r0 == r1 or (r0 != r1 and
                    (((r0, r1) in E and tau[(r0, r1)][t0] == '1') or
                    ((r1, r0) in E and tau[(r1, r0)][t0] == '1'))):
                A_gg.append((u, v))
    return V_gg, A_gg, V0, F0


def get_winning_strategy(attractor):
    strategies = []
    for init_state in [(*crs, t) for *crs, t in attractor if t == 0]:
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
