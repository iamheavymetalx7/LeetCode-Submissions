class Solution:
    def makesquare(self, arr: List[int]) -> bool:
        
        n =len(arr)
        s = sum(arr)
        
        arr.sort(reverse=True)
        
        k=4
        
        if s%k!=0:
            return False
        
        subset_val = s//4
        
        vec =[0]*(4)
        
        
        def recur(idx):
            if idx>=n:
                return True
            curr = arr[idx]
            for j in range(4):
                if vec[j]+curr<=subset_val:
                    vec[j]+=curr
                    if recur(idx+1):
                        return True
                    vec[j]-=curr
                if vec[j]==0:
                    break
            return False
        return recur(0)