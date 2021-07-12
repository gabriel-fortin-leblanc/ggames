import itertools


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
