# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous_node = None
        
        while(current):
            temp_node = current.next
            current.next = previous_node
            previous_node = current
            current = temp_node
        return previous_node
        
"""
Remember to return the "previous node" not the current.
Don't need the dummy head in this program.
"""