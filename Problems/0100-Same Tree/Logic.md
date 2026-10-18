# 100. Same Tree

## Approach 1: Recursive DFS

### Logic / Intuition

Two binary trees are the same if:
1. Both trees are structurally identical.
2. Corresponding nodes have the same values.

We recursively compare the two trees node by node.

- If both nodes are `None`, they are identical, so return `True`.
- If only one node is `None`, the structures differ, so return `False`.
- If their values differ, return `False`.
- Otherwise, recursively compare their left and right subtrees.

Both subtrees must be identical, so we use `and`.

### Code
```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return (
            self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )
```

### Complexity Analysis

- **Time Complexity:** `O(n)`, where `n` is the number of nodes in the smaller tree in the worst case when both trees have the same size. More generally, it is `O(min(n, m))` until a mismatch is found, with a worst case of `O(min(n, m))` comparisons.
- **Auxiliary Space Complexity:** `O(h)`, where `h` is the maximum recursion depth. In the worst case, this is `O(n)` for a skewed tree.

---

## Approach 2: Iterative BFS Using Two Queues

### Logic / Intuition

Instead of recursion, we use two queues to compare the trees level by level.

- `queue1` stores nodes from tree `p`.
- `queue2` stores corresponding nodes from tree `q`.

At each step:
1. Remove one node from each queue.
2. If both nodes are `None`, continue.
3. If only one node is `None`, return `False`.
4. If their values differ, return `False`.
5. Add their left and right children to their respective queues.

If all corresponding nodes match, return `True`.

We use `deque` because `popleft()` efficiently removes elements from the front of a queue.

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
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        queue1 = deque()
        queue2 = deque()

        queue1.append(p)
        queue2.append(q)

        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()

            if not node1 and not node2:
                continue

            elif not node1 or not node2 or node1.val != node2.val:
                return False

            queue1.append(node1.left)
            queue1.append(node1.right)

            queue2.append(node2.left)
            queue2.append(node2.right)

        return not queue1 and not queue2
```
### Complexity Analysis

- **Time Complexity:** `O(n)` when both trees contain `n` nodes and are identical. More generally, `O(min(n, m))` comparisons occur before a mismatch, with the queues processing corresponding positions.
- **Auxiliary Space Complexity:** `O(w)`, where `w` is the maximum width of the trees. In the worst case, this is `O(n)`.

---



Both solutions check **node values and tree structure**, including missing children.
