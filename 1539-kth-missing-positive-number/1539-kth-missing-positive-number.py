class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l,r= -1,len(arr)
        while r>l+1:
            m =(l+r)//2
            print(m)
            
            if arr[m]-m-1<k:
                l=m
            else:
                r=m
        return r+k
        
            
                
        