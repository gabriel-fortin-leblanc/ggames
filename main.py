from multiprocessing import pool
import utils
import cop_robber_game as crg

import sys, os, time, re
import multiprocessing as mp


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
        print(f'{(2**sequence_length-1)**len(E)} problems produced')

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


def str_time_since(start):
    """
    Return a string that represents the time passed since "start".
    :param start: An integer representing the time in nanoseconds
    """
    HOURS_TO_NANOSECONDS = 3.6e12
    MINUTES_TO_NANOSECONDS = 6e10
    SECONDS_TO_NANOSECONDS = 1e9

    delta_time = time.time_ns() - start_time
    hours = delta_time // HOURS_TO_NANOSECONDS
    delta_time -= hours * HOURS_TO_NANOSECONDS
    minutes = delta_time // MINUTES_TO_NANOSECONDS
    delta_time -= minutes * MINUTES_TO_NANOSECONDS
    seconds = delta_time // SECONDS_TO_NANOSECONDS
    return f'HH:MM:SS = {hours}:{minutes}:{seconds}'


if __name__ == '__main__':
    ERROR_ARGS_MSG = \
'''Two file names must specified as argument. The first
one is a file containing an integer greater than 0 on the first
line that represents the number of cops, an integer greater than 0
that represents the length of the edge patterns on the second line
and a list of adjancy vertices on the third line in the following
format:\n
\t(1,2), (2,3), (1,3)\n
This is a list of couples of vertices.\n
The second file will contain the output of the program. If the
file doesn't exist, then it will be created. It contains every
presence mapping of k-cop-winning graph, one per line.
*** Don't forget to check the permissions of the files. ***'''

    MAX_SIZE_PROBLEMS_QUEUE = 1000

    
    print('Analyzing the arguments...')
    start_time = time.time_ns()
    args = sys.argv
    if len(args) != 3 or not os.access(args[1], os.R_OK):
        exit(ERROR_ARGS_MSG)
    if os.access(args[2], os.F_OK) and not os.access(args[2], os.W_OK):
        exit(ERROR_ARGS_MSG)
    
    V = set(); E = list()
    k = None; length = None; adjancy = list()
    file_str = None
    with open(args[1], 'r') as file:
        file_str = file.read().split('\n')
    if len(file_str) != 3:
        exit(ERROR_ARGS_MSG)
    try:
        k = int(re.search(r'\s*(\d+)\s*', file_str[0]).group(0))
        length = int(re.search(r'\s*(\d+)\s*', file_str[1]).group(0))
        for edge_str in re.findall(r'\((.+?)\)',
                file_str[2].replace(' ', '')):
            edge_str = edge_str.split(',')
            u = int(edge_str[0]); v = int(edge_str[1])
            V.add(u); V.add(v)
            E.append((u, v))
    except:
        exit(ERROR_ARGS_MSG)
    V = list(V)
    print(f'Analizing completed in {str_time_since(start_time)}')
    
    print('Initialization of the producer and the consumers...')
    start_time = time.time_ns()
    queue = mp.Queue(MAX_SIZE_PROBLEMS_QUEUE)
    lock = mp.Lock()
    file = open(args[2], 'w')
    producer = mp.Process(target=produce, args=(V, E, length, k, queue, lock))
    consumers_pool = mp.Pool(initializer=consume,
            initargs=(queue, lock, file))
    print(f'Initialization completed in {str_time_since(start_time)}')
    
    print('Computing...')
    start_time = time.time_ns()
    producer.start()
    producer.join()
    while not queue.empty():
        time.sleep(5)
    queue.close()
    queue.join_thread()
    consumers_pool.close()
    consumers_pool.join()
    print(f'Computing completed in {str_time_since(start_time)}')
