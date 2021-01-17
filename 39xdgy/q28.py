'''
implement strstr
32ms, 71.19%, 97.67%
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == "" and needle == "": return 0 
        return haystack.find(needle)
        