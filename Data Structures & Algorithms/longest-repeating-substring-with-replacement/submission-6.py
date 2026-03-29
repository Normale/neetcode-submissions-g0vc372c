class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_counts = dict()
        # todo handle aaabbbbbaaa, k=0

        left, right = 0, 0
        max_so_far = 0
        for right in range(len(s)):
            if s[right] in window_counts.keys():
                window_counts[s[right]] += 1
            else:
                window_counts[s[right]] = 1
            window_length = right - left + 1
            if window_length - max(window_counts.values()) > k:
                window_counts[s[left]] -= 1
                if window_counts[s[left]] == 0:
                    del window_counts[s[left]]
                left += 1
            else:
                if max_so_far < window_length:
                    max_so_far = window_length
        return max_so_far