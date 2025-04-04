from collections import deque

def AStarTreeSearchCities():
    
    # Graph representation
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'D': 5, 'E': 2},
        'C': {'F': 3, 'G': 4},
        'D': {'H': 3},
        'E': {'H': 6},
        'F': {'I': 4},
        'G': {'J': 2},
        'H': {'I': 1},
        'I': {'J': 2},
        'J': {}
    }
    
    # Heuristic values
    heuristic = {
        'A': 7, 'B': 6, 'C': 3, 'D': 5, 'E': 4, 'F': 2, 'G': 1, 'H': 3, 'I': 1, 'J': 0
    }
    
    def aStarTreeSearch(graph, start, goal, heuristic):
        # Priority queue to store nodes to be explored, sorted by f(n) = g(n) + h(n)
        frontier = deque()
        frontier.append((start, [start], 0))  # (currentNode, path, g(n))
        
        while frontier:
            # Sort the frontier by f(n) = g(n) + h(n)
            frontier = deque(sorted(frontier, key=lambda x: x[2] + heuristic[x[0]]))
            currentNode, path, gCost = frontier.popleft()
            
            # Check if the goal is reached
            if currentNode == goal:
                return path, gCost
            
            # Explore neighbors
            for neighbor, cost in graph[currentNode].items():
                newPath = list(path)
                newPath.append(neighbor)
                newGCost = gCost + cost
                frontier.append((neighbor, newPath, newGCost))
        
        return None, float('inf')  # If no path is found
    
    # Run A* Tree Search
    startNode = 'A'
    goalNode = 'J'
    path, cost = aStarTreeSearch(graph, startNode, goalNode, heuristic)
    
    print(f"A* Tree Search Path: {path}")
    print(f"Total Cost: {cost}")
