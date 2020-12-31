'''
Reverse Integer
28ms, 87.33%, 88.35%
'''
class Solution:
    def reverse(self, x: int) -> int:
        if(x < -2**31 or x > 2**31 - 1): return 0
        flag = x < 0
        if(flag): x *= -1
        
        out = int(str(x)[::-1])
        
        if(flag): out *= -1
        if(out < -2**31 or out > 2**31 - 1): return 0
        return out
        
        