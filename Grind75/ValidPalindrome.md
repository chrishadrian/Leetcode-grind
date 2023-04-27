# Valid Palindrome

Problem can be found in [here](https://leetcode.com/problems/valid-palindrome))!

### [Solution](1): Two Pointers

```python
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]+', '', s).lower()
        
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True
```

Time Complexity: O(n), Space Complexity: O(1), where n is the length of input string `s`

### [Solution](2): Python String Functions
```python
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()
        return s == s[::-1]
```

Time Complexity: O(n), Space Complexity: O(1), where n is the length of input string `s`

### Learning Keys
- Two pointers (start, end)
- Regex