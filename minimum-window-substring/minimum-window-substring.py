class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dt = defaultdict(int)
        left =0
        ds=defaultdict(int)
        
        for c in t:
            dt[ord(c)-ord('A')]+=1
        ans=int(1e19)
        
        sidx,eidx=-1,-1
        f=False
        print(dt)

        def check(dic1,dic2):
            for key in dic2.keys():
                if dic2[key]>dic1[key]:
                    return False
            return True
            
        
        for right in range(len(s)):
            ds[ord(s[right])-ord('A')]+=1

            while check(ds,dt):
                curr = right-left+1
                if curr<ans:
                    f=True
                    ans = curr
                    sidx=left
                    eidx=right
                if ds[ord(s[left])-ord('A')]==0:
                    continue 
                ds[ord(s[left])-ord('A')]-=1

                left+=1


            
        if f:
            return s[sidx:eidx+1]
            
        return ""     
            
            
