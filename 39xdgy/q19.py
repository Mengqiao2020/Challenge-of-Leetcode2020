'''
!
remove nth node from end of list
32ms, 76.23%, 66.80%
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        i = j = head
        while n>0:
            j = j.next
            n-=1
        if not j:
            return head.next
        while j.next:
            i = i.next
            j = j.next
        i.next = i.next.next
        return head