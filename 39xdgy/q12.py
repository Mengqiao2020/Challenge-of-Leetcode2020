'''
Integer to Roman
44ms, 84.66%, 77.17%
'''
class Solution:
    def intToRoman(self, num: int) -> str:
        num_4 = num // 1000
        after_4 = num % 1000
        num_3 = after_4 // 100
        after_3 = after_4 % 100
        num_2 = after_3 // 10
        num_1 = after_3 % 10
        
        output = num_4 * "M"
        
        if num_3 == 9: output += "CM"
        elif num_3 == 4: output += "CD"
        else: output += (num_3 // 5) * "D" + (num_3 % 5) * "C"
            
            
        if num_2 == 9: output += "XC"
        elif num_2 == 4: output += "XL"
        else: output += (num_2 // 5) * "L" +(num_2 % 5) * "X"
        
        if num_1 == 9: output += "IX"
        elif num_1 == 4: output += "IV"
        else: output += (num_1 // 5) * "V" + (num_1 % 5) * "I"
            
        return output
        