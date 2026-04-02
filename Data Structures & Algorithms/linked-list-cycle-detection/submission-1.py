# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = qui = head
        while qui and qui.next:
            slow = slow.next
            qui = qui.next.next
            if slow == qui:
                return True
        return False