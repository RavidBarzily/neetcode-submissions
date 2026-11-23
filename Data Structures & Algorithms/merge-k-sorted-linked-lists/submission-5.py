# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
    
        def mergeTwo(list1,list2):
            dummy = ListNode(0)
            curr = dummy
            while list1 and list2:
                if list1.val <= list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next

            curr.next = list1 or list2
            return dummy.next
        
        gap = 1
        while gap < len(lists):
            i = 0
            while i + gap < len(lists):
                lists[i] = mergeTwo(lists[i], lists[i + gap])
                i += gap * 2
            gap *= 2
        return lists[0]