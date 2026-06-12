class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def _get_1st_of_max(self):
        return heapq.nsmallest(1, self.max_heap)
    def _get_1st_of_min(self):
        return heapq.nsmallest(1, self.min_heap)

    def addNum(self, num: int) -> None:
        if num > self._get_1st_of_max(): # wrong
            heapq.heappush(self.max_heap, num)
        else:
            heapq.heappush(self.min_heap, -num)
        
        needs_balancing = abs( 
            len(self.max_heap) - len(self.min_heap)
        ) > 1
        if not needs_balacing:
            return

        if len(self.max_heap) < len(self.min_heap):
            # remove max from min heap
            heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap)
        else:
            heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap)

    def findMedian(self) -> float:
        lower = self._get_1st_of_min()
        higher = self._get_1st_of_max()

        if len(self.max_heap) == len(self.min_heap):
            return (lower + higher) / 2
        elif len(self.max_heap) < len(self.min_heap):
            return self.__get_1st_of_min()
        else:
            return self._get_1st_of_max()


        