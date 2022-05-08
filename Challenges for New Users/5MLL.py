# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head.next):
            return head
        
        i = 0
        result = []
        while(head):
            result.append(head)
            head = head.next
            i += 1

        mid = int(i/2)
        return result[mid]

# Runtime: 28 ms, faster than 94.54% of Python3 online submissions for Middle of the Linked List.
# Memory Usage: 13.8 MB, less than 56.86% of Python3 online submissions for Middle of the Linked List.
