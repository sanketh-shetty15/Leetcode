# Last updated: 02/08/2026, 18:07:27
1class Solution:
2    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
3        stack=[]
4        stack1=[]
5        stack2=[]
6        for i in nums:
7            if i<pivot:
8                stack.append(i)
9            elif i>pivot:
10                stack1.append(i)
11            else:
12                stack2.append(i)
13        return stack+stack2+stack1
14        