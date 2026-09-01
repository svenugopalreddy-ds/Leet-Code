
from collections import deque
from typing import List


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        # Number each litter cell from 0 to k-1.
        litter_id = {}
        start = None
        k = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter_id[(r, c)] = k
                    k += 1

        # All litter already collected.
        target = (1 << k) - 1

        # (row, col, remaining_energy, collected_mask)
        q = deque()
        q.append((start[0], start[1], energy, 0))

        # We only need to remember the maximum energy seen
        # for each (position, mask).
        #
        # If we reach the same position with the same mask
        # but MORE energy, that state dominates the one with
        # less energy.
        best = {(start[0], start[1], 0): energy}

        moves = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            for _ in range(len(q)):
                r, c, e, mask = q.popleft()

                if mask == target:
                    return moves

                # If no energy remains, we cannot move.
                if e == 0:
                    continue

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    ne = e - 1
                    nmask = mask

                    # Collect litter.
                    if (nr, nc) in litter_id:
                        nmask |= 1 << litter_id[(nr, nc)]

                    # Reset energy on R.
                    if classroom[nr][nc] == 'R':
                        ne = energy

                    key = (nr, nc, nmask)

                    # This state is useful only if we have more
                    # energy than any previous visit to the same
                    # position with the same collected litter.
                    if ne > best.get(key, -1):
                        best[key] = ne
                        q.append((nr, nc, ne, nmask))

            moves += 1

        return -1

