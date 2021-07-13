import utils
import cop_robber_game as crg
from multiprocessing import Lock, Queue


def produce(V, E, sequence_length, k, queue, printing_lock):
    """
    Initialize every "k"-cops and robber problem on edge periodic graph with a
    footprint ("V", "E") and edge pattern lengths of "sequence_length", and
    add them to the "queue". The "printing_lock" is used for printing logs.
    :param V: A list of vertices
    :param E: A list of edges
    :param sequence_length: The length of the edge patterns
    :param k: The number of cops that take place in the game
    :param queue: A thread-safe queue
    :param printing_lock: A lock for use the standard output
    """
    for presence_map in utils.generate_edge_presence_maps(E, sequence_length):
        queue.put((V, E, presence_map, k))
    with printing_lock:
        print(f'{2**sequence_length**len(E)} problems produced')

def consume(queue, printing_lock, output_file):
    """
    Take a problem from the "queue" and decide if it's k-cop-win. If it is,
    then the it writes the presence_map in the "output_file" using the
    "printing_lock".
    :param queue: A thread-safe queue containing the problems
    :param printing_lock: A lock for use the standard output and an output
                          file
    :param output_file: The file to write the presence maps.
    """
    V, E, tau, k = queue.get()
    if crg.is_kcop_win(V, E, tau, k):
        with printing_lock:
            print(f'A {k}-cop-winning graph has been found!')
            output_file.write(f'{tau}\n')


if __name__ == '__main__':
    V = []; E =[]
    k = 2; sequence_length = 10
    problem_queue = Queue()
    print_lock = Lock()

    
