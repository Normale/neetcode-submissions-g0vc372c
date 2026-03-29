class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, value in enumerate(temperatures):
            
            while len(stack) > 0 and value > stack[-1][1]:
                top_id, top_val = stack.pop()
                diff = i - top_id
                result[top_id] = diff
            stack.append((i, value))
        return result