# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def countlist(self,head):
        temp=head
        c=0
        while temp!=None:
            c+=1
            temp=temp.next
        return c
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        counta=self.countlist(headA)
        countb=self.countlist(headB)
        diff=counta-countb
        if diff>0:
            for i in range(diff):
                headA=headA.next
        else:
            for i in range(-1*diff):
                headB=headB.next
        while headA is not None and headB is not None:
            if headA==headB:
                return headA
            headA=headA.next
            headB=headB.next
        return None