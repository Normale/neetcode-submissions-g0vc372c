class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        if len(stones) == 1:
            return stones[0]
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone_one = heapq.heappop(stones)
            stone_two = heapq.heappop(stones)

            if stone_one == stone_two:
                continue
            else:
                heapq.heappush(stones, -abs(stone_one - stone_two))
                print("pushing", -abs(stone_one - stone_two), stone_one, stone_two)
                print(stones)
        return stones[0] if stones else 0 