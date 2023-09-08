def maximalRectangle(arr,n):
    prev_smaller =[-1 for _ in range(n)]
    next_smaller =[n for _ in range(n)]
    
    st=[]
    
    for i in range(n):
        
        while st and arr[i]<arr[st[-1]]:
            top = st.pop()
            next_smaller[top] = i
            
        
        if st:
            prev_smaller[i]=st[-1]
        
        st.append(i)

    maxArea =0
    for i in range(n):
        h = arr[i]
        width = next_smaller[i] - prev_smaller[i]-1
        maxArea = max(maxArea,width*h)
            
            
    return maxArea

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        dp =[0 for _ in range(m)]
        
        ans =0
        for i in range(n):
            for j in range(m):
                if matrix[i][j]=="1":
                    dp[j]+=1
                else:
                    dp[j]=0
            # print(dp)
            ans = max(ans,maximalRectangle(dp,m))
        
        return ans