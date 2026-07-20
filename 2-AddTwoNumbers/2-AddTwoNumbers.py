# Last updated: 20/07/2026, 18:41:05

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c=0
        temp,l=l1,l2
        while(temp!=None and l!=None):
            temp=temp.next
            l=l.next
        l={temp==None:l2}.get(True,l1)
        temp=l
        
        while (l1!=None or l2!=None):
            if l1==None:
                s = c+l2.val
                c=s//10
                l.val=(s%10)
                l={l.next==None:l}.get(True,l.next)
                l2=l2.next
            elif l2==None:
                s = c+l1.val
                c=s//10
                l.val=(s%10)
                l1=l1.next
                l={l.next==None:l}.get(True,l.next)
            else:
                s = c+l1.val+l2.val
                c=s//10
                l.val=(s%10)
                l2,l1=l2.next,l1.next
                l={l.next==None:l}.get(True,l.next)
        if c!=0:
            new_node=ListNode(1)
            l.next=new_node
        return temp