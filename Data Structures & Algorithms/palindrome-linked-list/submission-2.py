class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 1. Find the beginning of the second half
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the second half
        current = slow
        previous = None 

        while current:
            nextNode = current.next
            current.next = previous
            previous = current 
            current = nextNode
        
        if head == previous:
            return True
        else:
            return False