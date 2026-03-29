from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # todo: use deque
        # chat solved it so get back to it in a while    
        dq = deque()  # stores indices, decreasing by value
        result = []

        for i, num in enumerate(nums):
            # Remove elements outside the window
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # Maintain decreasing order — remove smaller elements from back
            while dq and nums[dq[-1]] <= num:
                dq.pop()

            dq.append(i)

            # Window is fully formed
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result