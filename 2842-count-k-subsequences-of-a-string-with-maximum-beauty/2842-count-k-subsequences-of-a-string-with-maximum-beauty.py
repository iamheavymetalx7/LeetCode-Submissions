class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        
        cnt = Counter(s)
        if k>len(cnt):
            return 0
        
        arr = sorted([k for k in cnt.values()],reverse=True)
        max_sum = sum(arr[:k])
        MOD = int(1e9)+7
        
        
        keys =[key for key in cnt.keys()]
        
        n=len(keys)
        
        @cache
        def recur(i,k,curr_sum):
            print(i,k)
            
            if k==0:
                if curr_sum==max_sum:
                    return 1
                return 0
            if i>=len(arr):
                return 0
                
            
            
            
            take = ((arr[i]*recur(i+1,k-1,curr_sum+arr[i]))%MOD)%MOD
            nottake =(recur(i+1,k,curr_sum))%MOD
            
            ans = nottake+take
            return ans
            
            
            
            return ans
        
        val = recur(0,k,0)
        return val
            
            
            