class MinStack:

    def __init__(self):
        self.s = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if len(self.min_stack) == 0 or self.min_stack[-1] >= val:
            self.min_stack.append(val)
        self.s.append(val)


    def pop(self) -> None:
        x = self.s.pop()        
        if self.min_stack[-1] == x:
            self.min_stack.pop()

    def top(self) -> int:
        if len(self.s) > 0:
            return self.s[-1]
        else:
            return None

    def getMin(self) -> int:
        return self.min_stack[-1]
