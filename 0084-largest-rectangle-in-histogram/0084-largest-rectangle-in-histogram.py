class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n =len(heights)
        next_smaller = [n for _ in range(n)]
        prev_smaller = [-1 for _ in range(n)]
        
        st=[]
        
        
        for i in range(n):
            
            while st and heights[st[-1]]>heights[i]:
                top = st.pop()
                next_smaller[top]=i
            
            if st:
                prev_smaller[i]=st[-1]
            st.append(i)
            
        maxArea= 0
        
#         print(next_smaller)
#         print(prev_smaller)
        
        for i in range(n):
            h = heights[i]
            width = next_smaller[i] - prev_smaller[i]-1
            maxArea = max(maxArea,width*h)
        return maxArea
        