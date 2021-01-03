'''
!
valid parantheses
28ms, 82.90%, 52.98%
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par_dic = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        
        for i in s:
            if i == "{" or i == "[" or i == "(":
                stack.append(i)
            else:
                if len(stack) > 0 and stack[-1] == par_dic[i]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0: return True
        return False

