class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixes = [1] * n
        suffixes = [1] * n
        results = [1] * n
        i = 1
        prefixes[0] = 1
        prefixes[1] = prefixes[0] * nums[0]
        # result[2] = result[1] * nums[1]
        # we got "prefix" product now we need suffix product
        # same approach but from the right and then multiply them?
        while i < n:
            prefixes[i] = prefixes[i-1] * nums[i-1]
            i += 1
        print(f"result so far{prefixes}")
        # nums=[1,2,4,6]
        # [1, 1, 2, 8]
        # 
        i -= 1
        while i > 0:
            i -= 1
            print(f"trying {i}")
            suffixes[i] = suffixes[i+1] * nums[i+1]
        for i in range(n):
            results[i] = prefixes[i] * suffixes[i]

        return results