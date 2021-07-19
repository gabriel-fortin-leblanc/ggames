import utils
from queue import Empty, Full
import cop_robber_game as crg
import time
import multiprocessing as mp


def str_time_since(start):
    """
    Return a string that represents the time passed since "start".
    :param start: An integer representing the time in nanoseconds
    """
    HOURS_TO_NANOSECONDS = 3.6e12
    MINUTES_TO_NANOSECONDS = 6e10
    SECONDS_TO_NANOSECONDS = 1e9

    delta_time = time.time_ns() - start
    hours = delta_time // HOURS_TO_NANOSECONDS
    delta_time -= hours * HOURS_TO_NANOSECONDS
    minutes = delta_time // MINUTES_TO_NANOSECONDS
    delta_time -= minutes * MINUTES_TO_NANOSECONDS
    seconds = delta_time // SECONDS_TO_NANOSECONDS
    return f'HH:MM:SS = {int(hours)}:{int(minutes)}:{int(seconds)}'


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
    # TODO: Manage logger
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
            output_file.write(out)
            output_file.flush()
            output_queue.task_done()
        except Empty: pass

def compute_all_problems(V, E, sequence_length, k, output,
        max_problem_queue_size=100, max_resolver_processes=5):
    problem_queue = mp.JoinableQueue(max_problem_queue_size)
    output_queue = mp.JoinableQueue()

    producer_process = mp.Process(target=produce,
            args=(V, E, sequence_length, k, problem_queue))
    consumers_pool = mp.Pool(processes=max_resolver_processes,
            initializer=problem_consume,
            initargs=(problem_queue, output_queue))
    output_process = mp.Process(target=output_consume,
            args=(output_queue, output))
    
    output_process.start()
    producer_process.start()

    problem_queue.join()
    consumers_pool.close()
    consumers_pool.join()

    output_queue.join()
    producer_process.join()
    output_process.terminate() # TODO: Must find another way...

    output.close()
