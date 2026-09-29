# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = head
        while a:
            temp = a
            front = a.next
            front.next = a
            a.next = None
            a = temp.next
        return a




        