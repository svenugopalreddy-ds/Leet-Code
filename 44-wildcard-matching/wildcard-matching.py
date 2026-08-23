class Solution:
    def isMatch(self, s, p):
        n = len(s)
        m = len(p)

        dp = [[False] * (m + 1) for _ in range(n + 1)]

        # Empty string matches empty pattern
        dp[0][0] = True

        # Empty string can only be matched by '*' characters
        for j in range(1, m + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
            else:
                break

        for i in range(1, n + 1):
            for j in range(1, m + 1):

                if p[j - 1] == '*':

                    # '*' matches empty OR one/more characters
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

                elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:

                    # Current characters match
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[n][m]