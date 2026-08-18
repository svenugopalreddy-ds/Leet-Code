class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversedHalf = 0

        while x > reversedHalf:
            digit = x % 10
            reversedHalf = reversedHalf * 10 + digit
            x //= 10

        return x == reversedHalf or x == reversedHalf // 10