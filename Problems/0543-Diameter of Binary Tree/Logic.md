# Diameter of Binary Tree

## Approach 1: Recursive Height Calculation (For Root's Diameter Only)

### Intuition

The diameter of a binary tree is the length of the longest path between any two nodes. The path may or may not pass through the root.

For a path passing through the root, the diameter is:

`height(root.left) + height(root.right)`

Here, height is measured in the number of edges from the root of a subtree to its deepest leaf. Since our `height()` function returns the number of nodes, adding the left and right heights gives the number of edges in the path through the root.

However, this approach only calculates the diameter passing through the root. The actual diameter might lie entirely inside the left or right subtree.

### Code
```py
class Solution:
    def height(self, root) -> int:
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.height(root.left) + self.height(root.right)
```

### Complexity Analysis

- **Time Complexity:** O(n), because calculating the height visits every node.
- **Space Complexity:** O(h), where h is the height of the tree, due to recursion.

**Important:** This code is not correct for all test cases because it only considers paths passing through the root.

---

## Approach 2: Recursive DFS (Calculate Height and Diameter Together)

### Intuition

Instead of calculating the diameter only at the root, we calculate it at every node.

At each node, the longest path passing through that node is:

`height(node.left) + height(node.right)`

We maintain a variable `ans` to store the maximum diameter found so far.

A recursive DFS function calculates the height of each subtree while updating `ans`. This avoids repeatedly calculating heights and ensures that we consider paths passing through every node.

### Algorithm

1. Initialize `ans = 0`.
2. Define a recursive function `height(root)`.
3. If the node is `None`, return `0`.
4. Recursively calculate the heights of the left and right subtrees.
5. Update `ans` with the maximum of its current value and `left_height + right_height`.
6. Return `1 + max(left_height, right_height)`.
7. Call `height(root)` and return `ans`.

### Code
```py
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def height(node):
            nonlocal ans

            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            ans = max(ans, left + right)

            return 1 + max(left, right)

        height(root)
        return ans
```

### Complexity Analysis

- **Time Complexity:** O(n), because every node is visited exactly once.
- **Space Complexity:** O(h), where h is the height of the tree, due to the recursion stack.

For a balanced tree, the auxiliary space is O(log n). For a skewed tree, it is O(n).

---

## Which Approach Is Better?

**Approach 2: Recursive DFS (Calculate Height and Diameter Together)** is the recommended solution. It considers every possible path through every node and calculates the diameter in O(n) time without repeatedly recalculating subtree heights.
