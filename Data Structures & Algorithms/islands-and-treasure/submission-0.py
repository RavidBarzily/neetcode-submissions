from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i,j))
        while queue:
            r,c = queue.popleft()
            if r + 1 < len(grid) and grid[r+1][c] == 2147483647:
                grid[r+1][c] = grid[r][c] + 1
                queue.append((r+1,c))
            if c + 1 < len(grid[0]) and grid[r][c+1] == 2147483647:
                grid[r][c+1] = grid[r][c] + 1
                queue.append((r,c+1))
            if r - 1 >= 0 and grid[r-1][c] == 2147483647:
                grid[r-1][c] = grid[r][c] + 1
                queue.append((r-1,c))
            if c - 1 >= 0 and grid[r][c-1] == 2147483647:
                grid[r][c-1] = grid[r][c] + 1
                queue.append((r,c-1))
        return None