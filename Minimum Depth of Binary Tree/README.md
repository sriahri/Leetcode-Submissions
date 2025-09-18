## Problem: https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
### 
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

### Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2

### Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

### Constraints:
The number of nodes in the tree is in the range [0, $$10^5$$].
-1000 <= Node.val <= 1000

# Solution
## Approach
The approach is to recursively check if the height of the left subtree is minimum or the right subtree is minimum. This is same as finding the height of the binary tree but here we use the min instead of the max if both nodes have children.

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
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left and root.right:
            return min(self.minDepth(root.left),self.minDepth(root.right))+1
        else:
            return max(self.minDepth(root.left),self.minDepth(root.right))+1
```
