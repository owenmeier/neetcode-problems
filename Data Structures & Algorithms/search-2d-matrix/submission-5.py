class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        

        while top <= bottom:
            middle = top + (bottom - top) // 2
            if matrix[middle][0] <= target <= matrix[middle][-1]:
                break
            elif matrix[middle][0] > target:
                bottom = middle - 1
            elif matrix[middle][0] < target:
                top = middle + 1
        # print(matrix[middle])
        left = 0
        right = len(matrix[middle]) - 1

        while left <= right:
            center = left + (right - left) // 2
            # print(center)
            if matrix[middle][center] == target:
                return True
            elif matrix[middle][center] > target:
                right = center - 1
            elif matrix[middle][center] < target:
                left = center + 1
        
        return False
        # print(matrix[middle])