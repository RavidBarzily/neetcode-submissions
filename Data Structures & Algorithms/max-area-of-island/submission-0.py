class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_area = 0
        def dfs(r,c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0 or (r,c) in visited:
                return 0
            area = 1
            visited.add((r,c))
            for dr,dc in directions:
                area += dfs(r + dr,c + dc)
            return area
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    max_area = max(max_area,dfs(i,j))
        return max_area