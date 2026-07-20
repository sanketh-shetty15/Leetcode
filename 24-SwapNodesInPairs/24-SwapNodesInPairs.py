# Last updated: 20/07/2026, 18:40:31
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):
        dummy=ListNode(0,head)
        prev=dummy
        while head and head.next:
            a=head
            b=head.next
            prev.next=b
            a.next=b.next
            b.next=a
            prev=a
            head=a.next
        return dummy.next
