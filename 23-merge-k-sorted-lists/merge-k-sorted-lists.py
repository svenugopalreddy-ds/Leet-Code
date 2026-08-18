import heapq

class Solution:
    def mergeKLists(self, lists):
        heap = []

        # Put the first node of every non-empty list into the heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        current = dummy

        while heap:
            val, i, node = heapq.heappop(heap)

            # Add smallest node to result
            current.next = node
            current = current.next

            # Add next node from the same list
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next