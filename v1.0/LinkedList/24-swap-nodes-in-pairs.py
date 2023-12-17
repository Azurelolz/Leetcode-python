# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        current = dummy
        while(current.next and current.next.next):
            temp = current.next
            temp1 = current.next.next.next
            current.next = current.next.next
            temp.next = temp1
            current.next.next = temp
            current = current.next.next
        return dummy.next
            
"""
Just need a temp node for first node and a temp node for the rest of nodes.
"""