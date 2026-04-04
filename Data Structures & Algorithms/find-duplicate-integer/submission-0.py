class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if nums[n] < 0:
                return n
            # we flip the value in n-th index to negative
            nums[n] = -1 * nums[n]
        