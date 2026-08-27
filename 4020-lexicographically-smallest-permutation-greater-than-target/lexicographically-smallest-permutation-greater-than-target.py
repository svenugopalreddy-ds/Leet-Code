class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        prefix = []

        for i in range(len(target)):
            t = ord(target[i]) - ord('a')

            # Keep the prefix equal to target if possible.
            if cnt[t] > 0:
                cnt[t] -= 1
                prefix.append(t)
                continue

            # We cannot match target[i].
            # First, try making THIS position larger.
            for c in range(t + 1, 26):
                if cnt[c] > 0:
                    cnt[c] -= 1

                    result = ''.join(chr(x + ord('a')) for x in prefix)
                    result += chr(c + ord('a'))

                    # Put remaining characters in smallest order.
                    for x in range(26):
                        result += chr(x + ord('a')) * cnt[x]

                    return result

            # No larger character at i.
            # Backtrack to an earlier position.
            for j in range(i - 1, -1, -1):
                # Restore the character used at position j.
                cnt[prefix[j]] += 1

                tj = ord(target[j]) - ord('a')

                # Try to increase position j.
                for c in range(tj + 1, 26):
                    if cnt[c] > 0:
                        cnt[c] -= 1

                        result = ''.join(
                            chr(x + ord('a'))
                            for x in prefix[:j]
                        )

                        result += chr(c + ord('a'))

                        # Smallest possible suffix.
                        for x in range(26):
                            result += chr(x + ord('a')) * cnt[x]

                        return result

            return ""

        # target itself was possible.
        # Find the next greater permutation by backtracking.
        for j in range(len(target) - 1, -1, -1):
            cnt[prefix[j]] += 1

            tj = ord(target[j]) - ord('a')

            for c in range(tj + 1, 26):
                if cnt[c] > 0:
                    cnt[c] -= 1

                    result = ''.join(
                        chr(x + ord('a'))
                        for x in prefix[:j]
                    )

                    result += chr(c + ord('a'))

                    for x in range(26):
                        result += chr(x + ord('a')) * cnt[x]

                    return result

        return ""