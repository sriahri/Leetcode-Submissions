# Definition for singly-linked list.
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
            
        