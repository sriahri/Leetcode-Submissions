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