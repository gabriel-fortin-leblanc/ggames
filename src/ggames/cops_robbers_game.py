"""
A Cops and Robbers game is played on an edge periodic (or static) graph
(V, E, tau) where tau is the presence mapping of the edges.
"""


from __future__ import annotations
import logging
import math, copy
import functools, itertools
import typing
from . import graph
from . import reachability_game as rg


class NPlayersCopsRobbersGame:
    """
    This class is the base class representing a cops and robbers game with N
    independant players. For every k in [1..N], the player k wins if he
    occupies the player k-1. Every cops and robbers game inherits from this
    one, or a subclass of it.
    """

    __slots__ = ['_players_count', '_graph', '_game_graph']

    def __init__(self, graph: typing.Any, n: int) -> typing.NoReturn:
        """Constructor method
        Builds an instance of cops and robbers game with ``n`` players that
        takes place on the ``graph``. The type of ``graph`` must be supported.
        See ``graph.AdjacencyMapGraph.create_instance`` for more information
        about the supported types of graph.

        :raises TypeError: An error is raised if ``graph`` is an instance of
                           an unsupported type.
        :raises ValueError: An error is raised if ``n`` is not greater than or
                            equal to 2.

        :param graph: The graph the game takes place on.
        :type graph: any
        :param n: The number of players in the game. This number must be
                  greater than 1.
        :type n: int
        """
        self.graph = graph
        self.player_count = n

    @property
    def players_count(self): # pragma: no cover
        return self._players_count

    @players_count.setter
    def players_count(self, players_count: int) -> typing.NoReturn:
        if players_count < 2:
            raise ValueError('The attribute players_count must be greater '
                'than 1.')
        self._players_count = players_count

    @players_count.getter
    def players_count(self) -> int:
        return self._players_count

    @property
    def graph(self): # pragma: no cover
        return self._graph

    @graph.setter
    def graph(self, graph: typing.Any) -> typing.NoReturn:
        self._graph = graph.AdjacencyMapGraph.create_instance(graph)

    @graph.getter
    def graph(self) -> typing.Type[graph._Graph]:
        return self._graph

    @property
    def game_graph(self): # pragma: no cover
        return self._game_graph

    @game_graph.setter
    def game_graph(self, game_graph: typing.Type[graph._Graph]) \
                   -> typing.NoReturn:
        self._game_graph = game_graph

    @game_graph.getter
    def game_graph(self) -> typing.Type[graph._Graph]:
        if self._game_graph is None:
            self._game_graph = self._compute_game_graph()
        return self._game_graph

    def _terminale_condition(self, state: typing.Tuple) -> typing.NoReturn:
        """
        Returns `True` if the ``state`` is a terminal one, `False` otherwise.

        :param state: A state (configuration) of the game.
        :type state: tuple
        :returns: `True` if the ``state`` is a terminal one.
        :rtype: bool
        """
        positions = state[:-1]
        for k in range(1, len(positions)):
            if positions[k] == positions[k-1]:
                return True
        return False

    def _compute_game_graph(self) -> graph.AdjacencyMapGraph:
        """
        Computes and returns the game graph of the game.

        :returns: A directed graph where each vertex is a state of the game and
                  the arcs represent the transition function between the
                  states.
        :rtype: :class:`AdjacencyMapGraph`
        """
        game_graph = graph.AdjacencyMapGraph()
        for s in range(self.players_count):
            for pos in itertools.product(self._graph.vertices(),
                                         repeat=self.players_count):
                state = (*pos, s)
                game_graph.insert_vertex(state)
                if self._terminal_condition(state):
                    continue
                for next_pos in self._graph.neighbours(pos[s]):
                    next_state = (*pos[:s], next_pos, *pos[s+1:], s+1)
                    game_graph.insert_edge(state, next_state)
        return game_graph

    def _compute_reachability_game(self, n: int) \
                                   -> reachability_game.ReachabilityGame:
        """
        Computes and returns a reachability game where the reachable set of the
        game is composed of the set where the player ``n`` in the cops and
        robbers game wins.

        :raises ValueError: An error is raised if n is not between 0 and
                            ``players_count``.

        :param n: The player of the cops and robbers game for which his winning
                  induces the reachable set. The integer ``n`` must be between
                  0 and ``players_count``.
        :type n: int
        :returns: The reachability game induced by the cops and robbers game.
        :rtype: reachability_game.ReachabilityGame
        """
        if n < 0 or n >= self.players_count:
            raise ValueError('The integer ``n`` must be between 0 and the '
                'attribute players_count.')

        v0 = set()
        v1 = set()
        finals = set()
        for v in self.game_graph.vertices():
            *pos, s in v.value
            pos_set = set(pos)
            if s == n:
                v0.add(v)
            else:
                v1.add(v)

            if n == 0 and self.game_graph.degree(v, True) == 0 and \
                    len(pos_set) == self.players_count:
                finals.add(v)
            elif len(pos_set) == self.players_count - 1 and \
                    pos[n] == pos[n - 1]:
                finals.add(v)
        return rg.ReachabilityGame(self.game_graph, v0, v1, finals)

    def is_n_player_win(self, n: int) -> bool:
        """
        Returns `True` if the player ``n`` wins, `False` otherwise.

        :param n: The interesting player.
        :type n: int
        :returns: `True` if the graph is n-player-winning, `False` otherwise.
        :rtype: bool
        """
        return not self._compute_reachability_game(n).who_win()


def get_game_graph(V, E, tau=None, k=1):
    """
    Compute the game graph where the "k"-cops and robbers game takes place on
    the edge periodic graph (V, E, tau). If "tau" is not specified, then the
    graph is considered to be static.
    :param V: The list of vertices
    :param E: The list of edges
    :param tau: The presence function of the edges in E in dict
    :param k: The number of cops in the game
    """
    logger = logging.getLogger('main.cops_robbers_game')
    logger.info('"cops_robbers_game.get_game_graph" called.')

    if tau is None: tau = {e: '1' for e in E}

    # Compute an adjacency matrix to simplify the algorithm.
    vertex_index = {u: index for index, u in enumerate(V)}
    adjacency = [[tau[(u, v)] if (u, v) in tau else
                    tau[(v, u)] if (v, u) in tau else
                    '1' if u == v else
                    '0' for u in V] for v in V]
    
    # Compute the least common multiple.
    pattern_lengths = list(map(len, tau.values()))
    time_horizon = functools.reduce(lambda x,y: abs(x*y) // math.gcd(x,y),
            pattern_lengths)

    # Compute the set of vertices of the game graph.
    V_gg = []; A_gg = []
    for t in range(time_horizon):
        for s in [False, True]:
            for *c, r in itertools.product(V, repeat=k+1):
                u = (*c, r, s, t)
                V_gg.append(u)
                if r in c: continue

                next_s = not s
                if s: # Robber's move
                    for next_r in V:
                        edge_pattern = adjacency[vertex_index[r]] \
                                [vertex_index[next_r]]
                        if edge_pattern[t%len(edge_pattern)] == '0' \
                                or next_r in c:
                            continue
                        A_gg.append((u, (*c, next_r, next_s,
                                (t+1)%time_horizon)))
                else: # Cops' move
                    for next_c in itertools.product(V, repeat=k):
                        valid_flag = True # This can be more effective
                        for i in range(len(c)):
                            edge_pattern = adjacency[vertex_index[c[i]]] \
                                    [vertex_index[next_c[i]]]
                            if c[i] != next_c[i] and \
                                    edge_pattern[t%len(edge_pattern)] == '0':
                                # It is impossible for a cops to move in
                                # one rounds to a non adjacent vertex.
                                valid_flag = False
                                break
                        if valid_flag:
                            A_gg.append((u, (*next_c, r, next_s,t)))

    return V_gg, A_gg


def game_graph_to_reachability_game(V_gg, A_gg):
    """
    Compute and return a reachable game corresponding to the game graph
    G = (V_gg, A_gg).
    :param V_gg: A list of vertices of a game graph
    :param A_gg: A list of edges of a game graph
    """
    logger = logging.getLogger('main.com_robber_game')
    logger.info('"cops_robbers_game.game_graph_to_reachability_game" called.')

    S0 = []; S1 = []
    A = copy.deepcopy(A_gg)
    F = []
    for v in V_gg:
        *c, r, s, t = v
        if r in c:
            F.append(v)
        if s:
            S1.append(v)
        else:
            S0.append(v)
    return S0, S1, A, F


def is_kcop_win(V, E, tau=None, k=1):
    """
    Compute if the time-varying graph ("V", "E", "tau") is "k"-cop win.
    :param V: A set of vertices
    :param E: A set of edges
    :param tau: A map from E to a set of bit sequences
    :param k: The number of cops that play on the time-varying graph
    """
    logger = logging.getLogger('main.com_robber_game')
    logger.info('"cops_robbers_game.is_kcop_win" called.')

    attractor = rg.get_attractor(
            *game_graph_to_reachability_game(
            *get_game_graph(V, E, tau, k)))

    n = len(V)
    starting_classes = dict()
    for *c, r, s, t in attractor:
        c = tuple(c)
        if t == 0 and not s:
            if c not in starting_classes:
                starting_classes[c] = set()
            starting_classes[c].add(r)
    for cls in starting_classes.values():
        if len(cls) == n:
            return True
    return False
