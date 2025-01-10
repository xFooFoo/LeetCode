'''
1137. N-th Tribonacci Number

The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537
 

Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
'''
class Solution:
    def tribonacci(self, n: int) -> int:
        res = 0
        if n <= 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            prev3, prev2, prev1 = 0, 1, 1
            for _ in range(3, n):
                prev3, prev2, prev1 = prev2, prev1, prev1 + prev2 + prev3
        
        return prev3 + prev2 + prev1
