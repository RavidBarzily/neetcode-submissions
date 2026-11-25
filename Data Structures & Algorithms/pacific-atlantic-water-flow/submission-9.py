from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def helper(curr):
            seen = set(curr)
            q = deque(list(curr))
            while q:
                i,j = q.popleft()
                for dr,dc in directions:
                    nr = dr + i
                    nc = dc + j
                    if 0 <= nr < len(heights) and 0 <= nc < len(heights[0]) and (nr,nc) not in seen and heights[nr][nc] >= heights[i][j]:
                        seen.add((nr,nc))
                        q.append((nr,nc))
            return seen

        pasific_start = set()
        atlantic_start = set()
        for i in range(len(heights)):
            pasific_start.add((i,0))
            atlantic_start.add((i,len(heights[0]) - 1))
        for j in range(len(heights[0])):
            pasific_start.add((0,j))
            atlantic_start.add((len(heights) - 1,j))

        pasific = helper(pasific_start)
        atlantic = helper(atlantic_start)

        return list(pasific & atlantic)