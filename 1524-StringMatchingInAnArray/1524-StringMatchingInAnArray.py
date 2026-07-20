# Last updated: 20/07/2026, 18:37:50
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        stack=[]
        for i in range(len(words)):
            for j in range(len(words)):
                if i!=j and words[i] in words[j]:
                    stack.append(words[i])
                    break
                    
        return stack
        