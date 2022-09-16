class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLength = 1
        i = 0
        n = len(s)
        start = 0
        while i < n:
            # case even
            l = i
            r = i+1
            while l>= 0 and r<n and s[l] == s[r]:
                if r-l+1>maxLength:
                    maxLength = r-l+1
                    start = l
                l-=1
                r+=1

            # case odd
            l = i-1
            r = i+1
            while l>= 0 and r<n and s[l] == s[r]:
                if r-l+1>maxLength:
                    maxLength = r-l+1
                    start = l
                l-=1
                r+=1
            i+=1
            
        return s[start:start+maxLength]

# This one was quite hard for me, so I looked at discussion and found out that I can use two pointers with coverage in both odd and even cases