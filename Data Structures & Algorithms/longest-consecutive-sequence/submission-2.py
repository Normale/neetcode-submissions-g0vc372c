class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_so_far = set()
        for n in nums_set:
            if n-1 in nums_set:
                continue
            current = set()
            current.add(n)
            while True:
                if (n+1) in nums_set:
                    current.add(n+1)
                    n += 1
                else:
                    break
            if len(current) > len(longest_so_far):
                longest_so_far = current
        return len(longest_so_far)