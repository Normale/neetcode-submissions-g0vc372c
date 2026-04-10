class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        prev1 = prev2 = 0  # 1 and 2 steps back

        while True:
            prev2 = prev1
            prev1 = slow
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while slow2 != slow:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow

"""NOTES:



1
2 < - 
3.    ^ 
…
4.    ^
2 - - 



Meeting point:


Road + A
M - meeting point



SLOW: ROAD + A
FAST: 2 X SLOW = 2 ROAD + 2 A

When they meet
Fast - slow = road + a
We are looking for 


Fast extra distance (the distance over road + a) must be multiple of cycle length so Fast = ROAD + A + n*C


2ROAD + 2A = ROAD + A  + n*C
So: ROAD + A = n * C

We are looking for road, so ROAD = n*C - A

So when we are in meeting point, the SLOW needs to travel (C-A) distance to an entrance.
We can now move another SLOW2 pointer to the beginning and travel them simultaneously.
Slow will need C-A distance, and the SLOW2 pointer will need ROAD to reach entrance. They will meet exactly at the entrance (although SLOW pointer might go `n` times around the cycle)

"""