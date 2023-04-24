# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicts = {}
        #1 we put all the nums into a hashmap, which keys will be the nums, and values will be the index
        for i, num in enumerate(nums):
            diff = target - num

            #2 if `target-num` matches one of the keys in the map, we will return the predecessor index (value of the matched key) and current index
            if diff in dicts:
                return [dicts[diff], i]
            else:
                dicts[num] = i