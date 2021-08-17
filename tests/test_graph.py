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


# Tests of AdjacencyMapGraph
def test_AMG_init():
	G = AdjacencyMapGraph()
	assert hasattr(G, '_adjacency_map')
	assert hasattr(G, '_count_edge')

	assert type(G._adjacency_map) is dict
	assert type(G._count_edge) is int

	assert len(G._adjacency_map) == 0
	assert G._count_edge == 0


def test_AMG_insert_vertex():
	G = AdjacencyMapGraph()
	# TODO: Must test Vertex and Edge before
