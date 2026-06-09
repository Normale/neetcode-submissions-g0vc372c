class KthLargest:

        def __init__(self, k: int, nums: List[int]):
            self.heap = []
            self.k = k
            for i in nums:
                self.add(i)
        def add(self, val: int) -> int:
            heapq.heappush(self.heap, val)

            if len(self.heap) > self.k:
                heapq.heappop(head)

            return self.heap[-1]
