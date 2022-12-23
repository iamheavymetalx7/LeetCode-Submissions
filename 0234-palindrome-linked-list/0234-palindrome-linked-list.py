# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        if (not head or not head.next):
            return head
        
        prev=None
        curr=head
        
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt

        return prev
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
        
        fast=head
        slow=self.reverse(slow)
        
        while slow:
            if slow.val!=fast.val:
                return False
            slow=slow.next
            fast=fast.next
            
        return True