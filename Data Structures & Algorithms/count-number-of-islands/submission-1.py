class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        queue = deque()
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    count += 1
                    queue.append((r, c))
                    visited.add((r, c))
                    while queue:
                        row, col = queue.popleft()
                        for dr, dc in directions:
                            nr = row + dr
                            nc = col + dc
                            if (
                                0 <= nr < len(grid)
                                and 0 <= nc < len(grid[0])
                                and grid[nr][nc] == "1"
                                and (nr, nc) not in visited
                            ):
                                visited.add((nr, nc))
                                queue.append((nr, nc))

        return count