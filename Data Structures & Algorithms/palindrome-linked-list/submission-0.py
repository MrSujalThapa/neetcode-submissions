class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 1. Find the beginning of the second half
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the second half
        previous = None
        current = slow

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        # 3. Compare both halves
        left = head
        right = previous

        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True