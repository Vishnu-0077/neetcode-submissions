# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        rev = head
        ans = ListNode()
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        rev = slow.next
        slow.next = None
        prev = None
        while rev is not None:
            temp = rev.next
            rev.next = prev
            prev = rev
            rev = temp
        
        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
        
        return 

            
        

        


        