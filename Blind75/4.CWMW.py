# Brute force solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        for i in range(0, len(height)):
            for j in range(i+1, len(height)):
                shorter = min(height[i], height[j])
                dist = j-i
                result = max(result, shorter*dist)
                
        return result

# The first approach that I did was using Brute Force. I iterated through all the heights twice so it has O(n^2) time complextiy.

# Two pointers solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        
        area = 0
        
        while (start < end):
            area = max(area, min(height[start], height[end]) * (end - start))
            
            if (height[start] < height[end]):
                start += 1
            else:
                end -= 1
        
        return area    

# The second approach was using two pointers. Instead of iterating through the list twice, I just need to iterate it once by moving the edge pointers until they came accross.
        
        