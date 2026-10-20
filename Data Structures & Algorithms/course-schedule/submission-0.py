class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        count = [0] * numCourses
        for a, b in prerequisites:
            graph[a].append(b)
            count[b] += 1
        queue = deque()
        for i in range(numCourses):
            if count[i] == 0:
                queue.append(i)
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for nxt in graph[node]:
                count[nxt] -= 1
                if count[nxt] == 0:
                    queue.append(nxt)
        if len(order) != numCourses:
            return False
        return True