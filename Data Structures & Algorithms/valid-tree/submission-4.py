class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n or len(edges) < n - 1:
            return False
        adj = {i: [] for i in range(n)}

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()

        def dfs(i):
            visited.add(i)
            for nei in adj[i]:
                if nei not in visited:
                    dfs(nei)

        dfs(0)
        return n == len(visited)