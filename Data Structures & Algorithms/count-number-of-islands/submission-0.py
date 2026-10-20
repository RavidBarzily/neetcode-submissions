class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        def findNewLand(i,j):
            if i >= len(grid) or i < 0 or j < 0 or j >= len(grid[0]) or grid[i][j]== "0":
                return
            grid[i][j] = "0"
            findNewLand(i+1,j)
            findNewLand(i,j+1)
            findNewLand(i-1,j)
            findNewLand(i,j-1)
        count = 0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    findNewLand(i,j)
        return count