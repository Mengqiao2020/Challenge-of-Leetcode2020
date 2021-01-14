'''
merge two sorted lists
28ms, 98.20%, 92.18%
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        flag = output = ListNode()
        
        while l1 or l2:
            if not l1:
                flag.next = l2
                break
            if not l2:
                flag.next = l1
                break
            
            if l1.val <= l2.val:
                flag.next = l1
                l1 = l1.next
            else:
                flag.next = l2
                l2 = l2.next
            flag = flag.next
            
        return output.next
        