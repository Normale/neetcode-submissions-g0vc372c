class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        c = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for number, freq in c.items():
            buckets[freq].append(number)
        result = []
        for freq in reversed(buckets):
            for n in freq:
                result.append(n)
                if len(result) == k:
                    return result