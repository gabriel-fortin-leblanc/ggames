"""
A reachable game is defined as (G, F) where G = (S_0, S_1, A) induced a
directed graph (S_0 U S_1, A) and F is a subset of S_1. A is a list of pairs
of elements of S_0 U S_1.
"""


def get_attractor(S0, S1, A, F):
    """
    Compute the attractor set.
    Credit : Dietmar Berwanger in "Graph games with perfect information"
    :param S0: A list of vertices
    :param S1: A list of vertices (must be disjointed of S0)
    :param A: A sub-list (subset) of S0 x S1 U S1 x S0
    :param F: A sub-list (subset) of S1 as list.
    """
    def propagate(vertex, in_attractor, num_out_degree, previous, S0_set):
        if in_attractor[vertex]: return

        in_attractor[vertex] = True
        for prev in previous[vertex]:
            num_out_degree[prev] -= 1
            if prev in S0_set or num_out_degree[prev] == 0:
                propagate(prev, in_attractor, num_out_degree, previous, S0_set)

    in_attractor = dict()
    previous = dict()
    num_out_degree = dict()
    S0_set = set(S0)

    for v in S0 + S1:
        in_attractor[v] = False
        previous[v] = set()
        num_out_degree[v] = 0
    
    for u, v in A:
        previous[v].add(u)
        num_out_degree[u] += 1
    
    for v in F:
        propagate(v, in_attractor, num_out_degree, previous, S0_set)
    
    return [vertex for vertex, is_in_attractor in in_attractor.items()
                if is_in_attractor]


def get_next_winning_moves(current_vertex, A, attractor, player0_move=True):
    """
    Compute a list of next moves that lead to a winning game for the player 0
    if "player0_move" with respect to the game on the graph with the set of
    arcs "A", its attractor set "attractor" and the vertex "current_vertex"
    the token is on.
    :param current_vertex: A vertex
    :param A: A list of arcs
    :param attractor: A list representing the attractor set.
    :param player0_move: A flag meaning that is at the player 0 to play.
    """
    attractor_set = set(attractor)
    if player0_move:
        return [v for u, v in A if u == current_vertex and v in attractor_set]
    else:
        return [v for u, v in A if u == current_vertex and v not in attractor_set]


if __name__ == '__main__':
    S0 = [1, 2]
    S1 = [3, 4, 5]
    A = [(1, 3), (2, 5), (3, 2), (3, 4), (4, 1), (4, 2)]
    F = [5]
    attractor = get_attractor(S0, S1, A, F)
    assert set(attractor) == {2, 5}
    next_moves_for_p0 = get_next_winning_moves(2, A, attractor)
    assert set(next_moves_for_p0) == {5}
    next_moves_for_p1 = get_next_winning_moves(4, A, attractor, False)
    assert set(next_moves_for_p1) == {1}

    S0 = [1, 2, 3, 4, 8, 9]
    S1 = [5, 6, 7, 10]
    A = [(1, 5), (2, 5), (2, 6), (3, 6), (3, 7), (4, 7), (5, 8), (6, 8),
            (6, 9), (7, 9), (8, 10), (9, 10)]
    F = [10]
    attractor = get_attractor(S0, S1, A, F)
    assert set(attractor) == set(S0 + S1)
    next_moves_for_p0 = get_next_winning_moves(3, A, attractor)
    assert set(next_moves_for_p0) == {6, 7}
    next_moves_for_p1 = get_next_winning_moves(6, A, attractor, False)
    assert set(next_moves_for_p1) == set()

    S0 = [1, 4]
    S1 = [2, 3, 5]
    A = [(1, 3), (1, 2), (2, 1), (2, 4), (3, 1), (3, 4), (4, 5)]
    F = [5]
    attractor = get_attractor(S0, S1, A, F)
    assert set(attractor) == {4, 5}
    next_moves_for_p0 = get_next_winning_moves(1, A, attractor)
    assert set(next_moves_for_p0) == set()
    next_moves_for_p0 = get_next_winning_moves(4, A, attractor)
    assert set(next_moves_for_p0) == {5}
    next_moves_for_p1 = get_next_winning_moves(2, A, attractor, False)
    assert set(next_moves_for_p1) == {1}
