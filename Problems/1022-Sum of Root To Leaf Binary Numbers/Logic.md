# 1022. Sum of Root To Leaf Binary Numbers

## Approach 1: Iterative BFS Using a Queue

### Logic / Intuition

Each node in the binary tree contains either `0` or `1`. Every root-to-leaf path represents a binary number.

We need to calculate the sum of all these binary numbers and return it as a decimal integer.

We use BFS and maintain a running binary number for every node.

The queue stores a pair:

`(node, current_number)`

When moving from a parent to a child, we update the number using:

`current_number = 2 * current_number + child.val`

### Why does this formula work?

Appending a binary digit to the right is equivalent to multiplying the existing number by `2` and adding the new digit.

For example, consider the binary path `1 -> 0 -> 1`:

- Start with `1`.
- Append `0`: `1 * 2 + 0 = 2`, which is binary `10`.
- Append `1`: `2 * 2 + 1 = 5`, which is binary `101`.

Therefore, the binary number `101` equals decimal `5`.

Whenever we reach a leaf node, the current number represents one complete root-to-leaf binary number, so we add it to `ans`.

### Algorithm

1. Initialize a queue with `(root, root.val)`.
2. Initialize `ans = 0`.
3. While the queue is not empty:
   - Remove `(node, count)` from the queue.
   - If the node is a leaf, add `count` to `ans`.
   - Otherwise, add its children to the queue, updating the binary number using `2 * count + child.val`.
4. Return `ans`.

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

    def sumRootToLeaf(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        queue = deque()

        # Store (node, binary number formed so far)
        queue.append((root, root.val))
        ans = 0

        while queue:
            node, count = queue.popleft()

            if self.isleaf(node):
                ans += count
                continue

            if node.left:
                queue.append((node.left, count * 2 + node.left.val))

            if node.right:
                queue.append((node.right, count * 2 + node.right.val))

        return ans
```

### Complexity Analysis

- **Time Complexity:** `O(n)` — every node is visited once.
- **Auxiliary Space Complexity:** `O(w)` — the queue stores nodes level by level, where `w` is the maximum width of the tree. Worst case: `O(n)`.

---

## Approach 2: Recursive DFS

### Logic / Intuition

We can solve the same problem using Depth-First Search (DFS).

Instead of storing the current binary number in a queue, we pass it as an argument to the recursive function.

For each node:

1. Update the number using `n = 2 * n + node.val`.
2. If the node is a leaf, add `n` to the answer.
3. Otherwise, recursively process the left and right subtrees, passing the updated number.

We use `self.ans` to maintain the total sum across all recursive calls.

### Algorithm

1. Initialize `self.ans = 0`.
2. Define a helper function `dfs(node, n)`.
3. If the node is `None`, return.
4. Update `n = 2 * n + node.val`.
5. If the node is a leaf, add `n` to `self.ans` and return.
6. Recursively call DFS for the left and right children.
7. Return `self.ans`.

### Code
```py
class Solution:
    def sumRootToLeaf(self, root: TreeNode | None) -> int:
        self.ans = 0

        def dfs(node: TreeNode | None, n: int = 0) -> None:
            if not node:
                return

            n = 2 * n + node.val

            if not node.left and not node.right:
                self.ans += n
                return

            dfs(node.left, n)
            dfs(node.right, n)

        dfs(root)
        return self.ans
```

### Complexity Analysis

- **Time Complexity:** `O(n)` — every node is visited once.
- **Auxiliary Space Complexity:** `O(h)` — the recursion stack depends on the height of the tree. Worst case: `O(n)` for a skewed tree.

---
