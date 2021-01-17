'''
!
remove duplicates from sorted array
80ms, 80.15%, 79.74%
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        count = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:  
                nums[count] = nums[i]
                count += 1
        return count
        
        