# 1. Recursive Approach

## Problem
Given the root of a binary tree, return the inorder traversal of its nodes' values.
Inorder Traversal: Left -> Node -> Right

## Logic / Intuition

In inorder traversal, we visit each node in the following order:

1. Traverse the left subtree.
2. Visit the current node and add its value to the result.
3. Traverse the right subtree.

We use a helper function called `inorder()` to recursively traverse the tree.

The `result` list is created outside the helper function so that every recursive call shares the same list. If we created a new list inside every recursive call, we would lose the results accumulated by previous calls unless we explicitly combined and returned them.

## Algorithm

1. Initialize an empty list `result`.
2. Define a helper function `inorder(root)`.
3. If the current node is `None`, return.
4. Recursively traverse the left subtree.
5. Append the current node's value to `result`.
6. Recursively traverse the right subtree.
7. Call `inorder(root)` and return `result`.

## Code
```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        # Left -> Node -> Right
        result = []

        def inorder(root):
            if root:
                inorder(root.left)
                result.append(root.val)
                inorder(root.right)

        inorder(root)
        return result
```

## Complexity Analysis

- Time Complexity: O(n), because every node is visited exactly once.
- Auxiliary Space Complexity: O(h), where h is the height of the tree, due to the recursive call stack.
- Output Space Complexity: O(n), for storing the traversal result.
- Worst-case auxiliary space: O(n) for a skewed tree.

---

# 2.Iterative Approach Using a Stack

## Logic / Intuition

The recursive approach uses the function call stack automatically. In the iterative approach, we manage the traversal ourselves using an explicit stack.

The key idea is to go as far left as possible before visiting a node.

Why? In inorder traversal, the left subtree must be processed before the current node.

Once there is no more left child:
1. Pop a node from the stack.
2. Add its value to `result`.
3. Move to its right subtree.
4. Repeat the process.

We continue while either `curr` is not `None` or the stack is not empty.

## Algorithm

1. Initialize an empty `stack` and an empty `result` list.
2. Set `curr = root`.
3. While `curr` exists or the stack is not empty:
   - Push `curr` onto the stack and move left until `curr` becomes `None`.
   - Pop the top node from the stack.
   - Append its value to `result`.
   - Move `curr` to the popped node's right child.
4. Return `result`.
```py
## Code

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        # Left -> Node -> Right
        stack = []
        result = []

        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right

        return result
```
The traversal is complete when `curr` is `None` and the stack is empty.

## Complexity Analysis

- Time Complexity: O(n), because every node is pushed and popped at most once.
- Auxiliary Space Complexity: O(h), where h is the height of the tree, for the stack.
- Output Space Complexity: O(n), for storing the traversal result.
- Worst-case auxiliary space: O(n) for a skewed tree.

---


