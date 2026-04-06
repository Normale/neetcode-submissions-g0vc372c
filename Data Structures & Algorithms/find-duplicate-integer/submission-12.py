class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            old_s = slow
            slow = nums[slow-1]
            fast = nums[nums[fast-1]]
            if slow == fast:
                return old_s

    