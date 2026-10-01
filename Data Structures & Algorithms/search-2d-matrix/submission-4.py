class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        l = 0
        r = m*n - 1

        if we got i:
            x = mod
            y = //
        '''
        l = 0

        x_base = len(matrix[0])
        y_base = len(matrix)

        r = x_base*y_base

        # Use edge case when there is 1 element
        while r > l:
            m = l + (r - l) // 2
            x = m % x_base
            y = m // x_base
            
            if matrix[y][x] > target:
                r = m
            elif matrix[y][x] < target:
                l = m + 1
            else:
                return True
        
        return False

            
        