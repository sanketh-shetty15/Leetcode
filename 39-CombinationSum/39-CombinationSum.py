# Last updated: 20/07/2026, 18:40:15
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def recur(idx, total, ans):
            if total == 0:
                res.append(ans[:])
                return 
            
            if idx >= len(candidates) or total < 0:
                return

            ans.append(candidates[idx])
            recur(idx, total - candidates[idx], ans)
            ans.pop()
            recur(idx + 1, total, ans)

        recur(0, target, [])
        return res