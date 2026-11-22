class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def helper(curr):
            visited = set()
            q = deque(curr)
        
            while q:
                r,c = q.popleft()
                visited.add((r,c))
                for dr,dc in directions:
                    nr = dr + r
                    nc = dc + c
                    if 0 <= nr < len(heights) and 0 <= nc < len(heights[0]) and (nr,nc) not in visited and heights[nr][nc] >= heights[r][c]:
                        visited.add((r,c))
                        q.append((nr,nc))
            
            return visited

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
