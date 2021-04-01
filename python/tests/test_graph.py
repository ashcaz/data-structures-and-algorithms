import pytest
from code_challenges.graph.graph import Vertex, Graph


def test_add_vertex_pass():
    vertex = Vertex("a")
    actual = vertex.value
    expected = "a"
    assert actual == expected


def test_add_vertex_fail():
    vertex = Vertex("a")
    actual = vertex.value
    expected = "b"
    assert actual != expected


def test_add_node():
    graph = Graph()
    expected = "a"
    actual = graph.add_node("a").value
    assert expected == actual


def test_add_edge_true():
    graph = Graph()
    a = graph.add_node("a")
    b = graph.add_node("b")
    graph.add_edge(a, b)
    assert True


def test_get_nodes():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    actual = graph.get_nodes()
    expected = ["a", "b"]
    assert actual == expected


def test_get_nodes_empty():
    graph = Graph()
    actual = graph.get_nodes()
    expected = None
    assert actual == expected


# @pytest.mark.skip("pending")
def test_one_node_one_edge_start():
    graph = Graph()
    a = graph.add_node("a")
    b = "b"

    with pytest.raises(KeyError):
        graph.add_edge(b, a)


def test_one_node_one_edge_end():
    graph = Graph()
    a = graph.add_node("a")
    b = "b"

    with pytest.raises(KeyError):
        graph.add_edge(a, b)


# @pytest.mark.skip("pending")
def test_get_neighbors():
    graph = Graph()
    a = graph.add_node("a")
    b = graph.add_node("b")
    graph.add_edge(a, b)
    actual = graph.get_neighbors("a")
    expected = ["b", 1]
    assert actual == expected


def test_size():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    expected = 2
    actual = graph.size()
    assert actual == expected


def test_size_fail():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    expected = 3
    actual = graph.size()
    assert actual != expected


def test_breadth_first(graph_one):
    actual = graph_one.breadth_first("a")
    expected = ["a", "b", "c", "d", "e"]
    assert actual == expected


@pytest.fixture
def graph_one():
    graph = Graph()
    a = graph.add_node("a")
    b = graph.add_node("b")
    c = graph.add_node("c")
    d = graph.add_node("d")
    e = graph.add_node("e")
    graph.add_edge(a, b)
    graph.add_edge(b, c)
    graph.add_edge(b, d)
    graph.add_edge(c, e)
    graph.add_edge(d, c)

    return graph