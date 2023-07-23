class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        
        
        ## next greater element hi toh hai
        n=len(temp)
        res =[0]*(n)
        
        st=[]
        
        for i in range(n):
            while st and temp[st[-1]]<temp[i]:
                idx = st.pop()
                res[idx]=i-idx
            
            st.append(i)
        
#         print(res)
        return res
        