# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isleaf(self,node):
        return (not node.left) and (not node.right)
    
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root: return False

        queue=deque()
        queue.append((root,root.val))

        while (queue):
            node,count=queue.popleft()

            if self.isleaf(node):
                if targetSum==count: return True

            if node.left: queue.append([node.left,count+node.left.val])
            if node.right: queue.append([node.right,count+node.right.val])
        
        return False

