class Solution:
    def expand(self, state, letter):
        if letter in state.keys():
            state[letter] += 1
        else:
            state[letter] = 1
    
    def shrink(self, state, letter):
        state[letter] -= 1
        if state[letter] == 0:
            del state[letter]

    def is_window_valid(self, state):
        for k,v in state.items():
            if v > 1: 
                return False
        return True

    def better(self, a, b):
        return b if b>a else a

    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        self.state = dict()
        best = 0

        for right in range(len(s)):
            self.expand(self.state, s[right])
            while not self.is_window_valid(self.state):
                self.shrink(self.state, s[left])
                left += 1

            best = self.better(best, right - left + 1)

        return best