class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        arr=zip(nums2,nums1)
        a=list(arr)
        a.sort(reverse=True)
        print(a)
        pq=[]
        tot=0
        ans=-1
        for x,y in a:
            heappush(pq,y)
            tot+=y
            
            if len(pq)>k:
                tot-=heappop(pq)
            # print(tot,"toto")
            if len(pq)==k:
                ans=max(ans, tot*x)
        return ans
            