
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0

        while i < len(words):
            # Find how many words fit in this line
            j = i
            line_length = 0

            while j < len(words):
                # Words need one space between them
                needed = line_length + len(words[j])

                if j > i:
                    needed += 1

                if needed > maxWidth:
                    break

                line_length = needed
                j += 1

            # Words from i to j-1 belong to this line
            line_words = words[i:j]
            total_word_length = sum(len(word) for word in line_words)
            gaps = len(line_words) - 1

            # Last line OR line has only one word
            if j == len(words) or gaps == 0:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
                result.append(line)

            else:
                # Fully justify
                total_spaces = maxWidth - total_word_length

                # Minimum spaces for every gap
                spaces = total_spaces // gaps

                # Extra spaces go to the left gaps
                extra = total_spaces % gaps

                line = ""

                for k in range(gaps):
                    line += line_words[k]
                    line += " " * (spaces + (1 if k < extra else 0))

                line += line_words[-1]

                result.append(line)

            i = j

        return result

