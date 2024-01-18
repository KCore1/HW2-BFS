# write tests for bfs
import pytest
import networkx as nx
from search import graph

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    g = graph.Graph('data/tiny_network.adjlist')
    assert len(g.bfs("Lani Wu")) == len(g.graph.nodes)
    assert len(g.bfs("Luke Gilbert")) == len(g.graph.nodes)
    assert g.bfs("Lani Wu") != g.bfs("Luke Gilbert")
    assert g.bfs("Lani Wu") == list(nx.bfs_tree(g.graph, "Lani Wu").nodes)
    assert g.bfs("Luke Gilbert") == list(nx.bfs_tree(g.graph, "Luke Gilbert").nodes)
    assert g.bfs("Lani Wu", "NOT Nevan Krogan") == None
    for node in g.graph.nodes:
        assert g.bfs("Lani Wu", node) == list(nx.shortest_path(g.graph, "Lani Wu", node))
    with pytest.raises(ValueError):
        g.bfs("NOT A NODE")
    with pytest.raises(ValueError):
        e = graph.Graph('test/empty.adjlist')
        e.bfs("Lani Wu")
    assert g.bfs("Lani Wu", "Lani Wu") == ["Luke Gilbert"] # This will cause an exception

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    pass
