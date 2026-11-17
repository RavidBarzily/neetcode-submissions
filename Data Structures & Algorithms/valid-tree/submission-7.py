class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        for a, b in edges:
            root_a, root_b = find(a), find(b)
            if root_a == root_b:       
                return False
            parent[root_b] = root_a

        return True