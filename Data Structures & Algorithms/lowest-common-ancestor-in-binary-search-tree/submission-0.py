# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        if root.val == q.val:
            return q
        if root.val == p.val:
            return p
        left,right = self.lowestCommonAncestor(root.right,p,q),self.lowestCommonAncestor(root.left,p,q)
        if left and right:
            return root
        elif left and not right:
            return left
        elif right and not left:
            return right