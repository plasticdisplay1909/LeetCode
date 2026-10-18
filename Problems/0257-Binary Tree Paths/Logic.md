# 257. Binary Tree Paths

## Approach: Iterative BFS (Level Order Traversal)

### Logic / Intuition

We are given the root of a binary tree and need to return all root-to-leaf paths as strings.

A root-to-leaf path starts at the root and ends at a leaf node. A leaf is a node that has neither a left nor a right child.

We use Breadth-First Search (BFS) with a queue.

Instead of storing only the node in the queue, we store a pair:

`(node, path)`

Here:
- `node` is the current tree node.
- `path` is the string representing the path from the root to that node.

For every node:
- If it is a leaf, add its path to the answer.
- If it has a left child, add that child and its updated path to the queue.
- If it has a right child, add that child and its updated path to the queue.

We use `"->"` to separate the node values in each path.

### Algorithm

1. If `root` is `None`, return an empty list.
2. Initialize a queue with `(root, str(root.val))`.
3. Initialize an empty list `ans`.
4. While the queue is not empty:
   - Remove `(node, path)` from the queue.
   - If the node is a leaf, append `path` to `ans`.
   - If the left child exists, add `(node.left, path + "->" + str(node.left.val))` to the queue.
   - If the right child exists, add `(node.right, path + "->" + str(node.right.val))` to the queue.
5. Return `ans`.

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

    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        if not root:
            return []

        queue = deque()
        queue.append((root, str(root.val)))

        ans = []

        while queue:
            node, path = queue.popleft()

            if self.isleaf(node):
                ans.append(path)

            if node.left:
                queue.append(
                    (node.left, path + "->" + str(node.left.val))
                )

            if node.right:
                queue.append(
                    (node.right, path + "->" + str(node.right.val))
                )

        return ans
```

### Complexity Analysis

Let:
- `n` be the number of nodes.
- `L` be the number of root-to-leaf paths.
- `h` be the height of the tree.

- **Time Complexity:** `O(n * h)` in the worst case when accounting for the cost of constructing and copying path strings.
- **Auxiliary Space Complexity:** `O(n * h)` in the worst case for storing path strings in the queue.
- **Output Space Complexity:** Depends on the total length of all returned paths, up to `O(L * h)` when node values have bounded string length.

### Important Edge Cases

- **Empty tree:** Return `[]`.
- **Single-node tree:** Return a list containing only the root value as a string, such as `["1"]`.
- **Negative values:** Convert node values to strings before concatenating them.

