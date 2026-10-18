# 897. Increasing Order Search Tree

## Approach: Recursive Inorder Traversal

### Logic / Intuition

The given tree is a Binary Search Tree (BST).

The key property of a BST is:
- All values in the left subtree are smaller than the current node.
- All values in the right subtree are greater than the current node.

Inorder traversal of a BST produces values in ascending order.

Our goal is to rearrange the tree so that:
- Every node has no left child.
- Every node except the last has a right child containing the next value in sorted order.

We use inorder traversal to visit the nodes in ascending order and construct a new tree using only right pointers.

### Key Variables

- `result`: A dummy node that acts as the starting point of the new tree.
- `curr`: Points to the last node inserted into the new tree.
- `nonlocal curr`: Allows the nested `inorder()` function to update the `curr` variable defined in the outer function.

### Algorithm

1. Create a dummy node `result`.
2. Set `curr = result`.
3. Define a recursive helper function `inorder(node)`.
4. If the node exists:
   - Recursively traverse its left subtree.
   - Create a new node with the current node's value and attach it to `curr.right`.
   - Move `curr` to the newly created node.
   - Recursively traverse its right subtree.
5. Call `inorder(root)`.
6. Return `result.right`, which points to the first actual node of the new tree.

### Code
```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def increasingBST(self, root: TreeNode | None) -> TreeNode | None:
        result = TreeNode()
        curr = result

        def inorder(node: TreeNode | None):
            # Left -> Node -> Right
            nonlocal curr

            if node:
                inorder(node.left)

                curr.right = TreeNode(node.val)
                curr = curr.right

                inorder(node.right)

        inorder(root)

        return result.right
```
### Complexity Analysis

- **Time Complexity:** `O(n)` — every node is visited exactly once.
- **Auxiliary Space Complexity:** `O(h)` — the recursive call stack depends on the height of the original tree.
- **Output Space Complexity:** `O(n)` — a new node is created for every input node.

Here, `n` is the number of nodes and `h` is the height of the tree.
