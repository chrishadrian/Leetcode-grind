class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if ((nums[i] + nums[j]) == target):
                    return [i,j]

                
        return []

# first solution looks so ugly since it's a brute force.
# Runtime: 4421 ms, faster than 20.50% of Python3 online submissions for Two Sum.
# Memory Usage: 14.9 MB, less than 76.40% of Python3 online submissions for Two Sum.

# after looking at the discussion board. i learned how to utilize enumerate() in python, and how to utilize hash table (dictionary) to solve the problem. To store a value in a key, you just need to use dictionaryList[key] = value. This is equivalent with dictionaryList = {'key' : 'value'}

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevNums = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in prevNums:
                return [prevNums[diff], index]
            prevNums[num] = index
        return

# Runtime: 90 ms, faster than 60.61% of Python3 online submissions for Two Sum.
# Memory Usage: 15.1 MB, less than 49.10% of Python3 online submissions for Two Sum.