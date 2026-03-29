class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        n = len(nums)
        for i in range(n):
            current = nums[i]
            diff = target - current
            if diff in d:
                return sorted([d[diff], i])
            d[current] = i