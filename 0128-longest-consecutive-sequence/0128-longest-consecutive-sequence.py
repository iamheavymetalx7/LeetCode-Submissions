class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        dic=defaultdict(int)
        
        
        
        for ele in nums:
            dic[ele]=1
        
        maxi =0
        cnt=0
        for x in dic:
            if x-1 in dic:
                continue
            cnt=0
            while x in dic:
                cnt+=1
                x+=1
                maxi=max(maxi,cnt)
                
        maxi=max(cnt,maxi)
        return maxi