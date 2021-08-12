"""
This package provides graph classes under different implementations.
"""
from typing import Union, Hashable, Optional, Any


class Vertex:
    """
    A class representing a vertex.
    """

    __slots__ = ['value']

    def __init__(self, value: Hashable):
        pass


class Edge:
    """
    A class representing an edge.
    """

    __slots__ = ['origin', 'destination', 'value']

    def __init__(self, origin: Vertex, destination: Vertex,
                 value: Optional(Hashable)) -> None:
        pass

    def endpoints() -> tuple[Vertex, Vertex]:
        pass

    def opposite(v: Vertex) -> Vertex:
        pass


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

