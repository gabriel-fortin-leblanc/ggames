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

class Graph:
    """
    The abstract data type graph.
    """

    def vertices() -> list[Vertex]:
        raise NotImplemented()

    def edges() -> list[Edge]:
        raise NotImplemented()

    def vertex_count() -> int:
        raise NotImplemented()

    def edge_count() -> int:
        raise NotImplemented()

    def degree(v: Vertex), out=True) -> int:
        raise NotImplemented()

    def incident_edges(v: Vertex, out=True) -> int:
        raise NotImplemented()

    def insert_vertex(v: Vertex) -> None:
        raise NotImplemented()

    def insert_edge(u: Vertex, v: Vertex) -> None:
        raise NotImplemented()

    def remove_vertex(v: Vertex) -> None:
        raise NotImplemented()

    def remove_edge(e: Edge) -> None:
        raise NotImplemented()


class AdjacencyListGraph(Graph):
    """
    A graph implemented with an adjacency list.
    """
    pass


class AdjacencyMapGraph(Graph):
    """
    A graph implemented with an adjacency hash table.
    """
    pass


class AdjacencyMatrixGraph(Graph):
    """
    A graph implemented wth an adjacency matrix.
    """
    pass

