# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) == 1:
            return False
        
        count = 0
       
        maps = {')':'(', ']':'[','}':'{'}
        arr = []
        
        for c in s:
            if (c == '(') or (c == '[') or (c =='{'):
                count += 1
                arr.append(c)
            else:
                if len(arr) == 0:
                    return False
                else:
                    if (arr.pop() != maps[c]):
                        return False
                    else:
                        count -= 1
            
        return (count == 0)
        

# Runtime: 31 ms, faster than 94.84% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 13.8 MB, less than 72.31% of Python3 online submissions for Valid Parentheses.
# Reflection: This problem was done by myself (without looking at discussion). However, the problem took me around 40 minutes until I got the correct answer.
# I was stuck because I didn't know about the constraints (the string could be one character only or start with closing parentheses). But the rest are fine.

# Lesson learned:
# 1. Read problem's constraints first before proceeding
# 2. Test edge cases and anomaly cases
# 3. Utilize map properly to reduce repeated code
