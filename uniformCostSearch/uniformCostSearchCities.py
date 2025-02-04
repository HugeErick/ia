from collections import defaultdict, deque

def uniformCostSearchCities():
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
    
    def greedy_search(graph, start, goal, heuristic):
        # Priority queue to store nodes to be explored, sorted by heuristic value
        frontier = deque()
        frontier.append((start, [start], 0))  # (current_node, path, total_cost)
        
        while frontier:
            # Sort the frontier by heuristic value of the last node in the path
            frontier = deque(sorted(frontier, key=lambda x: heuristic[x[0]]))
            current_node, path, total_cost = frontier.popleft()
            
            # Check if the goal is reached
            if current_node == goal:
                return path, total_cost
            
            # Explore neighbors
            for neighbor, cost in graph[current_node].items():
                if neighbor not in path:
                    new_path = list(path)
                    new_path.append(neighbor)
                    new_cost = total_cost + cost
                    frontier.append((neighbor, new_path, new_cost))
        
        return None, float('inf')  # If no path is found
    
    # Run Greedy Search
    start = 'A'
    goal = 'J'
    path, cost = greedy_search(graph, start, goal, heuristic)
    
    print(f"Greedy Search Path: {path}")
    print(f"Total Cost: {cost}")
