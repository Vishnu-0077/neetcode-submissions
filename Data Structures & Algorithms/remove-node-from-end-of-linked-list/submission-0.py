# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n is None or n==0:
            return head

        a = head
        co = 0
        while a is not None:
            a = a.next
            co +=1
        c = co-n+1
        
        if c ==1:
            return head.next

        x = head
        y = head.next
        for i in range(1, c-1):
            x = x.next
            y = y.next
        x.next = y.next
        y.next = None

        return head

        