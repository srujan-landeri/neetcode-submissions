from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque()
        time = 0

        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append([i, j, 0]) # row, col, time

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while len(q) > 0:

            r, c, t = q.popleft()
            time = max(time, t)

            for d in dirs:

                nr = r + d[0]
                nc = c + d[1]

                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                    q.append([nr, nc, time + 1])
                    grid[nr][nc] = 2

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
                    
        return time