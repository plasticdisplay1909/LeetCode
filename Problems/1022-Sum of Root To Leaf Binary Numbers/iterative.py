# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isleaf(self,node: TreeNode | None) ->int:
        return not(node.left) and not(node.right)
    
    def sumRootToLeaf(self, root: TreeNode | None) -> int:
        # Number of nodes is atleast 1 so don't need to care about empty
        queue=deque()       # Implementing BFS

        # Initialization
        queue.append([root,root.val])
        ans=0

        while queue:
            node,count=queue.popleft()

            if self.isleaf(node):
                ans+=count
                continue
            
            if node.left:
                queue.append([node.left,count*2 + node.left.val])
            
            if node.right:
                queue.append([node.right,2*count + node.right.val])
        
        return ans
