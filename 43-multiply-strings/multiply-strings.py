class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        n = len(num1)
        m = len(num2)

        res = [0] * (n + m)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])

                p1 = i + j
                p2 = i + j + 1

                total = mul + res[p2]

                res[p2] = total % 10
                res[p1] += total // 10

        # Remove leading zeros
        result = ''.join(map(str, res)).lstrip('0')

        return result