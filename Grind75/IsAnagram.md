class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(t) == sorted(s)
        

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


