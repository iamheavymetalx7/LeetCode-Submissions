class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        dic= defaultdict(list)
        n=len(nums)
        for i,x in enumerate(nums):
            dic[x].append(i)
        
        ans = int(1e8)
        
        print(dic)
        
        for ele in dic:
            arr = dic[ele]
            maxi = (n-1-arr[-1])+arr[0]
            
            for i in range(1,len(arr)):
                maxi = max(maxi, arr[i]-arr[i-1]-1)
            
            ans= min(ans, (1+maxi)//2)
        return ans
                
                