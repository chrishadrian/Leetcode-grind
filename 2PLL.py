class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Ideal solution: Tortoise and hare, space O(1), 
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next is None:
            return True
		# "one" will be the pointer of last element of the first half with connections reversed in the first half using "point"
		# "two" will be the pointer of the first element of the second half.
        point, one = None, None
        slow, fast = head, head.next
        while fast.next and fast.next.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next
            one = temp
            one.next = point
            point = one
        two = None
        if fast.next:
            two = slow.next.next
        else:
            two = slow.next
        one = slow
        one.next = point
        point = one
        while one and two:
            if one.val != two.val:
                return False
            one = one.next
            two = two.next
        return True

# If we don't need to use space O(1), we can do:
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         palin = []
#         while(head):
#             palin.append(head.val)
#             head = head.next
#         return palin==palin[::-1]


