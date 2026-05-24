class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # First pass: calculate length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # If we need to remove the head
        if n == length:
            return head.next

        # Second pass: go to node just before the one to remove
        curr = head
        for _ in range(length - n - 1):
            curr = curr.next

        # Remove the node
        curr.next = curr.next.next

        return head
