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
        old_to_new = dict()
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        for i in old_to_new:
            old_to_new[i].next = old_to_new.get(i.next)
            old_to_new[i].random = old_to_new.get(i.random)
        return old_to_new.get(head)