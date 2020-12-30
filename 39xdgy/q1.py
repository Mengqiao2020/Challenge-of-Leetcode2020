'''
two sum
44ms, 87.18%, 98.99%
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(0, len(nums)):
            check_value = target - nums[i]
            if check_value in map: return [map[check_value], i]
            map[nums[i]] = i
        return []