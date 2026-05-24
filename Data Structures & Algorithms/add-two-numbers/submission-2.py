from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def findLength(l: Optional[ListNode]) -> int:
            c = 0
            while l:
                c += 1
                l = l.next
            return c

        def makeNumbers(l: Optional[ListNode], length: int) -> int:
            num = 0
            n = length
            while l:
                num = num + (l.val) * pow(10, length - n)
                n -= 1
                l = l.next
            return num  # <-- was missing

        totalSum = makeNumbers(l1, findLength(l1)) + makeNumbers(l2, findLength(l2))

        # Build the result linked list
        l3 = ptr = ListNode()
        ptr.next = ListNode(totalSum % 10)
        totalSum = totalSum // 10
        ptr = ptr.next

        while totalSum != 0:
            ptr.next = ListNode(totalSum % 10)
            ptr = ptr.next
            totalSum = totalSum // 10

        return l3.next
