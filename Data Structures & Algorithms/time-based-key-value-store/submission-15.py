class TimeMap:

    def __init__(self):
        self.data = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        t = (timestamp, value)
        if key in self.data:
            self.data[key].append(t)
        else:
            self.data[key] = [t,]       

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.data:
            return ""
        values = self.data[key]
        print(values)
        
        left, right = 0, len(values)-1
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1
        print(f"current value {left}")
        print(f"current values = {values=}")
        if right < 0:
            return ""
        # print(f"returning {values[mid]=}, second elemenet")
        return values[right][1]
        