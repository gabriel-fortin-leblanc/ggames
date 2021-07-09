import queue
import computer
import itertools
from multiprocessing import Process, Lock, Queue


def produce(V, E, k, sequence_length, queue, lock):
    for tvg in computer.generate_periodic_edge_graph((V, E), sequence_length):
        queue.put((tvg, k))
    with lock:
        print('Problems produced')

def consume(queue, lock):
    pass


if __name__ == '__main__':
    V = []; E =[]
    k = 2; sequence_length = 10
    problem_queue = Queue()
    print_lock = Lock()
    
    producer = Process(target=produce,
            args=(V, E, k, sequence_length, queue, print_lock))
    producer.start()

    
