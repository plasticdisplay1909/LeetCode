# Insert into a Binary Search Tree (BST)

## Approach

We use the Binary Search Tree property to find the correct position for the new node.

- All values in the left subtree are smaller than the current node.
- All values in the right subtree are greater than the current node.

## Intuition

1. If `root` is `None`, create a new node with `val` and return it.
2. Otherwise, start traversing from the root using a pointer `curr`.
3. If `val < curr.val`:
   - If the left child is empty, insert the new node there and return the original root.
   - Otherwise, move to the left child.
4. If `val > curr.val`:
   - If the right child is empty, insert the new node there and return the original root.
   - Otherwise, move to the right child.
5. If `val == curr.val`, return the original root without inserting a duplicate.

Continue until the node is inserted.

## Code
```py
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if root is None:
            root = TreeNode(val)
            return root

        curr = root

        while True:
            if val < curr.val:
                if not curr.left:
                    curr.left = TreeNode(val)
                    return root
                curr = curr.left

            elif val > curr.val:
                if not curr.right:
                    curr.right = TreeNode(val)
                    return root
                curr = curr.right

            else:
                return root  # Ignore duplicates
```

## Complexity Analysis

- Time Complexity: O(h), where h is the height of the BST.
  - Balanced BST: O(log n)
  - Skewed BST: O(n)
- Space Complexity: O(1), as we use only a constant amount of extra space.

## Key Points

- The BST property determines where the new node should be inserted.
- No rearrangement of existing nodes is needed.
- We return `root` because it represents the root of the entire tree, whereas `curr` points to a node within the tree.
- The `root is None` condition handles an empty tree.
