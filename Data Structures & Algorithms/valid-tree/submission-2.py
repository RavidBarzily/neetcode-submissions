class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()

        def dfs(i, parent):
            visited.add(i)
            for nei in adj[i]:
                if nei in visited and parent != nei:
                    return False
                elif nei not in visited:
                    if not dfs(nei,i):
                        return False
            return True
        
        return dfs(0,None) and n == len(visited)