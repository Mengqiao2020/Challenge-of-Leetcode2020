'''
!!!
Revers Node in K-Group
44ms, 91.90%, 45.70%
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = kth = head
        sub_head = dummy
        
        i = 1
        while kth.next:
            kth = kth.next 
            i+=1 
            if i%k == 0 and k > 1:
                pr = sub_head.next
                cur = pr.next
                while cur != kth:
                    tmp = cur.next 
                    cur.next, pr = pr, cur
                    cur = tmp
                tmp_sub_head = sub_head.next
                sub_head.next.next, sub_head.next = kth.next, kth
                kth.next = pr
                sub_head = kth = tmp_sub_head
                
        return dummy.next
        