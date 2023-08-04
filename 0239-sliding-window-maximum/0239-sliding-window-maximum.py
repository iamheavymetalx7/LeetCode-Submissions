class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        pq =[]
        

        
        
        
        for i in range(k):
            heappush(pq,[-nums[i],i])
        
        ans.append(-1*pq[0][0])
        
        for i in range(k,len(nums)):
            
            while pq and pq[0][1]<=i-k:
                heappop(pq)
            
            heappush(pq,[-nums[i],i])
            ans.append(-1*pq[0][0])
        return ans