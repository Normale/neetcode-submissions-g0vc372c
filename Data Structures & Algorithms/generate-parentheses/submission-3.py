class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(remaining, path, no_closing):
            if remaining == 0 and no_closing == 0:
                result.append(''.join(path))
            
            for p in "()":
                
                if p == "(":
                    path.append(p)
                    backtrack(remaining - 1, path, no_closing + 1)
                    path.pop()
                if p == ")":
                    if no_closing <= 0:
                        continue
                    path.append(p)
                    backtrack(remaining, path, no_closing - 1)
                    path.pop()
        backtrack(n, [], 0)
        return result