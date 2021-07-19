from ast import parse
import sys, time, json, argparse
import multiprocessing as mp

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


ERROR_ARGS_MSG = \
'''Two file names must be specified as arguments. The first
file should contain an integer greater than 0 on the first
line that represents the number of cops, an integer greater than 0
on the second line that represents the length of the edge patterns
and a list of adjacency vertices on the third line in the following
format:\n
\t(1,2), (2,3), (1,3)\n
This is a list of couples of vertices.\n
The second file should contain the output of the program. If the
file doesn't exist, then it will be created. It contains every
presence mapping of the k-cop-winning graph, one per line.
*** Don't forget to check the permissions of the files. ***'''


def create_parser():
    """
    Create the arguments parser of the program.
    """
    parser = argparse.ArgumentParser(
            prog=PROGRAM_NAME,
            description=PROGRAM_DESCRIPTION)
    
    parser.add_argument('k')
    parser.add_argument('graph_file_path')
    parser.add_argument('--output_path', '-o')
    parser.add_argument('--verbose', '-v', action='store_true')
    parser.add_argument('--version', action='store_true')
    # All edge periodic graph with the length ?
    parser.add_argument('--all', '-a')
    # TODO : Should also add help. The description
    # should be better by including description of every argument.
    return parser


def extract_graph(graph_str):
    """
    Extract the graph from a string.
    :param graph_str: A graph in JSon format.
    """
    json_object = json.loads(graph_str)
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
        output.write(crg.is_kcop_win(graph[0], graph[1],
                tau=graph[2] if len(graph) == 2 else None, k=parsed_args.k))



if __name__ == '__main__':
    main(sys.argv[1:])
