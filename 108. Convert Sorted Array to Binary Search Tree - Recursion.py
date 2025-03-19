'''
108. Convert Sorted Array to Binary Search Tree

Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced
 binary search tree.

 

Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def splitArray(nums: List[int]) -> Optional[TreeNode]:
            n = len(nums)
            #Base case
            if n == 0:
                return None
            if n == 1:
                return TreeNode(nums[0])
                
            left_nums, middle_num, right_nums = nums[:n//2], nums[n//2], nums[n//2 + 1:]
            root = TreeNode(middle_num)
            root.left = splitArray(left_nums)
            root.right = splitArray(right_nums)
            return root

        nums.sort()
        return splitArray(nums)