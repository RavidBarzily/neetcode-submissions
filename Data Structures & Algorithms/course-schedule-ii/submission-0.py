class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        count = [0] * numCourses
        for a,b in prerequisites:
                graph[b].append(a)
                count[a] += 1
        q = deque()
        for i in range(numCourses):
            if count[i] == 0:
                q.append(i)
        order = []
        while q:
                curr = q.popleft()
                order.append(curr)
                for i in graph[curr]:
                    count[i] -= 1
                    if count[i] == 0:
                        q.append(i)
        if len(order) != numCourses:
            return []
        return order
