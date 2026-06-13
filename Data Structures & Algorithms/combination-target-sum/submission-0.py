class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = set()
        def backtrack(index, path):
            if sum(path) == target:
                results.add(path.copy())
            for i in range(len(nums)):
                path.append(nums[i])
                backtrack(index + 1, path)
                path.pop()
        backtrack(0, [])
        return results