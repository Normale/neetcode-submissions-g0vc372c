class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = set()
        len_nums = len(candidates)
        def backtrack(combo, start):
            if sum(combo) == target:
                results.append(sorted(combo))

            for i in range(start, len_nums):
                combo.append(candidates[i])
                backtrack(combo, i + 1)
                combo.pop()
            
        return list(results)