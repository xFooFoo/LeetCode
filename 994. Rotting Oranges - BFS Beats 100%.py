'''
994. Rotting Oranges

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
'''

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set() # aka infected
        rotten_q = deque()
        freshOranges = 0
        mins = 0
        directions = [(-1, 0), (1,0), (0, -1), (0, 1)] # up down left right

        # One pass to initialise the rotten_q and count the number of fresh oranges
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    rotten_q.append((row,col))
                if grid[row][col] == 1:
                    freshOranges += 1
        
        while rotten_q:
            startFreshOranges = freshOranges
            for _ in range(len(rotten_q)):
                r, c = rotten_q.popleft()
                #print(f"current {r},{c}")
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr,nc) not in visited and 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        #print(f"infected {nr},{nc}")
                        grid[nr][nc] = 2 # make neighbouring fresh orange rotten
                        freshOranges -= 1
                        visited.add((nr,nc))
                        rotten_q.append((nr,nc))
            # No changes in freshOrange count means the run should have "finished" in the previous
            if startFreshOranges == freshOranges:
                break
            else:
                mins += 1
            #print(f"end of min {mins}")

        return mins if freshOranges == 0 else -1