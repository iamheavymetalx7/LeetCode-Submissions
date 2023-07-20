class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        n = len(a)
        
        st=[]
        
        for x in a:
            if not st:
                st.append(x)
                continue
            
            if st[-1]>0 and x<0:
                f = 0
                while st and abs(st[-1])<=abs(x) and st[-1]>0 and x<0 and not f:
                    if abs(st[-1])==abs(x):
                        f=1
                    st.pop()
                
                if (not st or (st[-1]<0 and x<0) or (st[-1]>0 and x>0)) and not f:
                    st.append(x)
            
            
            else:
                st.append(x)
            
        return st