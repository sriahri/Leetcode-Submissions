## Problem: https://leetcode.com/problems/count-complete-tree-nodes/description/
### 
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

### Example 1:
Input: root = [1,2,3,4,5,6]
Output: 6

### Example 2:
Input: root = []
Output: 0

### Example 3:
Input: root = [1]
Output: 1

### Constraints:
The number of nodes in the tree is in the range [0, 5 * $$10^4$$].
0 <= Node.val <= 5 * $$10^4$$
The tree is guaranteed to be complete.

# Solution
## Approach
The approach is to count the height of the left subtree and the right subtree first. If the heights are same, the number of the nodes is 2**height - 1. Use the recursion and check all the heights and nodes.

## Complexity
- Time complexity:
$$O(logn)$$

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
    def leftHeight(self, root):
        count = 0
        while root:
            count += 1
            root = root.left
        return count
    def rightHeight(self, root):
        count = 0
        while root:
            count += 1
            root = root.right
        return count
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lh = self.leftHeight(root)
        rh = self.rightHeight(root)

        if lh == rh:
            return 2**rh - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
```