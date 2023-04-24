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
    
# re-learn about stack and queue. It was actually a really easy problem when you notice that it's a stack data structure (FILO).
# prioritize left bracket first, put it into the stack. if it's not the opening brackets, then deal with the edge cases there. as long as it's valid, just remove the last index in the stac
# but if the stack is empty (which means the closing bracket comes first), return false. same case when the closing bracket didn't match the last index in the stack.