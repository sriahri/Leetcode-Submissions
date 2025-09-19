## Problem: https://leetcode.com/problems/reverse-linked-list/description/
### 
Given the head of a singly linked list, reverse the list, and return the reversed list.

### Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

### Example 2:
Input: head = [1,2]
Output: [2,1]

### Example 3:
Input: head = []
Output: []

### Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

# Solution
## Approach
The approach is to use change(shift) the pointer to the previous using recursion and also using the iteration.

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
    def fun(self,current,prev):
        if current is None:
            return prev
        temp=current.next
        current.next=prev
        return self.fun(temp,current)
    def reverseList(self, head: ListNode) -> ListNode:
        # prev=None
        # current=head
        # while current is not None:
        #     temp=current.next
        #     current.next=prev
        #     prev=current
        #     current=temp
        # return prev
        return self.fun(head,None)
```