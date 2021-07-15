from multiprocessing import pool
import utils
import cop_robber_game as crg

import sys, os, time, re
from queue import Empty, Full
import multiprocessing as mp


def produce(V, E, sequence_length, k, problem_queue):
    """
    Initialize every "k"-cops and robber problem on edge periodic graph with a
    footprint ("V", "E") and edge pattern lengths of "sequence_length", and
    add them to the "problem_queue".
    :param V: A list of vertices
    :param E: A list of edges
    :param sequence_length: The length of the edge patterns
    :param k: The number of cops that take place in the game
    :param problem_queue: A thread-safe queue
    """
    for presence_map in utils.generate_edge_presence_maps(E, sequence_length):
        problem_queue.put((V, E, presence_map, k))
    print(f'{(2**sequence_length-1)**len(E)} problems produced')

def problem_consume(problem_queue, output_queue):
    """
    Take a problem from the "problem_queue" and decide if it's k-cop-win. If
    it is, then the it adds the presence_map in the "output_queue" in string.
    :param problem_queue: A thread-safe queue containing the problems
    :param output_queue: A queue to add the presence maps.
    """
    try:
        problem = problem_queue.get(timeout=3)
        if problem is None: return
        V, E, tau, k = problem
        if crg.is_kcop_win(V, E, tau, k):
            output_queue.put(f'{tau}\n')
        problem_queue.task_done()
    except Empty: pass


def output_consume(output_queue, output_file):
    """
    It writes every string in "output_queue" in the "output_file".
    :param output_queue: A queue containing strings
    :param output_file: A writable file
    """
    while True:
        try:
            out = output_queue.get(timeout=3)
            print(f'A {k}-cop-winning graph has been found!')
            output_file.write(out)
            output_file.flush()
            output_queue.task_done()
        except Empty: pass


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
    return f'HH:MM:SS = {int(hours)}:{int(minutes)}:{int(seconds)}'


if __name__ == '__main__':
    # TODO: Change the file format to JSON.
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

    MAX_SIZE_PROBLEMS_QUEUE = int(1e4)
    MAX_RESOLVER_PROCESSES = None # The pool will use all CPU available.

    
    print('Analyzing the arguments...')
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
    
    print('Initialization of the producer, the resolver and '\
        'the writer processes...')
    problem_queue = mp.JoinableQueue(MAX_SIZE_PROBLEMS_QUEUE)
    output_queue = mp.JoinableQueue()
    output_file = open(args[2], 'w')

    producer_process = mp.Process(target=produce,
            args=(V, E, length, k, problem_queue))
    consumers_pool = mp.Pool(processes=MAX_RESOLVER_PROCESSES,
            initializer=problem_consume,
            initargs=(problem_queue, output_queue))
    output_process = mp.Process(target=output_consume,
            args=(output_queue, output_file))
    
    print('Computing...')
    start_time = time.time_ns()
    
    output_process.start()
    # Writer process is ready to write k-cops-winnning graph.
    producer_process.start()
    # Producer process has starting to add problems to the queue.
    
    problem_queue.join()
    # All problems has been removed from the queue.
    consumers_pool.close()
    consumers_pool.join()
    # All problems has been resolved.

    output_queue.join()
    # All k-cops-winning graph has been written.

    # "Close" zombie processes.
    producer_process.join()
    output_process.terminate() # TODO: Must find another way...

    # Flush the buffer and close the file.
    output_file.close()
    print(f'Computing completed in {str_time_since(start_time)}')
