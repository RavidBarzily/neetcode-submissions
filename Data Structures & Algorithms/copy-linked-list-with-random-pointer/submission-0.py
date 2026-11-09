"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map = dict()
        curr = head
        while curr:
            map[curr] = Node(curr.val)
            curr = curr.next
        for i in map:
            map[i].next = map.get(i.next)
            map[i].random = map.get(i.random)
        return map.get(head)