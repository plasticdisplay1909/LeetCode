# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode | None) -> TreeNode | None:
        result=TreeNode()
        curr=result

        def inorder(node : TreeNode):
            'Left->Node->Right'
            nonlocal curr
            
            if node:
                inorder(node.left)
                curr.right=TreeNode(node.val)

                curr=curr.right
                inorder(node.right)
        
        inorder(root)

        return result.right


