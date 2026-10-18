# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root: return 0
        queue=deque()
        queue.append(root)

        levels=0

        # Applying BFS-modified
        while queue:
            n=len(queue)
            levels+=1
            for i in range(n):
                node=queue.popleft()

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        
        return levels
