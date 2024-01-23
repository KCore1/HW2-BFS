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
    print(g.bfs("Lani Wu"))
    print(list(nx.bfs_tree(g.graph, "Lani Wu").nodes))
    assert len(g.bfs("Lani Wu")) == len(g.graph.nodes)
    assert len(g.bfs("Luke Gilbert")) == len(g.graph.nodes)
    assert g.bfs("Lani Wu") != g.bfs("Luke Gilbert")
    assert g.bfs("Lani Wu") == list(nx.bfs_tree(g.graph, "Lani Wu").nodes)
    assert g.bfs("Luke Gilbert") == list(nx.bfs_tree(g.graph, "Luke Gilbert").nodes)
    with pytest.raises(ValueError):
        g.bfs("NOT A NODE")
    with pytest.raises(ValueError):
        e = graph.Graph('test/empty.adjlist')
        e.bfs("Lani Wu")
    

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
    g = graph.Graph('data/citation_network.adjlist')
    assert g.bfs("Lani Wu", "NOT Nevan Krogan") == None
    # testing length only, since path may differ
    assert len(g.bfs("Lani Wu", "Nevan Krogan")) == len(list(nx.shortest_path(g.graph, "Lani Wu", "Nevan Krogan")))
    assert len(g.bfs("Nevan Krogan", "Lani Wu")) == len(list(nx.shortest_path(g.graph, "Nevan Krogan", "Lani Wu")))
    assert len(g.bfs("Luke Gilbert", "Hani Goodarzi")) == len(list(nx.shortest_path(g.graph, "Luke Gilbert", "Hani Goodarzi")))
    assert len(g.bfs("Hani Goodarzi", "Luke Gilbert")) == len(list(nx.shortest_path(g.graph, "Luke Gilbert", "Hani Goodarzi")))