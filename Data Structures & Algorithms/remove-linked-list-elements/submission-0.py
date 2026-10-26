# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        current = head
        prev = None

        while current:
            nextNode = current.next
            if current.val == val:
                if current == head:
                    head = current.next
                else:
                    prev.next = nextNode
            current = current.next