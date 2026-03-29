class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        from collections import Counter
        c = Counter(nums)
        n = len(c)
        result = list()
        for k, count_of_k in c.items():
            for k2, count_of_k2 in c.items():
                if k > k2: 
                    continue
                target = -(k + k2)
                
                if target < k2:
                    continue
                if target not in c:
                    continue

                if k == k2 == target:
                    if c[k] >= 3:
                        result.append([k,k2,target])
                elif k == k2:
                    if c[k] >= 2:
                        result.append([k,k2, target])
                elif k2 == target:
                    if c[k2] >= 2:
                        result.append([k,k2, target])
                else:
                    result.append([k,k2,target])

        return result