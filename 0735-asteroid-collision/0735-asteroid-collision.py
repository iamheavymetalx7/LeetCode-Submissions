class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        
        
        ans=[]
        i=0
        for ele in asteroids:
            # print(ele,"inside for")
            while st and ele<0<st[-1]:
                # print(ele,"inside while")
                if st[-1]<-1*ele:
                    st.pop()
                    continue
                elif st[-1]==-1*ele:
                    st.pop()
                break
            else:
                st.append(ele)
        
        return st