"""
This package provides graph classes under different implementations.
"""
from typing import Union, Hashable, Optional, Any


class Vertex:
    """
    A class representing a vertex.
    """

    __slots__ = ['value']

    def __init__(self, value: Hashable) -> None:
        """Build a new vertex."""
        self = value = value

    def __eq__(self, v: Vertex) -> bool:
        """Return if v is equal to this vertex."""
        return self.value == v.value

    def __str__(self) -> str:
        """Return the string representation of this vertex."""
        return str(self.value)


class Edge:
    """
    A class representing an edge.
    """

    __slots__ = ['origin', 'destination', 'value']

    def __init__(self, origin: Vertex, destination: Vertex,
                 value: Optional(Hashable)) -> None:
        """
        Build an edge from the two vertices. It can be considered oriented or
        not.
        """
        self.origin = origin
        self.destination = destination
        self.value = value

    def endpoints(self) -> tuple[Vertex, Vertex]:
        """Return a tuple containing the vertices origin and destination."""
        return (self.origin, self.destination)

    def opposite(self, v: Vertex) -> Vertex:
        """Return the opposite vertex."""
        if self.origin == v:
            return self.destination
        elif self.destination == v:
            return self.origin
        else:
            raise ValueError(f'The vertex {v} is not part of this edge.')

    def __str__(self) -> str:
        """Return a string representation of this edge."""
        return f'Edge(origin={self.origin}, destination={self.destination}, '\
            f'value={self.value})'

    def __eq__(self, e: Edge) -> bool:
        """Return if the edge e is equal to this one."""
        return self.origin == e.origin and \
               self.destination == e.destination and \
               self.value == e.value

    def __ne__(self, e: Edge) -> bool:
        """Return if the edge is not equal to this one."""
        return not self.__eq__(e)

    def __contains__(self, v: Vertex) -> bool:
        """Return if the vertex v is one of the endpoints."""
        return self.origin == v or self.destination == v


class Graph:
    """
    The abstract data type graph.
    """

    def vertices(self) -> list[Vertex]:
        """Return a list of the vertices of the graph."""
        raise NotImplemented()

    def edges(self) -> list[Edge]:
        """Return a list of edges of the graph."""
        raise NotImplemented()

    def vertex_count(self) -> int:
        """Return the number of vertices the graph contains."""
        raise NotImplemented()

    def edge_count(self) -> int:
        """Return the number of edges the graph contains."""
        raise NotImplemented()

    def get_edge(self, u: Vertex, v: Vertex) -> Edge:
        """
        Return the edge composed of the origin u to the destination v if it's
        in the graph.
        """
        raise NotImplemented()

    def degree(self, v: Vertex), out=True) -> int:
        """Return the degree of the vertex v."""
        raise NotImplemented()

    def incident_edges(self, v: Vertex, out=True) -> list[Edge]:
        """Return a list of the incident edges of the vertex v."""
        raise NotImplemented()

    def insert_vertex(self, v: Vertex) -> None:
        """Insert the vertex v in the graph."""
        raise NotImplemented()

    def insert_edge(self, u: Vertex, v: Vertex) -> None:
        """
        Insert the edge (u, v) in the graph. If a vertex doesn't exist in
        the graph, it will be added.
        """
        raise NotImplemented()

    def remove_vertex(self, v: Vertex) -> None:
        """
        Remove the vertex v from the graph. Every incident edge will be also
        deleted.
        """
        raise NotImplemented()

    def remove_edge(self, e: Edge) -> None:
        """Remove the edge e from the graph."""
        raise NotImplemented()


class AdjacencyMapGraph(Graph):
    """
    A graph implemented with an adjacency hash table.
    """

    __slots__ = ['_adjacency_map', '_count_edge']

    def __init__(self):
        """Build an instance of an AdjacencyMapGraph."""
        self._adjacency_map = dict()
        self._count_edge = 0

    def vertices(self) -> list[Vertex]:
        """Return a list of the vertices of the graph."""
        return list(self._adjacency_map.keys())

    def edges(self) -> list[Edge]:
        """Return a list of edges of the graph."""
        return list(self._adjacency_map.values())

    def vertex_count(self) -> int:
        """Return the number of vertices the graph contains."""
        return len(self._adjacency_map)

    def edge_count(self) -> int:
        """Return the number of edges the graph contains."""
        return self._count_edge

    def get_edge(self, u: Vertex, v: Vertex) -> Edge:
        """
        Return the edge composed of the vertices u and v if it's
        in the graph.
        """
        return self._adjacency_map[u][v]

    def degree(self, v: Vertex), out=True) -> int:
        """Return the degree of the vertex v."""
        if out:
            count = 0
            for e in self._adjacency_map[v].values():
                if self.origin == v:
                    count += 1
            return count
        else:
            return len(self._adjacency_map[v])

    def incident_edges(self, v: Vertex, out=True) -> list[Edge]:
        """Return a list of the incident edges of the vertex v."""
        if out:
            return [e for e in self._adjacency_map[v].values()
                    if e.origin == v]
        else:
            return list(self._adjacency_map[v].values())

    def insert_vertex(self, v: Vertex) -> None:
        """Insert the vertex v in the graph."""
        self._adjacency_map[v] = dict()

    def insert_edge(self, u: Vertex, v: Vertex) -> None:
        """
        Insert the edge (u, v) in the graph. If a vertex doesn't exist in
        the graph, it will be added.
        """
        if u not in self._adjacency:
            self.insert_vertex(u)
        if v not in self._adjacency:
            self.insert_vertex(v)
        self._adjacency_map[u][v] = Edge(u, v)
        self._adjacency_map[v][u] = Edge(u, v)

    def remove_vertex(self, v: Vertex) -> None:
        """
        Remove the vertex v from the graph. Every incident edge will be also
        deleted.
        """
        if v not in self._adjacency_map:
            raise ValueError(f'The vertex {v} is not part of this graph.')

        for e in self._adjacency_map[v].values():
            self.remove_edge(e)
        del self.adjacency_map[v]

    def remove_edge(self, e: Edge) -> None:
        """Remove the edge e from the graph."""
        if e.origin not in self._adjacency_map or \
                e.destination not in self._adjacency_map or \
                e != self._adjacency_map[e.origin][e.destination]:
            raise ValueError(f'The edge {e} is not part of the graph.')
        del self._adjacency_map[e.origin][e.destination]
        del self._adjacency_map[e.destination][e.origin]


class AdjacencyMatrixGraph(Graph):
    """
    A graph implemented wth an adjacency matrix.
    """
    pass

