from collections import deque

def uniformCostSearchCities():
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
    
    def uniformCostSearch(graph, start, goal):
        # Priority queue to store nodes to be explored, sorted by total cost
        frontier = deque()
        frontier.append((start, [start], 0))  # (currentNode, path, totalCost)
        
        # Set to keep track of visited nodes
        visited = set()
        
        while frontier:
            # Sort the frontier by total cost
            frontier = deque(sorted(frontier, key=lambda x: x[2]))
            currentNode, path, totalCost = frontier.popleft()
            
            # Check if the goal is reached
            if currentNode == goal:
                return path, totalCost
            
            # Mark the current node as visited
            visited.add(currentNode)
            
            # Explore neighbors
            for neighbor, cost in graph[currentNode].items():
                if neighbor not in visited:
                    newPath = list(path)
                    newPath.append(neighbor)
                    newCost = totalCost + cost
                    frontier.append((neighbor, newPath, newCost))
        
        return None, float('inf')  # If no path is found
    
    # Run Uniform Cost Search
    startNode = 'A'
    goalNode = 'J'
    path, cost = uniformCostSearch(graph, startNode, goalNode)
    
    print(f"Uniform Cost Search Path: {path}")
    print(f"Total Cost: {cost}")
