class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1

        if len(nums) == 2:
            return min(nums)
        # [9,10,1,2,3,4,5,6,7,8]
        # [all] -> [9-2] -> [1-2] -> 1
        # 1. 9 - 3 - 8 - LEFT
        # 2. 9 - 10 - 2 - RIGHT
        # 3. 1 - 2 - LEFT
        # [5,6,7,8,9,10,1,2,3,4]
        # [all] -> [10-4] -> [10-2] -> [1-2] -> 1
        # 1. 5 - 9 - 4 - RIGHT
        # 2. 10 - 2 - 4 - LEFT
        # 3. 10 - 1 - 2 - RIGHT
        # 4. 1 - 2 - LEFT
        while left < right:
            if nums[left] < nums[right]:
                return nums[left]
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                print(f"currently at {nums[mid]}, moving to the right, because {nums[left]=} < {nums[mid]=}")
                left = mid + 1
            else:
                print(f"currently at {nums[mid]}, moving to the left because {nums[left]=} >= {nums[mid]=}")
                right = mid

        return nums[left]