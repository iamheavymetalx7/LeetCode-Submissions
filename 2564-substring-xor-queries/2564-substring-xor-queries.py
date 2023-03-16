class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        def calcNumber(l,r):
            p=1
            num=0
            for idx in range(l,r+1)[::-1]:
                if s[idx]=="1":
                    num+=p
                p*=2
            return num
        
        dic=defaultdict(list)
        n=len(s)
        for sub in range(1,31):
            for k in range(0,n-sub+1):
                ele = calcNumber(k,k+sub-1)
                
                if ele in dic:
                    continue
                else:
                    dic[ele]=[k,k+sub-1]
                
                k+=1
        
        to_ret=[]
        for x,y in queries:
            val = x^y
            if val in dic:
                to_ret.append(dic[val])
            else:
                to_ret.append([-1,-1])

        return to_ret
        