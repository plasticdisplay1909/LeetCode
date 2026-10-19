# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        # Counting number of node
        n,curr=0,head

        while curr:
            n,curr=n+1,curr.next
        
        self.curr=head

        def build(size):
            if size==0: return None

            left=build(size//2)
            root=TreeNode(self.curr.val)
            root.left=left

            self.curr=self.curr.next
            root.right=build(size- size//2 - 1)

            return root
        
        return build(n)
