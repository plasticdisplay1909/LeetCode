# 20. Valid Parentheses

## Intuition

We use a stack to keep track of opening brackets.
A stack follows the Last In, First Out (LIFO) principle. The most recently opened bracket must be the first one to close.

- If the character is an opening bracket, push it onto the stack.
- If the character is a closing bracket and the stack is empty, return `false`.
- Otherwise, check whether the top of the stack matches the closing bracket.
- If they match, pop the stack. Otherwise, return `false`.
- At the end, the string is valid only if the stack is empty.

## Approach

1. Initialize an empty stack.
2. Traverse the string character by character.
3. Push opening brackets onto the stack.
4. For each closing bracket, check whether the stack is empty.
5. Compare the closing bracket with the top of the stack.
6. Pop if they match; otherwise, return `false`.
7. Return `st.empty()` after processing the string.

## Code

~~~cpp
class Solution {
public:
    bool isValid(string s) {
        stack<char> st;

        for (char c : s) {
            if (c == '(' or c == '{' or c == '[')
                st.push(c);
            else {
                if (st.empty()) return false;

                if (
                    (c == ')' and st.top() == '(') ||
                    (c == ']' and st.top() == '[') ||
                    (c == '}' and st.top() == '{')
                )
                    st.pop();
                else
                    return false;
            }
        }

        return st.empty();
    }
};
~~~

## Complexity Analysis

Let n be the length of the string.

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)


## Alternatives
- We could have used a map
  -  `unordered_map<char, char> mapping = {{')', '('}, {']', '['}, {'}', '{'}};`
  -  But this has worst case look-up of `O(n)` for each charecter

- Could have implemented our own stack data structure
