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
        prev, slow.next = None, None

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        second = prev
        curr = head
        while curr and second:
            curr_nxt = curr.next
            second_nxt = second.next
            curr.next = second
            second.next = curr_nxt
            second, curr = second_nxt, curr_nxt
        


    