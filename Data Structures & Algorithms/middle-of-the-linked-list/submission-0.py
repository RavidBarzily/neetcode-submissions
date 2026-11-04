# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head.next
        count = 0
        while head:
            head = head.next
            count += 1
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if count%2 == 0:
            return slow.next
        else:
            return slow