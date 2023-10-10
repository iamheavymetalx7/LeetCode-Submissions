class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxQ,minQ = deque(),deque()
        
        n = len(nums)
        
        i=0;maxi=0
        
        for j,num in enumerate(nums):
            while maxQ and maxQ[-1]<num:
                maxQ.pop()
            maxQ.append(num)
            
            while minQ and minQ[-1]>num:
                minQ.pop()
            minQ.append(num)
            
            while maxQ[0]-minQ[0]>limit:
                if maxQ[0]==nums[i]:
                    maxQ.popleft()
                if minQ[0]==nums[i]:
                    minQ.popleft()
                
                i+=1
            maxi = max(maxi,j-i+1)
        return maxi