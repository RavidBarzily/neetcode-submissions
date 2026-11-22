# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        flag = head
        dummy = ListNode(0,head)
        curr = dummy
        for _ in range(n):
            flag = flag.next
        
        while flag:
            flag = flag.next
            curr = curr.next
        
        curr.next = curr.next.next
        return dummy.next