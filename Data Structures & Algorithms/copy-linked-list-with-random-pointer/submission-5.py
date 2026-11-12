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
            curr.next = Node(curr.val,nxt)
            curr = nxt
        
        curr = head
        copy = head.next
        while curr:
            if curr.random:
                copy.random = curr.random.next
            curr = curr.next.next
            if copy.next:
                copy = copy.next.next

        dummy = Node(0,head.next)
        copy = head.next
        curr = head
        while copy.next:
            nxt = copy.next
            copy.next = copy.next.next
            copy = copy.next
            curr.next = nxt
            
        return dummy.next