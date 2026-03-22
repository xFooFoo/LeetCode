# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorderTraverse(root: Optional[TreeNode]):
            if not root:
                return
            postorderTraverse(root.left)
            postorderTraverse(root.right)
            result.append(root.val)


        result: List[int] = []
        postorderTraverse(root)
        return result
        