# Invert Tree

Problem can be found in [here](https://leetcode.com/problems/invert-binary-tree/)!

### [Solution](): Recursion

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)

        temp = root.left
        root.left = root.right
        root.right = temp

        return root

```

Time Complexity: O(n), Space Complexity: O(h), where h is the height of the binary tree

### Learning Keys
- Recursion