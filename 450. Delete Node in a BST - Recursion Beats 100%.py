'''
450. Delete Node in a BST

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
 

Example 1:


Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
Example 3:

Input: root = [], key = 0
Output: []
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findSmallestNode(root: Optional[TreeNode]) -> Optional[TreeNode]:
            while root.left:
                root = root.left
            else:
                return root

        if not root:
            return

        if root.val == key:
            # Two Children Case
            if root.right and root.left:
                # Find the smallest leaf on the right branch to be the new root & then delete it
                smallestNode = findSmallestNode(root.right)
                root.val = smallestNode.val
                # Recursion to delete the smallest leaf node & reassign to the right
                root.right = self.deleteNode(root.right, smallestNode.val) # Always returns the root reference passed in
            # One Child Case
            elif root.left or root.right:
                # Set the only child as the new root
                root = root.left or root.right
            # No Children Case - we can just delete the current node
            else: 
                root = None
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root