class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n or len(edges) < n - 1:
            return False
        adj = {i: [] for i in range(n)}

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
                    q.append(nei)
                    visited.add(nei)
            
        return n == len(visited)