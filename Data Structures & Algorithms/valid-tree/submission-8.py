class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adj = {i: [] for i in range(n)}
        for a,b in edges:
            adj[a].append(b) 
            adj[b].append(a)
        print(adj)
        visited = set()
        def dfs(curr):
            visited.add(curr)
            for i in adj[curr]:
                if i not in visited:
                    dfs(i)

        dfs(0)
        return len(visited) == n
