'''
62. Unique Paths

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:

1 <= m, n <= 100
'''
class Solution:
    def __init__(self):
        self.paths = 0

    def uniquePaths(self, m: int, n: int) -> int: # m is down, n is right
        def traversePath(current_m: int, current_n: int):
            if current_m < m and current_n < n:
                traversePath(current_m + 1, current_n)   # move down
                traversePath(current_m, current_n  + 1)  # move right
            if current_m == m - 1 and current_n == n - 1:
                self.paths += 1
        

        traversePath(0, 0)
        return self.paths