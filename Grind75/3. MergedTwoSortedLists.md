# Merge Two Sorted Lists

Problem can be found in [here](https://leetcode.com/problems/merge-two-sorted-lists)!

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### [Solution](): Dummy Head

```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 if list1 else list2

        return dummy.next
```

Time Complexity: O(n+m), Space Complexity: O(1), where n and m are the length of list1 and list2, respectively.

### Learning Keys
- Curr pointer
- Dummy object
- If else shorthand in Python