# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        a=[]
        def inorder(root):
            if root:
                inorder(root.left)
                a.append(root.val)
                inorder(root.right)
        inorder(root)
        d=a[1]-a[0]
        for i in range(2,len(a)):
            d=min(d,a[i]-a[i-1])
        return d