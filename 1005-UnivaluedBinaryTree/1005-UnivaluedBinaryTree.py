# Last updated: 20/07/2026, 18:37:59
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        v=root.val
        levelsize=[root]
        while levelsize:
                node=levelsize.pop(0)
                if v!=node.val:
                    return False
                if node.left:
                    levelsize.append(node.left)
                if node.right:
                    levelsize.append(node.right)
        return True

        