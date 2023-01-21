class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        # condition 1: exactly 4 integers sep by single dots
        # condition 2: between 0 and 255 and no leading zeroes
        # given: string s and return all possible valid IP addresses
        
        ans=[]
        
        def valid(ss):
            if len(ss)<1 or len(ss)>3:
                return False
            if int(ss)>255:
                return False
            if int(ss)!=0 and ss[0]=="0":
                return False
            if int(ss)==0 and len(ss)>1:
                return False    
            return True
        
        for i in range(4):
            if not valid(s[:i]):
                continue
            
            for j in range(i,i+4):
                if not valid(s[i:j]):
                    continue
                
                for k in range(j,j+4):
                    if not valid(s[j:k]):
                        continue
                    
                    if not valid(s[k:]):
                        continue
                    
                    
                    ans.append(s[:i]+"."+s[i:j]+"."+s[j:k]+"."+s[k:])
        
        return ans
        