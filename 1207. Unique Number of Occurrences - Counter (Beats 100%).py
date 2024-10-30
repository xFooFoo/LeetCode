'''
1207. Unique Number of Occurrences
Solved
Easy
Topics
Companies
Hint
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
'''

from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occur_dict = {}
        # Adding letter, ocurrences to dict
        for num in arr:
            occur_dict[num] = occur_dict.get(num, 0) + 1
        
        # Check if any counts are not unique
        occur_counts = Counter(occur_dict.values())
        for count in occur_counts.values():
            if count > 1:
                return False
        return True
            