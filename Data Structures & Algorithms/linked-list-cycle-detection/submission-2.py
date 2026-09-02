# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False

        curr = head
        fast = head.next

        while curr:
            if curr == fast:
                return True
            if fast == None:
                return False
            if curr.next == None or fast.next == None:
                return False
            curr = curr.next
            fast = fast.next.next
        
        return False

