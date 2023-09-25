class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n=len(maxHeights)
        prv =[-1 for _ in range(n)]
        nxt =[n for _ in range(n)]
        
        st=[]
        
        for i,el in enumerate(maxHeights):
            
            while st and maxHeights[st[-1]]>=maxHeights[i]:
                t= st.pop()
            
            if st:
                prv[i]=st[-1]
            st.append(i)
        # print(prv)
        while st:
            st.pop()
        
        for i,el in enumerate(maxHeights):
            while st and maxHeights[st[-1]]>maxHeights[i]:
                top = st.pop()
                nxt[top]=i
                
            st.append(i)
        # print(nxt)
        
        lft=[0 for _ in range(n)]
        rgt = [0 for _ in range(n)]
        
        for i in range(n):
            if i==0:
                lft[0] = maxHeights[0]
                continue
            
            if lft[i]>=lft[i-1]:
                lft[i]+=lst[i-1]
            else:
                lft[i] = (i-prv[i])*maxHeights[i]+(0 if prv[i]<0 else lft[prv[i]])
        # print(lft)
                
        for i in range(n-1,-1,-1):
            if i==n-1:
                rgt[n-1]=maxHeights[n-1]
                continue
            
            if rgt[i]>=rgt[i+1]:
                rgt[i]+=rgt[i+1]
            else:
                rgt[i] = (nxt[i]-i)*maxHeights[i]+(0 if nxt[i]>=n else rgt[nxt[i]])
        # print(rgt)
        
                
        ans =[0 for _ in range(n)]
        
        for i in range(n):
            ans[i]=lft[i]+rgt[i]-maxHeights[i]
        
        return max(ans)
                
                