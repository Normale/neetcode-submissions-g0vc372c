class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # is_pal[i][j] is True if s[i:j+1] is a palindrome
        is_pal = [[False] * len(s) for _ in range(len(s))]

        for length in range(1, len(s)):
            for i in range(0, len(s) - length + 1):
                j = i + length - 1
                if (s[i] == s[j-1] and is_pal[i+1][j-1]) or length == 1:
                    is_pal[i][j] = True

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