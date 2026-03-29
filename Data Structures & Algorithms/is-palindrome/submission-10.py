class Solution: 
    def isPalindrome(self, s: str) -> bool:
        first, second = 0, len(s)-1
        while first < second:
            while first < second and not s[first].isalnum():
                first += 1
            while first < second and not s[second].isalnum():
                second -= 1
            if s[first].lower() != s[second].lower():
                return False
            else:
                first += 1
                second -= 1
        return True