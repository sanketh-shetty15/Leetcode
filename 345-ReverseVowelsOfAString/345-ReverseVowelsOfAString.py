# Last updated: 20/07/2026, 18:38:47
class Solution:
    def reverseVowels(self, s: str) -> str:
        vow="a","e","i","o","u","A","E","I","O","U"
        stack=[]
        for i in s:
            if i in vow:
                stack.append(i)
        stack=stack[::-1]
        res=[]
        j=0
        for i in s:
            if i in  vow:
                res.append(stack[j])
                j=j+1
            else:
                res.append(i)
        return "".join(res)
                

