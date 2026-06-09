class KthLargest:

        def __init__(self, k: int, nums: List[int]):
            self.heap = []
        
        def add(self, val: int) -> int:
            heapq.heappush(self.heap, val)

            if len(self.heap) > k:
                heapq.heappop(head)
            
            return heap[-1]
