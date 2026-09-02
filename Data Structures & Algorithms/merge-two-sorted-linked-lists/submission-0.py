# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        ans = ListNode()

        curr1 = list1
        curr2 = list2
        currlist = ans

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                currlist.next = curr1
                curr1 = curr1.next
            else:
                currlist.next = curr2
                curr2 = curr2.next
            currlist = currlist.next
        
        if curr1 != None:
            currlist.next = curr1
        else:
            currlist.next = curr2

        return ans.next