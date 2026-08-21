class Solution:
    def divide(self, dividend, divisor):
        # Overflow case
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1

            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            result += multiple

        if negative:
            result = -result

        return result