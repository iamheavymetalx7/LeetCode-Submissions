class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        new= []
        for h in hours:
            if h>8:
                new.append(1)
            else:
                new.append(-1)
        print(new)
        
        s =0
        
        ans=0
        dic = defaultdict(int)
        dic[0]=-1
        n =len(new)
        for r in range(n):
            s+=new[r]
            
            if s>0:
                ans = max(ans,r-dic[0])
            else:
                if (s-1) in dic:
                    ans = max(ans,r-dic[s-1])
            if s not in dic:
                dic[s]=r
        return ans