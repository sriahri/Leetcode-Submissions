## Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
### 
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

### Example 1:
Input: head = [1,1,2]
Output: [1,2]

### Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]

### Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.

# Solution
## Approach
The approach is to compare the next element and check if the next element is equal to the current element or not. If it is same, the next pointer is changed to its next element, else it stays the same.

## Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(1)$$

## Code
```python3 []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        temp=head
        if head is None:
            return 
        while temp.next is not None:
            if temp.val==temp.next.val:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return head
```
