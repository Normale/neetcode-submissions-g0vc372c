class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current_set = set()
        def backtrack(i, path):
            result.append(path.copy())
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
        return backtrack(0, [])