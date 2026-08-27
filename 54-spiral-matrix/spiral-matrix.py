class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:

            # 1. Left -> Right
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1

            # 2. Top -> Bottom
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1

            # 3. Right -> Left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1

            # 4. Bottom -> Top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1

        return res