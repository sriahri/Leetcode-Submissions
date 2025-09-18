## Problem: https://leetcode.com/problems/balanced-binary-tree/description/
### 
Given a binary tree, determine if it is height-balanced.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

### Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

### Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

### Example 3:
Input: root = []
Output: true

### Constraints:
The number of nodes in the tree is in the range [0, 5000].
-$$10^4$$ <= Node.val <= $$10^4$$

# Solution
## Approach
The approach is to recursively check if the left height subtree and right height subtree difference is greater than 1 or not. If so, return False

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
    def height(self, root):
        if not root:
            return 0
        left_height = self.height(root.left)
        right_height = self.height(root.right)

        if left_height == -1 or right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return 1 + max(left_height, right_height)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return True if self.height(root) != -1 else False
```
