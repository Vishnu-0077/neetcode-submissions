class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        d = 1
        num = 0
        
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            num += (v1 + v2) * d
            d *= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        num = str(num)[::-1]
        
        for digit in num:
            node.next = ListNode(int(digit))
            node = node.next
        
        return dummy.next
