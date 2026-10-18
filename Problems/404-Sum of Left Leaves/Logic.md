# 404. Sum of Left Leaves

## Approach: Iterative BFS (Level Order Traversal)

### Logic / Intuition

We are given the root of a binary tree and need to return the sum of all left leaf nodes.

A **left leaf** is a node that satisfies both conditions:
- It is the left child of its parent.
- It has no left or right children.

We use Breadth-First Search (BFS) with a queue to traverse the tree.

For every node:
- Check whether its left child exists.
- If the left child is a leaf, add its value to `count`.
- Add the left child to the queue to continue traversing the tree.
- Add the right child to the queue if it exists, because it may have left leaves of its own.

We do not add right leaves directly to the sum.

### Algorithm

1. If `root` is `None`, return `0`.
2. Initialize a queue with the root node.
3. Initialize `count = 0`.
4. While the queue is not empty:
   - Remove a node from the queue.
   - If its left child exists:
     - If the left child is a leaf, add its value to `count`.
     - Add the left child to the queue.
   - If its right child exists, add it to the queue.
5. Return `count`.

### Code
```py
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isleaf(self, node: TreeNode | None) -> bool:
        return not node.left and not node.right

    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        queue = deque()
        queue.append(root)

        count = 0

        while queue:
            node = queue.popleft()

            if node.left:
                if self.isleaf(node.left):
                    count += node.left.val

                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return count
```

### Complexity Analysis

- **Time Complexity:** `O(n)` — each node is visited at most once.
- **Auxiliary Space Complexity:** `O(w)`, where `w` is the maximum width of the tree. In the worst case, this is `O(n)`.

Here, `n` is the number of nodes in the tree.

### Important Edge Cases

- **Empty tree:** Return `0`.
- **Single-node tree:** Return `0`, because the root is not a left leaf.
- **Only right leaves:** Return `0` if there are no left leaves.
- **Negative node values:** Add them normally; the sum can be negative.

