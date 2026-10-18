# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isleaf(self, node:TreeNode | None) -> bool:
        return not(node.left) and not(node.right)

    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        queue=deque()
        queue.append(root)

        count=0
        while queue:
            node=queue.popleft()

            if node.left:
                if self.isleaf(node.left): count+=node.left.val
                queue.append(node.left)
            
            if node.right: queue.append(node.right)
        
        return count
