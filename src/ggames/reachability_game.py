"""
A reachable game is defined as (G, F) where G = (S_0, S_1, A) induced a
directed graph (S_0 U S_1, A) and F is a subset of S_1. A is a list of pairs
of elements of S_0 U S_1.
"""

import logging
from typing import Type, Any


class ReachabilityGame:

    __slots__ = ['vertices0', 'vertices1', 'digraph', 'finals', '_attractor']

    def __init__(self, vertices0: list, vertices1: list,
                 digraph: Any, finals: set) -> None:
        self.vertices0 = vertices0
        self.vertices1 = vertices1
        self.digraph = digraph
        self.finals = finals
        self._attractor = None

    @property
    def attractor(self):
        # TODO: The documentation about this property should be placed here.
        pass

    @attractor.getter
    def attractor(self):
        if self._attractor is None:
            self._attractor = self._compute_attractor()
        return self._attractor

    def who_wins(self, n:int) -> bool:
        starting_classes = dict()
        for *c, r, s, t in self.__getattribute__('attractor'):
            c = tuple(c)
            if t == 0 and not s:
                if c not in starting_classes:
                    starting_classes[c] = set()
                starting_classes[c].add(r)
        for cls in starting_classes.values():
            if len(cls) == n:
                return True
        return False

    def next_winning_moves(self, previous: Any, deg: Any) -> list:
        in_attractor = dict()
        S0_set = set(self.vertices0)
        propagate_stack = list(self.finals)

        for v in self.vertices0 + self.vertices1:
            in_attractor[v] = False

        while len(propagate_stack) > 0:
            vertex = propagate_stack.pop()
            in_attractor[vertex] = True

            for prev in previous[vertex]:
                deg[prev] -= 1
                if (prev in S0_set or deg[prev] == 0) \
                        and not in_attractor[prev]:
                    propagate_stack.append(prev)

        return [vertex for vertex, is_in_attractor in in_attractor.items()
                if is_in_attractor]

    def _compute_attractor(self) -> set:
        previous = dict()
        num_out_degree = dict()

        for v in self.vertices0 + self.vertices1:
            previous[v] = set()
            num_out_degree[v] = 0

        for u, v in self.digraph:
            previous[v].add(u)
            num_out_degree[u] += 1

        return set(self.next_winning_moves(previous, num_out_degree))


def get_attractor(S0, S1, A, F):
    """
    Compute the attractor set.
    Credit: Dietmar Berwanger in "Graph games with perfect information"
    This algorithm has been modified to not use recursion.
    :param S0: A list of vertices
    :param S1: A list of vertices (must be disjointed of S0)
    :param A: A sub-list (subset) of S0 x S1 U S1 x S0
    :param F: A sub-list (subset) of S1 as list.
    """
    logger = logging.getLogger('main.reachability_game')
    logger.info('"reachability_game.get_attractor" called.')
    
    in_attractor = dict()
    previous = dict()
    num_out_degree = dict()
    S0_set = set(S0)

    for v in S0 + S1:
        in_attractor[v] = False
        previous[v] = set()
        num_out_degree[v] = 0
    
    for u, v in A:
        previous[v].add(u)
        num_out_degree[u] += 1
    
    propagate_stack = list(F)
    while len(propagate_stack) > 0:
        vertex = propagate_stack.pop()
        in_attractor[vertex] = True

        for prev in previous[vertex]:
            num_out_degree[prev] -= 1
            if (prev in S0_set or num_out_degree[prev] == 0) \
                    and not in_attractor[prev]:
                propagate_stack.append(prev)
    
    return [vertex for vertex, is_in_attractor in in_attractor.items()
                if is_in_attractor]


def get_next_winning_moves(current_vertex, A, attractor, player0_move=True):
    """
    Compute a list of next moves that lead to a winning game for the player 0
    if "player0_move" with respect to the game on the graph with the set of
    arcs "A", its attractor set "attractor" and the vertex "current_vertex"
    the token is on.
    :param current_vertex: A vertex
    :param A: A list of arcs
    :param attractor: A list representing the attractor set.
    :param player0_move: A flag meaning that it's player 0's turn to play.
    """
    logger = logging.getLogger('main.reachability_game')
    logger.info('"reachability_game.get_next_winning_moves" called.')

    attractor_set = set(attractor)
    if player0_move:
        return [v for u, v in A if u == current_vertex and v in attractor_set]
    else:
        return [v for u, v in A if u == current_vertex and
            v not in attractor_set]
