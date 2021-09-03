"""
A reachable game is defined as (G, F) where G = (S_0, S_1, A) induced a
directed graph (S_0 U S_1, A) and F is a subset of S_1. A is a list of pairs
of elements of S_0 U S_1.
"""

import logging
import typing
from . import graph


class ReachabilityGame:

    __slots__ = ['vertices0', 'vertices1', 'finals', '_digraph', '_attractor']

    def __init__(self, vertices0: typing.Set[graph.Vertex],
                 vertices1: typing.Set[graph.Vertex],
                 finals: typing.Set[graph.Vertex],
                 digraph: typing.Any) -> typing.NoReturn:
        """Constructor method
        Builds a reachability game that takes place on the ``digraph``. The
        ``digraph`` must be an instance of a supported format. See
        `graph.AdjacencyMapGraph.create_instance` for more information about
        the different supported formats. The union of ``vertices0`` and
        ``vertices1`` must equals to the set of vertices of the digraph. Also,
        the set ``finals`` must be an non-empty subset of the set of vertices
        of the digraph.

        :raises ValueError: An error is raised if the sets ``vertices0``,
                            ``vertices1`` and ``finals`` don't statisfy the
                            conditions above.

        :param vertices0: The set of vertices owned by the player 0.
        :type vertices0: set of :class:`graph.Vertex`
        :param vertices1: The set of vertices owned by the player 1.
        :type vertices1: set of :class:`graph.Vertex`
        :param finals: The set of vertices the player 0 wants to reach.
        :type finals: set of :class:`graph.Vertex`
        :param digraph: The directed graph the game takes place on.
        :type digraph: any supported format
        """
        self.digraph = digraph
        V = set(self.digraph.vertices())
        if vertices0.union(vertices1) != V:
            raise ValueError('The union of the sets vertices0 and vertices1 '
                             'must equals to the set of vertices of the '
                             'digraph.')
        if len(finals) == 0 or not finals.issubset(V):
            raise ValueError('The set finals must be a subset of the set of '
                             'vertices of the digraph.')
        self.vertices0 = vertices0
        self.vertices1 = vertices1
        self.finals = finals

    @property
    def digraph(self): # pragma: no cover
        return self._digraph

    @digraph.setter
    def digraph(self, digraph: any) -> typing.NoReturn:
        self._digraph = graph.AdjacencyMapGraph.create_instance(digraph)

    @digraph.getter
    def digraph(self) -> graph.AdjacencyMapGraph:
        return self._digraph

    @property
    def attractor(self): # pragma: no cover
        return self._attractor

    @attractor.setter
    def attractor(self, attractor: typing.Set[graph.Vertex]) \
            -> typing.NoReturn:
        return self._attractor

    @attractor.getter
    def attractor(self) -> typing.Set[graph.Vertex]:
        if self._attractor is None:
            self._attractor = self._compute_attractor()
        return self._attractor

    def next_winning_moves(self, v: graph.Vertex) -> typing.List[graph.Vertex]:
        """
        Returns a list of next winning moves for player 0 if ``v`` is in
        ``vertices0`` or for player 1 otherwise. If there is no winning moves,
        an empty list is returned.

        :param v: The vertex the token is on.
        :type v: :class:`graph.Vertex`
        :returns: A list of next winning moves.
        :rtype: list of :class:`graph.Vertex`
        """
        if v in self.vertices0:
            return [u for u in self.digraph.neighbours(v, True) \
                    if u in self.attractor]
        else:
            return [u for u in self.digraph.neighbours(v, True) \
                    if u not in self.attractor]

    def _compute_attractor(self) -> typing.Set[graph.Vertex]:
        """
        Computes and returns the attractor set of this game.

        :returns: The attractor set.
        :rtype: set of :class:`graph.Vertex`
        """
        attractor = set()
        previous = dict()
        num_out_degree = dict()

        for v in self.digraph.vertices():
            previous[v] = set()
            num_out_degree[v] = 0

        for e in self.digraph.edges():
            previous[e.destination].add(e.origin)
            num_out_degree[e.origin] += 1

        propagate_stack = list(self.finals)
        while len(propagate_stack) > 0:
            vertex = propagate_stack.pop()
            attractor.add(vertex)

            for prev in previous[vertex]:
                num_out_degree[prev] -= 1
                if (prev in self.vertices0 or num_out_degree[prev] == 0) \
                        and prev not in attractor:
                    propagate_stack.append(prev)
        
        return attractor


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
