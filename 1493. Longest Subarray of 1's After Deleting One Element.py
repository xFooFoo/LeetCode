'''
1493. Longest Subarray of 1's After Deleting One Element

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''

from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1 # number of deletions required
        left = 0
        right = 0 # just in case if nums is empty

        for right in range(len(nums)):
            if nums[right] != 1:
                k -= 1

            if k < 0:
                if nums[left] != 1:
                    k += 1
                left += 1
        
        return right-left # don't need to +1 to convert index to length since we must delete one element

# nums = [1,1]
# s = Solution()    
# print(s.longestSubarray(nums))