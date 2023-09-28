class Solution:
    def rotatedDigits(self, m: int) -> int:
        
        x= str(m)

        n=len(x)
        
        dic = defaultdict(int)
        
        dic[0]=0
        dic[1]=1
        dic[8]=8
        dic[2]=5
        dic[5]=2
        dic[6]=9
        dic[9]=6
        
        
        def recur(idx,tight,has_changed):
            if idx>=n:
                if has_changed:
                    return 1
                return 0
            
            ub = 9 if not tight else int(x[idx])
            ans = 0
            for dig in range(ub+1):
                if dig in dic:
                    ans = ans+recur(idx+1,tight&(dig==ub),has_changed | (dic[dig]!=dig))
            return ans
        
        val = recur(0,1,0)
        return val
                    
                