class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        prev1 = prev2 = 0  # 1 and 2 steps back

        while True:
            prev2 = prev1
            prev1 = slow
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                return nums[prev2]  # value 2 steps back