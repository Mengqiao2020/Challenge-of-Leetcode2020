'''
String to Integer (atoi)
28ms, 93.42%, 19.81%
'''
class Solution:
    def myAtoi(self, s: str) -> int:
        if not s: return 0
        if len(s) == 1 and s.isdigit(): return int(s)
        if len(s) == 1 and not s.isdigit(): return 0
        
        start_index = 0
        for i in range(len(s)):
            if s[i] == " ":
                next
            elif s[i].isdigit() or s[i] == "+" or s[i] == "-":
                if(i == len(s) - 1): return 0
                start_index = i
                break
            else: return 0
            
        output_str = ""
        print(start_index)
        for i in range(start_index + 1, len(s)):
            if not s[i].isdigit():
                output_str = s[start_index: i]
                break
                
        if output_str == "": output_str = s[start_index:]
        try:
            output = int(output_str)
        except: return 0
        if output < -2**31: return -2**31
        if output > 2**31 - 1: return 2**31 - 1
        return output
