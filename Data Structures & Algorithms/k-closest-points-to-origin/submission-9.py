from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points:
            return None
        x = []
        for p in points:
            x1, y1 = p
            distance = sqrt(x1**2 + y1**2)
            heapq.heappush(x, (distance, p))
        
        return [i[0] for i in heapq.nlargest(k, x)]