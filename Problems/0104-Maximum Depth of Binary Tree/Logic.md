# 104. Maximum Depth of Binary Tree

## Approach 1: Iterative BFS (Level Order Traversal)

### Logic / Intuition

The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to a leaf node.

We use **Breadth-First Search (BFS)** to traverse the tree level by level.

The key idea is that each level represents one unit of depth.

- Initialize a queue with the root node.
- Process all nodes at the current level before moving to the next level.
- Increment `levels` once for every level processed.
- Add the left and right children of each node to the queue.
- When the queue becomes empty, return the total number of levels.

### Algorithm

1. If `root` is `None`, return `0`.
2. Initialize a queue and insert the root node.
3. Initialize `levels = 0`.
4. While the queue is not empty:
   - Store the current queue size in `n`.
   - Increment `levels` by `1`.
   - Process exactly `n` nodes.
   - For each node, add its non-null left and right children to the queue.
5. Return `levels`.

**Why do we store `n = len(queue)`?**

The queue may grow as we add children. Storing its size ensures that we process only the nodes belonging to the current level. Children added during that iteration are processed at the next level.

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
    def maxDepth(self, root: TreeNode | None) -> int:
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

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return levels
```

### Complexity Analysis

- **Time Complexity:** `O(n)` — every node is visited exactly once.
- **Auxiliary Space Complexity:** `O(w)`, where `w` is the maximum width of the tree. In the worst case, this is `O(n)`.

---

## Approach 2: Recursive DFS

### Logic / Intuition

The maximum depth of a binary tree can also be calculated recursively.

For every node:

- If the node is `None`, its depth is `0`.
- Otherwise, calculate the maximum depth of its left subtree and right subtree.
- Take the maximum of those two depths and add `1` for the current node.

The formula is:

    maxDepth(root) = 1 + max(maxDepth(root.left), maxDepth(root.right))

### Algorithm

1. If `root` is `None`, return `0`.
2. Recursively calculate the depth of the left subtree.
3. Recursively calculate the depth of the right subtree.
4. Return `1 + max(left_depth, right_depth)`.

### Code
```
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)
```
### Complexity Analysis

- **Time Complexity:** `O(n)` — every node is visited once.
- **Auxiliary Space Complexity:** `O(h)` — the recursion stack depends on the height of the tree.
- **Worst-case Auxiliary Space:** `O(n)` for a skewed tree.

---

