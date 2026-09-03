
class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        mn = min(nums1)

        # If the minimum is odd, it can turn every even
        # number into an odd number.
        if mn % 2 == 1:
            return True

        # Minimum is even. If there is any odd number,
        # the smallest odd number cannot be turned even.
        for x in nums1:
            if x % 2 == 1:
                return False

        return True


