'''
1718. Construct the Lexicographically Largest Valid Sequence

Given an integer n, find a sequence that satisfies all of the following:

The integer 1 occurs once in the sequence.
Each integer between 2 and n occurs twice in the sequence.
For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.
The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.

Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.

A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, sequence a has a number greater than the corresponding number in b. For example, [0,1,9,0] is lexicographically larger than [0,1,5,6] because the first position they differ is at the third number, and 9 is greater than 5.

 

Example 1:

Input: n = 3
Output: [3,1,2,3,2]
Explanation: [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the lexicographically largest valid sequence.
Example 2:

Input: n = 5
Output: [5,3,1,4,3,5,2,4,2]
 

Constraints:

1 <= n <= 20
'''

from typing import List
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ans = [0] * (2 * n - 1)
        used = set()
        def backtrack(index: int) -> bool:
            if index == len(ans):  # If all positions are filled
                return True

            if ans[index] != 0:  # Skip pre-filled positions
                return backtrack(index + 1)

            for num in range(n, 0, -1):  # Try placing largest to smallest
                if num in used:
                    continue

                if num == 1:  # 1 appears only once
                    ans[index] = 1
                    used.add(1)
                    if backtrack(index + 1):
                        return True
                    # False -> Undo changes and check next number in the loop   
                    ans[index] = 0
                    used.remove(1)
                else:  # num > 1, fill two positions at once
                    if index + num < len(ans) and ans[index + num] == 0:
                        ans[index] = ans[index + num] = num
                        used.add(num)
                        if backtrack(index + 1):
                            return True
                        # False -> Undo changes and check next number in the loop   
                        ans[index] = ans[index + num] = 0
                        used.remove(num)

            return False  # No valid sequence found

        backtrack(0)
        return ans