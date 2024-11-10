'''
437. Path Sum III

Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

 

Example 1:


Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
 

Constraints:

The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1                         # This ensures that when the PathSum - Target = 0, we add 1 too
        self.targetMet = 0

        def dfs(node: Optional[TreeNode], previousSum: int = 0):
            if not node:
                return

            currentSum = previousSum + node.val

            if freq[currentSum - targetSum]:
                self.targetMet += freq[currentSum - targetSum]
            freq[currentSum] += 1

            dfs(node.left, currentSum)
            dfs(node.right, currentSum)
            freq[currentSum] -= 1           # Delete path sum as we complete the paths

        dfs(root)
        return self.targetMet