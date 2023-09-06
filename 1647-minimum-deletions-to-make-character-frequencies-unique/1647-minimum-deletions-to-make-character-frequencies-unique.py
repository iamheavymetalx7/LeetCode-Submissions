class Solution:
    def minDeletions(self, s: str) -> int:
        ## good if there are no two diff chars with same frequency
        dic=Counter(s)
        arr = sorted([k for k in dic.values()],reverse = True)
        # print(arr)
        prev = int(1e5)+2
        n=len(arr)
        ops=0
        for i in range(n): 
            if arr[i]>=prev:
                ops+=min(arr[i]-prev+1,arr[i])
                arr[i]-=min(arr[i]-prev+1,arr[i])
            prev=arr[i]
        return ops