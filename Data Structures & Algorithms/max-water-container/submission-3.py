class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        best = 0
        while left < right:
            distance = right - left
            water = distance * min(heights[left], heights[right])
            if water > best:
                best = water
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return best