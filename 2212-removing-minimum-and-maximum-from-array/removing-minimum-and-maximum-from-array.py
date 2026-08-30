class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)

        min_index = 0
        max_index = 0

        for i in range(1, n):
            if nums[i] < nums[min_index]:
                min_index = i

            if nums[i] > nums[max_index]:
                max_index = i

        a = min(min_index, max_index)
        b = max(min_index, max_index)

        # Remove both from the front
        front = b + 1

        # Remove both from the back
        back = n - a

        # Remove one from front and one from back
        both = (a + 1) + (n - b)

        return min(front, back, both)