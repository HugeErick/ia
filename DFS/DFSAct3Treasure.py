from collections import deque

def findTreasureDfs(island, start, treasure):
    rows = len(island)
    cols = len(island[0])

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    queue = deque([(start[0], start[1], [start])])

    visited = set([start])

    while queue:
        row, col, path = queue.pop()
        print(f"Exploring position: ({row}, {col})")

        if (row, col) == treasure:
            return path

        for dx, dy in directions:
            newRow, newCol = row + dx, col + dy

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

def DFSAct3TreasureMap():
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
    path = findTreasureDfs(island, start, treasure)
    
    # Print the result
    if path:
        print("\nPath found! Here's the route:")
        printPathOnMap(island, path)
        print(f"\nSteps to reach treasure: {len(path) - 1}")
    else:
        print("No path to treasure exists!")
