"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        minimum = 0
        maximum = len(nums)
        while maximum > 1:
            mid = maximum - 1 //2
            if nums[mid] > target:
                maximum = mid
            elif nums[mid] <= target:
                minimum = mid

if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 2
    sol = Solution()
    result = sol.searchInsert(nums, target)
    print(result)

"""
O(n) solution
class Solution(object):
    def searchInsert(self, nums, target):
        for num in nums:
            if num >= target:
                result = nums.index(num)
                break
            else:
                result = len(nums)
        return result
"""

