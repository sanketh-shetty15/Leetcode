# Last updated: 20/07/2026, 18:40:32
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists):
        minHeap = []

        for node in lists:
            if node:
                heapq.heappush(minHeap, (node.val, id(node), node))

        dummy = ListNode(0)
        current = dummy

        while minHeap:
            value, _, node = heapq.heappop(minHeap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(minHeap, (node.next.val, id(node.next), node.next))

        return dummy.next
