import math
import functools


def get_game_graph(V, E, k, tau=None, time_horizon=None):
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
    if time_horizon is None:
        # Compute the least common multiple.
        pattern_length = list(map(len, tau.values()))
        time_horizon = (math.prod(pattern_length) //
                functools.reduce(math.gcd, pattern_length))
