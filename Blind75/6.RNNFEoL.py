# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]
 
# Constraints:
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp_head = head
        k = 0
        while (temp_head is not None):
            k += 1
            temp_head = temp_head.next;
            
        if (k == 1):
            return None
    
        k -= n
        
        if (k == 0):
            temp_head = head
            head = head.next
            del temp_head
            return head
        
        temp_head = head
        for i in range(k-1):
            temp_head = temp_head.next
            
        temp = temp_head.next
        temp_head.next = temp_head.next.next
        del temp
        
        return head

# Best case scenario (code has not been optimized yet):
# Runtime: 36 ms, faster than 91.19% of Python3 online submissions for Remove Nth Node From End of List.
# Memory Usage: 13.8 MB, less than 97.98% of Python3 online submissions for Remove Nth Node From End of List.