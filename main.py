from os import stat
from outerplanar import get_game_graph, get_attractor
import networkx as nx
import random as rand
import matplotlib.pyplot as plt
import itertools


def show(V, E):
    G = nx.Graph()
    G.add_nodes_from(V)
    G.add_edges_from(E)
    nx.draw(G)
    plt.show()


# Create an outerplanar graph
V = list(range(8))
E = [(i, (i+1)%8) for i in range(8)]
E.extend([(0, 6), (1, 6), (1, 5), (2, 5), (2, 4)])

tau = {(i, (i+1)%8): '1' for i in range(8)}
tau[(0, 6)] = '01'
tau[(1, 5)] = '01'
tau[(2, 4)] = '01'
tau[(1, 6)] = '10'
tau[(2, 5)] = '10'

V_gg, A_gg, V0, F0 = get_game_graph(V, E, tau, 1, 2)
attractor = get_attractor(V_gg, A_gg, V0, F0)
robber_winning_state = set(V0) - attractor

game_graph = nx.DiGraph()
game_graph.add_nodes_from(V_gg)
game_graph.add_edges_from(A_gg)

pos = nx.spring_layout(game_graph)
nx.draw(game_graph, pos)
nx.draw_networkx_nodes(game_graph, pos, robber_winning_state, node_color='r')

plt.show()
