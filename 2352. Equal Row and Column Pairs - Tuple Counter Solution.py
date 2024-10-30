'''
2352. Equal Row and Column Pairs

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

 

Example 1:


Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
Example 2:


Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
 

Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 105
'''

from collections import Counter
from typing import List
class Solution:
    # Only works for a n x n matrix
    def transpose(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        output =[[0] * n for i in range(n)]
        # print(output)
        for i in range(n):
            for j in range(n):
                output[j][i] = grid[i][j]
        #print(output)
        return output

    def equalPairs(self, grid: List[List[int]]) -> int:
        pairs = 0
        row_count = Counter(map(tuple, grid))
        col_tuple = map(tuple, self.transpose(grid))
        for col in col_tuple:
            #print(f'col {col}')
            if col in row_count:
                pairs += row_count[col]
        return pairs
        