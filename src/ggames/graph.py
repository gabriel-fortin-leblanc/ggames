"""
This module provides a interface for graphs that is used in this package.
"""
from __future__ import annotations
import collections
import typing


class Vertex:
    """
    A class representing a vertex. This is a wrapper for a value.
    """

    __slots__ = ['_value']

    def __init__(self, value: typing.Optional(typing.Hashable)=None) \
                 -> typing.NoReturn:
        """Constructor method
        Builds a new vertex.

        :raises TypeError: An error is raised if ``value`` is not hashable.

        :param value: The ``value`` the vertex wraps. It must be hashable.
        :type value: any
        """
        self.value = value

    @property
    def value(self): # pragma: no cover
        self._value

    @value.setter
    def value(self, value: typing.Hashable) -> typing.NoReturn:
        hash(value) # Check if value is hashable.
        self._value = value

    @value.getter
    def value(self) -> typing.Any:
        return self._value

    def __eq__(self, v: Vertex) -> bool:
        """
        Returns `True` if the value of ``v`` is equal to the value of this
        instance, `False` otherwise.

        :param v: A vertex to compare.
        :type v: Vertex
        :returns: `True` if the two vertices are equal, `False` otherwise.
        :rtype: bool
        """
        return self.value == v.value

    def __ne__(self, v: Vertex) -> bool:
        """
        Returns `True` if the value of ``v`` is not equal to the value of this
        instance, `False` otherwise.

        :params v: A vertex to compare.
        :type: Vertex
        :returns: `True` if the two vertices are not equal, `False` otherwise.
        :rtype: bool
        """
        return not self.__eq__(v)

    def __str__(self) -> str:
        """
        Returns the string representation of this vertex. It calls the __str__
        magic method of the value wrapped in this format Vertex(``value``).

        :returns: Returns a string representation of the instance.
        :rtype: str
        """
        return f'Vertex({self.value})'

    def __hash__(self) -> int:
        """
        Returns a hashing representation of the ``value`` of the instance.

        :returns: The hashing representation of the ``value``.
        :rtype: int
        """
        return hash(self.value)


class Edge:
    """
    This class represents an edge. It can be either oriented or not since
    it contains two attributes ``origin`` and ``destination`` that may express
    an orientation.
    """

    __slots__ = ['_origin', '_destination', '_value']

    def __init__(self, origin: Vertex, destination: Vertex,
                 value: typing.Optional(typing.Hashable)=None) \
                 -> typing.NoReturn:
        """Constructor method
        Builds an edge from the two vertices ``origin`` and ``destination``. 
        It can be considered oriented or not.

        :raises TypeError: An error is raised if ``origin`` or ``destination``
                           is not an instance of the :class:`Vertex`, or even
                           if the ``value`` is not hashable.

        :param origin: The origin vertex if it's oriented, or simply one of
                       the two vertices.
        :type origin: Vertex
        :param destination: The destination vertex if it's oriented, or simply
                            one of the two vertices.
        :type destination: Vertex
        :param value: A value that can be used as an attribute of the edge.
                      This value is optional and must be hashable.
        :type value: any
        """
        self.origin = origin
        self.destination = destination
        self.value = value

    @property
    def origin(self): # pragma: no cover
        return self._origin

    @origin.setter
    def origin(self, origin: Vertex) -> typing.NoReturn:
        if type(origin) is not Vertex:
            raise TypeError('The attribute origin must be of type Vertex.')
        self._origin = origin

    @origin.getter
    def origin(self) -> Vertex:
        return self._origin

    @property
    def destination(self): # pragma: no cover
        return self._destination

    @destination.setter
    def destination(self, destination: Vertex) -> typing.NoReturn:
        if type(destination) is not Vertex:
            raise TypeError('The attribute destination must be of type '
                'Vertex.')
        self._destination = destination

    @destination.getter
    def destination(self) -> Vertex:
        return self._destination

    @property
    def value(self): # pragma: no cover
        return self._value

    @value.setter
    def value(self, value: typing.Hashable) -> typing.NoReturn:
        hash(value) # Check if value is hashable.
        self._value = value

    @value.getter
    def value(self) -> typing.Any:
        return self._value

    def endpoints(self) -> typing.Tuple[Vertex, Vertex]:
        """
        Returns a tuple containing the vertices ``origin`` and ``destination``.

        :returns: A tuple containing the two vertices that composed the edge.
                  Since it can be oriented, the position is
                  (``origin``, ``destination``).
        :rtype: tuple(Vertex, Vertex)
        """
        return (self.origin, self.destination)

    def opposite(self, v: Vertex) -> Vertex:
        """
        Returns the opposite vertex of ``v``. If ``v`` is not part of this
        edge, None is returned.

        :param v: A vertex contained in the edge.
        :type v: Vertex
        :returns: The opposite vertex of ``v``.
        :rtype: Vertex
        """
        if self.origin == v:
            return self.destination
        elif self.destination == v:
            return self.origin
        else:
            return None

    def __str__(self) -> str:
        """
        Returns a string representation of this edge in this format
        Edge(``origin``, ``destination``, ``value``) if the value exists
        otherwise the last attribute is skipped.

        :returns: A string representation of this edge.
        :rtype: str
        """
        return f'Edge({self.origin}, {self.destination}' +\
            (f', {self.value})' if self.value is not None else ')')

    def __eq__(self, e: Edge) -> bool:
        """
        Returns True if the edge ``e`` is equal to this one, False otherwise.
        For two edges to be equal, each of their attributes must also be equal.

        :param e: The other edge to compare with.
        :type e: Edge
        :returns: True if the two edges are equal or False otherwise.
        :rtype: bool
        """
        return self.origin == e.origin and \
               self.destination == e.destination and \
               self.value == e.value

    def __ne__(self, e: Edge) -> bool:
        """
        Returns True if the edge ``e`` is not equal to this one, False
        otherwise. It uses __eq__ to compute it.

        :param e: The edge to compare with.
        :type e: Edge
        :returns: True if the two edges are not equal.
        :rtype: bool
        """
        return not self.__eq__(e)

    def __contains__(self, v: Vertex) -> bool:
        """
        Returns if the vertex v is one of the endpoints.

        :param v: The vertex to check.
        :type v: Vertex
        :returns: True if one of his vertices is equal to ``v`` or False
                  otherwise.
        :rtype: bool
        """
        return self.origin == v or self.destination == v

    def __hash__(self) -> int:
        """
        Returns a hash representation of the instance.

        :returns: A hash representation of the instance.
        :rtype: int
        """
        return hash((self._origin, self._destination, self._value))


class _Graph: # pragma: no cover
    """
    The abstract data type graph. This class must not be instanciate. It is
    only used as interface. It provides a wrapper to not be dependant of a
    specific library.
    """

    def vertices(self) -> typing.List[Vertex]:
        """
        Returns a list of the vertices of the graph.
        """
        raise NotImplemented()

    def edges(self) -> typing.List[Edge]:
        """
        Returns a list of edges of the graph.
        """
        raise NotImplemented()

    def vertex_count(self) -> int:
        """
        Returns the number of vertices the graph contains.
        """
        raise NotImplemented()

    def edge_count(self) -> int:
        """
        Returns the number of edges the graph contains.
        """
        raise NotImplemented()

    def has_edge(self, e: Edge) -> bool:
        """
        Returns if the edge ``e`` is in the graph.
        """

    def get_edge(self, u: Vertex, v: Vertex) -> Edge:
        """
        Return the edge composed of the origin u to the destination v if it's
        in the graph.
        """
        raise NotImplemented()

    def degree(self, v: Vertex, out: bool=False) -> int:
        """
        Returns the degree of the vertex v. Only the out degree of ``v`` is
        returned if ``out`` is True. To get the in degree of ``v``, the user
        can use *G.degree(v, False) - G.degree(v)* for a given graph *G*.
        """
        raise NotImplemented()

    def neighbours(self, v: Vertex, out: bool=False) -> List[Vertex]:
        """
        Returns a list of all adjacency vertices of ``v``. If ``out`` is True,
        then the edges are considered oriented and only the out adjacency
        vertices of ``v`` are returned.
        """
        raise NotImplemented()

    def incident_edges(self, v: Vertex, out: bool=False) -> typing.List[Edge]:
        """
        Returns a list of the incident edges of the vertex v.
        """
        raise NotImplemented()

    def insert_vertex(self, v: Vertex) -> bool:
        """
        Inserts the vertex v in the graph.
        """
        raise NotImplemented()

    def insert_edge(self, u: Vertex, v: Vertex,
                    value: typing.Optional(typing.Any)=None) -> bool:
        """
        Inserts the edge (u, v) in the graph. If a vertex doesn't exist in
        the graph, it will be added.
        """
        raise NotImplemented()

    def remove_vertex(self, v: Vertex) -> bool:
        """
        Removes the vertex v from the graph. Every incident edge will be also
        deleted.
        """
        raise NotImplemented()

    def remove_edge(self, e: Edge) -> bool:
        """Remove the edge e from the graph."""
        raise NotImplemented()


class AdjacencyMapGraph(_Graph):
    """
    A graph implemented with an adjacency hash table. It follows the interface
    :class:`Graph`.
    """

    __slots__ = ['_adjacency_map', '_edge_count']

    @staticmethod
    def create_instance(graph: typing.Any) -> AdjacencyMapGraph:
        """
        Returns a graph instance of :class:`AdjacencyMapGraph` from another
        type of graph.
        The types of graph supported are:
            * AdjacencyMapGraph
        If ``graph`` is an instance of :class:`AdjacencyMapGraph`, then a deep
        copy is processed.

        :raises TypeError: An error is returned if ``graph`` is an instance of
                           an unsupported type.

        :param graph: The graph to represent as :class:`AdjacencyMapGraph`.
        :type graph: A supported type of graph as specified above.
        :returns: A copy of ``graph`` as :class:`AdjacencyMapGraph`.
        :rtype: :class:`AdjacencyMapGraph`.
        """
        if type(graph) is AdjacencyMapGraph:
            return AdjacencyMapGraph.copy(graph)
        raise TypeError(f'The type {type(graph)} is not supported as a graph.')

    @staticmethod
    def copy(graph: AdjacencyMapGraph) -> AdjacencyMapGraph:
        """
        Returns a deep copy of an AdjacencyMapGraph instance.

        :param graph: The graph to copy.
        :type graph: :class:`AdjacencyMapGraph`
        :returns: A deep copy of the ``graph``. Each vertex is a copy and each
                  edge is also a copy. Only the values of the components remain
                  the same.
        :rtype: :class:`AdjacencyMapGraph`.
        """
        graph_copy = AdjacencyMapGraph()
        for v in graph.vertices():
            graph_copy.insert_vertex(Vertex(v.value))
        for e in graph.edges():
            graph_copy.insert_edge(e.origin, e.destination, e.value)
        return graph_copy

    def __init__(self) -> typing.NoReturn:
        """Constructor method
        Builds an instance of an :class:`AdjacencyMapGraph`. The operation
        is performed in O(1).
        """
        self._adjacency_map = dict()
        self._edge_count = 0

    def vertices(self) -> typing.List[Vertex]:
        """
        Returns a list of the vertices of the graph. The operation is
        performed in O(n) for a graph of n vertices.

        :returns: A list of the vertices of the graph.
        :rtype: list of :class:`Vertex`
        """
        return list(self._adjacency_map.keys())

    def edges(self) -> typing.List[Edge]:
        """
        Returns a list of edges of the graph. The operation is performed in
        O(m) for a graph of m edges.

        :returns: A list of the edges of the graph.
        :rtype: list of :class:`Edge`
        """
        return list({e for edge_dict in self._adjacency_map.values() \
                     for e in edge_dict.values()})

    def vertex_count(self) -> int:
        """
        Returns the number of vertices the graph contains. The operation is
        performed in O(1).

        :returns: The number of vertices the graph contains.
        :rtype: int
        """
        return len(self._adjacency_map)

    def edge_count(self) -> int:
        """
        Returns the number of edges the graph contains. The operation is
        performed in O(1).

        :returns: The number of edges the graph contains.
        :rype: int
        """
        return self._edge_count

    def has_edge(self, e: Edge) -> bool:
        """
        Returns if the edge ``e`` is in the graph. The operation is performed
        in O(1) expected.

        :returns: A boolean meaning if the edge ``e`` is in the graph.
        :rtype: bool
        """
        return e.origin in self._adjacency_map and \
            e.destination in self._adjacency_map[e.origin] and \
            e == self._adjacency_map[e.origin][e.destination]

    def get_edge(self, u: Vertex, v: Vertex) -> Edge:
        """
        Returns the edge composed of the vertices ``u`` and ``v`` if it's
        in the graph, otherwise None is returned. This operation is performed
        in O(1) expected.

        
        :param u: A vertex contains in the edge requested.
        :type u: :class:`Vertex`.
        :param v: A vertex contains in the edge requested.
        :type v: :class:`Vertex`.
        :returns: The edge composed of ``u`` and ``v``.
        :rtype: :class:`Edge`
        """
        if u not in self._adjacency_map or \
                v not in self._adjacency_map[u]:
            return None
        e = self._adjacency_map[u][v]
        if e.origin == u and e.destination == v:
            return e
        return None

    def degree(self, v: Vertex, out: bool=False) -> int:
        """
        Returns the degree of the vertex ``v``. If ``out`` is True, then
        the number of out edges is returned, the number of every incident
        edges is returned otherwise. The operation is performed in O(d_v) where
        d_v is the degree of the vertex ``v``. If ``v`` is not in the graph,
        None is returned.

        :param v: The vertex ``v`` for the one the degree is requested.
        :type v: :class:`Vertex`
        :returns: The degree of the vertex ``v``.
        :rtype: int
        """
        if v not in self._adjacency_map:
            return None
        if out:
            count = 0
            for e in self._adjacency_map[v].values():
                if e.origin == v:
                    count += 1
            return count
        else:
            return len(self._adjacency_map[v])

    def neighbours(self, v: Vertex, out: bool=False) -> typing.List[Vertex]:
        """
        Returns a list of all neighbours of ``v``. If ``out`` is True, then
        only the out neighbours of ``v`` are returned.

        :param v: The vertex for the one the neighbours are requested.
        :type v: :class:`Vertex`
        :returns: A list of all neighbours of ``v``.
        :rtype: list of :class:`Vertex`
        """
        if v not in self._adjacency_map:
            return None
        if out:
            return [u for u, e in self._adjacency_map[v].items() \
                    if e.origin == v]
        else:
            return self._adjacency_map[v].keys()

    def incident_edges(self, v: Vertex, out: bool=False) -> typing.List[Edge]:
        """
        Returns a list of the incident edges of the vertex ``v``. This
        operation is performed in O(d_v) where d_v is the degree of ``v``.

        :param v: The vertex whose incident edges are requested.
        :type v: Vertex
        :param out: A flag meaning if only the out incident edges are
                    requested.
        :returns: list of :class:`Edge`
        """
        if out:
            return [e for e in self._adjacency_map[v].values()
                    if e.origin == v]
        else:
            return list(self._adjacency_map[v].values())

    def insert_vertex(self, v: Vertex) -> bool:
        """
        Inserts the vertex ``v`` in the graph. This operation is performed in
        O(1) expected.

        :param v: The new vertex to add to the graph.
        :type v: Vertex
        :returns: A boolean meaning if the operation is a succeed. The vertex
                  could already been in the graph.
        :type: bool
        """
        if v in self._adjacency_map:
            return False
        self._adjacency_map[v] = dict()
        return True

    def insert_edge(self, u: Vertex, v: Vertex,
                    value: typing.Optional(typing.Any)=None) -> bool:
        """
        Inserts the edge (u, v) in the graph. If a vertex doesn't exist in
        the graph, it will be added. This operation is performed in O(1)
        expected.

        :param u: The vertex origin of the edge.
        :type u: Vertex
        :param v: The vertex dertination of the edge.
        :type v: Vertex
        :param value: The value of the edge.
        :type value: any, optional
        :returns: A boolean meaning if the operation succeed. The operation
                  fails if the edge is already in the graph.
        :rtype: bool
        """
        if u not in self._adjacency_map:
            self.insert_vertex(u)
        if v not in self._adjacency_map:
            self.insert_vertex(v)
        if v in self._adjacency_map[u]:
            return False
        self._adjacency_map[u][v] = Edge(u, v, value)
        self._adjacency_map[v][u] = Edge(u, v, value)
        self._edge_count += 1
        return True

    def remove_vertex(self, v: Vertex) -> bool:
        """
        Removes the vertex ``v`` from the graph. Every incident edge will be
        also deleted.

        :param v: The vertex to remove.
        :type v: Vertex
        :returns: A boolean meaning if the removal was correctly performed. If
                  the vertex is not in the graph, then False is returned.
        :rtype: bool
        """
        if v not in self._adjacency_map:
            return False


        edges = list(self._adjacency_map[v].values())
        for e in edges:
            self.remove_edge(e)
        del self._adjacency_map[v]
        return True

    def remove_edge(self, e: Edge) -> bool:
        """
        Removes the edge ``e`` from the graph.

        :param e: The edge to remove.
        :type e: Edge
        :returns: True if the edge was in the graph and has been removed,
                  otherwise False.
        :rtype: bool
        """
        if e.origin not in self._adjacency_map or \
                e.destination not in self._adjacency_map[e.origin] or \
                e != self._adjacency_map[e.origin][e.destination]:
            return False
        del self._adjacency_map[e.origin][e.destination]
        del self._adjacency_map[e.destination][e.origin]
        self._edge_count -= 1
        return True

    def __eq__(self, graph: AdjacencyMapGraph) -> bool:
        """
        Returns True if ``graph`` is equal to this instance, otherwise False.
        For two graphs to be equal, they must have the same set of vertices and
        the same set of edges.

        :param graph: The graph to compare.
        :type graph: AdjacencyMapGraph
        :returns: True if ``graph`` is equal to this instance, False otherwise.
        :rtype: bool
        """
        return set(self.vertices()) == set(graph.vertices()) and \
            set(self.edges()) == set(graph.edges())

    def __ne__(self, graph: AdjacencyMapGraph) -> bool:
        """
        Returns True if ``graph`` is not equal to this instance, False
        otherwise. This function uses the function __eq__ to decide this one.

        :param graph: The graph to compare.
        :type graph: AdjacencyMapGraph
        :returns: True if ``graph`` is not equal to this instance.
        :rtype: bool
        """
        return not self.__eq__(graph)