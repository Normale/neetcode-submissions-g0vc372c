from collections import Counter
class Solution:
    def is_window_valid(self, tmp_cnt: Counter) -> bool:
        for k,v in tmp_cnt.items():
            if self.target[k] < tmp_cnt[k]:
                return False

        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        self.target = Counter(s1)

        tmp_counter = Counter()
        left, right = 0, 0
        
        for right in range(len(s2)):
            right_val = s2[right]
            if right_val in tmp_counter:
                tmp_counter[right_val] += 1
            else:
                tmp_counter[right_val] = 1
            
            while not self.is_window_valid(tmp_counter):
                tmp_counter[s2[left]] -= 1
                left += 1

            if tmp_counter == self.target:
                return True
        return False
