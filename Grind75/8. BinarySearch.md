# Binary Search

Problem can be found in [here](https://leetcode.com/problems/binary-search)!

### [Solution](1) Iterative

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            # target is in the righthand side of mid, so we need to update left
            elif nums[mid] < target:
                left = mid + 1
            # target is in the lefthand side of mid, so we need to update right
            else:
                right = mid - 1

        return -1
```

Time Complexity: O(logn), Space Complexity: O(1)

### [Solution](1) Recursive

```python
class Solution:
    def binarySearch(self, nums: List[int], target: int, left: int, right: int) -> int:
        if left > right:
            return -1
        
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binarySearch(nums, target, mid+1, right)
        else:
            return self.binarySearch(nums, target, left, mid-1)
    
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target, 0, len(nums)-1)
```

Time Complexity: O(logn), Space Complexity: O(1)

### Learning Keys
- Some problems can be solved iteratively or recursively
- Divide and Conquer (left-mid-right)


