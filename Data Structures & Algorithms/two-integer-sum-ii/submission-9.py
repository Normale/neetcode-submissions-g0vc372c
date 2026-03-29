class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, 1
        n = len(numbers)
        while True:
            if (right >= n and left < n-1) or numbers[left] + numbers[right] > target :
                left += 1
                right = left + 1
                continue
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            right += 1