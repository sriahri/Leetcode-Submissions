## Problem: https://leetcode.com/problems/merge-two-sorted-lists/description/
### You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

### Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

### Example 2:
Input: list1 = [], list2 = []
Output: []

### Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

### Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

# Solution

## Approach
One of the approaches is to recursively append the list1 or list2 nodes depending on their values.
The other approach is to use a loop to compare both the nodes value and append them to the resultant list and finally return the list after all the nodes are processed.

## Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(n)$$

## Code
```python3 []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val <=l2.val:
            temp=l1
            temp.next=self.mergeTwoLists(l1.next,l2)
        else:
            temp=l2
            temp.next=self.mergeTwoLists(l1,l2.next)
        return temp

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                temp = list1
                list1 = list1.next
            else:
                temp.next = list2
                temp = list2
                list2 = list2.next
        if list1:
            temp.next = list1
        else:
            temp.next = list2
        return dummy.next
```
