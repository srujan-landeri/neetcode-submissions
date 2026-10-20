from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Initialize constants
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left
        
        # Initialize queue for BFS
        q = deque()
        
        # Add all treasure cells (0) to the queue and set their distances to 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        # BFS to update distances
        while q:
            r, c = q.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check if the new cell is valid and is an INF cell
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF:
                    # Update distance for the land cell
                    grid[nr][nc] = grid[r][c] + 1
                    # Enqueue the cell for further BFS
                    q.append((nr, nc))
                    