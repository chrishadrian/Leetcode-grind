class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []
        longest = 0
        for c in s:
            if c in window:
                for i in range(window.index(c) + 1):
                    window.pop(0)
            window.append(c)
            if (len(window) > longest):
                longest = len(window)
        
        window.clear()
        return longest


# I used the sliding window algorithm (without looking at the discussion) to answer this solution. Learned about index() and clear()
# Runtime: 77 ms, faster than 69.71% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.1 MB, less than 13.71% of Python3 online submissions for Longest Substring Without Repeating Characters.
