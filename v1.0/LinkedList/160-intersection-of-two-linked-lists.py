# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a_size = 0
        b_size = 0
        cur_a = headA
        cur_b = headB
        while(cur_a):
            cur_a = cur_a.next
            a_size += 1

        while(cur_b):
            cur_b = cur_b.next
            b_size += 1
        cur_a = headA
        cur_b = headB
        if a_size > b_size:
            cur_a, cur_b = cur_b, cur_a
            a_size, b_size = b_size, a_size
        
        for i in range(b_size - a_size):
            cur_b = cur_b.next
        
        while(cur_a and cur_b):
            if cur_a == cur_b:
                return cur_a
            else:
                cur_a = cur_a.next
                cur_b = cur_b.next
        return None

"""
Find the length of the two linked lists and then align their head
The point is to make linked list B the longest
Than check if they are the same, if not than both list = list.next
"""