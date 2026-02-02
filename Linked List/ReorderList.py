#  -> The solution works by finding the middle of the linked list using slow & fast pointers, reversing the second half in-place, and then merging the two halves alternately to achieve the required reordered structure.

#  -> Time Complexity : O(n) - Each node is visited a constant number of times across finding the middle, reversing, and merging.

#  -> Space Complexity : O(1) - The list is modified in-place without using any extra data structures.👇

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = head
        slow = head

        # Step 1: Find the middle of the list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Step 2: Reverse the second half of the list
        second = slow.next
        slow.next = None
        node = None

        while second:
            temp = second.next
            second.next = node
            node = second
            second = temp

        # Step 3: Merge the two halves
        first = head
        second = node

        while second:
            temp1, temp2 = first.next, second.next
            first.next, second.next = second, temp1
            first, second = temp1, temp2