from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(i,j,visited,prev):
            if not (0 <= i < len(heights)) or not (0 <= j < len(heights[0])) or heights[i][j] < prev or (i,j) in visited:
                return visited
            
            visited.add((i,j))
            dfs(i + 1,j,visited,heights[i][j])
            dfs(i - 1,j,visited,heights[i][j])
            dfs(i,j + 1,visited,heights[i][j])
            dfs(i,j - 1,visited,heights[i][j])

            return visited

        pasific = set()
        atlantic = set()
        for i in range(len(heights)):
            pasific = dfs(i,0,pasific,heights[i][0])
            atlantic = dfs(i,len(heights[0]) - 1,atlantic,heights[i][len(heights[0]) - 1])
        for j in range(len(heights[0])):
            pasific = dfs(0,j,pasific,heights[0][j])
            atlantic = dfs(len(heights) - 1,j,atlantic,heights[len(heights) - 1][j])

        return list(pasific & atlantic)