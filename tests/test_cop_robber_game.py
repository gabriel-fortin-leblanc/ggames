from ggames.cop_robber_game import *


# K2
V = [1, 2]
E = [(1, 2)]
K2 = (V, E)
V_gg = [(1, 1, 1, False, 0), (1, 1, 1, True, 0),
        (1, 1, 2, False, 0), (1, 1, 2, True, 0),
        (1, 2, 1, False, 0), (1, 2, 1, True, 0),
        (1, 2, 2, False, 0), (1, 2, 2, True, 0),
        (2, 1, 1, False, 0), (2, 1, 1, True, 0),
        (2, 1, 2, False, 0), (2, 1, 2, True, 0),
        (2, 2, 1, False, 0), (2, 2, 1, True, 0),
        (2, 2, 2, False, 0), (2, 2, 2, True, 0)]
A_gg = [((1, 1, 2, False, 0), (1, 1, 2, True, 0)),
        ((1, 1, 2, False, 0), (1, 2, 2, True, 0)),
        ((1, 1, 2, False, 0), (2, 1, 2, True, 0)),
        ((1, 1, 2, False, 0), (2, 2, 2, True, 0)),
        ((1, 1, 2, True, 0), (1, 1, 2, False, 0)),
        ((2, 2, 1, False, 0), (1, 1, 1, True, 0)),
        ((2, 2, 1, False, 0), (1, 2, 1, True, 0)),
        ((2, 2, 1, False, 0), (2, 1, 1, True, 0)),
        ((2, 2, 1, False, 0), (2, 2, 1, True, 0)),
        ((2, 2, 1, True, 0), (2, 2, 1, False, 0))]
K2_gg2 = V_gg, A_gg
S0 = [(1, 1, 1, False, 0), (1, 1, 2, False, 0),
      (1, 2, 1, False, 0), (1, 2, 2, False, 0),
      (2, 1, 1, False, 0), (2, 1, 2, False, 0),
      (2, 2, 1, False, 0), (2, 2, 2, False, 0)]
S1 = [(1, 1, 1, True, 0), (1, 1, 2, True, 0),
      (1, 2, 1, True, 0), (1, 2, 2, True, 0),
      (2, 1, 1, True, 0), (2, 1, 2, True, 0),
      (2, 2, 1, True, 0), (2, 2, 2, True, 0)]
F = [(1, 1, 1, False, 0), (1, 1, 1, True, 0),
     (1, 2, 1, False, 0), (1, 2, 1, True, 0),
     (1, 2, 2, False, 0), (1, 2, 2, True, 0),
     (2, 1, 1, False, 0), (2, 1, 1, True, 0),
     (2, 1, 2, False, 0), (2, 1, 2, True, 0),
     (2, 2, 2, False, 0), (2, 2, 2, True, 0)]
A = A_gg
K2_rg2 = S0, S1, A, F

# K3
V = [1, 2, 3]
E = [(1, 2), (2, 3), (3, 1)]
K3 = V, E
V_gg = [(1, 1, False, 0), (1, 1, True, 0),
        (1, 2, False, 0), (1, 2, True, 0),
        (1, 3, False, 0), (1, 3, True, 0),
        (2, 1, False, 0), (2, 1, True, 0),
        (2, 2, False, 0), (2, 2, True, 0),
        (2, 3, False, 0), (2, 3, True, 0),
        (3, 1, False, 0), (3, 1, True, 0),
        (3, 2, False, 0), (3, 2, True, 0),
        (3, 3, False, 0), (3, 3, True, 0)]
A_gg = [((1, 2, False, 0), (1, 2, True, 0)),
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
        ((3, 2, True, 0), (3, 2, False, 0))]
K3_gg = V_gg, A_gg
S0 = [(1, 1, False, 0), (1, 2, False, 0),
      (1, 3, False, 0), (2, 1, False, 0),
      (2, 2, False, 0), (2, 3, False, 0),
      (3, 1, False, 0), (3, 2, False, 0),
      (3, 3, False, 0)]
S1 = [(1, 1, True, 0), (1, 2, True, 0),
      (1, 3, True, 0), (2, 1, True, 0),
      (2, 2, True, 0), (2, 3, True, 0),
      (3, 1, True, 0), (3, 2, True, 0),
      (3, 3, True, 0)]
A = A_gg
F = [(1, 1, False, 0), (1, 1, True, 0),
     (2, 2, False, 0), (2, 2, True, 0),
     (3, 3, False, 0), (3, 3, True, 0)]
K3_rg = S0, S1, A, F

# C4
V = [1, 2, 3, 4]
E = [(1, 2), (2, 3), (3, 4), (4, 1)]
C4 = V, E

# d_C12
n = 12
V = list(range(n))
E = [(i, (i+1)%n) for i in range(n)]
tau = {(i, (i+1)%n): '1' for i in range(n-2)}
tau.update({(i, (i+1)%n): '0001' for i in range(n-2, n)})
d_C12 = V, E, tau

# d_P2
V = [1, 2, 3]
E = [(1, 2), (2, 3)]
tau = {(1, 2): '1', (2, 3): '01'}
d_P2 = V, E, tau
V_gg = [(1, 1, False, 0), (1, 1, True, 0),
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
        (3, 3, False, 1), (3, 3, True, 1)]
A_gg = [((1, 2, False, 0), (1, 2, True, 0)),
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
        ((3, 2, True, 1), (3, 2, False, 0))]
d_P2_gg = V_gg, A_gg
S0 = [(1, 1, False, 0), (1, 2, False, 0),
      (1, 3, False, 0), (2, 1, False, 0),
      (2, 2, False, 0), (2, 3, False, 0),
      (3, 1, False, 0), (3, 2, False, 0),
      (3, 3, False, 0), (1, 1, False, 1),
      (1, 2, False, 1), (1, 3, False, 1),
      (2, 1, False, 1), (2, 2, False, 1),
      (2, 3, False, 1), (3, 1, False, 1),
      (3, 2, False, 1), (3, 3, False, 1)]
S1 = [(1, 1, True, 0), (1, 2, True, 0),
      (1, 3, True, 0), (2, 1, True, 0),
      (2, 2, True, 0), (2, 3, True, 0),
      (3, 1, True, 0), (3, 2, True, 0),
      (3, 3, True, 0), (1, 1, True, 1),
      (1, 2, True, 1), (1, 3, True, 1),
      (2, 1, True, 1), (2, 2, True, 1),
      (2, 3, True, 1), (3, 1, True, 1),
      (3, 2, True, 1), (3, 3, True, 1)]
A = A_gg
F = [(1, 1, False, 0), (1, 1, True, 0),
     (2, 2, False, 0), (2, 2, True, 0),
     (3, 3, False, 0), (3, 3, True, 0),
     (1, 1, False, 1), (1, 1, True, 1),
     (2, 2, False, 1), (2, 2, True, 1),
     (3, 3, False, 1), (3, 3, True, 1)]
d_P2_rg = S0, S1, A, F



def test_get_game_graph():
    # K2
    V_gg, A_gg = get_game_graph(*K2, k=2)
    assert set(V_gg) == set(K2_gg2[0])
    assert set(A_gg) == set(K2_gg2[1])

    # K3
    V_gg, A_gg = get_game_graph(*K3)
    assert set(V_gg) == set(K3_gg[0])
    assert set(A_gg) == set(K3_gg[1])

    # d_P2
    V_gg, A_gg = get_game_graph(*d_P2)
    assert set(V_gg) == set(d_P2_gg[0])
    assert set(A_gg) == set(d_P2_gg[1])


def test_game_graph_to_reachability_game():
    # K2
    S0, S1, A, F = game_graph_to_reachability_game(*K2_gg2)
    assert set(S0) == set(K2_rg2[0])
    assert set(S1) == set(K2_rg2[1])
    assert set(A) == set(K2_rg2[2])
    assert set(F) == set(K2_rg2[3])
    
    # K3
    S0, S1, A, F = game_graph_to_reachability_game(*K3_gg)
    assert set(S0) == set(K3_rg[0])
    assert set(S1) == set(K3_rg[1])
    assert set(A) == set(K3_rg[2])
    assert set(F) == set(K3_rg[3])

    # d_P2
    S0, S1, A, F = game_graph_to_reachability_game(*d_P2_gg)
    assert set(S0) == set(d_P2_rg[0])
    assert set(S1) == set(d_P2_rg[1])
    assert set(A) == set(d_P2_rg[2])
    assert set(F) == set(d_P2_rg[3])


def test_is_kcop_win():
    # K3
    assert is_kcop_win(*K3)
    assert is_kcop_win(*K3, k=2)

    # C4
    assert not is_kcop_win(*C4)
    assert is_kcop_win(*C4, k=2)

    # d_C12
    assert is_kcop_win(*d_C12)
