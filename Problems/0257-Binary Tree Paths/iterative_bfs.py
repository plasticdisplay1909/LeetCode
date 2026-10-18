# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isleaf(self,node: TreeNode| None) -> bool:
        return not(node.left) and not(node.right)
    
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        queue=deque()

        queue.append((root,str(root.val)))
        ans=[]
        while queue:
            node,path=queue.popleft()

            if self.isleaf(node): ans.append(path)

            if node.left: 
                queue.append([node.left, path+'->'+str(node.left.val)])

            if node.right: 
                queue.append([node.right, path+'->'+str(node.right.val)])
        
        return ans
