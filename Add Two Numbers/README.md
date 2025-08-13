## Problem: https://leetcode.com/problems/add-two-numbers/description/
### You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 

### Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

### Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

### Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

### Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

# Solution
## Intuition
Convert the given linked lists into integers and add them. Again, convert the resultant sum into a linked list.


## Approach
First, convert the linked list L1 into an integer and then convert the linked list L2 to an integer. Now add both the numbers, now using the modulo and the division operator to convert the result sum back to a linked list and return the head of the linked list.

## Complexity
- Time complexity:
$$O(max(m, n) + 1)$$ Where m is the length of list L1 and n is the length of list L2.

- Space complexity:
$$O(max(m, n) + 1)$$ Where m is the length of list L1 and n is the length of list L2.

## Code
```python3 []# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_value, l2_value, count = 0, 0, 0
        while l1 is not None:
            l1_value += l1.val * (10**count)
            count += 1
            l1 = l1.next
        count = 0
        while l2 is not None:
            l2_value += l2.val * (10**count)
            count += 1
            l2 = l2.next
        result = l1_value + l2_value
        # print(l1_value, l2_value, result)
        # result_list = ListNode(result%10)
        # result = result//10
        # while result != 0:
        #     while result_list.next:
        #         result_list = result_list.next
        #     result_list.next = ListNode(result%10)
        #     result = result // 10
        # return result_list

        val = 0
        next = None
        result_list = ListNode(result%10)
        head = result_list
        result = result//10
        while result != 0:
            val = result%10
            head.next = ListNode(val)
            head = head.next
            result = result//10
        return result_list
```