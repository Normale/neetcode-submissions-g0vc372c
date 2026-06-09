from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        x = []
        for p in points:
            x1, y1 = p
            distance = sqrt(x1^2 + y1^2)
            heapq.heappush(x1, (distance, p))
        
        return heapq.nlargest(k, x)