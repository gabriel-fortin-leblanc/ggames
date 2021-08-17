"""
This module provides a interface for graphs that is used in this package.
"""
from __future__ import annotations
import collections
from typing import Union, Hashable, Optional, Any, NoReturn, Tuple, List, Set


class Vertex:
    """
    A class representing a vertex. This is a wrapper for a value.
    """

    __slots__ = ['_value']

    def __init__(self, value: Optional(Hashable) = None) -> NoReturn:
        """
        Builds a new vertex.

        :param value: The ``value`` the vertex wraps. It must be hashable.
        """
        self.value = value

    @property
    def value(self):
        self._value

    @value.setter
    def value(self, value):
        hash(value) # Check if value is hashable.
        self._value = value

    @value.getter
    def value(self):
        return self._value

    def __eq__(self, v: Vertex) -> bool:
        """
        Returns if ``v`` is equal to this vertex.

        :param v: A vertex to compare.
        :type v: Vertex
        :returns: A boolean meaning if the vertex ``v`` and the current
                  instance are equal.
        :rtype: bool
        """
        return self.value == v.value

    def __ne__(self, v: Vertex) -> bool:
        """
        Returns True if the value of ``v`` is not equal to the value of this
        instance.

        :params v: A vertex to compare.
        :type: Vertex
        :returns: True if the two vertices are not equal, False otherwise.
        :rtype: bool
        """
        return not self.__eq__(v)

    def __str__(self) -> str:
        """
        Returns the string representation of this vertex. It calls the __str__
        magic method of the value wrapped in this format Vertex(``value``).

        :returns: Returns a string representation of the vertex.
        :rtype: str
        """
        return f'Vertex({self.value})'


class Edge:
    """
    This class represents an edge. It can be either oriented or not since
    it contains two attributes ``origin`` and ``destination`` may express an
    orientation.
    """

    __slots__ = ['origin', 'destination', 'value']

    def __init__(self, origin: Vertex, destination: Vertex,
                 value: Optional(Any)) -> NoReturn:
        """
        Builds an edge from the two vertices. It can be considered oriented or
        not.

        :param origin: The origin vertex if it's oriented, or simply one of
                       the two vertices.
        :type origin: Vertex
        :param destination: The destination vertex if it's oriented, or simply
                            one of the two vertices.
        :param value: A value that can be used as an attribute of the edge.
                      This value is optional and can be of any type.
        """
        self.origin = origin
        self.destination = destination
        self.value = value

    def endpoints(self) -> Tuple[Vertex, Vertex]:
        """
        Returns a tuple containing the vertices origin and destination.

        :returns: A tuple containing the two vertices that composed the edge.
                  Since it can be oriented, the position is
                  (``origin``, ``destination``).
        :rtype: tuple
        """
        return (self.origin, self.destination)

    def opposite(self, v: Vertex) -> Vertex:
        """
        Returns the opposite vertex.

        :param v: A vertex contained in the edge.
        :type v: Vertex

        :raises ValueError: If the vertex ``v`` is not part of the edge.

        :returns: The opposite vertex of ``v``.
        :rtype: Vertex
        """
        if self.origin == v:
            return self.destination
        elif self.destination == v:
            return self.origin
        else:
            raise ValueError(f'The vertex {v} is not part of this edge.')

    def __str__(self) -> str:
        """
        Returns a string representation of this edge in this format
        Edge(``origin``, ``destination``, ``value``) if the value exists
        otherwise the last attribute is skipped.
        """
        return f'Edge(origin={self.origin}, destination={self.destination}' +\
            (f' ,{self.value})' if self.value is not None else ')')

    def __eq__(self, e: Edge) -> bool:
        """
        Returns if the edge ``e`` is equal to this one. For two edges to be
        equal, each of their attributes must also be equal.

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
        Returns if the edge is not equal to this one. It uses __eq__ to
        compute it.

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


class Graph:
    """
    The abstract data type graph. This class must not be instanciate. It is
    only used as interface. It provides a wrapper to not be dependant of a
    specific library.
    """

    def vertices(self) -> List[Vertex]:
        """
        Returns a list of the vertices of the graph.
        """
        raise NotImplemented()

    def edges(self) -> list[Edge]:
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

    def degree(self, v: Vertex, out=True) -> int:
        """
        Returns the degree of the vertex v. Only the out degree of ``v`` is
        returned if ``out`` is True. To get the in degree of ``v``, the user
        can use *G.degree(v, False) - G.degree(v)* for a given graph *G*.
        """
        raise NotImplemented()

    def incident_edges(self, v: Vertex, out=True) -> list[Edge]:
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
                    value: Optional(Any)) -> bool:
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


class AdjacencyMapGraph(Graph):
    """
    A graph implemented with an adjacency hash table. It follows the interface
    :class:`Graph`.
    """

    __slots__ = ['_adjacency_map', '_count_edge']

    def __init__(self) -> NoReturn:
        """
        Builds an instance of an :class:`AdjacencyMapGraph`. The operation
        is performed in O(1).
        """
        self._adjacency_map = dict()
        self._count_edge = 0

    def vertices(self) -> list[Vertex]:
        """
        Returns a list of the vertices of the graph. The operation is
        performed in O(n) for a graph of n vertices.

        :returns: A list of the vertices of the graph.
        :rtype: list of :class:`Vertex`
        """
        return list(self._adjacency_map.keys())

    def edges(self) -> list[Edge]:
        """
        Returns a list of edges of the graph. The operation is performed in
        O(m) for a graph of m edges.

        :returns: A list of the edges of the graph.
        :rtype: list of :class:`Edge`
        """
        return [{e for edge_dict in self._adjacency_map.values() \
                for e in edge_dict.values()}]

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
        return self._count_edge

    def has_edge(self, e: Edge) -> bool:
        """
        Returns if the edge ``e`` is in the graph. The operation is performed
        in O(1) expected.

        :returns: A boolean meaning if the edge ``e`` is in the graph.
        :rtype: bool
        """
        adj_vertices = self._adjacency_map[e.origin]
        if adj_vertices is None:
            return False
        return adj_vertices[e.destination] is not None

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
        return self._adjacency_map[u][v]

    def degree(self, v: Vertex, out=False) -> int:
        """
        Returns the degree of the vertex ``v``. If ``out`` is True, then
        the number of out edges is returned, the number of every incident
        edges is returned otherwise. The operation is performed in O(d_v) where
        d_v is the degree of the vertex ``v``.

        :param v: The vertex ``v`` for the one the degree is requested.
        :type v: :class:`Vertex`
        :returns: The degree of the vertex ``v``.
        :rtype: int
        """
        if out:
            count = 0
            for e in self._adjacency_map[v].values():
                if self.origin == v:
                    count += 1
            return count
        else:
            return len(self._adjacency_map[v])

    def incident_edges(self, v: Vertex, out=False) -> list[Edge]:
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
                    value: Optional(Any)) -> bool:
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
        if u not in self._adjacency:
            self.insert_vertex(u)
        if v not in self._adjacency:
            self.insert_vertex(v)
        if v in self._adjacency_map[u]:
            return False
        self._adjacency_map[u][v] = Edge(u, v, value)
        self._adjacency_map[v][u] = Edge(u, v, value)
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

        for e in self._adjacency_map[v].values():
            self.remove_edge(e)
        del self.adjacency_map[v]

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
                e.destination not in self._adjacency_map or \
                e != self._adjacency_map[e.origin][e.destination]:
            raise ValueError(f'The edge {e} is not part of the graph.')
        del self._adjacency_map[e.origin][e.destination]
        del self._adjacency_map[e.destination][e.origin]
