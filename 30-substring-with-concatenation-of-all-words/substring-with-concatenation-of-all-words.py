class Solution:
    def findSubstring(self, s, words):
        from collections import Counter

        word_len = len(words[0])
        word_count = len(words)
        required = Counter(words)

        ans = []

        for i in range(word_len):
            left = i
            right = i
            count = 0
            seen = {}

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word not in required:
                    seen.clear()
                    count = 0
                    left = right
                    continue

                seen[word] = seen.get(word, 0) + 1
                count += 1

                while seen[word] > required[word]:
                    left_word = s[left:left + word_len]
                    seen[left_word] -= 1
                    left += word_len
                    count -= 1

                if count == word_count:
                    ans.append(left)

        return ans