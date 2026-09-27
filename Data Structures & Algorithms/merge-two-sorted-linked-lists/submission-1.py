# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = ListNode()
        a = list1
        b = list2
        c = ans

        while a is not None and b is not None:
            if a.val>=b.val:
                c.next = b
                c = c.next
                b = b.next
            else:
                c.next = a
                c=c.next
                a = a.next
        
        while a is not None:
            c.next = a
            c = c.next
            a = a.next
        while b is not None:
            c.next = b
            c = c.next
            b = b.next
        
        return ans.next


        

            
        