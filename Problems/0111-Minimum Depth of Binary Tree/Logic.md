# 111. Minimum Depth of Binary Tree

## Approach 1: Iterative BFS (Level Order Traversal)

### Logic / Intuition

The minimum depth of a binary tree is the number of nodes along the shortest path from the root node down to the nearest leaf node.

A **leaf node** is a node that has no left child and no right child.

We use Breadth-First Search (BFS) to traverse the tree level by level.

The key observation is that **the first leaf node encountered during BFS has the minimum depth**.

Why?

- BFS processes nodes level by level, starting from the root.
- All nodes at a smaller depth are processed before nodes at a greater depth.
- Therefore, as soon as we encounter a leaf node, we can return the current depth without processing the remaining nodes.

### Algorithm

1. If `root` is `None`, return `0`.
2. Initialize a queue and insert the root node.
3. Initialize `levels = 0`.
4. While the queue is not empty:
   - Store the current queue size in `n`.
   - Increment `levels` by `1`.
   - Process exactly `n` nodes at the current level.
   - If a node has neither a left nor a right child, return `levels`.
   - Otherwise, add its non-null children to the queue.
5. Return `levels` if the loop finishes.

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
    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        queue = deque()
        queue.append(root)

        levels = 0

        # BFS - Level Order Traversal
        while queue:
            n = len(queue)
            levels += 1

            for i in range(n):
                node = queue.popleft()

                # First leaf node gives the minimum depth
                if not node.left and not node.right:
                    return levels

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return levels
```

### Important Edge Case

Consider this tree:

    1
     \
      2
       \
        3

Output:

    3

The minimum depth is `3`, not `1` or `2`, because a path must end at a leaf node. A node with only one child is not a leaf.

### Complexity Analysis

- **Time Complexity:** `O(n)` in the worst case, where `n` is the number of nodes. In practice, BFS may terminate early when it finds the first leaf.
- **Auxiliary Space Complexity:** `O(w)`, where `w` is the maximum width of the tree. In the worst case, this is `O(n)`.

---

## Approach 2: Recursive DFS

### Logic / Intuition

We can also calculate the minimum depth recursively.

However, there is an important detail: **we cannot simply take the minimum of the left and right subtree depths**, because a missing child has depth `0`.

Therefore, we handle three cases:

1. If the node is `None`, return `0`.
2. If the left child is missing, the minimum depth must come from the right subtree.
3. If the right child is missing, the minimum depth must come from the left subtree.
4. If both children exist, take the minimum of their depths and add `1`.

### Algorithm

1. If `root` is `None`, return `0`.
2. If `root.left` is `None`, return `1 + minDepth(root.right)`.
3. If `root.right` is `None`, return `1 + minDepth(root.left)`.
4. Otherwise, return `1 + min(minDepth(root.left), minDepth(root.right))`.

### Code
```py
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        if not root.left:
            return 1 + self.minDepth(root.right)

        if not root.right:
            return 1 + self.minDepth(root.left)

        return 1 + min(self.minDepth(root.left),self.minDepth(root.right))
```
### Complexity Analysis

- **Time Complexity:** `O(n)` — every node may need to be visited.
- **Auxiliary Space Complexity:** `O(h)` — due to the recursion stack, where `h` is the height of the tree.
- **Worst-case Auxiliary Space:** `O(n)` for a skewed tree.

---

