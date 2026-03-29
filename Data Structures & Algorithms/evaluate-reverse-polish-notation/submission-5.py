class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        operands = "+-*/"
        for t in tokens:
            if t in operands:
                second = s.pop()
                first = s.pop()
                result = int(eval(f"{first} {t} {second}"))
                print(f"{first} {t} {second} = {result}")
                s.append(result)
            else:
                s.append(t)
        return int(s[0])