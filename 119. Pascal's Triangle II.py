'''
119. Pascal's Triangle II

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33
'''
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        res = [1]
        print(res)
        for i in range(1, rowIndex+1):
            res = [sum(res[j - 1:j + 1]) if j > 0 else res[j] for j in range(0, i + 1)]  # We check if j > 0 otherwise we get negative slicing
            #print(res)
        return res



             

        