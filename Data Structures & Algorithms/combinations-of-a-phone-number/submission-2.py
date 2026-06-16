class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mappings = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        results = []
        path = []
        def dfs(i):
            if i == len(digits):
                results.append(''.join(path))
                return
            digit = digits[i]
            for letter in mappings[digit]:
                path.append(letter)
                dfs(i+1)
                path.pop()
        dfs(0)

        return results