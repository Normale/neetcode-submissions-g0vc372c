class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        x = []
        for p in points:
            x, y = p
            distance = sqrt(x^2 + y^2)
            heapq.heappush(x, (distance, p))
        
        return heapq.nlargest(k, x)