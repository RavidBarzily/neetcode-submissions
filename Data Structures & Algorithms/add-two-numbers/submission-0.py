# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = 0
        digit = 0
        carry = 0
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            curr_sum = l1.val + l2.val + carry
            digit = curr_sum % 10
            carry = curr_sum // 10
            curr.next = ListNode(digit)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            curr_sum = l1.val + carry
            digit = curr_sum % 10
            carry = curr_sum // 10
            curr.next = ListNode(digit)
            curr = curr.next
            l1 = l1.next
        while l2:
            curr_sum = l2.val + carry
            digit = curr_sum % 10
            carry = curr_sum // 10
            curr.next = ListNode(digit)
            curr = curr.next
            l2 = l2.next
        while carry > 0:
            digit = carry % 10
            carry = carry // 10
            curr.next = ListNode(digit)
            curr = curr.next
        return dummy.next