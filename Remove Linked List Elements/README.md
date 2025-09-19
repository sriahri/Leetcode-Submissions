## Problem: https://leetcode.com/problems/remove-linked-list-elements/description/
### 
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

### Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

### Example 2:
Input: head = [], val = 1
Output: []

### Example 3:
Input: head = [7,7,7,7], val = 7
Output: []

### Constraints:
The number of nodes in the list is in the range [0, $$10^4$$].
1 <= Node.val <= 50
0 <= val <= 50

# Solution
## Approach
The approach is to use change(shift) the pointer to the next if the node's value is the same as the given value.

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
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # while head is not None and head.val==val:
        #     head=head.next
        # temp=head
        # while temp is not None and temp.next is not None:
        #     if temp.next.val == val:
        #         temp.next=temp.next.next
        #     else:
        #         temp=temp.next
        # return head
        if head is None:
            return None
        head.next= self.removeElements(head.next,val);
        if head.val==val and head is not None:
            return head.next
        else:
            return head
```