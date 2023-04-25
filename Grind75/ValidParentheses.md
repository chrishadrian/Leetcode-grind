# Valid Parentheses

Problem can be found in [here](https://leetcode.com/problems/valid-parentheses)!

```python

### [Solution](): Stack (FILO)

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket = {"(": ")", "[": "]", "{": "}"}
        for char in s:
            # Case 1: Left Bracket, just simply push into stack
            if char in bracket:
                stack.append(char)
            # Case 2: Right Bracket, may cause invalid parentheses
            else:
                if not stack or bracket[stack[-1]] != char:
                    return False
                else:
                    stack.pop()
        
        return not stack
```

Time Complexity: O(n), Space Complexity: O(n), where n is the length of `nums`

### Learning Keys
- Stack (FILO)
- Analyze when the problem starts (right brackets)