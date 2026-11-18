class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def helper(starts):
            seen = set(starts)
            stack = list(starts)
            directions = [(1,0),(0,1),(-1,0),(0,-1)]
            while stack:
                i, j = stack.pop()
                for dr,dc in directions:
                    nr = dr + i
                    nc = dc + j
                    if (nr,nc) not in seen and 0 <= nr < len(heights) and 0 <= nc < len(heights[0]) and heights[i][j] <= heights[nr][nc]:
                        seen.add((nr,nc))
                        stack.append((nr,nc))

            return seen
        
        pasific_start = list()
        atlantic_start = list()
        for j in range(len(heights[0])):
            pasific_start.append((0,j))
            atlantic_start.append((len(heights) - 1,j))

        for i in range(len(heights)):
            pasific_start.append((i,0))
            atlantic_start.append((i,len(heights[0]) - 1))

        pasific = helper(pasific_start)
        atlantic = helper(atlantic_start)
        return list(pasific & atlantic)
