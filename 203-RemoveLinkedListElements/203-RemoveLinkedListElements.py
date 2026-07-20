# Last updated: 20/07/2026, 18:39:16
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        temp=ListNode(0)
        prev=temp
        temp.next=head
        current=head
        while current:
            if current.val==val:
                prev.next=current.next
            else:
                prev=current
            current=current.next
        return temp.next
                
               
            





      
        