from ast import parse
import sys, time, json, argparse
import multiprocessing as mp
from itertools import chain

import cop_robber_game as crg
import computer


PROGRAM_NAME = 'Cop-number computer'
PROGRAM_DESCRIPTION = \
'''This program takes a cop-number problem and decides if it is a k-cop-
winning graph. The graph can be either static or edge periodic. It proceeds
by reducing the problem to a reachability game.'''
PROGRAM_VERSION = \
'''''' # TODO: To complete

ERROR_JSON_MSG = \
'''The JSon is not well formatted.'''
ERROR_OPENING_OUTPUT_FILE_MSG = \
'''The output file cannot be opened. Check the permissions of the directory,
or if the file exists and cannot be overwritten.'''
ERROR_OPENING_GRAPH_FILE_MSG = \
'''The file containing the graph cannot be opened. Check if the file exists
and if the permission of reading is granted.'''

def create_parser():
    """
    Create the arguments parser of the program.
    """
    parser = argparse.ArgumentParser(
            prog=PROGRAM_NAME,
            description=PROGRAM_DESCRIPTION)
    
    parser.add_argument('k', type=int, help="the number of cops in the\
                        game. (Mandatory)")
    parser.add_argument('graph_file_path', help="the path to the file\
                        containing the description of the graph. (Mandatory)")
    parser.add_argument('--output_path', '-o', help="specify the path to\
                        the output file containing the presence mapping of\
                        the k-cop-win graph.")
    parser.add_argument('--verbose', '-v', action='store_true', help="output \
                        more information.") # TODO: Needs improvement
    parser.add_argument('--version', action='store_true', help="show the \
                        current version of the program.")
    # All edge periodic graph with the length ?
    parser.add_argument('--all', '-a', help="compute all snapshots of the \
                    graph.") # TODO: Needs improvement
    return parser


def extract_graph(graph_str):
    """
    Extract the graph from a string.
    :param graph_str: A graph in JSon format.
    """
    json_object = json.loads(graph_str)

    # Validate that the list of edges does not contain inexistent vertices.
    for i in set(list(chain(*json_object['E']))):
        if i not in json_object['V']:
            raise ValueError("Unexpected value detected in 'E' variable.")
    
    if 'tau' in graph_str:
        #Validate that every edge has a corresponding binary string.
        if len(json_object['E']) != len(json_object['tau']):
            raise ValueError("Unexpected number of elements in 'tau' variable.")
        
        # Validate that all elements in 'tau' are composed of binary strings.
        for binary_str in set(json_object['tau']):
            if not all(x in "01" for x in binary_str):
                raise ValueError("Unexpected value detected in 'tau' variable.")
    return json_object['V'], map(tuple, json_object['E'])




def main(args):
    parser = create_parser()
    parsed_args = parser.parse_args(args)
    
    if parsed_args.version:
        # If this argument is present, then we show the version and forget
        # the other arguements.
        print(PROGRAM_VERSION)
        exit(0)
    
    if parsed_args.output_path is not None:
        # If an output path is given, it will be used to output the result.
        # Otherwise, the standard output will be used.
        try:
            output = open(parsed_args.output_path, 'w')
        except OSError as error:
            sys.stderr.write(f'{ERROR_OPENING_OUTPUT_FILE_MSG}\n'\
                    '{error.strerror}')
            exit(error.errno)
    else:
        output = sys.stdout
    
    # Get the graph
    try:
        file = open(parsed_args.graph_file_path, 'r')
        graph_str = file.read()
        file.close()
    except OSError as error:
        sys.stderr.write(f'{ERROR_OPENING_GRAPH_FILE_MSG}\n'\
                '{error.strerror}')
        exit(error.errno)
    try:
        graph = extract_graph(graph_str)
    except json.JSONDecodeError as error:
        sys.stderr.write(f'{ERROR_JSON_MSG}\n{error.msg}')
        exit(1) # TODO: Find the proper error code for not well formatted JSON
    
    if parsed_args.all:
        computer.compute_all_problems(graph[0], graph[1], parsed_args.all,
                parsed_args.k, output)
    else:
        output.write(str(crg.is_kcop_win(graph[0], graph[1],
                tau=graph[2] if len(graph) == 3 else None, k=parsed_args.k)))



if __name__ == '__main__':
    main(sys.argv[1:])
