# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = head
        current = head
        count = 0
        while current:
            for i in range(count):
                if current.next == dummy:
                    return True
                dummy = dummy.next
            dummy = head
            current = current.next
            count += 1
        return False

"""
Kind of brute force solution, not the best, see cycle 2 practice
"""