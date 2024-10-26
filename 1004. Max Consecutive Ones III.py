'''
1004. Max Consecutive Ones III

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
'''

from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        currentOnes, maxOnes, nonOnes = 0, 0, 0
        for i in range(0, len(nums)):
            # Check new element into the window
            if nums[i] == 1:
                currentOnes += 1
            else:
                nonOnes += 1
                
                

            if nonOnes <= k:
                maxOnes = max(maxOnes, currentOnes + nonOnes)
            else: # We check the lost element from window
                #print(f'Run {i+1} currentOnes nonOnes {currentOnes} {nonOnes}')
                #print(f'Run {i+1} nums[i-(currentOnes+nonOnes+1)] {nums[i-(currentOnes+nonOnes+1)]}')
                if nums[i-(currentOnes+nonOnes-1)] == 1:
                    currentOnes -= 1
                # Case nonOnes = k, keep increasing max
                else:
                    nonOnes -= 1
                    maxOnes = max(maxOnes, currentOnes + nonOnes)
                    

            #print(f'Run {i+1}\nCurrentOnes {currentOnes}\nnonOnes {nonOnes}\nmaxOnes {maxOnes}')
            # Update max if at most k is flipped

        return maxOnes
              
# nums = [1,1,1,0,0,0,1,1,1,1,0]
# k = 2
# s = Solution()    
# print(s.longestOnes(nums, k))