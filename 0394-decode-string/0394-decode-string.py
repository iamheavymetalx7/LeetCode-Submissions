class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        n=len(s)
        res=""
        num=0
        
        for c in s:
            if c.isdigit():
                num=num*10+int(c)
            elif c=='[':
                st.append(res)
                st.append(num)
                res=""
                num=0
            elif c=="]":
                pnum=st.pop()
                pstr=st.pop()
                res=pstr+pnum*res
            else:
                res+=c

        # print(res)
    
        return res
        
            
        