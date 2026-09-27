# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        a = head

        c = 0
        while a is not None:
            a = a.next
            c+=1
        
        if c==1:
            head = None
            return head
        r = c-n+1
        if r==1:
            return head.next

        first = head
        while first is not None and first.next is not None and r!=1:
            prev = first
            first = first.next
            r-=1
        prev.next = first.next
        first.next = None

        return head


        


        