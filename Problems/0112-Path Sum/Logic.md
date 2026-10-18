# 112. Path Sum

## Approach: Iterative BFS (Level Order Traversal)

### Logic / Intuition

We are given the root of a binary tree and an integer `targetSum`. We need to determine whether the tree has a root-to-leaf path whose node values add up to `targetSum`.

A **root-to-leaf path** starts at the root and ends at a leaf node. A leaf is a node that has neither a left nor a right child.

We use Breadth-First Search (BFS) with a queue to traverse the tree.

Instead of storing only the node in the queue, we store a pair:

`(node, current_sum)`

Here, `current_sum` represents the sum of all node values along the path from the root to the current node.

For every node:
- If it is a leaf, check whether `current_sum == targetSum`.
- If the condition is satisfied, return `True`.
- Otherwise, add its children to the queue, updating the path sum for each child.

If no root-to-leaf path matches the target, return `False`.

### Algorithm

1. If `root` is `None`, return `False`.
2. Initialize a queue with `(root, root.val)`.
3. While the queue is not empty:
   - Remove `(node, current_sum)` from the queue.
   - If the node is a leaf and `current_sum == targetSum`, return `True`.
   - If the left child exists, add `(node.left, current_sum + node.left.val)` to the queue.
   - If the right child exists, add `(node.right, current_sum + node.right.val)` to the queue.
4. If no valid path is found, return `False`.

### Code

from collections import deque
```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isleaf(self, node):
        return (not node.left) and (not node.right)

    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False

        queue = deque()
        queue.append((root, root.val))

        while queue:
            node, count = queue.popleft()

            if self.isleaf(node):
                if targetSum == count:
                    return True

            if node.left:
                queue.append((node.left, count + node.left.val))

            if node.right:
                queue.append((node.right, count + node.right.val))

        return False
```

### Complexity Analysis

- **Time Complexity:** `O(n)` — in the worst case, every node is visited once.
- **Auxiliary Space Complexity:** `O(w)`, where `w` is the maximum width of the tree. In the worst case, this can be `O(n)`.

Here, `n` is the number of nodes in the tree.

### Important Edge Cases

- **Empty tree:** Return `False`, because no root-to-leaf path exists.
- **Single-node tree:** Return `True` only if the root value equals `targetSum`.
- **Negative values:** The algorithm works correctly because it compares the complete path sum rather than assuming node values are positive.
- **Matching sum at a non-leaf node:** Do not return `True` unless the node is a leaf.


    current_sum + child.val

**Always check the target sum at a leaf node**, because the problem requires a complete root-to-leaf path, not just any path whose sum matches the target.
