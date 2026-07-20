# Last updated: 20/07/2026, 18:39:36
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        
        def postorder(root):
            if not root:
                return
            
            postorder(root.left)
            postorder(root.right)
            ans.append(root.val)
        
        postorder(root)
        return ans
