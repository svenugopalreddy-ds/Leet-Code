
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the last digit
        for i in range(len(digits) - 1, -1, -1):

            if digits[i] < 9:
                digits[i] += 1
                return digits

            # 9 + 1 = 10
            digits[i] = 0

        # If we reach here, every digit was 9
        return [1] + digits

   