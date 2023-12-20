# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
            if(slow == fast):
                slow = head
                while(slow != fast):
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

"""
Fast-slow pointers solution
Assume the distance from head to the entrance is x
The distance from the entrance to the meet point is y
The distance from the meet point back to the entrance is z
slow pointer will go x + y distance
fast pointer will go x + y + n(y + z) distance, n is the count of cycles
We can know that: ( x + y ) * 2 = x + y + n(y + z)
And it equals to: x + y = n( y + z )
What exactly we want is the x, so it will be like x = ( n - 1 ) ( y + z ) + z

This means, 
starting from the head (which is x distance from the entrance) 
and the meeting point (which is z distance from the entrance in the cycle), 
both pointers will meet at the cycle entrance after traveling a distance of x.

In summary, 
when you start two pointers—one from the head of the list and another from the meeting point—both moving at the same speed, 
they will meet at the entrance of the cycle. 
This conclusion comes from the fact that the distance from the head to the cycle entrance (x) is the same 
as the distance needed to complete n-1 cycles plus the distance from the meeting point to the entrance (z).
"""