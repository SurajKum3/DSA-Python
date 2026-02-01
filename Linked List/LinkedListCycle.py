#  -> Uses the two-pointer technique (slow & fast). Slow moves one step, fast moves two steps, if a cycle exists, both pointers will eventually meet.

#  -> Time Complexity : O(n) - In the worst case, each node is visited at most a constant number of times by the pointers.

#  -> Space Complexity : O(1) - No extra data structures are use, only two pointers are maintained.👇


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
    
        return False