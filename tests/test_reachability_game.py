from ggames.reachability_game import *


S0 = [1, 2]
S1 = [3, 4, 5]
A = [(1, 3), (2, 5), (3, 2), (3, 4), (4, 1), (4, 2)]
F = [5]
reachability_game1 = S0, S1, A, F
attractor1 = [2, 5]

S0 = [1, 2, 3, 4, 8, 9]
S1 = [5, 6, 7, 10]
A = [(1, 5), (2, 5), (2, 6), (3, 6), (3, 7), (4, 7), (5, 8), (6, 8),
        (6, 9), (7, 9), (8, 10), (9, 10)]
F = [10]
reachability_game2 = S0, S1, A, F
attractor2 = S0 + S1

S0 = [1, 4]
S1 = [2, 3, 5]
A = [(1, 3), (1, 2), (2, 1), (2, 4), (3, 1), (3, 4), (4, 5)]
F = [5]
reachability_game3 = S0, S1, A, F
attractor3 = [4, 5]


def test_get_attractor():
    attractor = get_attractor(*reachability_game1)
    assert set(attractor) == set(attractor1)

    attractor = get_attractor(*reachability_game2)
    assert set(attractor) == set(attractor2)

    attractor = get_attractor(*reachability_game3)
    assert set(attractor) == set(attractor3)


def test_get_next_winning_moves():
    next_moves_for_p0 = get_next_winning_moves(2, reachability_game1[2],
            attractor1)
    assert set(next_moves_for_p0) == {5}
    next_moves_for_p1 = get_next_winning_moves(4, reachability_game1[2],
            attractor1, False)
    assert set(next_moves_for_p1) == {1}

    next_moves_for_p0 = get_next_winning_moves(3, reachability_game2[2],
            attractor2)
    assert set(next_moves_for_p0) == {6, 7}
    next_moves_for_p1 = get_next_winning_moves(6, reachability_game2[2],
            attractor2, False)
    assert set(next_moves_for_p1) == set()

    next_moves_for_p0 = get_next_winning_moves(1, reachability_game3[2],
            attractor3)
    assert set(next_moves_for_p0) == set()
    next_moves_for_p0 = get_next_winning_moves(4, reachability_game3[2],
            attractor3)
    assert set(next_moves_for_p0) == {5}
    next_moves_for_p1 = get_next_winning_moves(2, reachability_game3[2],
            attractor3, False)
    assert set(next_moves_for_p1) == {1}
