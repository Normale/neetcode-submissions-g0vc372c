class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # is_pal[i][j] is True if s[i:j+1] is a palindrome
        is_pal = [[False] * len(s) for _ in range(len(s))]

        for length in range(1, len(s) + 1):
            for i in range(0, len(s) - length + 1):
                j = i + length
                if s[i] == s[j-1] and (length <= 2 or is_pal[i+1][j-2]):
                    is_pal[i][j-1] = True

        result = []
        partition = []
        def dfs(i):
            if i == len(s):
                result.append(partition.copy())
                return
            for j in range(i, len(s)):
                if is_pal[i][j]:
                    partition.append(s[i:j+1])
                    dfs(j+1)
                    partition.pop()
        dfs(0)
        return result