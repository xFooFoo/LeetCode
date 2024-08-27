from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        runs = 0
        while sum(nums) > 0:
            i = 0
            while i < len(nums):
                if nums[i] <= 0:
                    nums.pop(i)
                else:
                    i += 1
            
            print(nums)

            runMinimum = min(nums)

            for j in range(0, len(nums)):
                nums[j] -= runMinimum
            print(nums)
            runs += 1
        return runs
