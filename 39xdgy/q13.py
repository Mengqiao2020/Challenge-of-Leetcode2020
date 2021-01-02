'''
!
Roman to Integer
32ms, 99.42%, 92.94%
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        value = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        output = value[s[-1]]
        
        for i in range(len(s)-1, 0, -1):
            if(value[s[i-1]] < value[s[i]]):
                output -= value[s[i-1]]
            else:
                output += value[s[i-1]]
                
                
        return output