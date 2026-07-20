# Last updated: 20/07/2026, 18:40:37
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        # mapping={")":"(","}":"{","]":"["}
        for ch in s:
            if ch=="(":
                stack.append(")")
            elif ch=="[":
                stack.append("]")
            elif ch=="{":
                stack.append("}")
            else:
                if not stack or stack.pop()!=ch:
                    return False

        return len(stack)==0
            
        #     if char in mapping.values():
        #         stack.append(char)

        #     else:
        #         if not stack or stack[-1]!=mapping[char]:
        #             return False
        #         stack.pop()
        # return not stack















    #     stack = []
    #     mapping = {')': '(', '}': '{', ']': '['}

    #     for char in s:
    #         if char in mapping.values():  
    #             stack.append(char)
    #         else:  
    #             if not stack or stack[-1] != mapping[char]:
    #                 return False
    #             stack.pop()

    #     return not stack
