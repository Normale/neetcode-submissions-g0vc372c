class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = set()
        len_nums = len(candidates)
        def backtrack(combo, start):
            current_sum = sum(combo)
            if current_sum == target:
                results.add(tuple(sorted(combo)))
            if current_sum > target:
                return
            
            for i in range(start, len_nums):
                combo.append(candidates[i])
                backtrack(combo, i + 1)
                combo.pop()
        backtrack([], 0)
        return [list(x) for x in results]