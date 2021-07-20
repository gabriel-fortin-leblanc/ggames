import timeit
import json, os, csv
from cop_robber_game import get_game_graph


PREFIX_TO_JSONS = 'graph_test_dir'
GRAPH_JSON_NAME = [
    'd_tree.json',
    'd_cycle_5.json',
    'd_hypercube_3.json',
]

graphs = []
print(os.getcwd())
for name in GRAPH_JSON_NAME:
    with open(os.path.join(PREFIX_TO_JSONS, name), 'r') as file:
        graph_str = file.read()
    json_object = json.loads(graph_str)
    V = json_object['V']
    E = list(map(tuple, json_object['E']))
    tau = {E[i]: seq for i, seq in enumerate(json_object['tau'])}
    graphs.append((V, E, tau))

"""
Analysis of cop_robber_game.get_game_graph
"""
NUMBER_TEST = 10 # Each call is expensive in time.
ks = [ 1, 2 ]
time_multithreaging = [[] for _ in range(len(GRAPH_JSON_NAME))]
time_no_multithreading = [[] for _ in range(len(GRAPH_JSON_NAME))]
for i, graph in enumerate(graphs):
    V, E, tau = graph
    for k in ks:
        mean = timeit.timeit('get_game_graph(V, E, tau, k)',
                globals=globals(), number=NUMBER_TEST)
        print(f'name = {GRAPH_JSON_NAME[i]}; k = {k}; THREADING; time = {mean}')
        time_multithreaging[i].append(mean)
        mean = timeit.timeit('get_game_graph(V, E, tau, k, False)',
                globals=globals(), number=NUMBER_TEST)
        print(f'name = {GRAPH_JSON_NAME[i]}; k = {k}; NO_THREADING; time = {mean}')
        time_no_multithreading[i].append(mean)

OUTPUT_NAME = 'output_analysis.csv'
FIELD_NAMES = ['name'] + [f'{k}t' for k in ks] + [str(k) for k in ks]
with open(OUTPUT_NAME, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, FIELD_NAMES)
    
    writer.writeheader()
    for i, name in enumerate(GRAPH_JSON_NAME):
        writer.writerow({
                **{'name': name},
                **{f'{k}t': time_multithreaging[i][j] for j, k in enumerate(ks)},
                **{str(k): time_no_multithreading[i][j] for j, k in enumerate(ks)}
                })
