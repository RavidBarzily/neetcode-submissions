# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        flag = head
        while n > 1:
            flag = flag.next
            n -= 1
        curr = head
        prev = None
        while flag.next:
            prev = curr
            flag = flag.next
            curr = curr.next
        if curr == head:
            return head.next
        prev.next = curr.next
        return head
        