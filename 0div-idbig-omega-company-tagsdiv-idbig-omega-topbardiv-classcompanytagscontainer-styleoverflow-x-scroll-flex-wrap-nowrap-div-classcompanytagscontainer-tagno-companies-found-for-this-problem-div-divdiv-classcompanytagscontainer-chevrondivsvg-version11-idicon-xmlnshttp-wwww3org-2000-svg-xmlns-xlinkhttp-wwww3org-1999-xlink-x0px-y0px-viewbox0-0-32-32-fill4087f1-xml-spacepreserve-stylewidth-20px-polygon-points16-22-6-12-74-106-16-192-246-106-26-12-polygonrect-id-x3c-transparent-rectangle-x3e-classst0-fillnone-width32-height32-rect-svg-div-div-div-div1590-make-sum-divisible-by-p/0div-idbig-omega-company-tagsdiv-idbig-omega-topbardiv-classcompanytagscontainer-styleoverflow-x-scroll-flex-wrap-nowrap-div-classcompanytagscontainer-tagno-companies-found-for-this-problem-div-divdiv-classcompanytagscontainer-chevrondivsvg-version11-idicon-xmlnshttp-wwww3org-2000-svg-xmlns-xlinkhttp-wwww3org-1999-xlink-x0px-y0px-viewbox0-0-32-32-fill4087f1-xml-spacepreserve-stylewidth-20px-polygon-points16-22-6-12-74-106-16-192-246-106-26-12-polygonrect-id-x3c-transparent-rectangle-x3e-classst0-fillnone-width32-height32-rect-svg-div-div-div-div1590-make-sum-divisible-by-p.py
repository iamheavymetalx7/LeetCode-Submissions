'''
- Suppose you know the remainder for the sum of the entire array. 
- How does removing a subarray affect that remainder? 
- What remainder does the subarray need to have in order to make the rest of the array sum up to be divisible by k?


Since we want smallest subarray, we remove the smallest subarray having need (as remainder)
'''

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        pref =0
        dic=defaultdict(int)
        
        need = sum(nums)%p
        if need==0:
            return 0
        
        n=len(nums)
        ans= n
        
        dic[0]=-1
        for i in range(n):
            pref+=nums[i]
            
            pref%=p
            if (pref-need)%p in dic:
                ans = min(ans,i-dic[(pref-need)%p])
            
            dic[pref]=i
        return ans if ans<n else -1
                