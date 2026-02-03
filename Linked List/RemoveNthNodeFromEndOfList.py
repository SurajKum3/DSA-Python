#  -> Used the two-pointer technique with a dummy node, where one pointer is moved n steps ahead and then both pointers move together so the second pointer lands just before the node to be removed.

#  -> Time Complexity : O(n) - The linked list is traversed only once, where N is the length of the list.

#  -> Space Complexity : O(1) - No extra data structures are used, only constant extra pointers are maintained.👇


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        dummy = res

        for _ in range(n):
            head = head.next
        
        while head:
            head = head.next
            dummy = dummy.next
        
        dummy.next = dummy.next.next

        return res.next