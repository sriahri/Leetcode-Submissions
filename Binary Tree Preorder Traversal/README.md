## Problem: https://leetcode.com/problems/binary-tree-preorder-traversal/description/
### 
Given the root of a binary tree, return the preorder traversal of its nodes' values.

### Example 1:
Input: root = [1,null,2,3]

Output: [1,2,3]

### Example 2:
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [1,2,4,5,6,7,3,8,9]

### Example 3:
Input: root = []

Output: []

### Example 4:
Input: root = [1]

Output: [1]

### Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

# Solution
## Approach
The approach is to perform the preorder traversal using recursion.

## Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(n)$$

## Code
```python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper(root, res)
        return res
    def helper(self, root, res):
        if root:
            res.append(root.val)
            self.helper(root.left, res)
            self.helper(root.right, res)
        
```
