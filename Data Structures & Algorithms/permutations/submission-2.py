from itertools import cycle
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        target_len = len(nums)
        def backtrack(start, path):
            if len(path) == target_len:
                results.append(path.copy())
            
            for k in range(target_len):
                i = (start + k) % target_len
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        backtrack(0, [])
        return results