class Solution:
    def swap(self, nums, left, right):
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp

    def partition(self, nums, left, right):
        pivot_value = nums[right]
        partition_index = left
        for j in range(left, right):
            if nums[j] < pivot_value:
                self.swap(nums, partition_index, j)
                partition_index += 1
        self.swap(nums, partition_index, right)
        return partition_index

    def quickSort(self, nums, left, right):
        if left < right:
            pivot_index = (left + right) // 2
            self.swap(nums, pivot_index, right)
            partition_index = self.partition(nums, left, right)
            self.quickSort(nums, left, partition_index - 1)
            self.quickSort(nums, partition_index + 1, right)

    def sortedSquares(self, nums: List[int]) -> List[int]:
        for index in range(len(nums)):
            nums[index] = nums[index] ** 2
        self.quickSort(nums, 0, len(nums)-1)
        return nums
    