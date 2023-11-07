class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        for index in range(1, len(nums)):
            if nums[index] != nums[index - 1]:
                nums[count] = nums[index]
                count += 1
        return count
