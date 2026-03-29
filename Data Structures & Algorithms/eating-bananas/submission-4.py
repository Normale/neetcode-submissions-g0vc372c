class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_bananas = max(piles)
        
        def get_time_for_given_speed(k: int):
            # k = current eating speed
            print("checking", k)
            result = 0
            for p in piles:
                result += (p+k-1) // k # ceil(p/i)
            return result
        # n = 10
        # h = 3
        # k = 1  2 3 4 5 9 10 20 30
        # t = 10 5 3 3 2 2 1  1  1
        upper = max_bananas
        lower = 1
        while lower <= upper:
            mid = (lower + upper) // 2

            current = get_time_for_given_speed(mid)
            if current <= h:
                best = mid
                upper = mid - 1
            else:
                lower = mid + 1
        return best



