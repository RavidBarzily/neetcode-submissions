from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i,j))
        while queue:
            r,c = queue.popleft()
            for dr,dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr,nc))
        return None