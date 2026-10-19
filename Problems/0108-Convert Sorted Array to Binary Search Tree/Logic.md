# Convert Sorted Array to Binary Search Tree

## Approach 1: Recursive Divide and Conquer (Using Index Ranges)

### Intuition

Since the array is sorted, choosing the middle element as the root ensures that smaller elements go into the left subtree and larger elements go into the right subtree.

We recursively apply the same process to the left and right halves of the array. This produces a height-balanced Binary Search Tree (BST).

### Algorithm

1. Define a recursive function `build(left, right)` to construct a BST from the given index range.
2. If `left > right`, return `None` because the range is empty.
3. Calculate the middle index: `mid = (left + right) // 2`.
4. Create a node with value `nums[mid]`.
5. Recursively construct the left subtree using `build(left, mid - 1)`.
6. Recursively construct the right subtree using `build(mid + 1, right)`.
7. Return the created node.
8. Initially, call `build(0, n - 1)`.

### Code
```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def build(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            node = TreeNode(nums[mid])

            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)

            return node

        n = len(nums)
        return build(0, n - 1)
```
### Complexity Analysis

- **Time Complexity:** O(n), because each element is used to create exactly one node.
- **Auxiliary Space Complexity:** O(log n) for the recursion stack because the resulting tree is balanced.
- **Total Space Complexity:** O(n), including the output tree.

---

## Approach 2: Recursive Divide and Conquer (Using Inorder Traversal)

### Intuition

An inorder traversal of a BST visits nodes in ascending order: left subtree, root, and right subtree.

Since the input array is already sorted, we can construct a balanced BST by simulating an inorder traversal.

Instead of selecting the middle element directly, we determine the size of each subtree:

- The left subtree contains `size // 2` elements.
- The root is the next unused element in the sorted array.
- The right subtree contains `size - size // 2 - 1` elements.

We maintain a global-like pointer `curr` to track the next unused array element. The `nonlocal` keyword allows the nested function to update this pointer.

### Algorithm

1. Initialize `curr = 0`.
2. Define a recursive function `build(size)` that constructs a BST containing `size` nodes.
3. If `size == 0`, return `None`.
4. Recursively construct the left subtree using `build(size // 2)`.
5. Create the root using `nums[curr]`.
6. Attach the constructed left subtree to the root.
7. Increment `curr` to move to the next array element.
8. Recursively construct the right subtree using `build(size - size // 2 - 1)`.
9. Attach the right subtree and return the root.
10. Initially, call `build(n)`.

### Code
```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        n = len(nums)
        curr = 0

        def build(size):
            nonlocal curr

            if size == 0:
                return None

            left_tree = build(size // 2)
            root = TreeNode(nums[curr])

            root.left = left_tree

            curr += 1

            right_tree = build(size - size // 2 - 1)
            root.right = right_tree

            return root

        return build(n)
```
### Complexity Analysis

- **Time Complexity:** O(n), because each element is processed exactly once.
- **Auxiliary Space Complexity:** O(log n) for the recursion stack because the constructed tree is balanced.
- **Total Space Complexity:** O(n), including the output tree.

---
