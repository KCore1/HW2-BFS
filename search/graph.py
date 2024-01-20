import queue
import networkx as nx
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)

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
        if end is not None:
            q = queue.PriorityQueue()
        else:
            q = queue.Queue()
            
        visited = []

        distance = {} # Distance from start node
        previous = {} # Previous node in path from start node to current node

        if len(self.graph.nodes) == 0:
            raise ValueError("Graph is empty")
        if start not in self.graph.nodes:
            raise ValueError("Start node not in graph")
        
        # Initialize distance and previous dictionaries
        for node in self.graph.nodes:
            distance[node] = float('inf')
            previous[node] = None

        q.put(PrioritizedItem(0, start)) # Add start node with 0 distance
        visited.append(start)
        distance[start] = 0

        while not q.empty():
            v = q.get().item # Get node with smallest distance

            if v == end:
                path = []
                while v is not None:
                    path.append(v)
                    v = previous[v]
                path.reverse()
                return path
            
            n = self.graph.neighbors(v)
            for w in n:
                if w not in visited:
                    visited.append(w)
                    if distance[w] > distance[v] + 1:
                        distance[w] = distance[v] + 1
                        previous[w] = v
                    q.put(PrioritizedItem(distance[w], w))
        
        if end is None:
            return visited
        else:
            return None




