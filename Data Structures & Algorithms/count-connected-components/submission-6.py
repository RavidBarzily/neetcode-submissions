class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        
        def find(i):
            if i == parent[i]:
                return i 
            parent[i] = find(parent[i])
            return find(parent[i])

        for a,b in edges:
            root_a, root_b = find(a), find(b)
            if root_a != root_b:
                parent[root_b] = root_a
                n -= 1
            

        return n