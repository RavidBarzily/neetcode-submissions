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
        if not head:
            return None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = Node(curr.val, nxt)
            curr = nxt

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
    
        curr = head
        sol = head.next
        while curr.next.next:
            nxt = curr.next
            curr.next =  curr.next.next
            nxt.next = curr.next.next
            curr = curr.next
        curr.next = None
        return sol