import heapq

class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def _get_1st_of_max(self):
        return -self.max_heap[0] if self.max_heap else None
    def _get_1st_of_min(self):
        return self.min_heap[0] if self.min_heap else None

    def addNum(self, num: int) -> None:
        if self.max_heap and num <= self._get_1st_of_max():
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        needs_balancing = abs(
            len(self.max_heap) - len(self.min_heap)
        ) > 1
        if not needs_balancing:
            return

        if len(self.max_heap) < len(self.min_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
        else:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

    def findMedian(self) -> float:
        lower = self._get_1st_of_max()
        higher = self._get_1st_of_min()

        if len(self.max_heap) == len(self.min_heap):
            return (lower + higher) / 2
        elif len(self.max_heap) > len(self.min_heap):
            return self._get_1st_of_max()
        else:
            return self._get_1st_of_min()