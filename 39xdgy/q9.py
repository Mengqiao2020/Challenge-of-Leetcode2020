'''
Palindrome Number
56ms, 881.15%, 28.67%
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]