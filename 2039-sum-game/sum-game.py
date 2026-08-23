class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        diff = 0
        q_left = 0
        q_right = 0

        for i in range(half):
            if num[i] == '?':
                q_left += 1
            else:
                diff += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                q_right += 1
            else:
                diff -= int(num[i])

        # If the number of ? is odd, Alice wins.
        if (q_left + q_right) % 2 == 1:
            return True

        # Bob wins only if the existing difference can be
        # exactly balanced by the remaining '?' positions.
        return diff * 2 != (q_right - q_left) * 9