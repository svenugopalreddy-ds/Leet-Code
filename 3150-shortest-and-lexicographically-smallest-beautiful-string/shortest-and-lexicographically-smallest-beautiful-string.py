class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = [i for i, ch in enumerate(s) if ch == '1']

        if len(ones) < k:
            return ""

        ans = ""

        for i in range(len(ones) - k + 1):
            left = ones[i]
            right = ones[i + k - 1]

            candidate = s[left:right + 1]

            if not ans:
                ans = candidate
            elif len(candidate) < len(ans):
                ans = candidate
            elif len(candidate) == len(ans) and candidate < ans:
                ans = candidate

        return ans