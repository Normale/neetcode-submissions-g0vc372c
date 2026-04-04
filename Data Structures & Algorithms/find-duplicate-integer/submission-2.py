class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, value in enumerate(nums):
            n = value - 1
            if nums[n] < 0:
                return n + 1
            # we flip the value in n-th index to negative
            nums[n] = -1 * nums[n]
