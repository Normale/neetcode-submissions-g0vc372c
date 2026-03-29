from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        water = 0
        while left < right:
            if height[left] < height[right]:
                left += 1
                if max_left < height[left]:
                    max_left = height[left]
                else:
                    water += max_left - height[left]
            else:
                right -= 1
                if max_right < height[right]:
                    max_right = height[right]
                else:
                    water += max_right - height[right]
        return water