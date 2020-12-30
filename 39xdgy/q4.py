'''
Median of Two Sorted Arrays
88ms, 81.36%, 98.49%
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        all_list = nums1 + nums2
        all_list.sort()
        if len(all_list) % 2 == 1:
            return all_list[len(all_list) // 2]
        
        return (all_list[len(all_list) // 2] + all_list[len(all_list) // 2 - 1]) / 2