# 101. Symmetric Tree

## Approach 1: Recursive DFS (Mirror Comparison)

### Logic / Intuition

A binary tree is symmetric if its left and right subtrees are mirror images of each other.

Two subtrees are mirrors if:
1. Both nodes are `None`.
2. Neither node is `None`, and their values are equal.
3. The left subtree of the first node mirrors the right subtree of the second node.
4. The right subtree of the first node mirrors the left subtree of the second node.

We use a helper function `is_mirror(n1, n2)` to compare the two subtrees recursively.

Notice that we compare opposite children:
- `n1.left` with `n2.right`
- `n1.right` with `n2.left`

If both comparisons are `True` and the current values match, the subtrees are mirrors.

### Algorithm

1. Define a helper function `is_mirror(n1, n2)`.
2. If both nodes are `None`, return `True`.
3. If only one node is `None`, return `False`.
4. If their values differ, return `False`.
5. Recursively compare `n1.left` with `n2.right`.
6. Recursively compare `n1.right` with `n2.left`.
7. Return the result of both comparisons.
8. Call `is_mirror(root.left, root.right)`.

### Code
```py
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def is_mirror(n1, n2):
            if not n1 and not n2:
                return True

            if not n1 or not n2:
                return False

            return (
                n1.val == n2.val
                and is_mirror(n1.left, n2.right)
                and is_mirror(n1.right, n2.left)
            )

        return is_mirror(root.left, root.right) if root else True
```

### Complexity Analysis

- **Time Complexity:** `O(n)` — each node is visited at most once.
- **Auxiliary Space Complexity:** `O(h)` — due to the recursion stack, where `h` is the tree height.
- **Worst-case Space Complexity:** `O(n)` for a skewed tree.

---

## Approach 2: Reverse One Subtree and Compare

### Logic / Intuition

Instead of directly comparing mirror positions, we can reverse one subtree and then check whether the two subtrees are identical.

The idea is based on two previously learned operations:
- Reverse a binary tree.
- Check whether two binary trees are identical.

If the tree is symmetric, reversing the right subtree should make it identical to the left subtree.

We use:
- `reverseTree()` to mirror a subtree iteratively using BFS and a queue.
- `isSameTree()` to compare two trees recursively.
- `isSymmetric()` to combine both operations.

### Algorithm

1. If the root is `None`, return `True`.
2. Reverse the right subtree using `reverseTree(root.right)`.
3. Compare the left subtree and the reversed right subtree using `isSameTree()`.
4. Return the comparison result.

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
    def reverseTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None

        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()

            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return root

    def isSameTree(
        self,
        p: TreeNode | None,
        q: TreeNode | None
    ) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        return (
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )

    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root:
            return True

        # Reverse the right subtree and compare it with the left subtree.
        root.right = self.reverseTree(root.right)

        return self.isSameTree(root.left, root.right)
```
### Complexity Analysis

- **Time Complexity:** `O(n)` — reversing the subtree and comparing the trees each take linear time.
- **Auxiliary Space Complexity:** `O(n)` in the worst case because the BFS queue can contain many nodes; the recursive comparison also uses a call stack.
- **Important:** This approach modifies the original tree by swapping the children of nodes in the right subtree.

---



Unlike `isSameTree()`, which compares left with left and right with right, symmetry requires comparing opposite sides.

**Important edge case:** Always handle `root = None`. An empty binary tree is symmetric.
