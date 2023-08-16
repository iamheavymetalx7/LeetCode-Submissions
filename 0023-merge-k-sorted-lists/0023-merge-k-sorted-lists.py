# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        head= tail = ListNode(0)
        
        heap =[]
        
        
        n=len(lists)
        for i in range(n):
            if lists[i]:
                heappush(heap,[lists[i].val,i,lists[i]])
        
        while heap:
            node = heappop(heap)
            node = node[2]
            tail.next=node
            tail = tail.next
            if node.next:
                i+=1
                heappush(heap,[node.next.val,i+1,node.next])
                
        return head.next