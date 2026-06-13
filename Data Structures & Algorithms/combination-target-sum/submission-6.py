class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = set()
        def backtrack(combo):
            if sum(combo) > target:
                return
            if sum(combo) == target:
                results.add(tuple(combo))
            for n in nums:
                if n == 0:
                    continue
                combo.append(n)
                backtrack(combo)
                combo.pop()
        backtrack([])
        return [list(x) for x in results]