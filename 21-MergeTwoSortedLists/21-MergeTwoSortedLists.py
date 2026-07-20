# Last updated: 20/07/2026, 18:40:35
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3=ListNode()
        list4=list3
        while list1 and list2:
            if list1.val>list2.val:
                list4.next=list2
                list2=list2.next
            else:
                list4.next=list1
                list1=list1.next
            list4=list4.next
        if list1:
            list4.next=list1
        else:
            list4.next=list2
        return list3.next


            #list3.add(list1.value)
            

            
        