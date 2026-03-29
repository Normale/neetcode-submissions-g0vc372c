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