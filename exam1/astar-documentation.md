# A* Graph Search Implementation Documentation

## Overview
This implementation provides an A* search algorithm for finding the optimal path in a communication network where nodes represent servers and edges represent connections with associated transmission times in milliseconds.

## Classes

### Node Class
```python
class Node:
    def __init__(self, name):
        self.name = name
        self.gCost = float('inf')
        self.hCost = float('inf')
        self.fCost = float('inf')
        self.parent = None
```
- `name`: Identifier for the server node
- `gCost`: Actual cost from start node to current node
- `hCost`: Heuristic estimate from current node to goal
- `fCost`: Total estimated cost (g + h)
- `parent`: Reference to the previous node in the optimal path

### Graph Class
```python
class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.heuristics = {}
```
- `nodes`: Dictionary storing Node objects
- `edges`: Dictionary storing connection costs between nodes
- `heuristics`: Dictionary storing heuristic values for each node

#### Graph Methods
- `addEdge(source, target, cost)`: Adds a directed edge with transmission time
- `addHeuristic(node, value)`: Adds heuristic value for a node

## A* Search Algorithm
```python
def aStarSearch(graph, start, goal)
```
### Parameters
- `graph`: Graph object containing network topology
- `start`: Starting server node
- `goal`: Destination server node

### Returns
- Tuple containing:
  1. List of nodes representing optimal path
  2. Total cost in milliseconds

### Algorithm Steps
1. Initialize open and closed sets
2. Set initial node costs (g=0, h=heuristic value)
3. While open set is not empty:
   - Select node with lowest f-cost
   - If goal reached, reconstruct and return path
   - Expand current node's neighbors
   - Update costs if better path found

## Usage Example
```python
# Create graph
networkGraph = Graph()

# Add edges (connections between servers)
edges = [
    ('A', 'B', 10),  # 10ms transmission time
    ('A', 'C', 15),  # 15ms transmission time
    # ...
]

# Add heuristic values
heuristics = [
    ('A', 20),
    ('B', 15),
    # ...
]

# Add data to graph
for source, target, cost in edges:
    networkGraph.addEdge(source, target, cost)
for node, value in heuristics:
    networkGraph.addHeuristic(node, value)

# Find optimal path
path, cost = aStarSearch(networkGraph, 'A', 'E')
```

## Performance Considerations
- Time Complexity: O(b^d) where b is branching factor and d is depth
- Space Complexity: O(|V|) where |V| is number of vertices
- Uses heuristic values to guide search towards goal
- Guarantees optimal path when heuristic is admissible

## Notes
- All costs represent transmission times in milliseconds
- Heuristic values must be admissible (never overestimate)
- Implementation assumes directed graph (one-way connections)
- Infinity used as initial cost to ensure proper updating
