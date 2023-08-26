class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        n = len(a)
        
        
        st=[]
        i=n-1
        ans=[]
        while i>=0:
            if a[i]<0:
                st.append(a[i])
            else:
                r = a[i]
                
                while st and r>0:
                    if r>abs(st[-1]):
                        st.pop()
                    else:
                        l=st.pop()
                        
                        # print(abs(l),r)
                        if abs(l)>r:
                            r=0
                        
                            st.append(l)
                        else:
                            r=0
                            continue
                    
                if r>=1:
                     ans.append(r)
            i-=1
        cur=[]
        while st:
            cur.append(st.pop())
        cur.extend(ans[::-1])
        return (cur)
            