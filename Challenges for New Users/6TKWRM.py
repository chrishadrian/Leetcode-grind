class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        result = []
        
        maxval = -1
        for row in mat:
            count = 0
            for nums in row:
                count += 1 * nums
            result.append(count)
            
        temp = []
        maxval = max(result)
        for num in range(k):
            val = min(result)
            row = result.index(val)
            temp.append(row)
            result[row] = maxval + 1
        
        return temp
                
                
# Runtime: 117 ms, faster than 80.69% of Python3 online submissions for The K Weakest Rows in a Matrix.
# Memory Usage: 14.2 MB, less than 51.39% of Python3 online submissions for The K Weakest Rows in a Matrix.

## Reflection:
# The code that I made is actually ugly, I was planning to use dictionary, and sort the dictionary by its value (number of 1 in this case). However, I didn't find the correct way to put in a dictionary to the list.
# After looking at the discussion of this problem, I finally found the algorithm that I wanted to implement (the one I mentioned above).
# Here is the code:

class Solution:
    def kWeakestRows(self, mat, k):
        flat = []
        
        for i, row in enumerate(mat):
            flat.append((sum(row),i)) # append number of 1 in the row, and its row number

        flat.sort() # sort here use the first variable in the brackets. if values are the same, look at the second variable. so it's sorting based on the total of number 1's in a row and row number
        print(flat)
        return [x[1] for x in flat[:k]] # returning the k first row numbers