class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0

        cols = set()
        diag1 = set()  # row - col
        diag2 = set()  # row + col

        def backtrack(row):
            nonlocal count

            # Successfully placed queens in all rows
            if row == n:
                count += 1
                return

            for col in range(n):

                # Same column
                if col in cols:
                    continue

                # Same diagonal
                if row - col in diag1:
                    continue

                # Same diagonal
                if row + col in diag2:
                    continue

                # Choose
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # Explore
                backtrack(row + 1)

                # Undo
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)

        return count