import itertools
from reachable_game import get_attractor
from cop_robber_game import get_game_graph, game_graph_to_reachable_game


def generate_periodic_edge_graph(footprint, sequence_length):
    """
    Generate every periodic edge graph with a sequence length of
    "sequence_length" and a footprint "footprint". Every periodic edge graph
    where the least common multiple of all sequence length is a divider of
    "sequence_length" are yielded by this function. The footprint is a tuple
    of two lists, a list of vertices and a list of edges.
    """
    V, E = footprint
    sequences = [str(seq).replace('0b', '').rjust(sequence_length, '0')
            for seq in range(1, 2**sequence_length)]
    for combination_seq in itertools.product(sequences, repeat=len(E)):
        tau = {e: combination_seq[i] for e, i in enumerate(E)}
        yield (V, E, tau)


def is_kcop_win(tvg, k=1):
    V, E, tau = tvg
    game = game_graph_to_reachable_game(*get_game_graph(V, E, k, tau))
    attractor = get_attractor(game)
    G, F = game
    S0, S1, A = G
    initial_state = [(*crs, t) for *crs, t in S0 if t == 0]
    return len(set(initial_state).intersection(attractor)) > 0

def resolve_problem(EPCR, on_succeed=None, on_failure=None):
    if is_kcop_win(*EPCR):
        if on_succeed is not None: on_succeed(EPCR)
    else:
        if on_failure is not None: on_failure(EPCR)
