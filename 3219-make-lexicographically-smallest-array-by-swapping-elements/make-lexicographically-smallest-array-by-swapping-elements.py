
class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        # (value, original_index)
        pairs = [(nums[i], i) for i in range(n)]

        # Sort by value
        pairs.sort()

        start = 0

        while start < n:
            end = start

            # Find the connected group
            while (
                end + 1 < n
                and pairs[end + 1][0] - pairs[end][0] <= limit
            ):
                end += 1

            # Get original indices in this group
            indices = [pairs[i][1] for i in range(start, end + 1)]

            # Smallest values should go to smallest indices
            indices.sort()

            for i, index in enumerate(indices):
                nums[index] = pairs[start + i][0]

            start = end + 1

        return nums
