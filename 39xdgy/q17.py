'''
letter combinations of phone number
36ms, 9.78%, 26.20%
??? No good answer found
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keywords = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        if len(digits) == 0: return []
        
        def recurse(digits):
            if len(digits) == 1: return [key for key in keywords[int(digits)]]
            else:
                l1 = [key for key in keywords[int(digits[0])]]
                l2 = recurse(digits[1:])
                return [a+b for a in l1 for b in l2]
            
        return recurse(digits)