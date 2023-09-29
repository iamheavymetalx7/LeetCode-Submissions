class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic  = defaultdict(int)
        for x in nums:
            dic[x]+=1

        maxi =0
        
        for x in dic:
            if x-1 in dic:
                continue
            
            cnt=1
            curr = x
            while curr+1 in dic:
                curr+=1
                cnt+=1
            maxi = max(maxi,cnt)
                
        return maxi