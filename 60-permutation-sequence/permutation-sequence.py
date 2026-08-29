
class Solution:
    def getPermutation(self, n, k):
        numbers = list(range(1, n + 1))
        result = []

        # Convert k to 0-based indexing
        k -= 1

        # factorial
        fact = 1
        for i in range(1, n):
            fact *= i

        for i in range(n, 0, -1):
            index = k // fact
            result.append(str(numbers[index]))
            numbers.pop(index)

            k %= fact

            if i > 1:
                fact //= (i - 1)

        return "".join(result)

