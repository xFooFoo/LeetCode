'''
216. Combination Sum III

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
 

Constraints:

2 <= k <= 9
1 <= n <= 60
'''
from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.output = []
        state = list(range(1,10))
        self.solve(k, n, [], state)
        return self.output

    def solve(self, k: int, n: int, curr_state: List[int], state: List[int]):
        # Base case: if k is 0 and sum of curr_state is n
        if k == 0 and n == 0:
            self.output.append(list(curr_state)) # use a copy of the list because we are passing its reference in further recurses
            return
        
        # Early exit if k or n becomes invalid i.e. not a valid solution
        if k <= 0 or n <= 0:
            return

        # Explore each number in state
        for i in range(len(state)):
            num = state[i]
            curr_state.append(num)
            
            # Recurse with reduced k and n, and use only numbers after the current one (to avoid duplicates)
            self.solve(k-1, n-num, curr_state, state[i+1:])

            # Backtrack
            curr_state.pop()
