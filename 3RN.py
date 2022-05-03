# First solution:
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        for cm in magazine:
            if cm in ransomNote:
                ransomNote.remove(cm)
                
        if (not ransomNote):
            return True
        else:
            return False
                    
# Runtime: 203 ms, faster than 5.55% of Python3 online submissions for Ransom Note.
# Memory Usage: 14.4 MB, less than 6.17% of Python3 online submissions for Ransom Note.

# Since runtime is much slower, I modified the code to:
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for char in ransomNote:
            if char in magazine:
                ransomNote = ransomNote.replace(char, '', 1)
                magazine = magazine.replace(char, '', 1)

        if (not ransomNote):
            return True
        else:
            return False

# Runtime: 38 ms, faster than 97.33% of Python3 online submissions for Ransom Note.
# Memory Usage: 14.1 MB, less than 94.37% of Python3 online submissions for Ransom Note.

# Lesson learned:
# - Learned python built-in function: list(), remove(), replace(), pop(), in
# - We don't need to convert string to list of char because it'd take more memory and runtime, and string is already a list of char
