from hmac import new
from operator import le
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        back = head
        cur = head
        iter = 0
        while cur.next != None:
            cur = cur.next
            iter += 1
        len = iter
        k = k % (len + 1)
        iter = 0
        cur = head
        while cur.next != None:
            cur = cur.next
            iter += 1
            if iter > k:
                back = back.next
        newhead = back.next
        back.next = None
        cur.next = head
        return newhead


sol = Solution()
list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
rotatedlist1 = sol.rotateRight(list1, 2)
while rotatedlist1:
    print(rotatedlist1.val, end=" -> ")
    rotatedlist1 = rotatedlist1.next
print()
list2 = ListNode(0, ListNode(1, ListNode(2)))
rotatedlist2 = sol.rotateRight(list2, 4)
while rotatedlist2:
    print(rotatedlist2.val, end=" -> ")
    rotatedlist2 = rotatedlist2.next
print()
