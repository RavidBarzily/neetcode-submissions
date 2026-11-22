class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adj = [[] for _ in range(n)]
        for a,b in edges:
            adj[a].append(b) 
            adj[b].append(a)
        visited = set()
        q = deque([0])
        visited.add(0)

        while q:
            curr = q.popleft()
            for nei in adj[curr]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
                    
        return len(visited) == n
