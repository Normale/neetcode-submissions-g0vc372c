class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2
        if len(A)>len(B):
            A,B = B,A
        
        l, r = 0, len(A) - 1
    
        while True:
            mid_A = (l+r) // 2
            mid_B = half - mid_A - 2 
            print(f"{mid_A=}{mid_B=}")
            Aleft = A[mid_A] if mid_A >= 0 else float('-inf')
            Aright = A[mid_A+1] if mid_A + 1 <= len(A) - 1 else float('inf')
            Bleft = B[mid_B] if mid_B >= 0 else float('-inf')
            Bright = B[mid_B+1] if mid_B + 1 <= len(B) - 1 else float('inf')
            print(f"{Aleft=}{Aright=}{Bleft=}{Bright=}")
            # is it valid?
            if Aleft <= Bright and Aright >= Bleft:
                if total % 2 == 0:
                    median = (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    median = min(Aright, Bright)
                return median
            elif Bleft > Aright:
                l = mid_A + 1
            else: # Aleft > Bright
                r = mid_A - 1