## Problem: https://leetcode.com/problems/symmetric-tree/description/
### 
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
 
### Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

### Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false

### Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100

# Solution

## Approach
The approach is to run a recursive approach and check if both the left and right subtrees are same or not. This means that check both the values at that particular node and recursively check by traversing (left, right) and (right, left).

## Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(1)$$

## Code
```python3 []
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
```
