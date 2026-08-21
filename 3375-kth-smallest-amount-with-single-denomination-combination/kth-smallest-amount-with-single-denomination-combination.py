from math import gcd

class Solution:
    def findKthSmallest(self, coins, k):
        n = len(coins)

        # Precompute LCM for every subset
        subsets = []

        for mask in range(1, 1 << n):
            lcm = 1
            bits = 0

            for i in range(n):
                if mask & (1 << i):
                    bits += 1

                    g = gcd(lcm, coins[i])
                    lcm = lcm // g * coins[i]

            subsets.append((lcm, bits))

        def count(x):
            total = 0

            for lcm, bits in subsets:
                if lcm > x:
                    continue

                value = x // lcm

                if bits % 2 == 1:
                    total += value
                else:
                    total -= value

            return total

        low = 1
        high = min(coins) * k

        while low < high:
            mid = (low + high) // 2

            if count(mid) >= k:
                high = mid
            else:
                low = mid + 1

        return low
        