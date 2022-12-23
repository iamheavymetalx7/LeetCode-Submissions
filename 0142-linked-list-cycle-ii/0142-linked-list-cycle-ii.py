# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def helper(head):
            global slow
            slow=head
            fast=head

            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next

                if slow==fast:
                    return True
            return False
        
        if helper(head):
            global slow
            fast=head
            while fast!=slow:
                fast=fast.next
                slow=slow.next
            
            return fast
            
        else:
            return None
                
        
        