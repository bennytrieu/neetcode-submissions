# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        curr1 = head
        curr2 = head
        count = 0
        
        while curr1:
            count += 1
            curr1 = curr1.next
        
        if count == 1:
            head = None
            return head
        
        for i in range(count - n):
            prev = curr2
            curr2 = curr2.next
        
        if count - n == 0:
            return head.next
        else:
            prev.next = curr2.next
            return head