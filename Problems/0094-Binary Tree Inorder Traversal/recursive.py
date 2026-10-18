# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        'Left -> Node -> Right'
        result=[]

        "Helper function "
        "We need this helper function otherwise each recursive call creates a new empty result"
        def inorder(root):
            if root:
                inorder(root.left)
                result.append(root.val)
                inorder(root.right)
        
        inorder(root)
        return result

        
        
