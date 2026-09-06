"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None

        diction = {}
        curr = head

        while curr:
            diction[curr] = Node(curr.val)
            curr = curr.next

        for real, copy in diction.items():
            if real.next:
                copy.next = diction[real.next]
            if real.random:
                copy.random = diction[real.random]
        return diction[head]