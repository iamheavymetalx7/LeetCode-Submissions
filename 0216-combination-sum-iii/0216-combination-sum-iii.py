class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        
        ans =[]
        
        vals = [i for i in range(1,10)]
        length = len(vals)
        
        
        def recur(n,k,arr,idx):
            # print(n,k,arr,idx)
            if k<0 or n<0 or idx>length :
                return 0
            if k==0 and n==0:
                ans.append(arr.copy())
                return
            
            for i in range(idx,length):
                if vals[i]<=n:
                    recur(n-vals[i],k-1,arr+[vals[i]],i+1)
        recur(n,k,[],0)
        
        return ans
                    