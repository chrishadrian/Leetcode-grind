class Solution:            
    def numberOfSteps(self, num: int) -> int:
        def countSteps(num: int, steps: int) -> int:
            # base case
            if (not num):
                return steps


            if (num % 2 == 0):
                return countSteps(num//2, 1+steps   )
            else:
                return countSteps(num-1, steps+=1)
                
        return countSteps(num, 0)
        
# Runtime: 30 ms, faster than 89.31% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
# Memory Usage: 13.8 MB, less than 53.76% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.

## One-liner helper function
class Solution:            
    def numberOfSteps(self, num: int) -> int:
        def countSteps(num: int, steps: int) -> int:
            return steps if (not num) else countSteps(num//2 if (num % 2 == 0) else num-1, steps+1)
          
        return countSteps(num, 0)
        
## Reflection:
# - Learned the ternary operation in python
# - Learned recursive function in python
