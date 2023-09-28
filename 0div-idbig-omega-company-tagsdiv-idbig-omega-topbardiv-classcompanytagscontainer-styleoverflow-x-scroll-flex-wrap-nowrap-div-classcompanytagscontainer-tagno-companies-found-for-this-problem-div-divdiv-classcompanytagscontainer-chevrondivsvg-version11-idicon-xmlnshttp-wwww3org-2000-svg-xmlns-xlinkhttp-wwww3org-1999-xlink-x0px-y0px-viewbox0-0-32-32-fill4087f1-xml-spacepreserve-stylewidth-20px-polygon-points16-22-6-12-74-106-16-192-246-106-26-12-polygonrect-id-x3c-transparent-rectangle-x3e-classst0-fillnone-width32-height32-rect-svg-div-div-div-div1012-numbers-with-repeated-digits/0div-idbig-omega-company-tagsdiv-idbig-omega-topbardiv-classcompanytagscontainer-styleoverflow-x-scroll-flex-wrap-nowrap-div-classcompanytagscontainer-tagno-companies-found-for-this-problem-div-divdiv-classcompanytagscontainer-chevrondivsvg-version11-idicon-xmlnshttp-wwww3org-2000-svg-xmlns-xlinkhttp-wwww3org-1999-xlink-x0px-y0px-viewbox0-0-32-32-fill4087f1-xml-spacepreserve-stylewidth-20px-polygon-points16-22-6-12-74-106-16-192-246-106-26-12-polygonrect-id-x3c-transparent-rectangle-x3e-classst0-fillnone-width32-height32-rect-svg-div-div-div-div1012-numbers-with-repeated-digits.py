class Solution:
    def numDupDigitsAtMostN(self, m: int) -> int:
        x = str(m)
        
        n=len(x)
        
        arr=[0 for _ in range(10)]
        
        @cache
        def recur(idx,started,tight,zero,one,two,three,four,five,six,seve,eigh,nine):
            if idx>=n:
                if one>=2 or two>=2 or three>=2 or four>=2 or five>=2 or six>=2 or seve>=2 or eigh>=2 or nine>=2 or zero>=2:
                    return 1
                return 0
            
            ub = 9 if not tight else int(x[idx])
            ans=0
            for dig in range(0,ub+1):
                
                if dig==0 and not started:
                    ans = ans + recur(idx+1,False,tight&(dig==ub),zero,one,two,three,four,five,six,seve,eigh,nine)
                else:
                    
                    ans = ans + recur(idx+1,True,tight&(dig==ub),zero+(dig==0),one+(dig==1),two+(dig==2),three+(dig==3),four+(dig==4),five+(dig==5),six+(dig==6),seve+(dig==7),eigh+(dig==8),nine+(dig==9))
            return ans
        
        val = recur(0,False,True,0,0,0,0,0,0,0,0,0,0)
        return val
                