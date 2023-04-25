# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1):
            return list2
        elif (not list2):
            return list1
        else:
            if (list1.val <= list2.val):
                pointA = list1
                pointB = list2
                res = list1
            else:
                pointA = list2
                pointB = list1
                res = list2

            while (pointA is not None):
                if pointB and pointA.val <= pointB.val:
                    while pointA.next and pointA.next.val < pointB.val:
                        pointA = pointA.next
                    temp = pointA.next
                    pointA.next = pointB
                    pointB = temp
                pointA = pointA.next

            return res

# Runtime: 66 ms, faster than 45.33% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 13.9 MB, less than 79.39% of Python3 online submissions for Merge Two Sorted Lists.
# Reflection: Took a while to solve this (no help was seeked when doing this problem). Again I didn't see the question thoroughly. Didn't test for edge cases. Didn't create a decent test cases. But overall, I realize I have gotten more familiar with two pointers and how to utilize it properly.


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1):
            return list2
        elif(not list2):
            return list1
        else:
            dummy = ListNode()
            tail = dummy
            
            while list1 and list2:
                if list1.val <= list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next
                
            if list1:
                tail.next = list1
            else:
                tail.next = list2

            return dummy.next

# This solution is more readable but not as fast as the code above.