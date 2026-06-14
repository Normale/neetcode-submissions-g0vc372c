class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(remaining, path, no_closing):
            if remaining == 0:
                result.append(path.copy())
            
            for p in "()":
                if remaining == 0 and no_closing == 0:
                    path.append(p)
                    return
                if p == "(":
                    no_closing += 1
                    remaining -= 1
                if p == ")":
                    if no_closing <= 0:
                        continue
                    no_closing -= 1
                backtrack(remaining, path, no_closing)
                path.pop()
        backtrack(n, [], 0)
        return results