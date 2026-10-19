# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if root is None: 
            root=TreeNode(val)
            return root
        
        curr=root
        while True:
            if val < curr.val:
                if not curr.left:
                    curr.left= TreeNode(val)
                    return root
                curr=curr.left
            elif val > curr.val:
                if not curr.right:
                    curr.right= TreeNode(val)
                    return root
                curr=curr.right
            else: return root       # Ignore duplicates
