'''
Longest Substring Without Repeating Characters
36ms, 99.91%, 42.84%
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = ""
        temp_out = ""
        for char in s:
            if char not in temp_out: temp_out += char
            else:
                if len(temp_out) > len(output):
                    output = temp_out
                temp_out = temp_out[temp_out.index(char)+1:] + char
            #print(temp_out)
                
        if len(temp_out) > len(output):
            output = temp_out
            
        return len(output)