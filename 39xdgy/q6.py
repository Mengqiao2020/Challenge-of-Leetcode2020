'''
ZigZag Conversion
52ms, 86.41%, 35.37%
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix = []
        group_num = 2*numRows - 2
        output = ""
        index_bottom = numRows - 1
        if len(s) <= 2 or numRows == 1: return s
        for i in range(numRows):
            matrix.append("")
            
        for i in range(len(s)):
            check_index = i % group_num
            if check_index >= numRows: check_index = index_bottom - (check_index % index_bottom)
            matrix[check_index] += s[i]
        
        
        return "".join(matrix)