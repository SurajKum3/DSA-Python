#  -> Used an iterative pointer-reversal technique where each node’s next pointer is redirected to its previous node while traversing the list once.

#  -> Time Complexity : O(n) - Each node in the linked list is visited exactly once.

#  -> Space Complexity : O(1) - The reversal is done in-place using only a constant amount of extra memory (no additional data structures).👇


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None

        while head:
            temp = head.next
            head.next = node
            node = head
            head = temp
        
        return node