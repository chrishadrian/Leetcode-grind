class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutionSet = set()
        nums.sort()
        
        n = len(nums)
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1
            
            while (j < k):
                sums = nums[i] + nums[j] + nums[k]
                if (sums == 0):
                    solutionSet.add((nums[i], nums[j], nums[k]))
                    
                if sums < 0:
                    j+=1
                else:
                    k-=1
            
            
        return list(map(list, solutionSet))
                
# This is the first result that I got. I iterate through all the numbers in the list. And in every number, I use double pointer to find the perfect combination to get 0. This is still considered as cumbersome because it does the same thing twice. Therefore, I added an if statement to get rid of the duplicate operations.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutionSet = set()
        nums.sort()
        
        n = len(nums)
        
        for i in range(n - 2):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1
            
            while (j < k):
                sums = nums[i] + nums[j] + nums[k]
                if (sums == 0):
                    solutionSet.add((nums[i], nums[j], nums[k]))
                    
                if sums < 0:
                    j+=1
                else:
                    k-=1    
            
            
        return list(map(list, solutionSet))
                
# Runtime: 892 ms, faster than 73.75% of Python3 online submissions for 3Sum.
# Memory Usage: 19.3 MB, less than 6.75% of Python3 online submissions for 3Sum.