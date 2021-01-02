'''
longest common prefix
28ms, 91.99%, 70.51%
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs.sort(key = len)
        
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        output = strs[0]
        
        for word in strs[1:]:
            while output != "":
                if output != word[:len(output)]:
                    output = output[:-1]
                else: break
                    
            if not output: return ""
            
        return output