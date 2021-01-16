'''
!
merge k sorted lists
80ms, 99.89%, 33.17%
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        flattened_sorted = []
        for ls in lists:
            element = ls
            while element:
                flattened_sorted.append(element.val)
                element = element.next
        
        if not flattened_sorted: return
        flattened_sorted.sort()

        start = ListNode(flattened_sorted[0])
        output = start
        for idx, element in enumerate(flattened_sorted):
            if idx < len(flattened_sorted) - 1:
                output.val = element
                output.next = ListNode(flattened_sorted[idx + 1])
                output = output.next
                
        return start