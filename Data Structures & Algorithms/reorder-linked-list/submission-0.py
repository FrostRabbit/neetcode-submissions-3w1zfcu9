# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n1,n2=head,head.next
        while n2 and n2.next:
            n1 = n1.next
            n2 = n2.next.next
        
        N1 = head
        N2 = n1.next
        n1.next = None
        pre = None
        while N2:
            temp = N2.next
            N2.next = pre
            pre = N2
            N2 = temp
        
        N2 = pre

        while N2:
            temp1,temp2 = N1.next,N2.next
            N1.next = N2
            N2.next = temp1
            N1 = temp1
            N2 = temp2
