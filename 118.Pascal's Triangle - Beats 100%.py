'''
118. Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Base case
        if numRows <= 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            curr = [sum(res[i-1][j:j+2]) for j in range(0, len(res[i-1]) - 1)]
            res.append([*[1], *curr, *[1]])
        return res