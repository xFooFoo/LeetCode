'''
215. Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def build_max_heap(nums: List[int], n: int):
            # Starts heapifying from the last non-leaf node
            for idx in range(n//2, 0, -1):
                heapify(nums, n, idx)

        def heapify(nums: List[int], n: int, idx: int):
            largest = idx
            left = idx * 2
            right = idx * 2 + 1

            if left < n and nums[largest] < nums[left]:
                largest = left
            if right < n and nums[largest] < nums[right]:
                largest = right
            
            if largest != idx:
                nums[idx], nums[largest] = nums[largest], nums[idx] # swap smaller parent with largest child
                heapify(nums, n, largest) # heapify the swapped ex-parent now-child node
        
        # This makes indexing easier by starting at index-1
        nums = [None] + nums
        n = len(nums)
        build_max_heap(nums, n)

        # Find kth largest element
        for _ in range(k-1):
            nums[1], nums[n-1] = nums[n-1], nums[1] # Swap largest & smallest element
            n -= 1 # Essentially delete the largest element
            heapify(nums, n, 1) # Restore heap property

        return nums[1] # return kth largest element


