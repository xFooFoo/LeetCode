'''
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
'''

'''
Intuition:
We keep performing XOR sequentially. What this does is to keep to flipping bits but the beauty
is when the same number is met twice, the bits would cancel themselves into all 0's, eventually...
And the remainder will be the number that only appears once and not cancelled by the XOR operation 
''' 

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        output = 0
        for num in nums:
            output = output^num
        return output