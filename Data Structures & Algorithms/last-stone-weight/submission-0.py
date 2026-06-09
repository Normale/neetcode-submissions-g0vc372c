class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        x = heapq.heapify(stones)

        while len(x) > 1:
            stone_one = heapq.heappop(x)
            stone_two = heapq.heappop(x)

            if stone_one == stone_two:
                continue
            else:
                heapq.heappush(x, max(stone_one, stone_two))
        return x[0] if x else 0 