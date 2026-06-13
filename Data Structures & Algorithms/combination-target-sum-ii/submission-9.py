class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()

        def backtrack(start, remaining, combo):
            if remaining == 0:
                results.append(combo.copy())
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remaining:
                    break
                val = candidates[i]
                combo.append(val)
                backtrack(i+1, remaining-val, combo)
                combo.pop()
        backtrack(0, target, [])
        return results