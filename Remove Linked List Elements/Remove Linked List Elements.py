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