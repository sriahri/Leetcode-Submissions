# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, nodeL, nodeR):
        if not nodeL or not nodeR:
            return nodeL==nodeR
        if nodeL.val != nodeR.val:
            return False
        if self.helper(nodeL.left, nodeR.right) and self.helper(nodeL.right, nodeR.left):
            return True
        return False
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.helper(root.left, root.right)