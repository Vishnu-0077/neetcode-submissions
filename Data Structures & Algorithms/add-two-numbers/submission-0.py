# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        d = 1
        num = 0
        while l1 or l2:
            num+=(l1.val+l2.val)*d
            d*=10
            l1=l1.next
            l2=l2.next
        num = str(num)
        num = num[::-1]
        for i in range(len(num)):
            node.next = ListNode(int(num[i]))
            node = node.next
        return dummy.next


        