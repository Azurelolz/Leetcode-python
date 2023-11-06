"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
 
Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        node = ListNode()
        new_list = list1 + list2
        index = 0
        while index < len(new_list)-1:
            node.val = new_list[index]
            node.next = new_list[index+1]
            if node.val > node.next:
                new_list[index], new_list[index+1] = node.next, node.val
                index = index -1
            else:
                index += 1
            
        return new_list

if __name__ == "__main__":
    list1 = [1,2,4]
    list2 = [1,3,4]
    sol = Solution()
    result = sol.mergeTwoLists(list1, list2)
    print(result)


"""
cheating solution
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        new_list = list1 + list2
        return sorted(new_list)
"""
