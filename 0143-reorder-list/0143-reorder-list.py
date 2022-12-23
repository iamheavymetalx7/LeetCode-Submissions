# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        curr=head
        prev=None
        
        
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
            
        return prev
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head
        
        fast=head
        slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        first_half=head
        second_half=self.reverse(slow)
        
        while first_half is not None and second_half is not None:
            temp=first_half.next
            first_half.next=second_half
            first_half=temp
            
            temp=second_half.next
            second_half.next=first_half
            second_half=temp
        if first_half is not None:
            first_half.next=None
            
