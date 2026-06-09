class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        x = nums
        heapq.heapify(x)
        return x.nlargest(k, x)[0]