class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lower_h = 0
        upper_h = len(matrix) - 1
        lower_v = 0
        upper_v = len(matrix[0]) - 1
        while lower_h <= upper_h:
            mid_h = (lower_h + upper_h) // 2

            if matrix[mid_h][0] <= target <= matrix[mid_h][-1]:
                row = matrix[mid_h]
                while lower_v <= upper_v:
                    mid_v = (lower_v + upper_v) // 2
                    if row[mid_v] == target:
                        return True
                    elif row[mid_v] < target:
                        lower_v = mid_v + 1
                    else:
                        upper_v = mid_v - 1
                return False
            elif matrix[mid_h][0] > target:
                upper_h = mid_h - 1
            elif matrix[mid_h][-1] < target:
                lower_h = mid_h + 1
        return False