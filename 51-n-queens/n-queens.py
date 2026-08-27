class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []

        board = [["."] * n for _ in range(n)]

        cols = set()
        diag1 = set()  # row - col
        diag2 = set()  # row + col

        def backtrack(row):
            # All rows have a queen
            if row == n:
                result.append(["".join(r) for r in board])
                return

            for col in range(n):
                # Check whether this position is attacked
                if col in cols:
                    continue

                if row - col in diag1:
                    continue

                if row + col in diag2:
                    continue

                # Place queen
                board[row][col] = "Q"
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # Move to next row
                backtrack(row + 1)

                # Remove queen (backtrack)
                board[row][col] = "."
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return result