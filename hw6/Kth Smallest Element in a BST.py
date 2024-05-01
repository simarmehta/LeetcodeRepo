# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def _inorder(node):
            if not node:
                return
            _inorder(node.left)
            if len(res) == k:
                return
            res.append(node.val)
            _inorder(node.right)

        _inorder(root)
        return res[-1]
