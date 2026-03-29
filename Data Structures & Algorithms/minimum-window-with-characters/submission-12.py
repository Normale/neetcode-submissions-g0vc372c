from collections import Counter
class Solution:
    def has_it_all(self, tmp_cnt: Counter):
        for k, v in self.target.items():
            # y: 1 x:1 a:1 z:1 
            # self.target[y]=1, [x]=1, [z]=1, [a]=0
            if self.target[k] > tmp_cnt.get(k, 0):
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        self.target = Counter(t)
        if len(t) == 0 or len(s) == 0 or len(t) > len(s):
            return ""
        tmp_counter = Counter()
        best_so_far = ""
        left = 0
        for right in range(len(s)):
            right_val = s[right]
            if right_val in tmp_counter:
                tmp_counter[right_val] += 1
            else:
                tmp_counter[right_val] = 1
            # shrink from left - if the string already suffices, try to make it shorter 

            while self.has_it_all(tmp_counter):
                if (right - left) < len(best_so_far) or not best_so_far:
                    best_so_far = s[left:right+1]
        
                tmp_counter[s[left]] -= 1
                if tmp_counter[s[left]] == 0:
                    del tmp_counter[s[left]]
                left += 1

        return best_so_far





# from collections import Counter

# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         if not s or not t or len(t) > len(s):
#             return ""

#         target = Counter(t)
#         window = Counter()

#         required = len(target)      # number of unique chars required
#         formed = 0                  # how many are currently satisfied

#         left = 0
#         best_len = float("inf")
#         best_start = 0

#         for right in range(len(s)):
#             char = s[right]
#             window[char] += 1

#             if char in target and window[char] == target[char]:
#                 formed += 1

#             while formed == required:
#                 window_len = right - left + 1
#                 if window_len < best_len:
#                     best_len = window_len
#                     best_start = left

#                 left_char = s[left]
#                 window[left_char] -= 1
#                 if left_char in target and window[left_char] < target[left_char]:
#                     formed -= 1

#                 left += 1

#         if best_len == float("inf"):
#             return ""

#         return s[best_start:best_start + best_len]