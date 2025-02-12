class Node:
    def __init__(self, name):
        self.name = name
        self.gCost = float('inf')
        self.hCost = float('inf')
        self.fCost = float('inf')
        self.parent = None

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.heuristics = {}

    def addEdge(self, source, target, cost):
        if source not in self.nodes:
            self.nodes[source] = Node(source)
        if target not in self.nodes:
            self.nodes[target] = Node(target)
            
        if source not in self.edges:
            self.edges[source] = {}
        self.edges[source][target] = cost

    def addHeuristic(self, node, value):
        self.heuristics[node] = value

def aStarSearch(graph, start, goal):
    openSet = {start}
    closedSet = set()
    
    graph.nodes[start].gCost = 0
    graph.nodes[start].hCost = graph.heuristics[start]
    graph.nodes[start].fCost = graph.heuristics[start]

    while openSet:
        current = min(openSet, key=lambda x: graph.nodes[x].fCost)
        
        if current == goal:
            path = []
            cost = graph.nodes[current].gCost
            while current:
                path.append(current)
                current = graph.nodes[current].parent
            return path[::-1], cost

        openSet.remove(current)
        closedSet.add(current)

        if current in graph.edges:
            for neighbor, edgeCost in graph.edges[current].items():
                if neighbor in closedSet:
                    continue

                tentativeGCost = graph.nodes[current].gCost + edgeCost

                if neighbor not in openSet:
                    openSet.add(neighbor)
                elif tentativeGCost >= graph.nodes[neighbor].gCost:
                    continue

                graph.nodes[neighbor].parent = current
                graph.nodes[neighbor].gCost = tentativeGCost
                graph.nodes[neighbor].hCost = graph.heuristics[neighbor]
                graph.nodes[neighbor].fCost = tentativeGCost + graph.heuristics[neighbor]

    return None, float('inf')

networkGraph = Graph()

edges = [
    ('A', 'B', 10),
    ('A', 'C', 15),
    ('B', 'D', 12),
    ('C', 'D', 10),
    ('D', 'E', 5)
]

heuristics = [
    ('A', 20),
    ('B', 15),
    ('C', 10),
    ('D', 5),
    ('E', 0)
]

for source, target, cost in edges:
    networkGraph.addEdge(source, target, cost)

for node, value in heuristics:
    networkGraph.addHeuristic(node, value)

path, cost = aStarSearch(networkGraph, 'A', 'E')
print(f"Optimal Path: {' -> '.join(path)}")
print(f"Total Cost: {cost} ms (milliseconds)")
