# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        queue1=deque()
        queue2=deque()

        queue1.append(p)
        queue2.append(q)

        while (queue1 and queue2):
            node1=queue1.popleft()
            node2=queue2.popleft()

            if (not node1) and (not node2):
                continue
            elif (not node1) or (not node2) or (node1.val !=node2.val):
                return False

            queue1.append(node1.left)
            queue1.append(node1.right)

            queue2.append(node2.left)
            queue2.append(node2.right)
        
        return (not queue1) and (not queue2)
