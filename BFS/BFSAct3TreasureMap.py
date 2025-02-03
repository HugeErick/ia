from collections import deque

def findTreasureBfs(island, start, treasure):
    rows = len(island)
    cols = len(island[0])
    
    # Define possible movements (up, right, down, left)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # Queue will store (row, col, path)
    queue = deque([(start[0], start[1], [start])])
    
    # Keep track of visited cells
    visited = set([start])
    
    while queue:
        row, col, path = queue.popleft()
        print(f"Exploring position: ({row}, {col})")
        
        # Check if we found the treasure
        if (row, col) == treasure:
            return path
        
        # Try all possible directions
        for dx, dy in directions:
            newRow, newCol = row + dx, col + dy
            
            # Check if the new position is valid
            # the first two lines is index bounding 
            # then if it it is not an obstacle
            # and finally if not visited
            if (0 <= newRow < rows and 
                0 <= newCol < cols and 
                island[newRow][newCol] != 1 and 
                (newRow, newCol) not in visited):
                
                visited.add((newRow, newCol))
                newPath = path + [(newRow, newCol)]
                queue.append((newRow, newCol, newPath))
    
    return None  # No path found

def printPathOnMap(island, path):
    if not path:
        print("No path found!")
        return
        
    # Create a copy of the island for visualization
    visualMap = []
    for row in island:
        visualMap.append(list(str(cell) for cell in row))
    
    # Mark the path with '*'
    for i, (row, col) in enumerate(path):
        if i == 0:
            visualMap[row][col] = 'S'  # Start
        elif i == len(path) - 1:
            visualMap[row][col] = 'T'  # Treasure
        else:
            visualMap[row][col] = '*'
    
    # Print the map with the path
    for row in visualMap:
        print(' '.join(row))

def BFSAct3TreasureMap():
    island = [
        [0, 0, 1, 0],
        [1, 0, 1, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 1],
        [0, 0, 0, 'T'],
    ]
    
    start = (0, 0)
    treasure = (4, 3)
    
    # Find path to treasure
    path = findTreasureBfs(island, start, treasure)
    
    # Print the result
    if path:
        print("\nPath found! Here's the route:")
        printPathOnMap(island, path)
        print(f"\nSteps to reach treasure: {len(path) - 1}")
    else:
        print("No path to treasure exists!")
