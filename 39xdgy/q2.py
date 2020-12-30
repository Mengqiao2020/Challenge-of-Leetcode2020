'''
Add Two Numbers
68ms, 74.44%, 8.53%
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        l1_val = 0
        while l1.next != None:
            l1_val += l1.val
            l1 = l1.next
        l1_val += l1.val
        
        l2_val = 0
        while l2.next != None:
            l2_val += l2.val
            l2 = l2.next
        l2_val += l2.val
        
        total = l1_val + l2_val
        '''
        
        temp_val = l1.val + l2.val
        indent = 0
        if temp_val >= 10:
            temp_val -= 10
            indent = 1
            
        output = ListNode(val = temp_val)
        
        if l1.next != None and l2.next == None:
            output.next = Solution.addTwoNumbers(self, l1.next, ListNode(val = indent))
        elif l2.next != None and l1.next == None:
            output.next = Solution.addTwoNumbers(self, ListNode(val = indent), l2.next)
        elif l1.next == None and l2.next == None and indent == 1:
            output.next = ListNode(val = 1)
        elif l1.next != None and l2.next != None:
            l1.next.val += indent
            output.next = Solution.addTwoNumbers(self, l1.next, l2.next)
        
        
        
        
        
        return output
        
            
        