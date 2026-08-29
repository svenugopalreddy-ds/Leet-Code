
class Solution:
    def rotateRight(self, head, k):
        if head is None or head.next is None or k == 0:
            return head

        # Find length and tail
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Reduce unnecessary rotations
        k = k % length

        if k == 0:
            return head

        # Make the list circular
        tail.next = head

        # Find the new tail
        steps = length - k - 1
        new_tail = head

        for _ in range(steps):
            new_tail = new_tail.next

        # The node after new_tail becomes the new head
        new_head = new_tail.next

        # Break the circle
        new_tail.next = None

        return new_head

