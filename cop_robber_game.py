import math
import functools
import itertools
import copy


def get_game_graph(V, E, k=1, tau=None, time_horizon=None):
    """
    Compute the game graph where the k-cops and robber game takes place on the
    edge periodic graph (V, E, tau) with a time horizon "time_horizon". If
    "tau" is not specified, then the graph is considered to be static. If only
    "time_horizon" is not specified, then the least common multiple is computed
    to replace it.
    :param V: The list of vertices
    :param E: The list of edges
    :param tau: The presence function of the edges in E in dict
    :param k: The number of cops in the game
    :param time_horizon: The time horizon which is the least common multiple
                         of the values of tau.
    """
    # TODO: Have to be rewrite for the readability.
    # TODO: May remove the following lines by adding conditions
    if tau is None:
        tau = {e: '1' for e in E}
    # Compute an adjancy matrix to simplify the algorithm.
    vertex_index = {u: index for index, u in enumerate(V)}
    adjancy = [[tau[(u, v)] if (u, v) in tau else
                    tau[(v, u)] if (v, u) in tau else
                    '0' for u in V] for v in V]
    
    if time_horizon is None:
        # Compute the least common multiple.
        if len(tau) == 0:
            time_horizon = 1
        else:
            pattern_length = list(map(len, tau.values()))
            time_horizon = (math.prod(pattern_length) //
                    functools.reduce(math.gcd, pattern_length))

    # Compute the set of vertices of the game graph.
    V_gg = [(*c, r, s, t)
                for t in range(time_horizon)
                for s in [False, True]
                for *c, r in itertools.product(V, repeat=k+1)]
    
    # Compute the set of arcs of the game graph.
    A_gg = []
    for u, v in itertools.product(V_gg, repeat=2):
        *c0, r0, s0, t0 = u
        *c1, r1, s1, t1 = v
        if r0 in c0: continue

        if t0 == t1 and not s0 and s1 and r0 == r1:
            # Cops' move
            valid_flag = True
            for i in range(len(c0)):
                if c0[i] != c1[i] and \
                        adjancy[vertex_index[c0[i]]][vertex_index[c1[i]]] \
                        [t0%len(adjancy[vertex_index[c0[i]]]
                            [vertex_index[c1[i]]])] == '0':
                    # It is impossible for a cops to move in
                    # one rounds to a non adjacent vertex.
                    valid_flag = False
                    break
            if valid_flag:
                A_gg.append((u, v))
        
        elif (t0 + 1)%time_horizon == t1 and s0 and not s1 and c0 == c1 and \
                r1 not in c1:
            # Robber's move
            if r0 == r1 or (r0 != r1 and \
                    adjancy[vertex_index[r0]][vertex_index[r1]] \
                    [t0%len(adjancy[vertex_index[r0]][vertex_index[r1]])] \
                        == '1'):
                A_gg.append((u, v))
    return V_gg, A_gg


def game_graph_to_reachable_game(V_gg, A_gg):
    """
    Compute and return a reachable game corresponding to the game graph
    G = (V_gg, A_gg).
    :param V_gg: A list of vertices of a game graph
    :param A_gg: A list of edges of a game graph
    """
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
    G = (S0, S1, A)
    return G, F


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
    G, F = game_graph_to_reachable_game(V_gg, A_gg)
    S0, S1, A = G
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
    G, F = game_graph_to_reachable_game(V_gg, A_gg)
    S0, S1, A = G
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
    V_gg, A_gg = get_game_graph(V, E, tau=tau)
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
    G, F = game_graph_to_reachable_game(V_gg, A_gg)
    S0, S1, A = G
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
