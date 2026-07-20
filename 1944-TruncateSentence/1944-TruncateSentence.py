# Last updated: 20/07/2026, 18:37:41
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        stack=[]
        count=0
        for i in s:
            if i!=" ":
                stack.append(i)
            elif i==" ":
                stack.append(i)
                count+=1
                if count==k:
                    break
        if stack[-1]==" ":
            stack.pop()
        return "".join(stack)



      

        # words = s.split(" ")
        # first_k_words = words[:k]
        # result = " ".join(first_k_words)

        # return result
            
        