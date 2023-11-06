"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
 
Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = 0
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                if current_sum >= max_num:
                    max_num = current_sum
        return max_num

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    # nums = [5,4,-1,7,8]
    # nums = [1]
    sol = Solution()
    result = sol.maxSubArray(nums)
    print(result)


"""
Time complexity O(nlogn) ,Not good enough


# Solution with array numbers

class Solution(object):
    def maxSubArray(self, nums):
        max_num = 0
        target_array = []
        for i in range(len(nums)):
            current_sum = 0
            current_array = []
            for j in range(i, len(nums)):
                current_sum += nums[j]
                current_array.append(nums[j])
                if current_sum >= max_num:
                    max_num = current_sum
                    target_array = current_array
                    print(max_num)
                    print(target_array)
        return max_num

# Better solution with time complexity O(N)

class Solution:
    def maxSubArray(self, nums):
        pre, suf = [*nums], [*nums]
        for i in range(1, len(nums)): pre[i] += max(0, pre[i-1])          
        for i in range(len(nums)-2,-1,-1): suf[i] += max(0, suf[i+1])
        def maxSubArray(A, L, R):
            if L == R: return A[L]
            mid = (L + R) // 2
            return max(maxSubArray(A, L, mid), maxSubArray(A, mid+1, R), pre[mid] + suf[mid+1])
        return maxSubArray(nums, 0, len(nums)-1)

"""