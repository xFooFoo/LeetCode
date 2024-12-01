'''
69. Sqrt(x)

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

Constraints:

0 <= x <= 231 - 1
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        upper = x//2
        lower = 1
        mid = (upper + lower)//2

        if x == 1: return 1

        while lower <= upper:
            if mid == x//mid:
                return mid
            elif mid * mid > x:
                upper = mid - 1
            else:
                lower = mid + 1
            mid = (upper + lower)//2
        return mid