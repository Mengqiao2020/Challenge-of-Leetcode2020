'''
Container with most water
136ms, 99.93%, 14.43%
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        output = 0
        while l < r:
            if height[l] <= height[r]:
                temp_out = (r-l)*height[l]
                l += 1
                
                if temp_out > output:
                    output = temp_out
                    
            else:
                temp_out = (r-l)*height[r]
                r -= 1
                
                if temp_out > output:
                    output = temp_out
                    
        return output