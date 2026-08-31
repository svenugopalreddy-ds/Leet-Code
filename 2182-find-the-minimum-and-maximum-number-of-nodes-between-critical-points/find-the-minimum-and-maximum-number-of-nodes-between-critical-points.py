class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first = -1          # position of first critical point
        prev_critical = -1 # position of previous critical point
        min_dist = float('inf')

        prev = head
        curr = head.next
        pos = 1

        while curr.next:
            # Check whether curr is a local maximum or minimum
            if ((curr.val > prev.val and curr.val > curr.next.val) or
                (curr.val < prev.val and curr.val < curr.next.val)):

                if first == -1:
                    # First critical point
                    first = pos
                else:
                    # Distance from previous critical point
                    min_dist = min(min_dist, pos - prev_critical)

                prev_critical = pos

            prev = curr
            curr = curr.next
            pos += 1

        # Fewer than 2 critical points
        if first == -1 or first == prev_critical:
            return [-1, -1]

        max_dist = prev_critical - first

        return [min_dist, max_dist]