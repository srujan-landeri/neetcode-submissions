class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        area = 0
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area = max(area, self.dfs(grid, i, j))
                    print(i, j, area)
        
        return area

    def dfs(self, grid, r, c):
        
        area = 0

        if r >= len(grid) or c >= len(grid[0]) or c <= -1 or r <= -1 or grid[r][c] == 0:
            return area
        else:
            area += 1

        grid[r][c] = 0

        area += self.dfs(grid, r + 1, c)
        area += self.dfs(grid, r - 1, c)
        area += self.dfs(grid, r, c + 1)
        area += self.dfs(grid, r, c - 1)
        
        return area