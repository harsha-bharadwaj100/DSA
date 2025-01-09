# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)  # A dummy node to simplify list handling
        current = dummy  # Pointer to the current node in the result list
        carry = 0  # Initialize carry to 0

        while l1 or l2 or carry:
            # Calculate the sum of the current digits and the carry
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry

            # Update carry and the current node's value
            carry = total // 10
            current.next = ListNode(total % 10)

            # Move pointers forward
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


# Example usage
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

solution = Solution()
o3 = solution.addTwoNumbers(l1, l2)

# Print the resulting list
while o3:
    print(o3.val, end=" -> " if o3.next else "\n")
    o3 = o3.next
