'''
171. Excel Sheet Column Number

Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701
 

Constraints:

1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].
'''
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        col_num = 0
        n = len(columnTitle) # 2, 1, 0 for len 3
        base_val = ord('A')

        for i in range(n):
            col_num  += (ord(columnTitle[i]) - base_val + 1) * 26**(n - i - 1)
        
        return col_num