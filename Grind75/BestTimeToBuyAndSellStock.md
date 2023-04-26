# Best Time to Buy and Sell Stock

Problem can be found in [here](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)!

### [Solution](): Two Pointers (slow, fast)

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxProfit = 0

        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit > 0:
                if profit > maxProfit:
                    maxProfit = profit
                right += 1
            else:
                left, right = right, right + 1
                
        return maxProfit
```

Time Complexity: O(n), Space Complexity: O(1), where n is the length of `prices`

### Learning Keys
- Two pointers (left/right, slow/fast)