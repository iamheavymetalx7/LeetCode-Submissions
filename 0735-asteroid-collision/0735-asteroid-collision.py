class Solution:
    def asteroidCollision(self, ast: List[int]) -> List[int]:
        
        st=[]
        n=len(ast)
        
        for ele in ast:
            while st and ele<0<st[-1]:
                if st[-1]<-1*ele:
                    st.pop()
                    continue
                elif st[-1]==(-1)*ele:
                    st.pop()
                break
            else:
                st.append(ele)
        return st
                
                    

                
                
                