class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        nums = nums.sort()
        result = []
        
        def backtrack(start, path):
            result.append(path.copy())

            for i in range(start, len(nums)):
                if nums[i] == nums[i-1]:
                    continue
                
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])
        return result