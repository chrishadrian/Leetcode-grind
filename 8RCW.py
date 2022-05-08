class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxv = 0
        for customer in accounts:
            wealth = sum(customer)
            
            if (wealth > maxv):
                maxv = wealth
            
        return maxv

# Runtime: 53 ms, faster than 90.28% of Python3 online submissions for Richest Customer Wealth.
# Memory Usage: 13.9 MB, less than 32.48% of Python3 online submissions for Richest Customer Wealth.