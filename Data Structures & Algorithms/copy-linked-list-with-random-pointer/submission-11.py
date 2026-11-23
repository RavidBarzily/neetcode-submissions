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
        dummy = Node(0)
        curr = head
        while curr:
            nxt = curr.next
            curr.next = Node(curr.val, nxt)
            curr = nxt

        curr = head
        dummy.next = curr.next
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
    
        copy = dummy.next
        curr = head
        while curr.next.next:
            copy.next, curr.next =  copy.next.next, curr.next.next
            copy, curr = copy.next, curr.next

        return dummy.next