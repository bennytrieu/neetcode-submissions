# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = head
        arr = []
        while dummy:
            arr.append(dummy.val)
            dummy = dummy.next
        
        left = 1
        right = len(arr) - 1

        if len(arr) == 1:
            return
        else:
            while right >= left:
                if right == left:
                    head.next = ListNode(arr[right])
                    head = head.next
                    right -= 1
                    left += 1
                else:
                    head.next = ListNode(arr[right])
                    head = head.next
                    right -= 1
                    head.next = ListNode(arr[left])
                    head = head.next
                    left += 1
        print(arr)