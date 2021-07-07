import math
import itertools
import functools


def get_game_graph(V, E, tau, k, T=None):
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
        pattern_length = list(map(len, tau.values()))
        T = math.prod(pattern_length) // functools.reduce(math.gcd, pattern_length)

    V_gg = []; A_gg = []
    V0 = set(); F0 = set()
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
            # Cops' move
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


def get_next_moves(V, A, attractor, cops_move=True, others_move=None):
    """
    Return a list of all possible winning moves for a time-varying graph if 
    """
    if cops_move:
        if others_move is None: # The initial cops' move.
            return [(*crs, t) for *crs, t in attractor if t == 0]
        
        else:
            possible_vertices = set([v for u, v in A if u == others_move])
            return list(possible_vertices.intersection(attractor))

    else:
        possible_vertices = set([v for u, v in A if u == others_move])
        return list(possible_vertices.difference(attractor))


if __name__ == '__main__':

    # Test of obvious cop-win graph
    V_C3 = list(range(3))
    E_C3 = [(i, (i+1)%3) for i in range(3)]
    tau_C3 = {e: '1' for e in E_C3}
    
    V_gg, A_gg, V0, F0 = get_game_graph(V_C3, E_C3, tau_C3, 1)
    assert set(V_gg) == {(0, 0, False, 0), (0, 0, True, 0), (0, 1, False, 0),
                         (0, 1, True, 0), (0, 2, False, 0), (0, 2, True, 0),
                         (1, 0, False, 0), (1, 0, True, 0), (1, 1, False, 0),
                         (1, 1, True, 0), (1, 2, False, 0), (1, 2, True, 0),
                         (2, 0, False, 0), (2, 0, True, 0), (2, 1, False, 0),
                         (2, 1, True, 0), (2, 2, False, 0), (2, 2, True, 0)}
    """
    assert set(A_gg) == {((0, 0, False, 0), (0, 0, True, 0)),
                         ((0, 0, False, 0), (1, 0, True, 0)),
                         ((0, 0, False, 0), (2, 0, True, 0)),
                         ((0, 0, True, 0), (0, 0, False, 0)),
                         ((0, 0, True, 0), (0, 1, False, 0)),
                         ((0, 0, True, 0), (0, 2, False, 0)),
                         ((0, 1, False, 0), (0, 1, True, 0)),
                         ((0, 1, False, 0), (1, 1, True, 0)),
                         ((0, 1, False, 0), (2, 1, True, 0)),
                         ((1, 0, False, 0), (1, 0, True, 0)),
                         ((1, 0, False, 0), (0, 0, True, 0)),
                         ((1, 0, False, 0), (2, 0, True, 0)), # TODO : To continue...
                         }
    """

    attractor = get_attractor(V_gg, A_gg, V0, F0)
    assert attractor == set(V_gg)
    
