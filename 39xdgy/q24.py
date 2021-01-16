'''
Swap Nodes in Pairs
24ms, 95.64%, 92.89%
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head: return
        if not head.next: return head
        empty = ListNode()
        
        is_head = True
        
        while True:
            if is_head and head.next:
                is_head = False
                temp_node = head.next
                head.next = head.next.next
                temp_node.next = head
                empty.next = temp_node
                head = empty.next.next
            elif head.next and head.next.next:
                temp_node = head.next.next
                head.next.next = temp_node.next
                temp_node.next = head.next
                head.next = temp_node
                head = head.next.next
            else:
                break
                
        return empty.next