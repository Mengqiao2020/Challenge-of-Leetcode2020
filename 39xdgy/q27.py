'''
!
remove element
28ms, 92.72%, 75.89%
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while(val in nums):
            del nums[nums.index(val)]
        return len(nums)
        