import queue
import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        A method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        q = queue.Queue()
        visited = []
        frontier = []
        if len(self.graph.nodes) == 0:
            raise ValueError("Graph is empty")
        if start not in self.graph.nodes:
            raise ValueError("Start node not in graph")
        q.put(start)
        visited.append(start)
        while not q.empty():
            v = q.get()
            n = self.graph.neighbors(v)
            for w in n:
                if w not in visited:
                    q.put(w)
                    frontier.append(w)
                    if w == end:
                        visited.append(w)
                        return visited
            visited.extend(frontier)
            frontier.clear()
        if end is None:
            return visited
        else:
            return None




