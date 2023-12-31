from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode()
        temp = 0

        l1_val = l1.val
        l1 = l1.next
        result_tail = result
        result_tail.next = ListNode(1)

        return output.next

l1 = [2,4,3]
l2 = [5,6,4]

r = Solution()
result = r.mergeTwoLists(l1, l2)

print(result)

"""
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [0], l2 = [0]
Output: [0]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""