'''
divide two integers
28ms, 91.02%, 80.81%
'''
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        output = dividend // divisor
        if output < 0 and dividend % divisor != 0: output += 1
             
        if -2**31 <= output < 2**31 -1:
            return output 
        else: return 2**31 - 1