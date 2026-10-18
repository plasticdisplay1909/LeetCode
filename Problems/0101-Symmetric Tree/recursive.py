# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseTree(self,root: TreeNode | None)-> TreeNode|None:
        if not root: return

        queue=deque()
        queue.append(root)

        while queue:
            node=queue.popleft()

            node.left,node.right=node.right,node.left
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        
        return root

    def isSameTree(self,p:TreeNode | None,q:TreeNode|None):
        if not p and not q: return True
        if not p or not q: return False
        

        return p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        
    def isSymmetric(self, root: TreeNode | None) -> bool:
        # Idea -> Reverse one half of the tree and compare for equality we have done both of them in sepearte questions

        root.right=self.reverseTree(root.right)

        return self.isSameTree(root.left,root.right)
