class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        pq = []
        total = 0
        maxres=0
        for a,b in sorted(zip(nums1,nums2),key=lambda x:-x[1]):
            heappush(pq,a)
            total+=a
            
            if len(pq)>k:
                total-=heappop(pq)
            
            if len(pq)==k:
                maxres=max(maxres,total*b)
        return maxres
        
        