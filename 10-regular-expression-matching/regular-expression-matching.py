class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            # Pattern is completely consumed
            if j == len(p):
                return i == len(s)

            # Does current pattern character match current string character?
            first_match = (
                i < len(s) and
                (p[j] == s[i] or p[j] == '.')
            )

            # Next pattern character is '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                # Option 1: '*' matches zero characters
                # Option 2: '*' matches one+ characters
                result = (
                    dfs(i, j + 2) or
                    (first_match and dfs(i + 1, j))
                )
            else:
                # Normal character / '.'
                result = first_match and dfs(i + 1, j + 1)

            memo[(i, j)] = result
            return result

        return dfs(0, 0)