class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n=len(a)
        m=len(b)
        string=""
        
        if n>m:
            mini=m
            rem = a[:n-mini]
        else:
            mini=n
            rem=b[:m-mini]
        
        carry=0
        for i in range(mini):
            if a[-i-1]=="1" and a[-i-1]==b[-1-i]:
                if carry:
                    string+="1"
                    carry=1
                else:
                    string+="0"
                    carry=1
            elif a[-i-1]=="0" and a[-1-i]==b[-i-1]:
                if carry:
                    string+="1"
                    carry=0
                else:
                    string+="0"
            else:
                if carry:
                    string+="0"
                    carry=1
                else:
                    string+="1"
                    
        if m==n:
            if carry:
                string+=str(carry)
            return string[::-1]
        
        print(rem)
        for ele in rem[::-1]:
            if ele=="1" and carry:
                string+="0"
                carry=1
            elif ele=="0" and carry:
                string+="1"
                carry=0
            else:
                string+=ele
                carry=0
                
        if carry:
            string+=str(carry)
        
        return string[::-1]
        
        
                
        
        