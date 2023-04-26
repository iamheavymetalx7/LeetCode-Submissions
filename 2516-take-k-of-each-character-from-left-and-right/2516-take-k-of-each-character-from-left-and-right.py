class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        
        if k==0:
            return 0    
        
        cf = Counter(s)
        
        n=len(s)
        
        if cf['a']<k or cf['b']<k or cf['c']<k:
            return -1
        
        map_a=defaultdict(int)
        map_b=defaultdict(int)
        map_c=defaultdict(int)
        
        map_a[0]=n; ca=0
        
        map_b[0]=n; cb=0
        
        map_c[0]=n; cc=0
        
        
        for i in range(n-1,-1,-1):
            if s[i]=="a":
                ca+=1
                map_a[ca]=i
            elif s[i]=="b":
                cb+=1
                map_b[cb]=i
            else:
                cc+=1
                map_c[cc]=i
        

        aa,bb,dd=0,0,0
        
        ans=n-min(map_a[k-aa],map_b[k-bb],map_c[k-dd]   )

        for i in range(n):
            if s[i]=="a":
                aa+=1
            elif s[i]=="b":
                bb+=1
            else:
                dd+=1
                
            mini= min(map_a[max(0,k-aa)],map_b[max(0,k-bb)],map_c[max(0,k-dd)] )
            val= i+1+n-mini
            
            ans=min(ans,val)
        return ans