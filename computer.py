import itertools
import functools
from reachable_game import get_attractor
from cop_robber_game import get_game_graph, game_graph_to_reachable_game


def get_bit_sequences(length, zero_sequence_included=True):
    """
    Compute every bit sequences of length "length" in str. If the flag
    "zero_sequence_included" is set to False, then the sequence composed
    only '0' is not included.
    :param length: The length of the bit sequence
    :param zero_sequence_included: A flag for including the sequence of only
                                   '0' in the series.
    """
    return [str(bin(num)).replace('0b', '', 1).rjust(length, '0') for num in
            range(0 if zero_sequence_included else 1, 2**length)]


def generate_edge_presence_maps(E, sequence_length):
    """
    Generate every mapping of "E" to the set of bit sequences of length
    "sequence_length". This last doesn't contain the bit sequence of
    only '0'.
    :param E: A list of edges.
    :param sequence_length: The length of the bit sequences.
    """
    sequences = get_bit_sequences(sequence_length, False)
    for seq_combination in itertools.product(sequences, repeat=len(E)):
        yield {e: seq_combination[i] for i, e in enumerate(E)}


def is_kcop_win(V, E, tau, k=1):
    """
    Compute if the time-varying graph ("V", "E", "tau") is "k"-cop win.
    :param V: A set of vertices
    :param E: A set of edges
    :param tau: A map from E to a set of bit sequences
    :param k: The number of cops that play on the time-varying graph
    """
    game = game_graph_to_reachable_game(*get_game_graph(V, E, k, tau))
    attractor = get_attractor(game)

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

def resolve_problem(EPCR, on_succeed=None, on_failure=None):
    if is_kcop_win(*EPCR):
        if on_succeed is not None: on_succeed(EPCR)
    else:
        if on_failure is not None: on_failure(EPCR)


if __name__ == '__main__':
    sequences = list(get_bit_sequences(1))
    assert sequences == ['0', '1']
    sequences = list(get_bit_sequences(1, False))
    assert sequences == ['1']
    sequences = list(get_bit_sequences(3, False))
    assert sequences == ['001', '010', '011', '100', '101', '110', '111']

    E = [1, 2]
    edge_presence_maps = list(generate_edge_presence_maps(E, 1))
    assert edge_presence_maps == [{1: '1', 2: '1'}]
    edge_presence_maps = list(generate_edge_presence_maps(E, 2))
    assert edge_presence_maps == [{1: '01', 2: '01'}, {1: '01', 2: '10'},
                                  {1: '01', 2: '11'}, {1: '10', 2: '01'},
                                  {1: '10', 2: '10'}, {1: '10', 2: '11'},
                                  {1: '11', 2: '01'}, {1: '11', 2: '10'},
                                  {1: '11', 2: '11'}]
    
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
