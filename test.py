from cop_robber_game import *
from reachable_game import *

V = list(range(12))
E = [(0,1),(0,2),(0,3), (0,9),(0,10),(0,11),  (1,2),  (2,3),  (3,4),(3,6),  (4,5),(4,6),  (5,6),  (6,7),(6,8),(6,9),  (7,8),  (8,9),  (9,10), (10,11)]
tau = {e:'1' for e in E}
tau[(0,2)] = '000100'
tau[(0,3)] = '001000'
tau[(2,3)] = '010000'
tau[(3,4)] = '100'
tau[(3,6)] = '100'
tau[(4,6)] = '010'
k = 2

print(is_kcop_win(V, E, tau, k))
