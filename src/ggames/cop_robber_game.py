"""
A cops and robber game is played on an edge periodic (or static) graph
(V, E, tau) where tau is the presence mapping of the edges.
"""


import logging
import math, copy
import functools, itertools
from reachability_game import get_attractor



def get_game_graph(V, E, tau=None, k=1):
    """
    Compute the game graph where the "k"-cops and robber game takes place on
    the edge periodic graph (V, E, tau). If "tau" is not specified, then the
    graph is considered to be static.
    :param V: The list of vertices
    :param E: The list of edges
    :param tau: The presence function of the edges in E in dict
    :param k: The number of cops in the game
    """
    logger = logging.getLogger('main.cop_robber_game')
    logger.info('"cop_robber_game.get_game_graph" called.')

    if tau is None: tau = {e: '1' for e in E}

    # Compute an adjacency matrix to simplify the algorithm.
    vertex_index = {u: index for index, u in enumerate(V)}
    adjacency = [[tau[(u, v)] if (u, v) in tau else
                    tau[(v, u)] if (v, u) in tau else
                    '1' if u == v else
                    '0' for u in V] for v in V]
    
    # Compute the least common multiple.
    if len(tau) == 0:
        time_horizon = 1
    else:
        pattern_lengths = list(map(len, tau.values()))
        time_horizon = functools.reduce(lambda x,y: abs(x*y) // math.gcd(x,y),
                pattern_lengths)

    # Compute the set of vertices of the game graph.
    V_gg = []; A_gg = []
    for t in range(time_horizon):
        for s in [False, True]:
            for *c, r in itertools.product(V, repeat=k+1):
                u = (*c, r, s, t)
                V_gg.append(u)
                if r in c: continue

                next_s = not s
                if s: # Robber's move
                    for next_r in V:
                        edge_pattern = adjacency[vertex_index[r]] \
                                [vertex_index[next_r]]
                        if edge_pattern[t%len(edge_pattern)] == '0' \
                                or next_r in c:
                            continue
                        A_gg.append((u, (*c, next_r, next_s,
                                (t+1)%time_horizon)))
                else: # Cops' move
                    for next_c in itertools.product(V, repeat=k):
                        valid_flag = True # This can be more effective
                        for i in range(len(c)):
                            edge_pattern = adjacency[vertex_index[c[i]]] \
                                    [vertex_index[next_c[i]]]
                            if c[i] != next_c[i] and \
                                    edge_pattern[t%len(edge_pattern)] == '0':
                                # It is impossible for a cops to move in
                                # one rounds to a non adjacent vertex.
                                valid_flag = False
                                break
                        if valid_flag:
                            A_gg.append((u, (*next_c, r, next_s,t)))

    return V_gg, A_gg


def game_graph_to_reachability_game(V_gg, A_gg):
    """
    Compute and return a reachable game corresponding to the game graph
    G = (V_gg, A_gg).
    :param V_gg: A list of vertices of a game graph
    :param A_gg: A list of edges of a game graph
    """
    logger = logging.getLogger('main.com_robber_game')
    logger.info('"cop_robber_game.game_graph_to_reachability_game" called.')

    S0 = []; S1 = []
    A = copy.deepcopy(A_gg)
    F = []
    for v in V_gg:
        *c, r, s, t = v
        if r in c:
            F.append(v)
        if s:
            S1.append(v)
        else:
            S0.append(v)
    return S0, S1, A, F


def is_kcop_win(V, E, tau, k=1):
    """
    Compute if the time-varying graph ("V", "E", "tau") is "k"-cop win.
    :param V: A set of vertices
    :param E: A set of edges
    :param tau: A map from E to a set of bit sequences
    :param k: The number of cops that play on the time-varying graph
    """
    logger = logging.getLogger('main.com_robber_game')
    logger.info('"cop_robber_game.is_kcop_win" called.')

    attractor = get_attractor(
                            *game_graph_to_reachability_game(
                            *get_game_graph(V, E, tau, k)))

    n = len(V)
    starting_classes = dict()
    for *c, r, s, t in attractor:
        c = tuple(c)
        if t == 0 and not s:
            if c not in starting_classes:
                starting_classes[c] = set()
            starting_classes[c].add(r)
    for cls in starting_classes.values():
        if len(cls) == n:
            return True
    return False


if __name__ == '__main__':
    # K_3
    V = [1, 2, 3]
    E = [(1, 2), (2, 3), (3, 1)]
    V_gg, A_gg = get_game_graph(V, E)
    assert set(V_gg) == {(1, 1, False, 0), (1, 1, True, 0),
                         (1, 2, False, 0), (1, 2, True, 0),
                         (1, 3, False, 0), (1, 3, True, 0),
                         (2, 1, False, 0), (2, 1, True, 0),
                         (2, 2, False, 0), (2, 2, True, 0),
                         (2, 3, False, 0), (2, 3, True, 0),
                         (3, 1, False, 0), (3, 1, True, 0),
                         (3, 2, False, 0), (3, 2, True, 0),
                         (3, 3, False, 0), (3, 3, True, 0)}
    assert set(A_gg) == {((1, 2, False, 0), (1, 2, True, 0)),
                         ((1, 2, False, 0), (2, 2, True, 0)),
                         ((1, 2, False, 0), (3, 2, True, 0)),
                         ((1, 2, True, 0), (1, 2, False, 0)),
                         ((1, 2, True, 0), (1, 3, False, 0)),
                         ((1, 3, False, 0), (1, 3, True, 0)),
                         ((1, 3, False, 0), (2, 3, True, 0)),
                         ((1, 3, False, 0), (3, 3, True, 0)),
                         ((1, 3, True, 0), (1, 2, False, 0)),
                         ((1, 3, True, 0), (1, 3, False, 0)),
                         ((2, 1, False, 0), (1, 1, True, 0)),
                         ((2, 1, False, 0), (2, 1, True, 0)),
                         ((2, 1, False, 0), (3, 1, True, 0)),
                         ((2, 1, True, 0), (2, 1, False, 0)),
                         ((2, 1, True, 0), (2, 3, False, 0)),
                         ((2, 3, False, 0), (1, 3, True, 0)),
                         ((2, 3, False, 0), (2, 3, True, 0)),
                         ((2, 3, False, 0), (3, 3, True, 0)),
                         ((2, 3, True, 0), (2, 1, False, 0)),
                         ((2, 3, True, 0), (2, 3, False, 0)),
                         ((3, 1, False, 0), (1, 1, True, 0)),
                         ((3, 1, False, 0), (2, 1, True, 0)),
                         ((3, 1, False, 0), (3, 1, True, 0)),
                         ((3, 1, True, 0), (3, 1, False, 0)),
                         ((3, 1, True, 0), (3, 2, False, 0)),
                         ((3, 2, False, 0), (1, 2, True, 0)),
                         ((3, 2, False, 0), (2, 2, True, 0)),
                         ((3, 2, False, 0), (3, 2, True, 0)),
                         ((3, 2, True, 0), (3, 1, False, 0)),
                         ((3, 2, True, 0), (3, 2, False, 0))}
    S0, S1, A, F = game_graph_to_reachability_game(V_gg, A_gg)
    assert set(S0) == {(1, 1, False, 0), (1, 2, False, 0),
                       (1, 3, False, 0), (2, 1, False, 0),
                       (2, 2, False, 0), (2, 3, False, 0),
                       (3, 1, False, 0), (3, 2, False, 0),
                       (3, 3, False, 0)}
    assert set(S1) == {(1, 1, True, 0), (1, 2, True, 0),
                       (1, 3, True, 0), (2, 1, True, 0),
                       (2, 2, True, 0), (2, 3, True, 0),
                       (3, 1, True, 0), (3, 2, True, 0),
                       (3, 3, True, 0)}
    assert set(F) == {(1, 1, False, 0), (1, 1, True, 0),
                      (2, 2, False, 0), (2, 2, True, 0),
                      (3, 3, False, 0), (3, 3, True, 0)}
    assert set(A) == set(A_gg)


    # K_2
    V = [1, 2]
    E = [(1, 2)]
    V_gg, A_gg = get_game_graph(V, E, k=2)
    assert set(V_gg) == {(1, 1, 1, False, 0), (1, 1, 1, True, 0),
                         (1, 1, 2, False, 0), (1, 1, 2, True, 0),
                         (1, 2, 1, False, 0), (1, 2, 1, True, 0),
                         (1, 2, 2, False, 0), (1, 2, 2, True, 0),
                         (2, 1, 1, False, 0), (2, 1, 1, True, 0),
                         (2, 1, 2, False, 0), (2, 1, 2, True, 0),
                         (2, 2, 1, False, 0), (2, 2, 1, True, 0),
                         (2, 2, 2, False, 0), (2, 2, 2, True, 0)}
    assert set(A_gg) == {((1, 1, 2, False, 0), (1, 1, 2, True, 0)),
                         ((1, 1, 2, False, 0), (1, 2, 2, True, 0)),
                         ((1, 1, 2, False, 0), (2, 1, 2, True, 0)),
                         ((1, 1, 2, False, 0), (2, 2, 2, True, 0)),
                         ((1, 1, 2, True, 0), (1, 1, 2, False, 0)),
                         ((2, 2, 1, False, 0), (1, 1, 1, True, 0)),
                         ((2, 2, 1, False, 0), (1, 2, 1, True, 0)),
                         ((2, 2, 1, False, 0), (2, 1, 1, True, 0)),
                         ((2, 2, 1, False, 0), (2, 2, 1, True, 0)),
                         ((2, 2, 1, True, 0), (2, 2, 1, False, 0))}
    S0, S1, A, F = game_graph_to_reachability_game(V_gg, A_gg)
    assert set(S0) == {(1, 1, 1, False, 0), (1, 1, 2, False, 0),
                       (1, 2, 1, False, 0), (1, 2, 2, False, 0),
                       (2, 1, 1, False, 0), (2, 1, 2, False, 0),
                       (2, 2, 1, False, 0), (2, 2, 2, False, 0)}
    assert set(S1) == {(1, 1, 1, True, 0), (1, 1, 2, True, 0),
                       (1, 2, 1, True, 0), (1, 2, 2, True, 0),
                       (2, 1, 1, True, 0), (2, 1, 2, True, 0),
                       (2, 2, 1, True, 0), (2, 2, 2, True, 0)}
    assert set(F) == {(1, 1, 1, False, 0), (1, 1, 1, True, 0),
                      (1, 2, 1, False, 0), (1, 2, 1, True, 0),
                      (1, 2, 2, False, 0), (1, 2, 2, True, 0),
                      (2, 1, 1, False, 0), (2, 1, 1, True, 0),
                      (2, 1, 2, False, 0), (2, 1, 2, True, 0),
                      (2, 2, 2, False, 0), (2, 2, 2, True, 0)}
    assert set(A) == set(A_gg)

    
    # P_2
    V = [1, 2, 3]
    E = [(1, 2), (2, 3)]
    tau = {(1, 2): '1', (2, 3): '01'}
    V_gg, A_gg = get_game_graph(V, E, tau)
    assert set(V_gg) == {(1, 1, False, 0), (1, 1, True, 0),
                         (1, 2, False, 0), (1, 2, True, 0),
                         (1, 3, False, 0), (1, 3, True, 0),
                         (2, 1, False, 0), (2, 1, True, 0),
                         (2, 2, False, 0), (2, 2, True, 0),
                         (2, 3, False, 0), (2, 3, True, 0),
                         (3, 1, False, 0), (3, 1, True, 0),
                         (3, 2, False, 0), (3, 2, True, 0),
                         (3, 3, False, 0), (3, 3, True, 0),
                         (1, 1, False, 1), (1, 1, True, 1),
                         (1, 2, False, 1), (1, 2, True, 1),
                         (1, 3, False, 1), (1, 3, True, 1),
                         (2, 1, False, 1), (2, 1, True, 1),
                         (2, 2, False, 1), (2, 2, True, 1),
                         (2, 3, False, 1), (2, 3, True, 1),
                         (3, 1, False, 1), (3, 1, True, 1),
                         (3, 2, False, 1), (3, 2, True, 1),
                         (3, 3, False, 1), (3, 3, True, 1)}
    assert set(A_gg) == {((1, 2, False, 0), (1, 2, True, 0)),
                         ((1, 2, False, 0), (2, 2, True, 0)),
                         ((1, 2, True, 0), (1, 2, False, 1)),
                         ((1, 3, False, 0), (1, 3, True, 0)),
                         ((1, 3, False, 0), (2, 3, True, 0)),
                         ((1, 3, True, 0), (1, 3, False, 1)),
                         ((2, 1, False, 0), (1, 1, True, 0)),
                         ((2, 1, False, 0), (2, 1, True, 0)),
                         ((2, 1, True, 0), (2, 1, False, 1)),
                         ((2, 3, False, 0), (1, 3, True, 0)),
                         ((2, 3, False, 0), (2, 3, True, 0)),
                         ((2, 3, True, 0), (2, 3, False, 1)),
                         ((3, 1, False, 0), (3, 1, True, 0)),
                         ((3, 1, True, 0), (3, 1, False, 1)),
                         ((3, 1, True, 0), (3, 2, False, 1)),
                         ((3, 2, False, 0), (3, 2, True, 0)),
                         ((3, 2, True, 0), (3, 1, False, 1)),
                         ((3, 2, True, 0), (3, 2, False, 1)),
                         ((1, 2, False, 1), (1, 2, True, 1)),
                         ((1, 2, False, 1), (2, 2, True, 1)),
                         ((1, 2, True, 1), (1, 2, False, 0)),
                         ((1, 2, True, 1), (1, 3, False, 0)),
                         ((1, 3, False, 1), (1, 3, True, 1)),
                         ((1, 3, False, 1), (2, 3, True, 1)),
                         ((1, 3, True, 1), (1, 2, False, 0)),
                         ((1, 3, True, 1), (1, 3, False, 0)),
                         ((2, 1, False, 1), (1, 1, True, 1)),
                         ((2, 1, False, 1), (2, 1, True, 1)),
                         ((2, 1, False, 1), (3, 1, True, 1)),
                         ((2, 1, True, 1), (2, 1, False, 0)),
                         ((2, 3, False, 1), (1, 3, True, 1)),
                         ((2, 3, False, 1), (2, 3, True, 1)),
                         ((2, 3, False, 1), (3, 3, True, 1)),
                         ((2, 3, True, 1), (2, 3, False, 0)),
                         ((3, 1, False, 1), (2, 1, True, 1)),
                         ((3, 1, False, 1), (3, 1, True, 1)),
                         ((3, 1, True, 1), (3, 1, False, 0)),
                         ((3, 1, True, 1), (3, 2, False, 0)),
                         ((3, 2, False, 1), (2, 2, True, 1)),
                         ((3, 2, False, 1), (3, 2, True, 1)),
                         ((3, 2, True, 1), (3, 1, False, 0)),
                         ((3, 2, True, 1), (3, 2, False, 0))}
    S0, S1, A, F = game_graph_to_reachability_game(V_gg, A_gg)
    assert set(S0) == {(1, 1, False, 0), (1, 2, False, 0),
                       (1, 3, False, 0), (2, 1, False, 0),
                       (2, 2, False, 0), (2, 3, False, 0),
                       (3, 1, False, 0), (3, 2, False, 0),
                       (3, 3, False, 0), (1, 1, False, 1),
                       (1, 2, False, 1), (1, 3, False, 1),
                       (2, 1, False, 1), (2, 2, False, 1),
                       (2, 3, False, 1), (3, 1, False, 1),
                       (3, 2, False, 1), (3, 3, False, 1)}
    assert set(S1) == {(1, 1, True, 0), (1, 2, True, 0),
                       (1, 3, True, 0), (2, 1, True, 0),
                       (2, 2, True, 0), (2, 3, True, 0),
                       (3, 1, True, 0), (3, 2, True, 0),
                       (3, 3, True, 0), (1, 1, True, 1),
                       (1, 2, True, 1), (1, 3, True, 1),
                       (2, 1, True, 1), (2, 2, True, 1),
                       (2, 3, True, 1), (3, 1, True, 1),
                       (3, 2, True, 1), (3, 3, True, 1)}
    assert set(F) == {(1, 1, False, 0), (1, 1, True, 0),
                      (2, 2, False, 0), (2, 2, True, 0),
                      (3, 3, False, 0), (3, 3, True, 0),
                      (1, 1, False, 1), (1, 1, True, 1),
                      (2, 2, False, 1), (2, 2, True, 1),
                      (3, 3, False, 1), (3, 3, True, 1)}
    assert set(A) == set(A_gg)

    # K_3
    V = [1, 2, 3]
    E = [(1, 2), (2, 3), (1, 3)]
    tau = {e: '1' for e in E}
    assert is_kcop_win(V, E, tau)
    assert is_kcop_win(V, E, tau, 2)

    # K_4
    V = [1, 2, 3, 4]
    E = [(1, 2), (2, 3), (3, 4), (4, 1)]
    tau = {e: '1' for e in E}
    assert not is_kcop_win(V, E, tau)
    assert is_kcop_win(V, E, tau, 2)

    # K_12
    n = 12
    V = list(range(n))
    E = [(i, (i+1)%n) for i in range(n)]
    tau = {(i, (i+1)%n): '1' for i in range(n-2)}
    tau.update({(i, (i+1)%n): '0001' for i in range(n-2, n)})
    assert is_kcop_win(V, E, tau)