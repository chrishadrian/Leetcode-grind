# Valid Palindrome

Problem can be found in [here](https://leetcode.com/problems/valid-palindrome))!

### [Solution](): Stack (FILO)

```python
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]+', '', s).lower()
        print(s)
        
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True
```

Time Complexity: O(n), Space Complexity: O(n), where n is the length of input string `s`

### Learning Keys
- Two pointers (start, end)
- Regex