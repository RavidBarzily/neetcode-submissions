# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        prev = slow.next = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        curr, second = head, prev
        while second:
            curr_nxt, second_nxt = curr.next, second.next
            curr.next = second
            second.next = curr_nxt
            second, curr = second_nxt, curr_nxt