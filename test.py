from cop_robber_game import *
from reachable_game import *
import time

V = list(range(12))
E = [(0,1),(0,2),(0,3), (0,9),(0,10),(0,11),  (1,2),  (2,3),  (3,4),(3,6),  (4,5),(4,6),  (5,6),  (6,7),(6,8),(6,9),  (7,8),  (8,9),  (9,10), (10,11)]
tau = {e:'11001' for e in E}
"""
tau[(0,2)] = '0001'
tau[(0,3)] = '0010'
tau[(2,3)] = '0100'
tau[(3,4)] = '1001'
tau[(3,6)] = '1011'
tau[(4,6)] = '0101'
"""
k = 2

start = time.time_ns()
V_gg, A_gg = get_game_graph(V, E, tau, k)
print(f'|V_gg| = {len(V_gg)}\n|A_gg| = {len(A_gg)}\nTime = {(time.time_ns() - start)/1e9}')

start = time.time_ns()
S0, S1, A, F = game_graph_to_reachable_game(V_gg, A_gg)
print(f'Time = {(time.time_ns() - start)/1e9}')

start = time.time_ns()
attractor = get_attractor(S0, S1, A, F)
print(f'Time = {(time.time_ns() - start)/1e9}')
