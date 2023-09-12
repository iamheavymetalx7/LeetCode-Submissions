class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        
        for i in range(n):
            if nums[i]==0:
                nums[i]=-1
        
        s=0
        ans= 0
        dic=defaultdict(int)
        dic[0]=-1
   
        for i in range(n):
            s+=nums[i]
            

            
            if s in dic:
                ans= max(ans,i-dic[s])
            
            if s not in dic:
                dic[s]=i
        return ans