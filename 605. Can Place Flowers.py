'''
605. Can Place Flowers
Easy
Topics
Companies
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
'''
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        size = len(flowerbed)
        idx = size -1
        # Flowerbed size 1 case, ABS sum gives less than 1 in  (0,0), (0,1) & (1,0) case
        if size == 1:
            return flowerbed[0] + n <= 1
        # Left-most Plot Case (0,0)
        if (not flowerbed[0] and not flowerbed[1]):
            flowerbed[0] = 1 # plant at left-most as convention
            n -= 1
        # Check Right-most Plot Case if itself and its left are both empty
        if (not flowerbed[idx] and not flowerbed[idx - 1]):
            flowerbed[idx] = 1 # plant at left-most as convention
            n -= 1
        # Case for everything in between
        for i in range (1, idx):
            if (not flowerbed[i-1] and not flowerbed[i] and not flowerbed[i+1]):
                flowerbed[i] = 1
                n -= 1

        return n <= 0




'''# TESTING
print(Solution().canPlaceFlowers([1,0,0,0,1], 1))
print(Solution().canPlaceFlowers([1,0,0,0,1], 2))
#'''