# Is Anagram

Problem can be found in [here](https://leetcode.com/problems/valid-anagram))!

### [Solution](1): Sorted function

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(t) == sorted(s)
```

Time Complexity: O(nlogn), Space Complexity: O(1)

### [Solution](2): Hash Map
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        memo = {}
        for char in s:
            try:
                memo[char] += 1
            except KeyError:
                memo[char] = 1

        for char in t:
            try:
                memo[char] -= 1
            except KeyError:
                return False

        for count in memo.values():
            if count != 0:
                return False
        
        return True        
```

### Learning Keys
- Try Catch in Python
- Sorted function
- Key Values Hash Map
