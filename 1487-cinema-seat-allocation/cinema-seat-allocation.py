from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(
        self, n: int, reservedSeats: List[List[int]]
    ) -> int:

        rows = defaultdict(set)

        for row, seat in reservedSeats:
            rows[row].add(seat)

        # Every completely empty row can fit 2 groups.
        answer = 2 * (n - len(rows))

        for reserved in rows.values():
            left = all(seat not in reserved for seat in range(2, 6))
            middle = all(seat not in reserved for seat in range(4, 8))
            right = all(seat not in reserved for seat in range(6, 10))

            if left and right:
                # 2-5 and 6-9
                answer += 2
            elif left or middle or right:
                # At least one block is available
                answer += 1

        return answer