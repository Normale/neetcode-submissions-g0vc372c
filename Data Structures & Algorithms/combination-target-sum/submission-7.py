class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        def backtrack(combo, start):
            total = sum(combo)
            if total == target:
                results.append(combo.copy())
                return
            if total > target:
                return
            for i in range(start, len(nums)):
                combo.append(nums[i])
                backtrack(combo, i)
                combo.pop()
        backtrack([], 0)
        return results