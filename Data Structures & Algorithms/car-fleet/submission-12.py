class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_sorted = sorted(zip(position, speed), reverse=True) # O nlogn
        buff = []
        result = 0
        for pos, speed in pos_sorted:
            time_remaining = (target - pos) / speed
            if not buff or time_remaining > buff[-1][0]:
                buff.append((time_remaining, pos, speed))

        return len(buff)