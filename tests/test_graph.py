from ggames.graph import *


# Test of Vertex.
def test_Vertex_init():
	v = Vertex()
	assert hasattr(v, 'value')
	assert v.value is None

	try:
		# Test to pass unhashable value
		v = Vertex(list())
	except TypeError: pass
	else:
		raise AssertionError('test_Vertex_init failed to raise exception. '\
							 'The value of Vertex must be hashable.')

	v = Vertex(3)
	assert v.value == 3

def test_Vertex_eq_ne():
	v1 = Vertex()
	v2 = Vertex()
	assert v1 == v2

	v1.value = 3
	assert not v1 == v2
	assert v1 != v2

def test_Vertex_str():
	v = Vertex()
	assert str(v) == 'Vertex(None)'
	v.value = 'Hello'
	assert str(v) == 'Vertex(Hello)'

def test_Vertex_hash():
	v = Vertex()
	assert hash(v) == hash(None)
	v.value = 5
	assert hash(v) == hash(5)


# Test of Edge
def test_Edge_init():
	u = Vertex(0)
	v = Vertex(1)
	e = Edge(u, v)
	assert e.origin == u
	assert e.destination == v
	assert e.value is None

	e = Edge(v, u, 5)
	assert e.origin == v
	assert e.destination == u
	assert e.value == 5

def test_Edge_property():
	u = Vertex()
	v = Vertex('ok')
	e = Edge(u, v)
	try:
		e.origin = 3
	except TypeError: pass
	else:
		raise AssertionError('test_Edge_property failed to raise exception. '
			'The attribute origin of Edge must be a Vertex.')
	try:
		e.destination = 3
	except TypeError: pass
	else:
		raise AssertionError('test_Edge_property failed to raise exception. '
			'The attribute destination of Edge must be a Vertex.')

def test_Edge_endpoints():
	u = Vertex(0)
	v = Vertex(1)
	e = Edge(u, v)
	assert e.endpoints() == (u, v)
	assert e.endpoints() != (v, u)

def test_Edge_opposite():
	u = Vertex(0)
	v = Vertex(1)
	w = Vertex(3)
	e = Edge(u, v)
	assert e.opposite(u) == v
	assert e.opposite(v) == u
	assert e.opposite(w) is None

def test_Edge_str():
	u = Vertex('Hello')
	v = Vertex('World!')
	e = Edge(u, v)
	assert str(e) == 'Edge(Vertex(Hello), Vertex(World!))'

	e.value = '!!!'
	assert str(e) == 'Edge(Vertex(Hello), Vertex(World!), !!!)'

def test_Edge_eq_ne():
	u1 = Vertex(0)
	v1 = Vertex(1)
	u2 = Vertex(2)
	v2 = Vertex(3)
	e1 = Edge(u1, v1)
	e2 = Edge(u2, v2)
	assert e1 == e1
	assert e2 == e2
	assert e1 != e2

	e3 = Edge(u1, v1, 0)
	assert e1 != e3
	e1.value = 0
	assert e1 == e3

def test_Edge_contains():
	u = Vertex(0)
	v = Vertex(1)
	w = Vertex(2)
	e = Edge(u, v)
	assert u in e
	assert v in e
	assert w not in e

def test_Edge_hash():
	u = Vertex(0)
	v = Vertex(1)
	e = Edge(u, v)
	assert hash(e) == hash((0, 1, None))

	e.value = 'Hello'
	assert hash(e) == hash((0, 1, 'Hello'))


# Tests of AdjacencyMapGraph
def test_AMG_init():
	G = AdjacencyMapGraph()
	assert hasattr(G, '_adjacency_map')
	assert hasattr(G, '_edge_count')

	assert type(G._adjacency_map) is dict
	assert type(G._edge_count) is int

	assert len(G._adjacency_map) == 0
	assert G._edge_count == 0

def test_AMG_insert_vertex():
	G = AdjacencyMapGraph()
	u = Vertex(0)
	assert G.insert_vertex(u)
	assert not G.insert_vertex(u)
	assert u in G._adjacency_map
	assert type(G._adjacency_map[u]) is dict
	assert len(G._adjacency_map[u]) == 0

def test_AMG_insert_edge():
	G = AdjacencyMapGraph()
	u = Vertex(0)
	v = Vertex(1)
	assert G.insert_edge(u, v)
	assert not G.insert_edge(u, v)
	assert u in G._adjacency_map
	assert v in G._adjacency_map
	assert v in G._adjacency_map[u]
	assert u in G._adjacency_map[v]
	e = Edge(u, v)
	assert e == G._adjacency_map[u][v]
	assert e == G._adjacency_map[v][u]

	G = AdjacencyMapGraph()
	G.insert_vertex(u)
	G.insert_vertex(v)
	assert G.insert_edge(u, v, 0)
	assert not G.insert_edge(u, v, 0)
	assert u in G._adjacency_map
	assert v in G._adjacency_map
	assert v in G._adjacency_map[u]
	assert u in G._adjacency_map[v]
	e = Edge(u, v, 0)
	assert e == G._adjacency_map[u][v]
	assert e == G._adjacency_map[v][u]

def test_AMG_remove_edge():
	G = AdjacencyMapGraph()
	u = Vertex(0)
	v = Vertex(1)
	e = Edge(u, v, 2)
	G.insert_edge(u, v, 2)
	assert G.remove_edge(e)
	assert u in G._adjacency_map
	assert v in G._adjacency_map
	assert u not in G._adjacency_map[v]
	assert v not in G._adjacency_map[u]
	assert not G.remove_edge(e)

def test_AMG_remove_vertex():
	G = AdjacencyMapGraph()
	u = Vertex(0)
	v = Vertex(1)
	w = Vertex(2)
	G.insert_edge(u, v)
	G.insert_edge(v, w)
	G.insert_edge(w, u)
	assert G.remove_vertex(w)
	assert not G.remove_vertex(w)
	assert w not in G._adjacency_map
	assert w not in G._adjacency_map[u]
	assert w not in G._adjacency_map[v]

def test_AMG_incident_edge():
	G = AdjacencyMapGraph()
	u = Vertex(0)
	v = Vertex(1)
	w = Vertex(2)
	y = Vertex(3)
	G.insert_edge(u, v)
	G.insert_edge(v, w)
	G.insert_edge(w, u)
	G.insert_edge(w, y)
	edges = G.incident_edges(u)
	assert type(edges) is list
	assert {Edge(u, v), Edge(w, u)} == set(edges)
	edges = G.incident_edges(w)
	assert {Edge(v, w), Edge(w, u), Edge(w, y)} == set(edges)
	edges = G.incident_edges(w, True)
	assert {Edge(w, u), Edge(w, y)} == set(edges)

def test_AMG_degree():
	G = AdjacencyMapGraph()
	u = Vertex(0)
	v = Vertex(1)
	w = Vertex(2)
	y = Vertex(3)
	G.insert_edge(u, v)
	G.insert_edge(v, w)
	G.insert_edge(w, u)
	G.insert_edge(w, y)
	assert G.degree(u) == 2
	assert G.degree(w) == 3
	assert G.degree(u, True) == 1
	assert G.degree(w, True) == 2

	G = AdjacencyMapGraph()
	assert G.degree(u) is None

def test_AMG_has_edge():
	G = AdjacencyMapGraph()
	u = Vertex(0)
	v = Vertex(1)
	w = Vertex(2)
	y = Vertex(3)
	G.insert_edge(u, v)
	G.insert_edge(v, w)
	G.insert_edge(w, u)
	G.insert_edge(w, y)
	assert not G.has_edge(Edge(Vertex(), Vertex()))
	assert G.has_edge(Edge(u, v))
	assert not G.has_edge(Edge(u, v, 3))
	assert not G.has_edge(Edge(v, u))

def test_AMG_get_edge():
	G = AdjacencyMapGraph()
	u = Vertex(0)
	v = Vertex(1)
	w = Vertex(2)
	G.insert_edge(u, v)
	assert G.get_edge(v, w) is None
	assert G.get_edge(u, v) == Edge(u, v)

	G = AdjacencyMapGraph()
	G.insert_edge(u, v)
	assert G.get_edge(v, u) is None

def test_AMG_edge_count():
	G = AdjacencyMapGraph()
	assert G.edge_count() == 0
	G.insert_vertex(Vertex())
	assert G.edge_count() == 0
	G.insert_edge(Vertex(), Vertex(0))
	assert G.edge_count() == 1
	G.remove_edge(Edge(Vertex(), Vertex(0)))
	assert G.edge_count() == 0

def test_AMG_vertex_count():
	G = AdjacencyMapGraph()
	u = Vertex(0)
	v = Vertex(1)
	w = Vertex(2)
	y = Vertex(3)
	assert G.vertex_count() == 0
	G.insert_vertex(u)
	assert G.vertex_count() == 1
	G.insert_edge(v, u)
	assert G.vertex_count() == 2
	G.insert_edge(w, y)
	assert G.vertex_count() == 4
	G.remove_vertex(u)
	assert G.vertex_count() == 3

def test_AMG_vertices():
	G = AdjacencyMapGraph()
	u = Vertex(0)
	v = Vertex(1)
	w = Vertex(2)
	assert [] == G.vertices()
	assert type(G.vertices()) is list
	G.insert_edge(u, v)
	assert {u, v} == set(G.vertices())
	G.insert_vertex(v)
	assert {u, v} == set(G.vertices())
	G.insert_vertex(w)
	assert {u, v, w} == set(G.vertices())
	G.remove_vertex(u)
	assert {v, w} == set(G.vertices())

def test_AMG_edges():
	G = AdjacencyMapGraph()
	u = Vertex(0)
	v = Vertex(1)
	w = Vertex(2)
	y = Vertex(3)
	edges = G.edges()
	assert edges == []
	G.insert_vertex(u)
	G.insert_edge(u, v)
	edges = G.edges()
	assert len(edges) == 1
	assert Edge(u, v) in edges
	G.insert_edge(w, y)
	edges = G.edges()
	assert len(edges) == 2
	assert Edge(u, v) in edges
	assert Edge(w, y) in edges
