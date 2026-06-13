from itertools import cycle
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        target_len = len(nums)
        def backtrack(path,used):
            if len(path) == target_len:
                results.append(path.copy())
            
            for i in range(target_len):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
                used[i] = False
        backtrack([], [False] * target_len)
        return results