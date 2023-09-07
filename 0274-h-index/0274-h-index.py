class Solution:
    def hIndex(self, cite: List[int]) -> int:
        n=len(cite)
        buckets= [0 for _ in range(n+1)]
        
        for c in cite:
            if c>=n:
                buckets[n]+=1
            else:
                buckets[c]+=1
        # print(buckets)
        count =0
        for i in range(n,-1,-1):
            count+=buckets[i]
            
            if count>=i:
                return i
        