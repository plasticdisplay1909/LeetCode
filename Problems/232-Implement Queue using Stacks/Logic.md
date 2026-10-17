# 232. Implement Queue using Stacks

## Problem

Implement a first-in-first-out (FIFO) queue using only two stacks. The queue should support the following operations:

- `push(x)`: Push element `x` to the back of the queue.
- `pop()`: Remove and return the element at the front of the queue.
- `peek()`: Return the element at the front of the queue.
- `empty()`: Return `True` if the queue is empty, otherwise return `False`.

## Intuition

A queue follows the **FIFO (First In, First Out)** principle, whereas a stack follows the **LIFO (Last In, First Out)** principle.
We can simulate a queue using two stacks:

- `q1`: Stores newly pushed elements.
- `q2`: Stores elements in the order required for popping and peeking.

When `q2` is empty and we need to access the front element, transfer all elements from `q1` to `q2`. This reverses their order, making the oldest element accessible at the top of `q2`.

If `q2` is not empty, we use it directly without transferring elements.

## Approach

1. Initialize two empty stacks, `q1` and `q2`.
2. **Push:** Append the new element to `q1`.
3. **Pop:**
   - If `q2` is empty, transfer all elements from `q1` to `q2`.
   - Remove and return the top element of `q2`.
4. **Peek:**
   - If `q2` is empty, transfer all elements from `q1` to `q2`.
   - Return the top element of `q2` without removing it.
5. **Empty:** Return `True` if both stacks are empty.

## Python Solution

```python
class MyQueue:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        if not self.q2:
            while self.q1:
                self.q2.append(self.q1.pop())

        value = self.q2.pop()
        return value

    def peek(self) -> int:
        if not self.q2:
            while self.q1:
                self.q2.append(self.q1.pop())

        return self.q2[-1]

    def empty(self) -> bool:
        return (not self.q1) and (not self.q2)
```



## Complexity Analysis

Let `n` be the number of elements in the queue.

| Operation | Time Complexity |
|---|---|
| `push(x)` | O(1) |
| `pop()` | O(1) amortized |
| `peek()` | O(1) amortized |
| `empty()` | O(1) |

**Space Complexity:** O(n), where `n` is the number of elements stored in the queue.

### Why is pop() amortized O(1)?

An individual `pop()` or `peek()` can take O(n) time when all elements must be transferred from `q1` to `q2`.

However, each element is transferred from `q1` to `q2` at most once and removed from `q2` at most once. Therefore, across a sequence of operations, the amortized time complexity of `pop()` and `peek()` is O(1).

## Key Takeaway

Two stacks can simulate a queue by reversing the order of elements when necessary. The first stack handles insertion, while the second stack handles removal and access to the front element.

This approach achieves **amortized O(1) time per operation** and **O(n) space complexity**.

## Additional Note
The python solution using two list as stack seems to be a little worth-less. But the same approach in `C++` makes much more sense
