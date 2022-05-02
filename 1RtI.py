class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        map = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        
        if (len(s) == 1): return map[s[0]]
        
        for index in range(1, len(s)):
            value = map[s[index]]
            prev  = map[s[index - 1]]
            if (value > prev):
                if (index == 1): sum += value - prev
                else: sum += value - 2*prev
            else:
                if (index == 1): sum += prev
                sum += value
                
        return sum

# Runtime: 42 ms, faster than 95.79% of Python3 online submissions for Roman to Integer.
# Memory Usage: 14 MB, less than 31.95% of Python3 online submissions for Roman to Integer.

# Reflection:
# This is my first LeetCode problem. My approach wasn't really effective because I have to cover the base cases with a lot of if statements. Here is another solution from the problem's discussion that I think has a better implementation (https://leetcode.com/problems/roman-to-integer/discuss/1551160/Python3):
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         maps = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M': 1000}
#         pre = None
#         sums = 0
#         for i in s:
#             if pre and pre < maps[i]:
#                 sums += maps[i] - 2 * pre

#             else:
#                 sums += maps[i]
#                 pre = maps[i]
#         return sums
